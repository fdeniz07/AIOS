"""
Phase 3.3.3 version command tests.

Temporary directories and fake repositories only.
Does not modify the real AIOS VERSION file during assertions
beyond reading the live checkout for V01.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
AIOSCTL_PATH = REPO_ROOT / "scripts" / "aiosctl.py"


def run_cli(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(AIOSCTL_PATH), *args],
        cwd=str(cwd or REPO_ROOT),
        capture_output=True,
        text=True,
    )


def test_v01_version_command_returns_zero_and_shows_framework_version():
    result = run_cli("version")
    assert result.returncode == 0
    combined = (result.stdout or "") + (result.stderr or "")
    assert "AIOS" in combined
    assert "Framework Version : 1.0.1" in combined
    assert "CLI               : Integrated" in combined
    assert "Python            :" in combined
    assert "Repository        :" in combined
    assert str(REPO_ROOT) in combined


def test_v02_reads_version_from_fake_root(aiosctl, tmp_path: Path, monkeypatch):
    root = tmp_path / "fake_aios"
    root.mkdir()
    (root / "VERSION").write_text("9.9.9\n", encoding="utf-8")
    monkeypatch.setattr(aiosctl, "locate_repository_root", lambda: root)

    assert aiosctl.read_framework_version() == "9.9.9"

    monkeypatch.setattr(sys, "argv", ["aiosctl", "version"])
    assert aiosctl.main() == 0


def test_v03_missing_version_file_is_unspecified(
    aiosctl, tmp_path: Path, monkeypatch, caplog
):
    import logging

    root = tmp_path / "no_version"
    root.mkdir()
    # No VERSION file; rules/ also absent — version must still work.
    assert aiosctl.read_framework_version(root) == aiosctl.UNSPECIFIED_VERSION

    monkeypatch.setattr(aiosctl, "locate_repository_root", lambda: root)
    with caplog.at_level(logging.INFO, logger="AIOS"):
        aiosctl.command_version()

    messages = "\n".join(caplog.messages)
    assert "Framework Version : unspecified" in messages


def test_v04_empty_version_file_is_unspecified(aiosctl, tmp_path: Path):
    root = tmp_path / "empty_version"
    root.mkdir()
    (root / "VERSION").write_text("\n", encoding="utf-8")
    assert aiosctl.read_framework_version(root) == "unspecified"


def test_v05_does_not_require_rules_directory(aiosctl, tmp_path: Path, monkeypatch):
    root = tmp_path / "no_rules"
    root.mkdir()
    (root / "VERSION").write_text("2.0.0\n", encoding="utf-8")
    assert not (root / "rules").exists()

    monkeypatch.setattr(aiosctl, "locate_repository_root", lambda: root)
    monkeypatch.setattr(sys, "argv", ["aiosctl", "version"])
    assert aiosctl.main() == 0
    assert aiosctl.read_framework_version() == "2.0.0"


def test_v06_unavailable_root_is_graceful(aiosctl, monkeypatch, caplog):
    import logging

    monkeypatch.setattr(aiosctl, "locate_repository_root", lambda: None)
    assert aiosctl.read_framework_version() == "unspecified"

    with caplog.at_level(logging.INFO, logger="AIOS"):
        aiosctl.command_version()

    messages = "\n".join(caplog.messages)
    assert "Framework Version : unspecified" in messages
    assert "Repository        : (unavailable)" in messages


def test_v07_does_not_use_changelog_or_doc_versions(aiosctl, tmp_path: Path):
    root = tmp_path / "signals"
    root.mkdir()
    (root / "CHANGELOG.md").write_text("## v9.9.9\n", encoding="utf-8")
    (root / "MANIFEST.md").write_text("Version: 8.8.8\n", encoding="utf-8")
    # No VERSION file → unspecified despite other signals
    assert aiosctl.read_framework_version(root) == "unspecified"


def test_v08_first_line_only(aiosctl, tmp_path: Path):
    root = tmp_path / "multiline"
    root.mkdir()
    (root / "VERSION").write_text("3.1.4\n# comment\n", encoding="utf-8")
    assert aiosctl.read_framework_version(root) == "3.1.4"
