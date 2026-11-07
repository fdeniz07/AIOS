"""Fixtures for Module Contract Validation tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping, Optional

import pytest
import yaml

from tests.validation_structure.conftest import write_minimal_framework
from validation.module_contract import ModuleFileSystem, validate_module_contract


def write_module(
    root: Path,
    name: str,
    metadata: Optional[Mapping[str, Any]] = None,
    *,
    readme: Optional[str] = "# Module\n",
    write_yaml: bool = True,
) -> Path:
    """Create a Module package under ``root/modules/<name>``."""
    pkg = root / "modules" / name
    pkg.mkdir(parents=True, exist_ok=True)
    if write_yaml and metadata is not None:
        (pkg / "module.yaml").write_text(
            yaml.safe_dump(dict(metadata), sort_keys=False),
            encoding="utf-8",
        )
    if readme is not None:
        (pkg / "README.md").write_text(readme, encoding="utf-8")
    return pkg


def complete_draft(name: str = "sample-module", **overrides: Any) -> dict[str, Any]:
    """Return a complete valid draft metadata mapping."""
    data: dict[str, Any] = {
        "id": name,
        "version": "0.1.0",
        "title": "Sample Module",
        "summary": "A complete draft module for tests.",
        "status": "draft",
        "maturity": "experimental",
        "applies_when": ["when useful"],
        "avoid_when": ["when not"],
        "tags": ["sample"],
        "provides": ["sample-skill"],
        "requires_core": "1.0.0",
    }
    data.update(overrides)
    return data


@pytest.fixture
def framework(tmp_path: Path) -> Path:
    root = write_minimal_framework(tmp_path / "framework")
    (root / "modules").mkdir(exist_ok=True)
    return root


@pytest.fixture
def real_fs() -> ModuleFileSystem:
    return ModuleFileSystem()


def codes(result) -> list[str]:
    return [f.code for f in result.findings]


def codes_for(result, path_substr: str) -> list[str]:
    return [
        f.code
        for f in result.findings
        if f.path is not None and path_substr in f.path.replace("\\", "/")
    ]


def run_mod(root: Path, fs: Optional[ModuleFileSystem] = None):
    return validate_module_contract(explicit_root=root, fs=fs or ModuleFileSystem())
