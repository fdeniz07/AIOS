"""Primary FS-01 through FS-12 acceptance criteria."""

from __future__ import annotations

from pathlib import Path

from validation.framework_structure import (
    FileSystem,
    PathInspection,
    PathKind,
    validate_framework_structure,
)
from validation.models import Severity

from .conftest import write_minimal_framework


def _codes(result):
    return [f.code for f in result.findings]


def test_fs01_valid_minimal_framework_exit_zero(minimal_root: Path):
    result = validate_framework_structure(explicit_root=minimal_root)
    assert result.findings == ()
    assert result.execution_error is None
    assert result.exit_code() == 0


def test_fs02_missing_required_files_str001(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    (root / "README.md").unlink()
    (root / "ROADMAP.md").unlink()
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 1
    assert result.execution_error is None
    codes = _codes(result)
    assert codes.count("STR-001") >= 2
    paths = {f.path for f in result.findings if f.code == "STR-001"}
    assert "README.md" in paths
    assert "ROADMAP.md" in paths
    for f in result.findings:
        if f.code == "STR-001":
            assert f.severity is Severity.ERROR
            assert f.category == "framework-structure"
            assert f.rule == "STR-001"
            assert "Required framework file is missing:" in f.message


def test_fs03_missing_required_directories_str002(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    (root / "rules").rmdir()
    (root / "methodology").rmdir()
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 1
    paths = {f.path for f in result.findings if f.code == "STR-002"}
    assert "rules" in paths
    assert "methodology" in paths
    for f in result.findings:
        if f.code == "STR-002":
            assert f.rule == "STR-002"
            assert f.category == "framework-structure"
            assert "Required framework directory is missing:" in f.message


def test_fs04_type_mismatches_str003_str004(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    (root / "VERSION").unlink()
    (root / "VERSION").mkdir()
    (root / "rules").rmdir()
    (root / "rules").write_text("not-a-dir\n", encoding="utf-8")
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 1
    by_code = {f.code: f for f in result.findings}
    assert by_code["STR-003"].path == "VERSION"
    assert "must be a file" in by_code["STR-003"].message
    assert by_code["STR-004"].path == "rules"
    assert "must be a directory" in by_code["STR-004"].message


def test_fs05_valid_explicit_root(minimal_root: Path):
    result = validate_framework_structure(explicit_root=minimal_root)
    assert result.exit_code() == 0
    assert result.findings == ()


def test_fs06_upward_nearest_ancestor(tmp_path: Path):
    outer = write_minimal_framework(tmp_path / "outer")
    # Make outer a weaker candidate still valid: keep markers.
    nested = outer / "consumer" / "work"
    nested.mkdir(parents=True)
    # Add a nearer non-candidate that should be skipped.
    nearer = outer / "consumer"
    (nearer / "VERSION").write_text("x\n", encoding="utf-8")
    result = validate_framework_structure(start=nested)
    assert result.exit_code() == 0
    assert result.findings == ()


def test_fs07_root_not_found_str005(tmp_path: Path):
    start = tmp_path / "empty" / "deep"
    start.mkdir(parents=True)
    result = validate_framework_structure(start=start)
    assert result.exit_code() == 1
    assert result.execution_error is None
    assert len(result.findings) == 1
    f = result.findings[0]
    assert f.code == "STR-005"
    assert f.rule == "STR-005"
    assert f.path is None
    assert f.message == "AIOS Framework root was not found."
    assert "Run from inside an AIOS framework repository" in (f.suggestion or "")


def test_fs08_uninspectable_path_str006_exit_two(tmp_path: Path, minimal_root: Path):
    class BoomFS(FileSystem):
        def inspect(self, path: Path) -> PathInspection:
            rel = path.relative_to(minimal_root).as_posix() if path.is_relative_to(minimal_root) else ""
            if rel == "ROADMAP.md":
                return PathInspection(PathKind.ERROR, "PermissionError")
            return super().inspect(path)

    result = validate_framework_structure(explicit_root=minimal_root, fs=BoomFS())
    assert result.exit_code() == 2
    assert result.execution_error is not None
    assert any(f.code == "STR-006" for f in result.findings)
    f = next(f for f in result.findings if f.code == "STR-006")
    assert f.path == "ROADMAP.md"
    assert "PermissionError" in f.message
    assert f.category == "framework-structure"
    assert f.severity is Severity.ERROR


def test_fs09_optional_reserved_no_findings(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    # Optional absent: fine. Optional present wrong type: ignored.
    (root / "modules").write_text("file-not-dir\n", encoding="utf-8")
    (root / "packs").mkdir()
    # Reserved wrong types ignored.
    (root / "examples").write_text("x\n", encoding="utf-8")
    (root / "generators").mkdir()
    (root / "knowledge").write_text("x\n", encoding="utf-8")
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 0
    assert result.findings == ()


def test_fs10_unknown_root_entries_tolerated(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    (root / "weird-tooling").mkdir()
    (root / "NOTES.txt").write_text("hi\n", encoding="utf-8")
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 0
    assert result.findings == ()


def test_fs11_findings_deterministic(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    (root / "README.md").unlink()
    (root / "AGENTS.md").unlink()
    (root / "rules").rmdir()
    a = validate_framework_structure(explicit_root=root)
    b = validate_framework_structure(explicit_root=root)
    assert a.findings == b.findings
    assert a.exit_code() == b.exit_code() == 1
    serialized = [(f.code, f.path, f.rule, f.message) for f in a.findings]
    assert serialized == [(f.code, f.path, f.rule, f.message) for f in b.findings]
    assert serialized == sorted(serialized, key=lambda item: (item[0], item[1] or ""))


def test_fs12_read_only(tmp_path: Path, minimal_root: Path):
    def snapshot(base: Path) -> dict[str, tuple[str, int, int, bytes | None]]:
        """name → (kind, mode, mtime_ns, contents-or-None)."""
        entries: dict[str, tuple[str, int, int, bytes | None]] = {}
        for p in sorted(base.rglob("*")):
            rel = p.relative_to(base).as_posix()
            st = p.lstat()
            mode = st.st_mode
            mtime = st.st_mtime_ns
            if p.is_symlink():
                entries[rel] = ("symlink", mode, mtime, None)
            elif p.is_file():
                entries[rel] = ("file", mode, mtime, p.read_bytes())
            elif p.is_dir():
                entries[rel] = ("dir", mode, mtime, None)
            else:
                entries[rel] = ("other", mode, mtime, None)
        return entries

    before_root = snapshot(minimal_root)
    before_parent_names = sorted(p.name for p in tmp_path.iterdir())
    stamp = tmp_path / "stamp.txt"
    stamp.write_text("before\n", encoding="utf-8")
    stamp_meta = (
        stamp.read_bytes(),
        stamp.stat().st_mode,
        stamp.stat().st_mtime_ns,
    )

    result = validate_framework_structure(explicit_root=minimal_root)
    assert result.exit_code() == 0

    assert snapshot(minimal_root) == before_root
    assert stamp.read_bytes() == stamp_meta[0]
    assert stamp.stat().st_mode == stamp_meta[1]
    assert stamp.stat().st_mtime_ns == stamp_meta[2]
    after_parent_names = sorted(p.name for p in tmp_path.iterdir())
    assert after_parent_names == sorted([*before_parent_names, "stamp.txt"])
    assert after_parent_names == ["framework", "stamp.txt"]
