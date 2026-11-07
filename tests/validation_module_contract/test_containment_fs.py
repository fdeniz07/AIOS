"""D12 containment, MOD-021 unreliable FS, in-root symlink acceptance."""

from __future__ import annotations

import os
import stat as stat_mod
from pathlib import Path

import pytest

from validation.framework_structure import PathInspection
from validation.module_contract import ModuleFileSystem, validate_module_contract

from .conftest import complete_draft, codes, run_mod, write_module


class ExternalFollowGuardFS(ModuleFileSystem):
    """Instrumented FS that forbids target-following ops on out-of-root symlinks.

    ``resolve`` / ``lstat`` remain allowed (needed for containment classification).
    ``stat``, ``inspect``, and ``read_text`` must not follow a successfully
    resolved out-of-root symlink target.
    """

    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.violations: list[tuple[str, str]] = []

    def _is_successful_out_of_root_symlink(self, path: Path) -> bool:
        try:
            entry = ModuleFileSystem.lstat(self, path)
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


def test_module_yaml_out_of_root_mod024_never_follows(framework: Path, tmp_path: Path):
    external = tmp_path / "external.yaml"
    external.write_text("id: leaked\nstatus: active\n", encoding="utf-8")
    pkg = framework / "modules" / "sample-module"
    pkg.mkdir(parents=True)
    (pkg / "README.md").write_text("# x\n", encoding="utf-8")
    try:
        (pkg / "module.yaml").symlink_to(external)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")

    guard = ExternalFollowGuardFS(framework)
    result = validate_module_contract(explicit_root=framework, fs=guard)
    assert "MOD-024" in codes(result)
    assert "MOD-001" not in codes(result)
    assert "MOD-003" not in codes(result)
    assert guard.violations == []


def test_readme_out_of_root_unknown_status_mod024_never_follows(
    framework: Path, tmp_path: Path
):
    external = tmp_path / "ext-readme.md"
    external.write_text("EXTERNAL_SECRET\n", encoding="utf-8")
    pkg = framework / "modules" / "sample-module"
    pkg.mkdir(parents=True)
    try:
        (pkg / "README.md").symlink_to(external)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")

    guard = ExternalFollowGuardFS(framework)
    result = validate_module_contract(explicit_root=framework, fs=guard)
    assert "MOD-001" in codes(result)
    assert "MOD-024" in codes(result)
    assert "MOD-002" not in codes(result)
    assert guard.violations == []


def test_modules_out_of_root_never_follows(framework: Path, tmp_path: Path):
    external = tmp_path / "ext-modules"
    external.mkdir()
    (external / "pkg").mkdir()
    (external / "pkg" / "module.yaml").write_text("id: leaked\n", encoding="utf-8")
    modules = framework / "modules"
    modules.rmdir()
    try:
        modules.symlink_to(external, target_is_directory=True)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")

    guard = ExternalFollowGuardFS(framework)
    result = validate_module_contract(explicit_root=framework, fs=guard)
    assert codes(result) == ["MOD-024"]
    assert guard.violations == []


def test_candidate_out_of_root_never_follows(framework: Path, tmp_path: Path):
    external = tmp_path / "external-pkg"
    external.mkdir()
    (external / "module.yaml").write_text("secret: value\n", encoding="utf-8")
    link = framework / "modules" / "leaked"
    try:
        link.symlink_to(external, target_is_directory=True)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")

    guard = ExternalFollowGuardFS(framework)
    result = validate_module_contract(explicit_root=framework, fs=guard)
    assert "MOD-024" in codes(result)
    assert guard.violations == []


def test_in_root_symlink_module_yaml_accepted(framework: Path):
    pkg = framework / "modules" / "sample-module"
    pkg.mkdir(parents=True)
    real = pkg / "real-module.yaml"
    real.write_text(
        __import__("yaml").safe_dump(complete_draft()),
        encoding="utf-8",
    )
    try:
        (pkg / "module.yaml").symlink_to(real)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    (pkg / "README.md").write_text("# Module\n", encoding="utf-8")
    result = run_mod(framework)
    assert "MOD-024" not in codes(result)
    assert "MOD-001" not in codes(result)
    assert result.exit_code() == 0


def test_broken_module_yaml_symlink_mod001(framework: Path):
    pkg = framework / "modules" / "sample-module"
    pkg.mkdir(parents=True)
    try:
        (pkg / "module.yaml").symlink_to(pkg / "gone.yaml")
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    (pkg / "README.md").write_text("# x\n", encoding="utf-8")
    result = run_mod(framework)
    assert "MOD-001" in codes(result)
    assert "MOD-024" not in codes(result)
    assert "MOD-021" not in codes(result)


def test_yaml_permission_error_mod021_exit2(framework: Path):
    write_module(framework, "sample-module", complete_draft())
    target = framework / "modules" / "sample-module" / "module.yaml"

    class BoomFS(ModuleFileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == target:
                raise PermissionError("denied")
            return super().lstat(path)

    result = validate_module_contract(explicit_root=framework, fs=BoomFS())
    assert "MOD-021" in codes(result)
    assert "MOD-001" not in codes(result)
    assert result.execution_error is not None
    assert result.exit_code() == 2


def test_readme_read_error_mod021_deprecated(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nOk.\n",
    )
    target = framework / "modules" / "sample-module" / "README.md"

    class BoomReadFS(ModuleFileSystem):
        def read_text(self, path: Path) -> str:
            if path == target:
                raise OSError("io failure")
            return super().read_text(path)

    result = validate_module_contract(explicit_root=framework, fs=BoomReadFS())
    assert "MOD-021" in codes(result)
    assert "MOD-012" not in codes(result)
    assert "MOD-002" not in codes(result)
    assert result.exit_code() == 2


def test_modules_iterdir_error_mod021(framework: Path):
    write_module(framework, "sample-module", complete_draft())
    modules = framework / "modules"

    class BoomListFS(ModuleFileSystem):
        def iterdir(self, path: Path) -> list[Path]:
            if path == modules:
                raise OSError("cannot list")
            return super().iterdir(path)

    result = validate_module_contract(explicit_root=framework, fs=BoomListFS())
    assert "MOD-021" in codes(result)
    assert result.exit_code() == 2


def test_resolve_failure_on_symlink_mod021(framework: Path, tmp_path: Path):
    external = tmp_path / "ext.yaml"
    external.write_text("x: 1\n", encoding="utf-8")
    pkg = framework / "modules" / "sample-module"
    pkg.mkdir(parents=True)
    (pkg / "README.md").write_text("# x\n", encoding="utf-8")
    link = pkg / "module.yaml"
    try:
        link.symlink_to(external)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")

    class BoomResolveFS(ModuleFileSystem):
        def resolve(self, path: Path, *, strict: bool = False) -> Path:
            if path == link:
                raise OSError("loop")
            return super().resolve(path, strict=strict)

    result = validate_module_contract(explicit_root=framework, fs=BoomResolveFS())
    assert "MOD-021" in codes(result)
    assert "MOD-024" not in codes(result)
    assert result.exit_code() == 2


def test_read_only_snapshot_no_writes(framework: Path):
    write_module(framework, "sample-module", complete_draft())

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
    result = run_mod(framework)
    after = snapshot(framework)
    assert before == after
    assert result.exit_code() == 0


def test_deterministic_aggregation_duplicate_identity(framework: Path):
    write_module(framework, "sample-module", complete_draft(id=""))
    a = run_mod(framework)
    b = run_mod(framework)
    assert [f.to_dict() for f in a.findings] == [f.to_dict() for f in b.findings]
