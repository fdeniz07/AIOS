"""Discovery and candidate classification (§4 / D1 / D2 / D12)."""

from __future__ import annotations

from pathlib import Path

import pytest

from validation.models import Severity
from validation.module_contract import validate_module_contract

from .conftest import complete_draft, codes, run_mod, write_module


def test_modules_absent_zero_findings(framework: Path):
    (framework / "modules").rmdir()
    result = run_mod(framework)
    assert result.findings == ()
    assert result.execution_error is None
    assert result.exit_code() == 0


def test_modules_file_is_mod019(framework: Path):
    modules = framework / "modules"
    modules.rmdir()
    modules.write_text("not a dir\n", encoding="utf-8")
    result = run_mod(framework)
    assert codes(result) == ["MOD-019"]
    assert result.findings[0].severity is Severity.ERROR
    assert result.exit_code() == 1


def test_modules_broken_symlink_is_mod019(framework: Path):
    modules = framework / "modules"
    modules.rmdir()
    try:
        modules.symlink_to(framework / "missing-modules-target")
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    result = run_mod(framework)
    assert "MOD-019" in codes(result)
    assert "MOD-024" not in codes(result)


def test_ignore_modules_readme_and_accept_directory(framework: Path):
    (framework / "modules" / "README.md").write_text("# Catalog\n", encoding="utf-8")
    write_module(framework, "sample-module", complete_draft())
    result = run_mod(framework)
    assert "MOD-018" not in codes(result)
    assert result.exit_code() == 0


def test_unexpected_file_child_mod018(framework: Path):
    (framework / "modules" / "stray.txt").write_text("x\n", encoding="utf-8")
    write_module(framework, "sample-module", complete_draft())
    result = run_mod(framework)
    assert "MOD-018" in codes(result)
    stray = [f for f in result.findings if f.code == "MOD-018"][0]
    assert stray.path == "modules/stray.txt"
    assert stray.severity is Severity.WARNING


def test_nested_package_not_discovered(framework: Path):
    write_module(framework, "sample-module", complete_draft())
    nested = framework / "modules" / "sample-module" / "nested-child"
    nested.mkdir()
    (nested / "module.yaml").write_text("id: nested\nstatus: active\n", encoding="utf-8")
    result = run_mod(framework)
    paths = [f.path for f in result.findings]
    assert not any(p and "nested-child" in p for p in paths)


def test_candidate_out_of_root_symlink_mod024(framework: Path, tmp_path: Path):
    external = tmp_path / "external-pkg"
    external.mkdir()
    (external / "module.yaml").write_text("secret: value\n", encoding="utf-8")
    link = framework / "modules" / "leaked"
    try:
        link.symlink_to(external, target_is_directory=True)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")

    from .test_containment_fs import ExternalFollowGuardFS

    guard = ExternalFollowGuardFS(framework)
    result = validate_module_contract(explicit_root=framework, fs=guard)
    assert "MOD-024" in codes(result)
    assert guard.violations == []


def test_modules_out_of_root_symlink_mod024_no_children(framework: Path, tmp_path: Path):
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

    from .test_containment_fs import ExternalFollowGuardFS

    guard = ExternalFollowGuardFS(framework)
    result = validate_module_contract(explicit_root=framework, fs=guard)
    assert codes(result) == ["MOD-024"]
    assert guard.violations == []
