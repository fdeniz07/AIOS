"""Phase 8.3 Module Contract Validator (read-only).

Implements ``docs/MODULE_CONTRACT_VALIDATION_DESIGN.md`` exactly.
Reuses Phase 8.2 ``FileSystem.inspect`` / root discovery; findings use ``MOD-*``.
"""

from __future__ import annotations

import datetime as datetime_mod
import re
import stat as stat_mod
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Mapping, Optional, Sequence

import yaml

from .framework_structure import FileSystem, PathKind, _discover_upward
from .models import Finding, Severity, ValidationResult, aggregate_findings

CATEGORY = "module-contract"

STATUS_VALUES = frozenset({"draft", "active", "deprecated"})
MATURITY_VALUES = frozenset({"experimental", "stable"})

KNOWN_TOP_LEVEL = frozenset(
    {
        "id",
        "version",
        "title",
        "summary",
        "status",
        "maturity",
        "applies_when",
        "avoid_when",
        "tags",
        "provides",
        "requires_core",
        "deprecation",
    }
)

# Lowercase English kebab-case Module id / tag pattern.
_KEBAB_RE = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")
# SemVer MAJOR.MINOR.PATCH with optional pre-release / build metadata.
_SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)
_ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_MIGRATION_HEADING = "## Migration"

MSG = {
    "MOD-001": "module.yaml is missing, wrong type, or a broken symlink: {path}",
    "MOD-002": "README.md is missing, wrong type, or a broken symlink: {path}",
    "MOD-003": "module.yaml could not be parsed as a YAML mapping: {path}",
    "MOD-004": "Required metadata field is missing or empty: {field} ({path})",
    "MOD-005": "Metadata field has invalid type: {field} ({path})",
    "MOD-006": "Invalid Module id format (expected lowercase kebab-case): {path}",
    "MOD-007": "Invalid SemVer value for {field}: {path}",
    "MOD-008": "Invalid status enum value: {path}",
    "MOD-009": "Invalid maturity enum value: {path}",
    "MOD-010": "Forbidden metadata key 'dependencies' is present: {path}",
    "MOD-011": "deprecation object is inconsistent with status or not an object: {path}",
    "MOD-012": "Deprecated Module README lacks exact '## Migration' heading: {path}",
    "MOD-013": "Unknown metadata field '{field}': {path}",
    "MOD-014": "Optional applicability list is missing: {field} ({path})",
    "MOD-015": "maturity should normally be omitted when status is deprecated: {path}",
    "MOD-016": "deprecation.reason is missing: {path}",
    "MOD-017": "Directory name does not match metadata id: {path}",
    "MOD-018": "Unexpected non-directory child under modules/: {path}",
    "MOD-019": "modules exists but is not a directory: {path}",
    "MOD-021": (
        "Filesystem inspection or resolution unreliable: {path} ({error_class})"
    ),
    "MOD-022": "Invalid deprecation.successor id format: {path}",
    "MOD-023": "Non-kebab-case tags entry '{tag}': {path}",
    "MOD-024": "Symlink resolves outside the Framework root: {path}",
    "MOD-025": "Invalid deprecation.sunset format (expected YYYY-MM-DD): {path}",
}

SUGGESTION = {
    "MOD-001": "Add a regular module.yaml file under the Module package directory.",
    "MOD-002": "Add a regular README.md file under the Module package directory.",
    "MOD-003": "Fix YAML syntax so module.yaml parses to a mapping.",
    "MOD-004": "Provide a non-empty value for required field '{field}'.",
    "MOD-005": "Correct the YAML type of field '{field}'.",
    "MOD-006": "Use a lowercase English kebab-case Module id.",
    "MOD-007": "Use SemVer MAJOR.MINOR.PATCH for '{field}'.",
    "MOD-008": "Set status to exactly draft, active, or deprecated.",
    "MOD-009": "Set maturity to experimental or stable, or omit the field.",
    "MOD-010": "Remove the forbidden dependencies key from module.yaml.",
    "MOD-011": "Include deprecation only when status is deprecated, as an object.",
    "MOD-012": "Add an exact '## Migration' heading to the deprecated Module README.",
    "MOD-013": "Remove or rename unknown field '{field}', or document an approved extension.",
    "MOD-014": "Add a list of strings for '{field}'.",
    "MOD-015": "Omit maturity when status is deprecated.",
    "MOD-016": "Add a short deprecation.reason string.",
    "MOD-017": "Rename the directory or set id to match the directory name.",
    "MOD-018": "Remove non-directory children under modules/ (except catalog README.md).",
    "MOD-019": "Ensure modules/ is a directory at the Framework root.",
    "MOD-021": "Resolve the filesystem error preventing inspection of {path}.",
    "MOD-022": "Use a lowercase kebab-case Module id for deprecation.successor.",
    "MOD-023": "Use lowercase kebab-case for tags entries.",
    "MOD-024": "Replace the out-of-root symlink with an in-root path.",
    "MOD-025": "Use ISO date format YYYY-MM-DD for deprecation.sunset.",
}


class Containment(str, Enum):
    INSIDE = "inside"
    OUTSIDE = "outside"
    BROKEN = "broken"
    ERROR = "error"
    NOT_SYMLINK = "not_symlink"


@dataclass
class _Abort(Exception):
    """Internal: unreliable FS inspection requiring exit 2."""

    finding: Finding


@dataclass
class _CandidateContext:
    dir_name: str
    rel_dir: str
    abs_dir: Path
    status: Optional[str] = None  # known valid status or None (unknown)
    module_id: Optional[str] = None
    findings: list[Finding] = field(default_factory=list)


def _rel(path: str) -> str:
    return path.replace("\\", "/")


def _finding(
    code: str,
    *,
    severity: Severity,
    path: Optional[str] = None,
    field: Optional[str] = None,
    tag: Optional[str] = None,
    error_class: Optional[str] = None,
) -> Finding:
    display_path = path if path is not None else "-"
    message = MSG[code].format(
        path=display_path,
        field=field or "-",
        tag=tag or "-",
        error_class=error_class or "OSError",
    )
    suggestion = SUGGESTION[code].format(
        path=display_path,
        field=field or "-",
        tag=tag or "-",
    )
    return Finding(
        code=code,
        severity=severity,
        category=CATEGORY,
        message=message,
        path=path,
        rule=code,
        suggestion=suggestion,
    )


class ModuleFileSystem(FileSystem):
    """FileSystem plus list/read/resolve hooks for Module Contract Validation."""

    def iterdir(self, path: Path) -> list[Path]:
        return sorted(path.iterdir(), key=lambda p: p.name.lower())

    def read_text(self, path: Path) -> str:
        return path.read_text(encoding="utf-8")

    def resolve(self, path: Path, *, strict: bool = False) -> Path:
        return path.resolve(strict=strict)

    def is_symlink(self, path: Path) -> bool:
        return stat_mod.S_ISLNK(self.lstat(path).st_mode)


def _is_empty_string(value: Any) -> bool:
    return isinstance(value, str) and value.strip() == ""


def _is_kebab(value: str) -> bool:
    return bool(_KEBAB_RE.fullmatch(value))


def _is_semver(value: str) -> bool:
    return bool(_SEMVER_RE.fullmatch(value))


def _is_iso_date(value: str) -> bool:
    """Return True only for a real calendar date in YYYY-MM-DD form."""
    if not _ISO_DATE_RE.fullmatch(value):
        return False
    try:
        datetime_mod.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _check_symlink_containment(
    path: Path,
    root: Path,
    fs: ModuleFileSystem,
) -> Containment:
    """Classify symlink containment for an existing path (lstat-able).

    Non-symlinks → NOT_SYMLINK.
    Successfully resolved out-of-root → OUTSIDE (do not follow/stat/read target).
    Broken symlink → BROKEN.
    Resolution/permission failure → ERROR.

    Containment is decided from ``resolve(strict=True)`` before any
    target-following ``stat`` / ``inspect`` / ``read_text`` call. Out-of-root
    targets are never inspected after a successful outside resolve.
    """
    try:
        entry = fs.lstat(path)
    except FileNotFoundError:
        return Containment.NOT_SYMLINK
    except OSError:
        return Containment.ERROR

    if not stat_mod.S_ISLNK(entry.st_mode):
        return Containment.NOT_SYMLINK

    try:
        # strict=True: missing final target → FileNotFoundError (BROKEN),
        # without classifying a dangling out-of-root link as OUTSIDE.
        resolved = fs.resolve(path, strict=True)
        root_resolved = fs.resolve(root, strict=False)
    except FileNotFoundError:
        return Containment.BROKEN
    except OSError:
        return Containment.ERROR

    try:
        resolved.relative_to(root_resolved)
    except ValueError:
        # Outside: stop here — never inspect/stat/read the external target.
        return Containment.OUTSIDE
    return Containment.INSIDE


def _abort_mod021(path: str, error_class: Optional[str] = None) -> None:
    finding = _finding(
        "MOD-021",
        severity=Severity.ERROR,
        path=path,
        error_class=error_class or "OSError",
    )
    raise _Abort(finding)


def _inspect_or_abort(path: Path, rel: str, fs: ModuleFileSystem) -> PathKind:
    inspection = fs.inspect(path)
    if inspection.kind is PathKind.ERROR:
        _abort_mod021(rel, inspection.error_class)
    return inspection.kind


def _entry_classification(
    path: Path,
    rel: str,
    root: Path,
    fs: ModuleFileSystem,
) -> tuple[str, Optional[PathKind]]:
    """Classify an in-scope path for entry-point / discovery use.

    Returns ``(result, kind)`` where result is one of:
    ``missing``, ``file``, ``directory``, ``other``, ``outside``, ``error``.
    ``error`` always raises ``_Abort`` instead of returning.
    """
    # Probe existence via lstat first for containment on symlinks.
    try:
        entry = fs.lstat(path)
    except FileNotFoundError:
        return "missing", PathKind.MISSING
    except OSError as exc:
        _abort_mod021(rel, type(exc).__name__)

    if stat_mod.S_ISLNK(entry.st_mode):
        containment = _check_symlink_containment(path, root, fs)
        if containment is Containment.ERROR:
            _abort_mod021(rel)
        if containment is Containment.OUTSIDE:
            return "outside", None
        if containment is Containment.BROKEN:
            return "other", PathKind.OTHER
        # INSIDE (or NOT_SYMLINK unexpected): fall through to inspect type
        kind = _inspect_or_abort(path, rel, fs)
        if kind is PathKind.FILE:
            return "file", kind
        if kind is PathKind.DIRECTORY:
            return "directory", kind
        if kind is PathKind.MISSING:
            return "missing", kind
        return "other", kind

    kind = _inspect_or_abort(path, rel, fs)
    if kind is PathKind.FILE:
        return "file", kind
    if kind is PathKind.DIRECTORY:
        return "directory", kind
    if kind is PathKind.MISSING:
        return "missing", kind
    return "other", kind


def _resolve_framework_root(
    *,
    explicit_root: Optional[Path],
    start: Optional[Path],
    fs: ModuleFileSystem,
) -> Optional[Path]:
    """Return Framework root for Module discovery, or None if none usable."""
    if explicit_root is not None:
        root_path = Path(explicit_root)
        kind = _inspect_or_abort(root_path, _rel(str(root_path)), fs)
        if kind is not PathKind.DIRECTORY:
            return None
        return root_path

    starting = Path(start) if start is not None else Path.cwd()
    root, _findings, execution_error = _discover_upward(starting, fs)
    if execution_error is not None:
        # Incomplete discovery — surface as MOD-021 at the discovery boundary.
        _abort_mod021(_rel(str(starting)), "DiscoveryIncomplete")
    return root


def _discover_candidates(
    root: Path,
    fs: ModuleFileSystem,
) -> tuple[list[Path], list[Finding]]:
    """Discover Module candidate directories under ``modules/``."""
    findings: list[Finding] = []
    modules_path = root / "modules"
    modules_rel = "modules"

    result, kind = _entry_classification(modules_path, modules_rel, root, fs)

    if result == "missing":
        return [], []
    if result == "outside":
        findings.append(
            _finding("MOD-024", severity=Severity.ERROR, path=modules_rel)
        )
        return [], findings
    if result in {"file", "other"}:
        findings.append(
            _finding("MOD-019", severity=Severity.ERROR, path=modules_rel)
        )
        return [], findings
    # directory
    try:
        children = fs.iterdir(modules_path)
    except OSError as exc:
        _abort_mod021(modules_rel, type(exc).__name__)

    candidates: list[Path] = []
    for child in children:
        name = child.name
        child_rel = _rel(f"modules/{name}")
        if name == "README.md":
            continue

        cres, _ckind = _entry_classification(child, child_rel, root, fs)
        if cres == "outside":
            findings.append(
                _finding("MOD-024", severity=Severity.ERROR, path=child_rel)
            )
            continue
        if cres == "directory":
            candidates.append(child)
            continue
        # missing should not occur for listed children; treat as unexpected
        findings.append(
            _finding("MOD-018", severity=Severity.WARNING, path=child_rel)
        )

    return candidates, findings


def _validate_metadata_fields(
    data: Mapping[str, Any],
    yaml_rel: str,
    ctx: _CandidateContext,
) -> None:
    """Validate metadata mapping fields per design §5 / R8 / D8."""
    # --- status first (drives D8 severity and lifecycle) ---
    status_known = False
    status_value: Optional[str] = None

    def _field_path(field_name: str) -> str:
        """Distinct path so (rule, path) aggregation keeps per-field findings."""
        return f"{yaml_rel}#{field_name}"

    if "status" not in data or data["status"] is None or _is_empty_string(data["status"]):
        ctx.findings.append(
            _finding(
                "MOD-004",
                severity=Severity.ERROR,
                path=_field_path("status"),
                field="status",
            )
        )
    elif not isinstance(data["status"], str):
        ctx.findings.append(
            _finding(
                "MOD-005",
                severity=Severity.ERROR,
                path=_field_path("status"),
                field="status",
            )
        )
    elif data["status"] not in STATUS_VALUES:
        # Non-empty invalid enum
        ctx.findings.append(
            _finding("MOD-008", severity=Severity.ERROR, path=yaml_rel)
        )
    else:
        status_known = True
        status_value = data["status"]
        ctx.status = status_value

    draft_lenient = status_known and status_value == "draft"
    required_missing_severity = (
        Severity.WARNING if draft_lenient else Severity.ERROR
    )

    def _required_string(field_name: str, *, format_code: Optional[str] = None) -> Optional[str]:
        # R8: missing/empty → MOD-004; else wrong type → MOD-005; else format.
        fpath = _field_path(field_name)
        if field_name not in data or data[field_name] is None:
            ctx.findings.append(
                _finding(
                    "MOD-004",
                    severity=required_missing_severity,
                    path=fpath,
                    field=field_name,
                )
            )
            return None
        value = data[field_name]
        if isinstance(value, str) and value.strip() == "":
            ctx.findings.append(
                _finding(
                    "MOD-004",
                    severity=required_missing_severity,
                    path=fpath,
                    field=field_name,
                )
            )
            return None
        if not isinstance(value, str):
            ctx.findings.append(
                _finding(
                    "MOD-005",
                    severity=Severity.ERROR,
                    path=fpath,
                    field=field_name,
                )
            )
            return None
        if format_code == "MOD-006" and not _is_kebab(value):
            ctx.findings.append(
                _finding("MOD-006", severity=Severity.ERROR, path=fpath)
            )
            return None
        if format_code == "MOD-007" and not _is_semver(value):
            ctx.findings.append(
                _finding(
                    "MOD-007",
                    severity=Severity.ERROR,
                    path=fpath,
                    field=field_name,
                )
            )
            return None
        return value

    module_id = _required_string("id", format_code="MOD-006")
    if module_id is not None:
        ctx.module_id = module_id
    _required_string("version", format_code="MOD-007")
    _required_string("title")
    _required_string("summary")

    # maturity (optional)
    if "maturity" in data and data["maturity"] is not None:
        mat = data["maturity"]
        if not isinstance(mat, str):
            ctx.findings.append(
                _finding(
                    "MOD-005",
                    severity=Severity.ERROR,
                    path=_field_path("maturity"),
                    field="maturity",
                )
            )
        elif mat not in MATURITY_VALUES:
            ctx.findings.append(
                _finding(
                    "MOD-009",
                    severity=Severity.ERROR,
                    path=_field_path("maturity"),
                )
            )
        elif status_known and status_value == "deprecated":
            ctx.findings.append(
                _finding("MOD-015", severity=Severity.WARNING, path=yaml_rel)
            )

    # applies_when / avoid_when
    for list_field in ("applies_when", "avoid_when"):
        if list_field not in data or data[list_field] is None:
            ctx.findings.append(
                _finding(
                    "MOD-014",
                    severity=Severity.WARNING,
                    path=_field_path(list_field),
                    field=list_field,
                )
            )
        else:
            value = data[list_field]
            if not isinstance(value, list):
                ctx.findings.append(
                    _finding(
                        "MOD-005",
                        severity=Severity.ERROR,
                        path=_field_path(list_field),
                        field=list_field,
                    )
                )
            elif not all(isinstance(item, str) for item in value):
                ctx.findings.append(
                    _finding(
                        "MOD-005",
                        severity=Severity.ERROR,
                        path=_field_path(list_field),
                        field=list_field,
                    )
                )

    # tags
    if "tags" in data and data["tags"] is not None:
        tags = data["tags"]
        if not isinstance(tags, list):
            ctx.findings.append(
                _finding(
                    "MOD-005",
                    severity=Severity.ERROR,
                    path=_field_path("tags"),
                    field="tags",
                )
            )
        elif not all(isinstance(item, str) for item in tags):
            ctx.findings.append(
                _finding(
                    "MOD-005",
                    severity=Severity.ERROR,
                    path=_field_path("tags"),
                    field="tags",
                )
            )
        else:
            for tag in tags:
                if not _is_kebab(tag):
                    ctx.findings.append(
                        _finding(
                            "MOD-023",
                            severity=Severity.WARNING,
                            path=f"{yaml_rel}#tag:{tag}",
                            tag=tag,
                        )
                    )

    # provides
    if "provides" in data and data["provides"] is not None:
        provides = data["provides"]
        if not isinstance(provides, list) or not all(
            isinstance(item, str) for item in provides
        ):
            ctx.findings.append(
                _finding(
                    "MOD-005",
                    severity=Severity.ERROR,
                    path=_field_path("provides"),
                    field="provides",
                )
            )

    # requires_core (optional)
    if "requires_core" in data and data["requires_core"] is not None:
        rc = data["requires_core"]
        if _is_empty_string(rc):
            ctx.findings.append(
                _finding(
                    "MOD-007",
                    severity=Severity.ERROR,
                    path=_field_path("requires_core"),
                    field="requires_core",
                )
            )
        elif not isinstance(rc, str):
            ctx.findings.append(
                _finding(
                    "MOD-005",
                    severity=Severity.ERROR,
                    path=_field_path("requires_core"),
                    field="requires_core",
                )
            )
        elif not _is_semver(rc):
            ctx.findings.append(
                _finding(
                    "MOD-007",
                    severity=Severity.ERROR,
                    path=_field_path("requires_core"),
                    field="requires_core",
                )
            )

    # dependencies forbidden
    if "dependencies" in data:
        ctx.findings.append(
            _finding("MOD-010", severity=Severity.ERROR, path=yaml_rel)
        )

    # unknown top-level keys (not dependencies)
    for key in data:
        if key == "dependencies":
            continue
        if key not in KNOWN_TOP_LEVEL:
            ctx.findings.append(
                _finding(
                    "MOD-013",
                    severity=Severity.WARNING,
                    path=f"{yaml_rel}#field:{key}",
                    field=str(key),
                )
            )

    # deprecation object
    if "deprecation" in data and data["deprecation"] is not None:
        dep = data["deprecation"]
        if not isinstance(dep, Mapping):
            ctx.findings.append(
                _finding("MOD-011", severity=Severity.ERROR, path=yaml_rel)
            )
        elif not (status_known and status_value == "deprecated"):
            ctx.findings.append(
                _finding("MOD-011", severity=Severity.ERROR, path=yaml_rel)
            )
        else:
            # reason recommended
            if "reason" not in dep or dep["reason"] is None or _is_empty_string(
                dep.get("reason")
            ):
                # missing reason → MOD-016; wrong type for reason → MOD-005?
                if "reason" in dep and dep["reason"] is not None and not isinstance(
                    dep["reason"], str
                ):
                    ctx.findings.append(
                        _finding(
                            "MOD-005",
                            severity=Severity.ERROR,
                            path=_field_path("deprecation.reason"),
                            field="deprecation.reason",
                        )
                    )
                else:
                    ctx.findings.append(
                        _finding(
                            "MOD-016", severity=Severity.WARNING, path=yaml_rel
                        )
                    )
            elif not isinstance(dep["reason"], str):
                ctx.findings.append(
                    _finding(
                        "MOD-005",
                        severity=Severity.ERROR,
                        path=_field_path("deprecation.reason"),
                        field="deprecation.reason",
                    )
                )

            if "successor" in dep and dep["successor"] is not None:
                succ = dep["successor"]
                if not isinstance(succ, str):
                    ctx.findings.append(
                        _finding(
                            "MOD-005",
                            severity=Severity.ERROR,
                            path=_field_path("deprecation.successor"),
                            field="deprecation.successor",
                        )
                    )
                elif not _is_empty_string(succ) and not _is_kebab(succ):
                    ctx.findings.append(
                        _finding(
                            "MOD-022", severity=Severity.WARNING, path=yaml_rel
                        )
                    )

            if "sunset" in dep and dep["sunset"] is not None:
                sunset = dep["sunset"]
                if not isinstance(sunset, str):
                    ctx.findings.append(
                        _finding(
                            "MOD-005",
                            severity=Severity.ERROR,
                            path=_field_path("deprecation.sunset"),
                            field="deprecation.sunset",
                        )
                    )
                elif not _is_empty_string(sunset) and not _is_iso_date(sunset):
                    ctx.findings.append(
                        _finding(
                            "MOD-025", severity=Severity.ERROR, path=yaml_rel
                        )
                    )
    # R9: missing deprecation object when deprecated → no finding

    # D3 directory name vs id
    if ctx.module_id is not None and ctx.module_id != ctx.dir_name:
        ctx.findings.append(
            _finding(
                "MOD-017",
                severity=Severity.WARNING,
                path=ctx.rel_dir,
            )
        )


def _validate_readme(
    ctx: _CandidateContext,
    root: Path,
    fs: ModuleFileSystem,
) -> None:
    """Lifecycle-independent D12 + status-dependent MOD-002 / MOD-012."""
    readme_path = ctx.abs_dir / "README.md"
    readme_rel = _rel(f"{ctx.rel_dir}/README.md")

    result, _kind = _entry_classification(readme_path, readme_rel, root, fs)

    if result == "outside":
        ctx.findings.append(
            _finding("MOD-024", severity=Severity.ERROR, path=readme_rel)
        )
        return

    status = ctx.status  # known valid or None

    if result in {"missing", "other", "directory"}:
        # wrong type includes directory / OTHER / broken
        if status is not None:
            severity = (
                Severity.WARNING if status == "draft" else Severity.ERROR
            )
            ctx.findings.append(
                _finding("MOD-002", severity=severity, path=readme_rel)
            )
        # unknown status: no MOD-002 / MOD-012
        return

    if result != "file":
        return

    # Existing in-root readable file — Migration check only for deprecated
    if status != "deprecated":
        return

    try:
        text = fs.read_text(readme_path)
    except OSError as exc:
        _abort_mod021(readme_rel, type(exc).__name__)

    has_migration = any(
        line.strip() == _MIGRATION_HEADING for line in text.splitlines()
    )
    if not has_migration:
        ctx.findings.append(
            _finding("MOD-012", severity=Severity.ERROR, path=readme_rel)
        )


def _validate_candidate(
    candidate: Path,
    root: Path,
    fs: ModuleFileSystem,
) -> list[Finding]:
    dir_name = candidate.name
    rel_dir = _rel(f"modules/{dir_name}")
    ctx = _CandidateContext(
        dir_name=dir_name,
        rel_dir=rel_dir,
        abs_dir=candidate,
    )

    yaml_path = candidate / "module.yaml"
    yaml_rel = _rel(f"{rel_dir}/module.yaml")

    result, _kind = _entry_classification(yaml_path, yaml_rel, root, fs)

    if result == "outside":
        ctx.findings.append(
            _finding("MOD-024", severity=Severity.ERROR, path=yaml_rel)
        )
        _validate_readme(ctx, root, fs)
        return list(ctx.findings)

    if result in {"missing", "other", "directory"}:
        ctx.findings.append(
            _finding("MOD-001", severity=Severity.WARNING, path=yaml_rel)
        )
        # status remains unknown — README lifecycle skip; D12 still runs
        _validate_readme(ctx, root, fs)
        return list(ctx.findings)

    # Usable in-root file — read and parse
    try:
        raw = fs.read_text(yaml_path)
    except OSError as exc:
        _abort_mod021(yaml_rel, type(exc).__name__)

    try:
        loaded = yaml.safe_load(raw)
    except yaml.YAMLError:
        ctx.findings.append(
            _finding("MOD-003", severity=Severity.ERROR, path=yaml_rel)
        )
        _validate_readme(ctx, root, fs)
        return list(ctx.findings)

    if not isinstance(loaded, Mapping):
        ctx.findings.append(
            _finding("MOD-003", severity=Severity.ERROR, path=yaml_rel)
        )
        _validate_readme(ctx, root, fs)
        return list(ctx.findings)

    _validate_metadata_fields(loaded, yaml_rel, ctx)
    _validate_readme(ctx, root, fs)
    return list(ctx.findings)


def validate_module_contract(
    *,
    explicit_root: Optional[Path] = None,
    start: Optional[Path] = None,
    fs: Optional[ModuleFileSystem] = None,
) -> ValidationResult:
    """Run Module Contract Validation and return a ValidationResult."""
    filesystem = fs or ModuleFileSystem()
    findings: list[Finding] = []

    try:
        root = _resolve_framework_root(
            explicit_root=explicit_root,
            start=start,
            fs=filesystem,
        )
        if root is None:
            return ValidationResult(findings=())

        candidates, discovery_findings = _discover_candidates(root, filesystem)
        findings.extend(discovery_findings)

        for candidate in candidates:
            findings.extend(_validate_candidate(candidate, root, filesystem))

    except _Abort as abort:
        findings.append(abort.finding)
        return ValidationResult(
            findings=aggregate_findings(findings),
            execution_error=abort.finding.message,
        )

    return ValidationResult(findings=aggregate_findings(findings))


def make_module_contract_runner(
    *,
    explicit_root: Optional[Path] = None,
    start: Optional[Path] = None,
    fs: Optional[ModuleFileSystem] = None,
) -> Callable[[], Sequence[Finding]]:
    """Return an orchestrator-compatible callable.

    Execution failures (MOD-021) raise ``ValidatorAbortError`` for exit 2.
    """
    from .orchestrator import ValidatorAbortError

    def _run() -> Sequence[Finding]:
        result = validate_module_contract(
            explicit_root=explicit_root,
            start=start,
            fs=fs,
        )
        if result.execution_error is not None:
            raise ValidatorAbortError(result.execution_error, result.findings)
        return result.findings

    return _run
