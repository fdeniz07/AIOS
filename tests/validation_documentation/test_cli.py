"""CLI registration for Documentation Integrity Validation."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from validation import __main__ as validation_main

from tests.validation_structure.conftest import write_minimal_framework

from .conftest import write_md

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_cli_registers_documentation_integrity(capsys, tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    write_md(root, "docs/extra.md", "# Extra\n")
    code = validation_main.main(["--root", str(root)])
    out = capsys.readouterr().out
    assert code == 0
    assert "documentation-integrity" in out
    assert "Documentation Integrity Validation" in out
    assert "framework-structure" in out
    assert "module-contract" in out
    assert "Pack validation" in out
    assert "NOT performed" in out
    assert "Documentation integrity and Pack validation are NOT performed" not in out
    assert "exit_code=0" in out


def test_cli_doc_error_exit_1(capsys, tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    write_md(root, "docs/broken.md", "[x](missing.md)\n")
    code = validation_main.main(["--root", str(root)])
    out = capsys.readouterr().out
    assert code == 1
    assert "DOC-001" in out
    assert "exit_code=1" in out


def test_cli_help_unchanged_flags():
    proc = subprocess.run(
        [sys.executable, "-m", "validation", "--help"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0
    assert "--root" in proc.stdout
    assert "--fix" not in proc.stdout


def test_cli_upward_discovery(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    write_md(root, "docs/ok.md", "# Ok\n")
    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = (
        str(REPO_ROOT) if not existing else os.pathsep.join([str(REPO_ROOT), existing])
    )
    proc = subprocess.run(
        [sys.executable, "-m", "validation"],
        cwd=str(root),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "documentation-integrity" in proc.stdout
    assert "exit_code=0" in proc.stdout
