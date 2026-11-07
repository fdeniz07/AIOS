"""CLI integration for Framework Structure Validation."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from validation import __main__ as validation_main

from .conftest import write_minimal_framework

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_cli_default_registers_framework_structure(capsys, minimal_root: Path, monkeypatch):
    monkeypatch.chdir(minimal_root)
    code = validation_main.main([])
    out = capsys.readouterr().out
    assert "framework-structure" in out
    assert "Framework Structure Validation" in out
    assert "Module contract validation and documentation integrity are NOT performed" in out
    assert "No domain validators are registered" not in out
    assert code == 0
    assert "exit_code=0" in out


def test_cli_explicit_root(capsys, minimal_root: Path):
    code = validation_main.main(["--root", str(minimal_root)])
    out = capsys.readouterr().out
    assert code == 0
    assert f"Explicit root: {minimal_root}" in out
    assert "framework-structure" in out
    assert "exit_code=0" in out


def test_cli_explicit_root_failure(capsys, tmp_path: Path):
    code = validation_main.main(["--root", str(tmp_path / "missing")])
    out = capsys.readouterr().out
    assert code == 1
    assert "STR-008" in out
    assert "exit_code=1" in out


def test_cli_subprocess_real_repo():
    proc = subprocess.run(
        [sys.executable, "-m", "validation", "--root", str(REPO_ROOT)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0
    assert "framework-structure" in proc.stdout
    assert "Framework Structure Validation" in proc.stdout
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
    # Only --root beyond argparse defaults.
    assert "--fix" not in proc.stdout
    assert "--module" not in proc.stdout


def test_cli_subprocess_default_upward_discovery(minimal_root: Path):
    """Real ``python -m validation`` with cwd-based upward discovery (no --root)."""
    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = (
        str(REPO_ROOT) if not existing else os.pathsep.join([str(REPO_ROOT), existing])
    )
    proc = subprocess.run(
        [sys.executable, "-m", "validation"],
        cwd=str(minimal_root),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "framework-structure" in proc.stdout
    assert "Framework Structure Validation" in proc.stdout
    assert "exit_code=0" in proc.stdout
    assert "Explicit root:" not in proc.stdout
