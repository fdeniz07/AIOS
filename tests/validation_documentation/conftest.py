"""Fixtures for Documentation Integrity Validation tests."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import pytest

from tests.validation_structure.conftest import write_minimal_framework
from validation.documentation_integrity import (
    DocFileSystem,
    validate_documentation_integrity,
)


@pytest.fixture
def framework(tmp_path: Path) -> Path:
    return write_minimal_framework(tmp_path / "framework")


@pytest.fixture
def real_fs() -> DocFileSystem:
    return DocFileSystem()


def codes(result) -> list[str]:
    return [f.code for f in result.findings]


def run_doc(root: Path, fs: Optional[DocFileSystem] = None):
    return validate_documentation_integrity(
        explicit_root=root, fs=fs or DocFileSystem()
    )


def write_md(root: Path, rel: str, content: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path
