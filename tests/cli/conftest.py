"""Fixtures for aiosctl sync regression tests (temporary directories only)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
AIOSCTL_PATH = REPO_ROOT / "scripts" / "aiosctl.py"


@pytest.fixture(scope="session")
def aiosctl():
    """Load scripts/aiosctl.py as a module without requiring package install."""
    spec = importlib.util.spec_from_file_location("aiosctl", AIOSCTL_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["aiosctl"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def fake_aios_root(tmp_path: Path) -> Path:
    """Temporary AIOS-like root with an empty rules/ directory."""
    root = tmp_path / "aios_root"
    (root / "rules").mkdir(parents=True)
    return root


@pytest.fixture
def project_dir(tmp_path: Path) -> Path:
    """Temporary consumer project directory (not a real consumer repo)."""
    project = tmp_path / "consumer_project"
    project.mkdir()
    return project
