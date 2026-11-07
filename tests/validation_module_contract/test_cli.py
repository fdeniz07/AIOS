"""CLI registration for Module Contract Validation (D10 / D11)."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from validation import __main__ as validation_main

from tests.validation_structure.conftest import write_minimal_framework

from .conftest import complete_draft, write_module

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_cli_registers_module_contract(capsys, tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    (root / "modules").mkdir()
    write_module(root, "sample-module", complete_draft())
    code = validation_main.main(["--root", str(root)])
    out = capsys.readouterr().out
    assert code == 0
    assert "module-contract" in out
    assert "framework-structure" in out
    assert "Module Contract Validation" in out
    assert "Documentation integrity" in out
    assert "NOT performed" in out
    assert "No domain validators are registered" not in out
    assert "exit_code=0" in out


def test_cli_real_repo_subprocess():
    proc = subprocess.run(
        [sys.executable, "-m", "validation", "--root", str(REPO_ROOT)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "module-contract" in proc.stdout
    assert "framework-structure" in proc.stdout
    assert "exit_code=0" in proc.stdout


def test_cli_no_extra_flags():
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
    assert "--module" not in proc.stdout


def test_cli_module_error_exit_1(capsys, tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    (root / "modules").mkdir()
    write_module(root, "sample-module", {"status": "active"})
    code = validation_main.main(["--root", str(root)])
    out = capsys.readouterr().out
    assert code == 1
    assert "MOD-004" in out
    assert "exit_code=1" in out


def test_cli_upward_discovery_with_modules(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    (root / "modules").mkdir()
    write_module(root, "sample-module", complete_draft())
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
    assert "module-contract" in proc.stdout
    assert "exit_code=0" in proc.stdout
