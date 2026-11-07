"""Shared fixtures for Framework Structure Validation tests."""

from __future__ import annotations

from pathlib import Path

import pytest

from validation.framework_structure import (
    REQUIRED_DIRECTORIES,
    REQUIRED_FILES,
    FileSystem,
)


def write_minimal_framework(root: Path) -> Path:
    """Create a minimal valid Framework root under ``root``."""
    root.mkdir(parents=True, exist_ok=True)
    for rel in REQUIRED_DIRECTORIES:
        (root / rel).mkdir(parents=True, exist_ok=True)
    for rel in REQUIRED_FILES:
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# {rel}\n", encoding="utf-8")
    return root


@pytest.fixture
def minimal_root(tmp_path: Path) -> Path:
    return write_minimal_framework(tmp_path / "framework")


@pytest.fixture
def real_fs() -> FileSystem:
    return FileSystem()
