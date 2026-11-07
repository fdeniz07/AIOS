"""Production ``FileSystem.inspect`` path — exercises real lstat/stat logic.

These tests must not override ``inspect()``. Failures are injected at
``lstat`` / ``stat`` (or created as real filesystem entries).
"""

from __future__ import annotations

import os
import stat as stat_mod
from pathlib import Path

import pytest

from validation.framework_structure import (
    FileSystem,
    PathKind,
    validate_framework_structure,
)

from .conftest import write_minimal_framework


def test_inspect_missing_path(tmp_path: Path):
    fs = FileSystem()
    result = fs.inspect(tmp_path / "does-not-exist")
    assert result.kind is PathKind.MISSING
    assert result.error_class is None


def test_inspect_regular_file_and_directory(tmp_path: Path):
    fs = FileSystem()
    file_path = tmp_path / "f.txt"
    file_path.write_text("x\n", encoding="utf-8")
    dir_path = tmp_path / "d"
    dir_path.mkdir()
    assert fs.inspect(file_path).kind is PathKind.FILE
    assert fs.inspect(dir_path).kind is PathKind.DIRECTORY


def test_inspect_permission_error_via_lstat_is_error(tmp_path: Path):
    target = tmp_path / "secret.txt"
    target.write_text("x\n", encoding="utf-8")

    class RaisingLstatFS(FileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == target:
                raise PermissionError("denied")
            return super().lstat(path)

    result = RaisingLstatFS().inspect(target)
    assert result.kind is PathKind.ERROR
    assert result.error_class == "PermissionError"


def test_inspect_io_error_via_lstat_is_error(tmp_path: Path):
    target = tmp_path / "noisy.txt"
    target.write_text("x\n", encoding="utf-8")

    class RaisingLstatFS(FileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == target:
                raise OSError("io failure")
            return super().lstat(path)

    result = RaisingLstatFS().inspect(target)
    assert result.kind is PathKind.ERROR
    assert result.error_class == "OSError"


def test_inspect_broken_symlink_is_other(tmp_path: Path):
    link = tmp_path / "broken"
    missing = tmp_path / "gone-target"
    try:
        link.symlink_to(missing)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    result = FileSystem().inspect(link)
    assert result.kind is PathKind.OTHER


def test_inspect_file_target_symlink_is_file(tmp_path: Path):
    real = tmp_path / "real.txt"
    real.write_text("ok\n", encoding="utf-8")
    link = tmp_path / "link.txt"
    try:
        link.symlink_to(real)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    result = FileSystem().inspect(link)
    assert result.kind is PathKind.FILE


def test_inspect_directory_target_symlink_is_directory(tmp_path: Path):
    real = tmp_path / "real-dir"
    real.mkdir()
    link = tmp_path / "link-dir"
    try:
        link.symlink_to(real, target_is_directory=True)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    result = FileSystem().inspect(link)
    assert result.kind is PathKind.DIRECTORY


def test_inspect_symlink_target_stat_error_is_error(tmp_path: Path):
    real = tmp_path / "real.txt"
    real.write_text("ok\n", encoding="utf-8")
    link = tmp_path / "link.txt"
    try:
        link.symlink_to(real)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")

    class RaisingStatFS(FileSystem):
        def stat(self, path: Path) -> os.stat_result:
            if path == link:
                raise PermissionError("target inaccessible")
            return super().stat(path)

    result = RaisingStatFS().inspect(link)
    assert result.kind is PathKind.ERROR
    assert result.error_class == "PermissionError"


def test_inspect_wrong_type_file_as_directory_mode(tmp_path: Path):
    """Non-file, non-dir mode bits classify as OTHER (via lstat, no override)."""
    path = tmp_path / "pipe-like"

    class FakeModeFS(FileSystem):
        def lstat(self, path_arg: Path) -> os.stat_result:
            if path_arg == path:
                # Character device mode — neither REG nor DIR.
                return os.stat_result(
                    (stat_mod.S_IFCHR | 0o666, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                )
            return super().lstat(path_arg)

    assert FakeModeFS().inspect(path).kind is PathKind.OTHER


def test_lstat_permission_error_reaches_str006_exit_two(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    blocked = root / "ROADMAP.md"

    class RaisingLstatFS(FileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == blocked:
                raise PermissionError("denied")
            return super().lstat(path)

    # Do not override inspect — production classification must run.
    result = validate_framework_structure(explicit_root=root, fs=RaisingLstatFS())
    assert result.exit_code() == 2
    assert result.execution_error is not None
    finding = next(f for f in result.findings if f.code == "STR-006")
    assert finding.path == "ROADMAP.md"
    assert "PermissionError" in finding.message
    assert finding.rule == "STR-006"
    assert finding.category == "framework-structure"


def test_symlink_target_stat_error_reaches_str006(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    real = tmp_path / "agents-real.md"
    real.write_text("linked\n", encoding="utf-8")
    agents = root / "AGENTS.md"
    agents.unlink()
    try:
        agents.symlink_to(real)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")

    class RaisingStatFS(FileSystem):
        def stat(self, path: Path) -> os.stat_result:
            if path == agents:
                raise OSError("cannot stat target")
            return super().stat(path)

    result = validate_framework_structure(explicit_root=root, fs=RaisingStatFS())
    assert result.exit_code() == 2
    assert any(f.code == "STR-006" and f.path == "AGENTS.md" for f in result.findings)


def test_permission_error_not_silently_missing(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    blocked = root / "VERSION"

    class RaisingLstatFS(FileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            # After candidate selection VERSION is re-inspected as required file.
            # Also boom during candidate markers — first marker VERSION.
            if path == blocked:
                raise PermissionError("denied")
            return super().lstat(path)

    result = validate_framework_structure(explicit_root=root, fs=RaisingLstatFS())
    assert result.exit_code() == 2
    assert any(f.code == "STR-006" for f in result.findings)
    assert not any(f.code == "STR-001" for f in result.findings)
    assert not any(f.code == "STR-009" for f in result.findings)


def test_inspect_lstat_not_a_directory_error_is_other(tmp_path: Path):
    target = tmp_path / "nested" / "child"

    class RaisingLstatFS(FileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == target:
                raise NotADirectoryError("parent is not a directory")
            return super().lstat(path)

    result = RaisingLstatFS().inspect(target)
    assert result.kind is PathKind.OTHER
    assert result.error_class is None


def test_inspect_stat_not_a_directory_error_for_symlink_is_other(tmp_path: Path):
    real = tmp_path / "real.txt"
    real.write_text("ok\n", encoding="utf-8")
    link = tmp_path / "link.txt"
    try:
        link.symlink_to(real)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")

    class RaisingStatFS(FileSystem):
        def stat(self, path: Path) -> os.stat_result:
            if path == link:
                raise NotADirectoryError("intermediate component is a file")
            return super().stat(path)

    result = RaisingStatFS().inspect(link)
    assert result.kind is PathKind.OTHER
    assert result.error_class is None


def test_required_file_parent_is_file_not_str006(tmp_path: Path):
    """Parent component is a file must not become an execution failure.

    Platform note: some hosts raise ``NotADirectoryError`` (OTHER → STR-003),
    others raise ``FileNotFoundError`` (MISSING → STR-001). Neither is STR-006.
    """
    import shutil

    root = write_minimal_framework(tmp_path / "fw")
    shutil.rmtree(root / "docs")
    (root / "docs").write_text("not-a-directory\n", encoding="utf-8")
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 1
    assert result.execution_error is None
    assert not any(f.code == "STR-006" for f in result.findings)
    assert any(f.code == "STR-004" and f.path == "docs" for f in result.findings)
    nested = [f for f in result.findings if f.path == "docs/FRAMEWORK_CONTRACT.md"]
    assert len(nested) == 1
    assert nested[0].code in {"STR-001", "STR-003"}


def test_required_file_not_a_directory_error_is_str003_not_str006(tmp_path: Path):
    """Injected NotADirectoryError on a required file → OTHER → STR-003."""
    root = write_minimal_framework(tmp_path / "fw")
    nested = root / "docs" / "FRAMEWORK_CONTRACT.md"

    class RaisingLstatFS(FileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == nested:
                raise NotADirectoryError("parent is a file")
            return super().lstat(path)

    result = validate_framework_structure(explicit_root=root, fs=RaisingLstatFS())
    assert result.exit_code() == 1
    assert result.execution_error is None
    assert not any(f.code == "STR-006" for f in result.findings)
    assert any(
        f.code == "STR-003" and f.path == "docs/FRAMEWORK_CONTRACT.md"
        for f in result.findings
    )


def test_required_directory_wrong_type_str004(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    (root / "rules").rmdir()
    (root / "rules").write_text("file\n", encoding="utf-8")
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 1
    assert any(f.code == "STR-004" and f.path == "rules" for f in result.findings)
    assert not any(f.code == "STR-006" for f in result.findings)


def test_explicit_root_parent_not_directory_str008_not_str006(tmp_path: Path):
    parent_file = tmp_path / "not-a-dir"
    parent_file.write_text("x\n", encoding="utf-8")
    bogus_root = parent_file / "child-root"

    class RaisingLstatFS(FileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == bogus_root:
                raise NotADirectoryError("parent is a file")
            return super().lstat(path)

    result = validate_framework_structure(
        explicit_root=bogus_root,
        fs=RaisingLstatFS(),
    )
    assert result.exit_code() == 1
    assert result.execution_error is None
    assert len(result.findings) == 1
    assert result.findings[0].code == "STR-008"
    assert not any(f.code == "STR-006" for f in result.findings)


def test_genuine_permission_error_still_str006_exit_two(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    blocked = root / "AGENTS.md"

    class RaisingLstatFS(FileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == blocked:
                raise PermissionError("denied")
            return super().lstat(path)

    result = validate_framework_structure(explicit_root=root, fs=RaisingLstatFS())
    assert result.exit_code() == 2
    assert any(f.code == "STR-006" and f.path == "AGENTS.md" for f in result.findings)


def test_genuine_io_oserror_still_str006_exit_two(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    blocked = root / "ROADMAP.md"

    class RaisingLstatFS(FileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == blocked:
                raise OSError("EIO simulated")
            return super().lstat(path)

    result = validate_framework_structure(explicit_root=root, fs=RaisingLstatFS())
    assert result.exit_code() == 2
    assert any(f.code == "STR-006" and f.path == "ROADMAP.md" for f in result.findings)
