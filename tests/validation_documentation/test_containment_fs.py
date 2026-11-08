"""D12 containment, broken symlinks, permission errors, instrumented FS."""

from __future__ import annotations

import os
import stat as stat_mod
from pathlib import Path

import pytest

from validation.documentation_integrity import DocFileSystem, validate_documentation_integrity
from validation.framework_structure import PathInspection

from .conftest import codes, run_doc, write_md


class ExternalFollowGuardFS(DocFileSystem):
    """Forbid target-following ops on successfully resolved out-of-root symlinks."""

    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.violations: list[tuple[str, str]] = []

    def _is_successful_out_of_root_symlink(self, path: Path) -> bool:
        try:
            entry = DocFileSystem.lstat(self, path)
        except OSError:
            return False
        if not stat_mod.S_ISLNK(entry.st_mode):
            return False
        try:
            target = Path.resolve(path, strict=True)
            root_resolved = Path.resolve(self.root, strict=False)
        except OSError:
            return False
        try:
            target.relative_to(root_resolved)
            return False
        except ValueError:
            return True

    def _reject(self, op: str, path: Path) -> None:
        self.violations.append((op, str(path)))
        raise AssertionError(
            f"{op}() must not follow out-of-root symlink target: {path}"
        )

    def stat(self, path: Path) -> os.stat_result:
        if self._is_successful_out_of_root_symlink(path):
            self._reject("stat", path)
        return super().stat(path)

    def inspect(self, path: Path) -> PathInspection:
        if self._is_successful_out_of_root_symlink(path):
            self._reject("inspect", path)
        return super().inspect(path)

    def read_text(self, path: Path) -> str:
        if self._is_successful_out_of_root_symlink(path):
            self._reject("read_text", path)
        try:
            resolved = Path.resolve(path, strict=True)
            root_resolved = Path.resolve(self.root, strict=False)
            resolved.relative_to(root_resolved)
        except ValueError:
            self._reject("read_text", path)
        except OSError:
            pass
        return super().read_text(path)


def test_out_of_root_markdown_symlink_doc003_never_reads(
    framework: Path, tmp_path: Path
):
    external = tmp_path / "external.md"
    external.write_text("# SECRET\n[x](https://example.com)\n", encoding="utf-8")
    link = framework / "docs" / "leaked.md"
    link.parent.mkdir(parents=True, exist_ok=True)
    try:
        link.symlink_to(external)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")

    guard = ExternalFollowGuardFS(framework)
    result = validate_documentation_integrity(explicit_root=framework, fs=guard)
    assert "DOC-003" in codes(result)
    assert guard.violations == []


def test_link_to_out_of_root_symlink_doc003_never_reads(
    framework: Path, tmp_path: Path
):
    external = tmp_path / "outside.md"
    external.write_text("SECRET\n", encoding="utf-8")
    link = framework / "docs" / "outside-link.md"
    link.parent.mkdir(parents=True, exist_ok=True)
    try:
        link.symlink_to(external)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    write_md(framework, "docs/a.md", "[x](outside-link.md)\n")

    guard = ExternalFollowGuardFS(framework)
    result = validate_documentation_integrity(explicit_root=framework, fs=guard)
    assert "DOC-003" in codes(result)
    assert guard.violations == []


def test_broken_symlink_target_doc001(framework: Path):
    link = framework / "docs" / "broken.md"
    link.parent.mkdir(parents=True, exist_ok=True)
    try:
        link.symlink_to(framework / "docs" / "gone-target.md")
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    write_md(framework, "docs/a.md", "[x](broken.md)\n")
    result = run_doc(framework)
    assert "DOC-001" in codes(result)
    assert "DOC-003" not in codes(result)
    assert "DOC-005" not in codes(result)


def test_permission_error_doc005_exit2(framework: Path):
    write_md(framework, "docs/a.md", "# Ok\n")
    target = framework / "docs" / "a.md"

    class BoomFS(DocFileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == target:
                raise PermissionError("denied")
            return super().lstat(path)

    result = validate_documentation_integrity(explicit_root=framework, fs=BoomFS())
    assert "DOC-005" in codes(result)
    assert result.execution_error is not None
    assert result.exit_code() == 2


def test_read_error_doc005_exit2(framework: Path):
    write_md(framework, "docs/a.md", "# Ok\n")
    target = framework / "docs" / "a.md"

    class BoomReadFS(DocFileSystem):
        def read_text(self, path: Path) -> str:
            if path == target:
                raise OSError("io failure")
            return super().read_text(path)

    result = validate_documentation_integrity(explicit_root=framework, fs=BoomReadFS())
    assert "DOC-005" in codes(result)
    assert result.exit_code() == 2


def test_iterdir_error_doc005(framework: Path):
    write_md(framework, "docs/a.md", "# Ok\n")
    docs = framework / "docs"

    class BoomListFS(DocFileSystem):
        def iterdir(self, path: Path) -> list[Path]:
            if path == docs:
                raise OSError("cannot list")
            return super().iterdir(path)

    result = validate_documentation_integrity(explicit_root=framework, fs=BoomListFS())
    assert "DOC-005" in codes(result)
    assert result.exit_code() == 2


def test_deterministic_findings(framework: Path):
    write_md(framework, "docs/a.md", "[x](missing.md)\n[y](missing2.md)\n")
    a = run_doc(framework)
    b = run_doc(framework)
    assert [f.to_dict() for f in a.findings] == [f.to_dict() for f in b.findings]


def test_read_only_no_writes(framework: Path):
    write_md(framework, "docs/a.md", "# Ok\n")

    def snapshot(root: Path) -> dict[str, tuple]:
        entries: dict[str, tuple] = {}
        for dirpath, dirnames, filenames in os.walk(root):
            for name in dirnames + filenames:
                p = Path(dirpath) / name
                rel = str(p.relative_to(root)).replace("\\", "/")
                st = p.lstat()
                entries[rel] = (st.st_mode, st.st_mtime_ns, st.st_size)
        return entries

    before = snapshot(framework)
    result = run_doc(framework)
    after = snapshot(framework)
    assert before == after
    assert result.exit_code() == 0
