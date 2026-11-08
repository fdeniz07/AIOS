"""Phase 8.4 Documentation Integrity Validator (read-only).

Inspects repository Markdown for broken local links/anchors/images while
preserving Phase 8.3 D12 containment guarantees.
"""

from __future__ import annotations

import re
import stat as stat_mod
from dataclasses import dataclass, field
from enum import Enum
from html.parser import HTMLParser
from pathlib import Path
from typing import Callable, Optional, Sequence
from urllib.parse import unquote

from markdown_it import MarkdownIt

from .framework_structure import FileSystem, PathKind, _discover_upward
from .models import Finding, Severity, ValidationResult, aggregate_findings

CATEGORY = "documentation-integrity"

MARKDOWN_SUFFIXES = frozenset({".md", ".markdown", ".mdown", ".mkd", ".mkdn"})

_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

# GitHub-compatible slug: drop punctuation GitHub removes; keep Unicode letters.
_GITHUB_PUNCT_RE = re.compile(
    r"[\u2000-\u206F\u2E00-\u2E7F\\'\"!#$%&()*+,./:;<=>?@\[\]^`{|}~]"
)

MSG = {
    "DOC-001": "Local link target does not exist: {target} ({path})",
    "DOC-002": "Local link target has an incompatible type: {target} ({path})",
    "DOC-003": "Local reference escapes the repository root: {target} ({path})",
    "DOC-004": "Local anchor target does not exist: {target} ({path})",
    "DOC-005": (
        "Documentation cannot be reliably inspected or processed: "
        "{path} ({error_class})"
    ),
    "DOC-006": "Local image target does not exist: {target} ({path})",
}

SUGGESTION = {
    "DOC-001": "Create the missing local target or correct the Markdown link href.",
    "DOC-002": "Point the link at a compatible file or directory target.",
    "DOC-003": "Replace the out-of-root path or symlink with an in-repository target.",
    "DOC-004": "Fix the fragment to match a heading slug or explicit HTML id/name.",
    "DOC-005": "Resolve the filesystem or parse error preventing inspection of {path}.",
    "DOC-006": "Create the missing local image or correct the image reference.",
}


class Containment(str, Enum):
    INSIDE = "inside"
    OUTSIDE = "outside"
    BROKEN = "broken"
    ERROR = "error"
    NOT_SYMLINK = "not_symlink"


@dataclass
class _Abort(Exception):
    finding: Finding


@dataclass(frozen=True)
class _Ref:
    """A local Markdown/HTML reference extracted from a source document."""

    href: str
    kind: str  # "link" | "image"
    line: Optional[int]


@dataclass
class _DocInfo:
    rel: str
    abs_path: Path
    anchors: set[str] = field(default_factory=set)
    refs: list[_Ref] = field(default_factory=list)


class DocFileSystem(FileSystem):
    """FileSystem plus discovery/read/resolve hooks for documentation validation."""

    def iterdir(self, path: Path) -> list[Path]:
        return sorted(path.iterdir(), key=lambda p: p.name.lower())

    def read_text(self, path: Path) -> str:
        return path.read_text(encoding="utf-8")

    def resolve(self, path: Path, *, strict: bool = False) -> Path:
        return path.resolve(strict=strict)

    def is_symlink(self, path: Path) -> bool:
        return stat_mod.S_ISLNK(self.lstat(path).st_mode)


def _rel(path: str) -> str:
    return path.replace("\\", "/")


def _finding(
    code: str,
    *,
    path: Optional[str] = None,
    target: Optional[str] = None,
    error_class: Optional[str] = None,
    line: Optional[int] = None,
) -> Finding:
    display_path = path if path is not None else "-"
    if line is not None and path is not None and f":{line}" not in display_path:
        # Keep human message informative; identity path may already include line.
        message_path = f"{path}:{line}"
    else:
        message_path = display_path
    message = MSG[code].format(
        path=message_path,
        target=target or "-",
        error_class=error_class or "OSError",
    )
    suggestion = SUGGESTION[code].format(path=display_path, target=target or "-")
    # Distinct (rule, path) so multiple refs in one file are not collapsed.
    identity_path = path
    if path is not None:
        parts = [path]
        if line is not None:
            parts.append(f"L{line}")
        if target is not None:
            parts.append(target)
        identity_path = "#".join(parts)
    return Finding(
        code=code,
        severity=Severity.ERROR,
        category=CATEGORY,
        message=message,
        path=identity_path,
        rule=code,
        suggestion=suggestion,
    )


def github_heading_slug(text: str) -> str:
    """Return a GitHub-compatible heading slug for ``text``.

    Behavior (documented + tested):
    - Trim and lowercase (Unicode-aware via ``str.lower``).
    - Remove punctuation characters GitHub strips (ASCII + common Unicode
      punctuation ranges), preserving letters (including German/Turkish),
      digits, spaces, hyphens, and underscores.
    - Replace whitespace runs with a single hyphen.
    - Strip leading/trailing hyphens.
    - Duplicate headings are disambiguated by callers via ``unique_slug``.
    """
    value = text.strip().lower()
    value = _GITHUB_PUNCT_RE.sub("", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-")


def unique_slug(base: str, seen: dict[str, int]) -> str:
    """Return a distinct slug for ``base``, appending ``-N`` for repeats."""
    count = seen.get(base, 0)
    seen[base] = count + 1
    if count == 0:
        return base
    return f"{base}-{count}"


def _is_external_href(href: str) -> bool:
    if not href or href.startswith("//"):
        return True
    match = _SCHEME_RE.match(href)
    if not match:
        return False
    # Any explicit URI scheme is non-local (http, mailto, tel, data, drive letters, …).
    return True


def _split_href(href: str) -> tuple[str, str]:
    """Return ``(path_part, fragment)`` without the leading ``#`` on fragment."""
    if href.startswith("#"):
        return "", href[1:]
    if "#" in href:
        path_part, frag = href.split("#", 1)
    else:
        path_part, frag = href, ""
    # Ignore query string for filesystem resolution.
    if "?" in path_part:
        path_part = path_part.split("?", 1)[0]
    return path_part, frag


class _HtmlRefParser(HTMLParser):
    """Collect href/src/id/name from HTML fragments inside Markdown."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hrefs: list[str] = []
        self.images: list[str] = []
        self.anchors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        mapping = {k.lower(): v for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "a":
            href = mapping.get("href")
            if href:
                self.hrefs.append(href)
            for key in ("id", "name"):
                value = mapping.get(key)
                if value:
                    self.anchors.append(value)
        elif tag_l == "img":
            src = mapping.get("src")
            if src:
                self.images.append(src)
        else:
            for key in ("id", "name"):
                value = mapping.get(key)
                if value:
                    self.anchors.append(value)


def _plain_text_from_children(children: Optional[Sequence]) -> str:
    if not children:
        return ""
    parts: list[str] = []
    for child in children:
        if child.type in {"text", "code_inline"}:
            parts.append(child.content)
        elif child.type == "softbreak":
            parts.append(" ")
        elif child.type == "image":
            parts.append(_plain_text_from_children(child.children))
        elif child.children:
            parts.append(_plain_text_from_children(child.children))
    return "".join(parts)


def _line_from_map(token_map: Optional[Sequence[int]]) -> Optional[int]:
    if token_map is None or len(token_map) < 1:
        return None
    # markdown-it maps are 0-based start lines; never invent beyond that.
    return int(token_map[0]) + 1


def _parse_markdown_document(text: str) -> tuple[set[str], list[_Ref]]:
    """Parse Markdown into anchors and local-ish references (pre-filter)."""
    md = MarkdownIt("commonmark")
    tokens = md.parse(text)
    anchors: set[str] = set()
    seen_slugs: dict[str, int] = {}
    refs: list[_Ref] = []

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.type == "heading_open":
            line = _line_from_map(token.map)
            inline = tokens[i + 1] if i + 1 < len(tokens) else None
            heading_text = (
                _plain_text_from_children(inline.children)
                if inline is not None and inline.type == "inline"
                else ""
            )
            base = github_heading_slug(heading_text)
            slug = unique_slug(base, seen_slugs)
            if slug:
                anchors.add(slug)
            i += 1
            continue

        if token.type == "fence" or token.type == "code_block":
            # Do not interpret fenced/indented code examples as references.
            i += 1
            continue

        if token.type == "html_block":
            line = _line_from_map(token.map)
            _collect_html(token.content, line, anchors, refs)
            i += 1
            continue

        if token.type == "inline" and token.children:
            line = _line_from_map(token.map)
            for child in token.children:
                if child.type == "link_open":
                    href = child.attrs.get("href") if child.attrs else None
                    if href:
                        refs.append(_Ref(href=str(href), kind="link", line=line))
                elif child.type == "image":
                    src = child.attrs.get("src") if child.attrs else None
                    if src:
                        refs.append(_Ref(href=str(src), kind="image", line=line))
                elif child.type == "html_inline":
                    _collect_html(child.content, line, anchors, refs)
        i += 1

    return anchors, refs


def _collect_html(
    fragment: str,
    line: Optional[int],
    anchors: set[str],
    refs: list[_Ref],
) -> None:
    parser = _HtmlRefParser()
    try:
        parser.feed(fragment)
        parser.close()
    except Exception:  # noqa: BLE001 — malformed HTML is not an execution failure
        return
    for href in parser.hrefs:
        refs.append(_Ref(href=href, kind="link", line=line))
    for src in parser.images:
        refs.append(_Ref(href=src, kind="image", line=line))
    for name in parser.anchors:
        if name:
            anchors.add(name)


def _check_symlink_containment(
    path: Path,
    root: Path,
    fs: DocFileSystem,
) -> Containment:
    """Classify symlink containment (D12). Never follow out-of-root targets."""
    try:
        entry = fs.lstat(path)
    except FileNotFoundError:
        return Containment.NOT_SYMLINK
    except OSError:
        return Containment.ERROR

    if not stat_mod.S_ISLNK(entry.st_mode):
        return Containment.NOT_SYMLINK

    try:
        resolved = fs.resolve(path, strict=True)
        root_resolved = fs.resolve(root, strict=False)
    except FileNotFoundError:
        return Containment.BROKEN
    except OSError:
        return Containment.ERROR

    try:
        resolved.relative_to(root_resolved)
    except ValueError:
        return Containment.OUTSIDE
    return Containment.INSIDE


def _abort_doc005(path: str, error_class: Optional[str] = None) -> None:
    raise _Abort(
        _finding("DOC-005", path=path, error_class=error_class or "OSError")
    )


def _is_markdown_name(name: str) -> bool:
    lower = name.lower()
    return any(lower.endswith(suffix) for suffix in MARKDOWN_SUFFIXES)


def _discover_markdown_files(
    root: Path,
    fs: DocFileSystem,
) -> list[Path]:
    """Deterministically discover Markdown files; never recurse directory symlinks."""
    found: list[Path] = []
    stack: list[Path] = [root]

    while stack:
        current = stack.pop()
        try:
            children = fs.iterdir(current)
        except FileNotFoundError:
            continue
        except OSError as exc:
            rel = _rel_to_root(current, root)
            _abort_doc005(rel, type(exc).__name__)

        # Reverse push so lexicographically smaller names are processed first
        # when using a stack, matching sorted(iterdir) ascending walk order.
        for child in reversed(children):
            name = child.name
            if name == ".git":
                continue
            try:
                entry = fs.lstat(child)
            except FileNotFoundError:
                continue
            except OSError as exc:
                _abort_doc005(_rel_to_root(child, root), type(exc).__name__)

            if stat_mod.S_ISLNK(entry.st_mode):
                containment = _check_symlink_containment(child, root, fs)
                if containment is Containment.ERROR:
                    _abort_doc005(_rel_to_root(child, root))
                if containment is Containment.OUTSIDE:
                    # Do not read external targets; surface boundary violation.
                    # Directory out-of-root links are not descended into.
                    if _is_markdown_name(name):
                        found.append(child)
                    continue
                if containment is Containment.BROKEN:
                    continue
                # In-root symlink: classify target type without reading outside.
                inspection = fs.inspect(child)
                if inspection.kind is PathKind.ERROR:
                    _abort_doc005(
                        _rel_to_root(child, root), inspection.error_class
                    )
                if inspection.kind is PathKind.DIRECTORY:
                    # Do not recursively follow directory symlinks.
                    continue
                if inspection.kind is PathKind.FILE and _is_markdown_name(name):
                    found.append(child)
                continue

            if stat_mod.S_ISDIR(entry.st_mode):
                stack.append(child)
                continue

            if stat_mod.S_ISREG(entry.st_mode) and _is_markdown_name(name):
                found.append(child)

    found.sort(key=lambda p: _rel_to_root(p, root).lower())
    return found


def _rel_to_root(path: Path, root: Path) -> str:
    try:
        return _rel(str(path.relative_to(root)))
    except ValueError:
        return _rel(str(path))


def _resolve_framework_root(
    *,
    explicit_root: Optional[Path],
    start: Optional[Path],
    fs: DocFileSystem,
) -> Optional[Path]:
    if explicit_root is not None:
        root_path = Path(explicit_root)
        inspection = fs.inspect(root_path)
        if inspection.kind is PathKind.ERROR:
            _abort_doc005(_rel(str(root_path)), inspection.error_class)
        if inspection.kind is not PathKind.DIRECTORY:
            return None
        return root_path

    starting = Path(start) if start is not None else Path.cwd()
    root, _findings, execution_error = _discover_upward(starting, fs)
    if execution_error is not None:
        _abort_doc005(_rel(str(starting)), "DiscoveryIncomplete")
    return root


def _load_document(
    path: Path,
    root: Path,
    fs: DocFileSystem,
    findings: list[Finding],
) -> Optional[_DocInfo]:
    rel = _rel_to_root(path, root)

    try:
        entry = fs.lstat(path)
    except FileNotFoundError:
        return None
    except OSError as exc:
        _abort_doc005(rel, type(exc).__name__)

    if stat_mod.S_ISLNK(entry.st_mode):
        containment = _check_symlink_containment(path, root, fs)
        if containment is Containment.ERROR:
            _abort_doc005(rel)
        if containment is Containment.OUTSIDE:
            findings.append(
                _finding("DOC-003", path=rel, target=rel)
            )
            return None
        if containment is Containment.BROKEN:
            _abort_doc005(rel, "BrokenSymlink")

    inspection = fs.inspect(path)
    if inspection.kind is PathKind.ERROR:
        _abort_doc005(rel, inspection.error_class)
    if inspection.kind is not PathKind.FILE:
        return None

    try:
        text = fs.read_text(path)
    except OSError as exc:
        _abort_doc005(rel, type(exc).__name__)

    try:
        anchors, refs = _parse_markdown_document(text)
    except Exception as exc:  # noqa: BLE001 — parser failures → DOC-005
        _abort_doc005(rel, type(exc).__name__)

    return _DocInfo(rel=rel, abs_path=path, anchors=anchors, refs=refs)


def _classify_local_target(
    target: Path,
    root: Path,
    fs: DocFileSystem,
    *,
    source_rel: str,
    missing_code: str,
) -> Optional[str]:
    """Classify a resolved local path; return a finding code or None if OK.

    Never reads file contents of the target. Out-of-root symlinks → DOC-003
    without following/stat/read of the external target.
    """
    try:
        entry = fs.lstat(target)
    except FileNotFoundError:
        return missing_code
    except OSError as exc:
        _abort_doc005(source_rel, type(exc).__name__)

    if stat_mod.S_ISLNK(entry.st_mode):
        containment = _check_symlink_containment(target, root, fs)
        if containment is Containment.ERROR:
            _abort_doc005(source_rel)
        if containment is Containment.OUTSIDE:
            return "DOC-003"
        if containment is Containment.BROKEN:
            return missing_code
        # In-root symlink: inspect type only.
        inspection = fs.inspect(target)
        if inspection.kind is PathKind.ERROR:
            _abort_doc005(source_rel, inspection.error_class)
        if inspection.kind is PathKind.MISSING:
            return missing_code
        if inspection.kind is PathKind.OTHER:
            return "DOC-002"
        if missing_code == "DOC-006" and inspection.kind is not PathKind.FILE:
            return "DOC-002"
        # FILE or DIRECTORY OK for links; images require FILE (handled above).
        return None

    if stat_mod.S_ISREG(entry.st_mode):
        return None
    if stat_mod.S_ISDIR(entry.st_mode):
        if missing_code == "DOC-006":
            return "DOC-002"
        return None
    return "DOC-002"


def _resolve_local_path(
    path_part: str,
    source_file: Path,
    root: Path,
) -> Path:
    """Resolve a local href path against the source directory or repo root."""
    decoded = unquote(path_part)
    if decoded.startswith("/"):
        # Root-absolute within the repository (GitHub-style).
        return (root / decoded.lstrip("/")).resolve(strict=False)
    return (source_file.parent / decoded).resolve(strict=False)


def _is_inside_root(path: Path, root: Path, fs: DocFileSystem) -> bool:
    try:
        resolved = fs.resolve(path, strict=False)
        root_resolved = fs.resolve(root, strict=False)
        resolved.relative_to(root_resolved)
        return True
    except ValueError:
        return False
    except OSError:
        return False


def _validate_ref(
    ref: _Ref,
    doc: _DocInfo,
    root: Path,
    fs: DocFileSystem,
    docs_by_rel: dict[str, _DocInfo],
    anchor_cache: dict[str, set[str]],
    findings: list[Finding],
) -> None:
    href = ref.href.strip()
    if not href:
        return
    if _is_external_href(href):
        return

    path_part, fragment = _split_href(href)
    path_part = unquote(path_part)
    fragment = unquote(fragment)
    missing_code = "DOC-006" if ref.kind == "image" else "DOC-001"

    # Fragment-only reference against the current document.
    if path_part == "":
        if fragment == "":
            return
        if fragment not in doc.anchors:
            findings.append(
                _finding(
                    "DOC-004",
                    path=doc.rel,
                    target=f"#{fragment}",
                    line=ref.line,
                )
            )
        return

    # Path traversal / resolution
    try:
        target = _resolve_local_path(path_part, doc.abs_path, root)
    except (OSError, ValueError) as exc:
        _abort_doc005(doc.rel, type(exc).__name__)

    if not _is_inside_root(target, root, fs):
        findings.append(
            _finding(
                "DOC-003",
                path=doc.rel,
                target=href,
                line=ref.line,
            )
        )
        return

    code = _classify_local_target(
        target,
        root,
        fs,
        source_rel=doc.rel,
        missing_code=missing_code,
    )
    if code is not None:
        findings.append(
            _finding(
                code,
                path=doc.rel,
                target=href,
                line=ref.line,
            )
        )
        return

    # Anchor check for links (not images) when a non-empty fragment is present.
    if ref.kind == "link" and fragment:
        target_rel = _rel_to_root(target, root)
        anchors = _anchors_for_path(
            target,
            target_rel,
            root,
            fs,
            docs_by_rel,
            anchor_cache,
            findings,
        )
        if anchors is None:
            return
        if fragment not in anchors:
            findings.append(
                _finding(
                    "DOC-004",
                    path=doc.rel,
                    target=href,
                    line=ref.line,
                )
            )


def _anchors_for_path(
    target: Path,
    target_rel: str,
    root: Path,
    fs: DocFileSystem,
    docs_by_rel: dict[str, _DocInfo],
    anchor_cache: dict[str, set[str]],
    findings: list[Finding],
) -> Optional[set[str]]:
    if target_rel in docs_by_rel:
        return docs_by_rel[target_rel].anchors
    if target_rel in anchor_cache:
        return anchor_cache[target_rel]

    # Only Markdown files expose heading/HTML anchors we understand.
    if not _is_markdown_name(target.name):
        # Non-markdown target with a fragment: cannot validate anchors; treat
        # as OK for DOC-004 (existence already checked).
        anchor_cache[target_rel] = set()
        return set()

    # Directory targets with fragments are not heading anchors.
    inspection = fs.inspect(target)
    if inspection.kind is PathKind.ERROR:
        _abort_doc005(target_rel, inspection.error_class)
    if inspection.kind is PathKind.DIRECTORY:
        anchor_cache[target_rel] = set()
        return set()

    loaded = _load_document(target, root, fs, findings)
    if loaded is None:
        anchor_cache[target_rel] = set()
        return set()
    anchor_cache[target_rel] = loaded.anchors
    return loaded.anchors


def validate_documentation_integrity(
    *,
    explicit_root: Optional[Path] = None,
    start: Optional[Path] = None,
    fs: Optional[DocFileSystem] = None,
) -> ValidationResult:
    """Run Documentation Integrity Validation and return a ValidationResult."""
    filesystem = fs or DocFileSystem()
    findings: list[Finding] = []

    try:
        root = _resolve_framework_root(
            explicit_root=explicit_root,
            start=start,
            fs=filesystem,
        )
        if root is None:
            return ValidationResult(findings=())

        md_files = _discover_markdown_files(root, filesystem)
        docs: list[_DocInfo] = []
        for path in md_files:
            info = _load_document(path, root, filesystem, findings)
            if info is not None:
                docs.append(info)

        docs_by_rel = {d.rel: d for d in docs}
        anchor_cache: dict[str, set[str]] = {}

        for doc in docs:
            for ref in doc.refs:
                _validate_ref(
                    ref,
                    doc,
                    root,
                    filesystem,
                    docs_by_rel,
                    anchor_cache,
                    findings,
                )

    except _Abort as abort:
        findings.append(abort.finding)
        return ValidationResult(
            findings=aggregate_findings(findings),
            execution_error=abort.finding.message,
        )

    return ValidationResult(findings=aggregate_findings(findings))


def make_documentation_integrity_runner(
    *,
    explicit_root: Optional[Path] = None,
    start: Optional[Path] = None,
    fs: Optional[DocFileSystem] = None,
) -> Callable[[], Sequence[Finding]]:
    """Return an orchestrator-compatible callable.

    Execution failures (DOC-005) raise ``ValidatorAbortError`` for exit 2.
    """
    from .orchestrator import ValidatorAbortError

    def _run() -> Sequence[Finding]:
        result = validate_documentation_integrity(
            explicit_root=explicit_root,
            start=start,
            fs=fs,
        )
        if result.execution_error is not None:
            raise ValidatorAbortError(result.execution_error, result.findings)
        return result.findings

    return _run
