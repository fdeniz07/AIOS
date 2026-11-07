"""Lifecycle-aware README validation (D7 / R7 / unknown status)."""

from __future__ import annotations

from pathlib import Path

import pytest

from validation.models import Severity

from .conftest import complete_draft, codes, run_mod, write_module


def test_active_missing_readme_mod002_error(framework: Path):
    write_module(
        framework,
        "sample-module",
        complete_draft(status="active"),
        readme=None,
    )
    result = run_mod(framework)
    mod002 = [f for f in result.findings if f.code == "MOD-002"]
    assert len(mod002) == 1
    assert mod002[0].severity is Severity.ERROR
    assert "MOD-012" not in codes(result)


def test_draft_missing_readme_mod002_warning(framework: Path):
    write_module(
        framework,
        "sample-module",
        complete_draft(status="draft"),
        readme=None,
    )
    result = run_mod(framework)
    mod002 = [f for f in result.findings if f.code == "MOD-002"]
    assert len(mod002) == 1
    assert mod002[0].severity is Severity.WARNING
    assert result.exit_code() == 0


def test_deprecated_missing_readme_mod002_only(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    write_module(framework, "sample-module", data, readme=None)
    result = run_mod(framework)
    assert "MOD-002" in codes(result)
    assert "MOD-012" not in codes(result)


def test_deprecated_readme_without_migration_mod012_only(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\nNo migration section.\n",
    )
    result = run_mod(framework)
    assert codes(result) == ["MOD-012"] or (
        "MOD-012" in codes(result) and "MOD-002" not in codes(result)
    )


def test_deprecated_readme_with_exact_migration_ok(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nSteps.\n",
    )
    result = run_mod(framework)
    assert "MOD-012" not in codes(result)
    assert "MOD-002" not in codes(result)


def test_migration_heading_must_be_exact(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## migration\n\nSteps.\n",
    )
    result = run_mod(framework)
    assert "MOD-012" in codes(result)


def test_unknown_status_no_mod002_even_if_readme_missing(framework: Path):
    write_module(
        framework,
        "sample-module",
        {"status": "weird", "id": "sample-module", "version": "1.0.0",
         "title": "T", "summary": "S",
         "applies_when": ["a"], "avoid_when": ["b"]},
        readme=None,
    )
    result = run_mod(framework)
    assert "MOD-002" not in codes(result)
    assert "MOD-012" not in codes(result)


def test_missing_yaml_no_mod002(framework: Path):
    write_module(framework, "sample-module", None, write_yaml=False, readme=None)
    result = run_mod(framework)
    assert "MOD-001" in codes(result)
    assert "MOD-002" not in codes(result)


def test_broken_readme_symlink_known_status_mod002(framework: Path):
    pkg = write_module(
        framework,
        "sample-module",
        complete_draft(status="active"),
        readme=None,
    )
    try:
        (pkg / "README.md").symlink_to(pkg / "missing-readme")
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    result = run_mod(framework)
    assert "MOD-002" in codes(result)
    assert "MOD-012" not in codes(result)
    assert "MOD-024" not in codes(result)


def test_broken_readme_symlink_unknown_status_no_mod002(framework: Path):
    pkg = write_module(
        framework,
        "sample-module",
        None,
        write_yaml=False,
        readme=None,
    )
    try:
        (pkg / "README.md").symlink_to(pkg / "missing-readme")
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    result = run_mod(framework)
    assert "MOD-001" in codes(result)
    assert "MOD-002" not in codes(result)
