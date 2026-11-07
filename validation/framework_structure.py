"""Phase 8.2 Framework Structure Validator (read-only)."""

from __future__ import annotations

import os
import stat as stat_mod
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Callable, Optional, Sequence

from .models import Finding, Severity, ValidationResult, aggregate_findings

CATEGORY = "framework-structure"

REQUIRED_FILES: tuple[str, ...] = (
    "README.md",
    "AGENTS.md",
    "MANIFEST.md",
    "PROJECT_STRUCTURE.md",
    "ROADMAP.md",
    "VERSION",
    "docs/FRAMEWORK_CONTRACT.md",
    "scripts/aiosctl.py",
)

REQUIRED_DIRECTORIES: tuple[str, ...] = (
    "docs",
    "rules",
    "methodology",
    "scripts",
    "tests",
)

ROOT_MARKERS: tuple[str, ...] = (
    "VERSION",
    "MANIFEST.md",
    "PROJECT_STRUCTURE.md",
    "docs/FRAMEWORK_CONTRACT.md",
)

GITHUB_PATH = ".github"

MSG = {
    "STR-001": "Required framework file is missing: {path}",
    "STR-002": "Required framework directory is missing: {path}",
    "STR-003": "Required path must be a file: {path}",
    "STR-004": "Required path must be a directory: {path}",
    "STR-005": "AIOS Framework root was not found.",
    "STR-006": (
        "Framework path or discovery marker could not be inspected: "
        "{path} ({error_class})"
    ),
    "STR-007": "Conditional path .github must be a directory when present.",
    "STR-008": "Explicit validation root is missing or not a directory: {path}",
    "STR-009": (
        "Explicit validation root is not an AIOS framework candidate "
        "(fewer than two root markers)."
    ),
}

SUGGESTION = {
    "STR-001": (
        "Create the required file at the Framework root "
        "(or restore it from AIOS Core)."
    ),
    "STR-002": (
        "Create the required directory at the Framework root "
        "(or restore it from AIOS Core)."
    ),
    "STR-003": (
        "Replace or relocate the non-file entry so {path} resolves to a regular file."
    ),
    "STR-004": (
        "Replace or relocate the non-directory entry so {path} resolves to a directory."
    ),
    "STR-005": (
        "Run from inside an AIOS framework repository, or pass --root to an "
        "explicit Framework root."
    ),
    "STR-006": (
        "Resolve the filesystem error preventing inspection of {path}, "
        "then re-run validation."
    ),
    "STR-007": "Ensure .github is a directory, or remove the non-directory entry.",
    "STR-008": "Pass --root with an existing directory path.",
    "STR-009": (
        "Point --root at a directory containing at least two of: VERSION, "
        "MANIFEST.md, PROJECT_STRUCTURE.md, docs/FRAMEWORK_CONTRACT.md."
    ),
}


class PathKind(str, Enum):
    MISSING = "missing"
    FILE = "file"
    DIRECTORY = "directory"
    OTHER = "other"
    ERROR = "error"


@dataclass(frozen=True)
class PathInspection:
    kind: PathKind
    error_class: Optional[str] = None


class FileSystem:
    """Read-only filesystem operations (injectable for tests).

    Classification uses explicit ``lstat`` / ``stat`` so permission and I/O
    errors are not confused with missing paths (pathlib ``exists`` /
    ``is_file`` / ``is_dir`` OSError-suppression differs across Python
    versions).
    """

    def lstat(self, path: Path) -> os.stat_result:
        return path.lstat()

    def stat(self, path: Path) -> os.stat_result:
        """Follow one symbolic-link level (``Path.stat`` default)."""
        return path.stat()

    def inspect(self, path: Path) -> PathInspection:
        try:
            entry = self.lstat(path)
        except OSError as exc:
            return self._classify_lookup_error(exc, missing_kind=PathKind.MISSING)

        if stat_mod.S_ISLNK(entry.st_mode):
            try:
                target = self.stat(path)
            except OSError as exc:
                # Broken link (FileNotFoundError) and NotADirectoryError → OTHER.
                return self._classify_lookup_error(exc, missing_kind=PathKind.OTHER)
            return self._kind_from_mode(target.st_mode)

        return self._kind_from_mode(entry.st_mode)

    @staticmethod
    def _classify_lookup_error(
        exc: OSError,
        *,
        missing_kind: PathKind,
    ) -> PathInspection:
        """Map lookup failures without treating all OSError as ERROR.

        - ``FileNotFoundError`` → ``missing_kind`` (MISSING for entries;
          OTHER for unresolved symlink targets).
        - ``NotADirectoryError`` → OTHER (a path component is a non-directory).
        - Other ``OSError`` (permission, I/O, …) → ERROR.
        """
        if isinstance(exc, FileNotFoundError):
            return PathInspection(missing_kind)
        if isinstance(exc, NotADirectoryError):
            return PathInspection(PathKind.OTHER)
        return PathInspection(PathKind.ERROR, type(exc).__name__)

    @staticmethod
    def _kind_from_mode(mode: int) -> PathInspection:
        if stat_mod.S_ISREG(mode):
            return PathInspection(PathKind.FILE)
        if stat_mod.S_ISDIR(mode):
            return PathInspection(PathKind.DIRECTORY)
        return PathInspection(PathKind.OTHER)


class CandidateStatus(str, Enum):
    CANDIDATE = "candidate"
    NOT_CANDIDATE = "not_candidate"
    INCOMPLETE = "incomplete"


@dataclass
class CandidateOutcome:
    status: CandidateStatus
    findings: list[Finding] = field(default_factory=list)
    execution_error: Optional[str] = None
    inspected_markers: list[str] = field(default_factory=list)


def _rel(path: str) -> str:
    return path.replace("\\", "/")


def _finding(
    code: str,
    *,
    path: Optional[str] = None,
    error_class: Optional[str] = None,
) -> Finding:
    message_template = MSG[code]
    suggestion_template = SUGGESTION[code]
    display_path = path if path is not None else "-"
    message = message_template.format(path=display_path, error_class=error_class or "OSError")
    suggestion = suggestion_template.format(path=display_path)
    return Finding(
        code=code,
        severity=Severity.ERROR,
        category=CATEGORY,
        message=message,
        path=path,
        rule=code,
        suggestion=suggestion,
    )


def evaluate_candidate(directory: Path, fs: FileSystem) -> CandidateOutcome:
    """Determine whether ``directory`` is a Framework root candidate."""
    valid = 0
    inspected: list[str] = []
    for marker in ROOT_MARKERS:
        if valid >= 2:
            break
        marker_path = directory / marker
        inspected.append(marker)
        inspection = fs.inspect(marker_path)
        if inspection.kind is PathKind.ERROR:
            finding = _finding(
                "STR-006",
                path=_rel(marker),
                error_class=inspection.error_class,
            )
            message = finding.message
            return CandidateOutcome(
                status=CandidateStatus.INCOMPLETE,
                findings=[finding],
                execution_error=message,
                inspected_markers=inspected,
            )
        if inspection.kind is PathKind.FILE:
            valid += 1
    if valid >= 2:
        return CandidateOutcome(
            status=CandidateStatus.CANDIDATE,
            inspected_markers=inspected,
        )
    return CandidateOutcome(
        status=CandidateStatus.NOT_CANDIDATE,
        inspected_markers=inspected,
    )


def _validate_required_paths(root: Path, fs: FileSystem) -> tuple[list[Finding], Optional[str]]:
    findings: list[Finding] = []
    execution_error: Optional[str] = None

    for rel in REQUIRED_FILES:
        target = root / rel
        inspection = fs.inspect(target)
        rel_path = _rel(rel)
        if inspection.kind is PathKind.MISSING:
            findings.append(_finding("STR-001", path=rel_path))
        elif inspection.kind is PathKind.ERROR:
            finding = _finding(
                "STR-006",
                path=rel_path,
                error_class=inspection.error_class,
            )
            findings.append(finding)
            execution_error = finding.message
            break
        elif inspection.kind is not PathKind.FILE:
            findings.append(_finding("STR-003", path=rel_path))

    if execution_error is not None:
        return findings, execution_error

    for rel in REQUIRED_DIRECTORIES:
        target = root / rel
        inspection = fs.inspect(target)
        rel_path = _rel(rel)
        if inspection.kind is PathKind.MISSING:
            findings.append(_finding("STR-002", path=rel_path))
        elif inspection.kind is PathKind.ERROR:
            finding = _finding(
                "STR-006",
                path=rel_path,
                error_class=inspection.error_class,
            )
            findings.append(finding)
            execution_error = finding.message
            break
        elif inspection.kind is not PathKind.DIRECTORY:
            findings.append(_finding("STR-004", path=rel_path))

    return findings, execution_error


def _validate_github(root: Path, fs: FileSystem) -> tuple[list[Finding], Optional[str]]:
    target = root / GITHUB_PATH
    inspection = fs.inspect(target)
    if inspection.kind is PathKind.MISSING:
        return [], None
    if inspection.kind is PathKind.DIRECTORY:
        return [], None
    if inspection.kind is PathKind.ERROR:
        finding = _finding(
            "STR-006",
            path=GITHUB_PATH,
            error_class=inspection.error_class,
        )
        return [finding], finding.message
    return [_finding("STR-007", path=GITHUB_PATH)], None


def _discover_upward(
    start: Path,
    fs: FileSystem,
) -> tuple[Optional[Path], list[Finding], Optional[str]]:
    current = start.resolve(strict=False)
    findings: list[Finding] = []
    while True:
        outcome = evaluate_candidate(current, fs)
        if outcome.status is CandidateStatus.CANDIDATE:
            return current, [], None
        if outcome.status is CandidateStatus.INCOMPLETE:
            return None, list(outcome.findings), outcome.execution_error
        parent = current.parent
        if parent == current:
            break
        current = parent
    return None, [_finding("STR-005")], None


def validate_framework_structure(
    *,
    explicit_root: Optional[Path] = None,
    start: Optional[Path] = None,
    fs: Optional[FileSystem] = None,
) -> ValidationResult:
    """Run Framework Structure Validation and return a ValidationResult."""
    filesystem = fs or FileSystem()
    findings: list[Finding] = []

    if explicit_root is not None:
        root_path = Path(explicit_root)
        try:
            inspection = filesystem.inspect(root_path)
        except OSError as exc:  # pragma: no cover - inspect already traps OSError
            finding = _finding(
                "STR-006",
                path=_rel(str(root_path)),
                error_class=type(exc).__name__,
            )
            return ValidationResult(
                findings=aggregate_findings([finding]),
                execution_error=finding.message,
            )

        if inspection.kind is PathKind.ERROR:
            finding = _finding(
                "STR-006",
                path=_rel(str(root_path)),
                error_class=inspection.error_class,
            )
            return ValidationResult(
                findings=aggregate_findings([finding]),
                execution_error=finding.message,
            )
        if inspection.kind is PathKind.MISSING or inspection.kind is not PathKind.DIRECTORY:
            finding = _finding("STR-008", path=_rel(str(root_path)))
            return ValidationResult(findings=aggregate_findings([finding]))

        outcome = evaluate_candidate(root_path, filesystem)
        if outcome.status is CandidateStatus.INCOMPLETE:
            return ValidationResult(
                findings=aggregate_findings(outcome.findings),
                execution_error=outcome.execution_error,
            )
        if outcome.status is CandidateStatus.NOT_CANDIDATE:
            finding = _finding("STR-009", path=_rel(str(root_path)))
            return ValidationResult(findings=aggregate_findings([finding]))
        root = root_path
    else:
        starting = Path(start) if start is not None else Path.cwd()
        root, discovery_findings, execution_error = _discover_upward(starting, filesystem)
        if execution_error is not None:
            return ValidationResult(
                findings=aggregate_findings(discovery_findings),
                execution_error=execution_error,
            )
        if root is None:
            return ValidationResult(findings=aggregate_findings(discovery_findings))

    required_findings, execution_error = _validate_required_paths(root, filesystem)
    findings.extend(required_findings)
    if execution_error is not None:
        return ValidationResult(
            findings=aggregate_findings(findings),
            execution_error=execution_error,
        )

    github_findings, execution_error = _validate_github(root, filesystem)
    findings.extend(github_findings)
    if execution_error is not None:
        return ValidationResult(
            findings=aggregate_findings(findings),
            execution_error=execution_error,
        )

    return ValidationResult(findings=aggregate_findings(findings))


def make_framework_structure_runner(
    *,
    explicit_root: Optional[Path] = None,
    start: Optional[Path] = None,
    fs: Optional[FileSystem] = None,
) -> Callable[[], Sequence[Finding]]:
    """Return an orchestrator-compatible callable.

    Execution failures (STR-006 unreliable completion) are surfaced by raising
    :class:`validation.orchestrator.ValidatorAbortError` so Phase 8.1.2 exit
    code 2 semantics apply while preserving findings.
    """
    from .orchestrator import ValidatorAbortError

    def _run() -> Sequence[Finding]:
        result = validate_framework_structure(
            explicit_root=explicit_root,
            start=start,
            fs=fs,
        )
        if result.execution_error is not None:
            raise ValidatorAbortError(result.execution_error, result.findings)
        return result.findings

    return _run
