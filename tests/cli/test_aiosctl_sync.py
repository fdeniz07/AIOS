"""
Phase 3.2 sync regression tests (T01–T17).

All fixtures use temporary directories only.
Does not modify the repository rules/ tree or real consumer projects.
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
AIOSCTL_PATH = REPO_ROOT / "scripts" / "aiosctl.py"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def write_rule(rules_dir: Path, name: str, body: str) -> Path:
    path = rules_dir / name
    path.write_text(body, encoding="utf-8")
    return path


def expected_dest_content(aiosctl, source_body: str) -> str:
    return aiosctl.build_header() + source_body


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def run_cli(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(AIOSCTL_PATH), *args],
        cwd=str(cwd or REPO_ROOT),
        capture_output=True,
        text=True,
    )


# ---------------------------------------------------------------------------
# Unit / integration against fabricated roots
# ---------------------------------------------------------------------------


def test_t01_normal_sync(aiosctl, fake_aios_root: Path, project_dir: Path):
    write_rule(fake_aios_root / "rules", "ALPHA.md", "alpha-body\n")
    write_rule(fake_aios_root / "rules", "BETA.md", "beta-body\n")

    aiosctl.sync_project(
        fake_aios_root,
        aiosctl.SyncOptions(project=project_dir),
    )

    agents = project_dir / ".agents"
    assert (agents / "ALPHA.md").is_file()
    assert (agents / "BETA.md").is_file()
    assert (agents / "AIOS_VERSION.md").is_file()
    assert (agents / "ALPHA.md").read_text(encoding="utf-8") == expected_dest_content(
        aiosctl, "alpha-body\n"
    )


def test_t02_missing_project_raises(aiosctl, fake_aios_root: Path, tmp_path: Path):
    missing = tmp_path / "does-not-exist"
    with pytest.raises(FileNotFoundError):
        aiosctl.sync_project(
            fake_aios_root,
            aiosctl.SyncOptions(project=missing),
        )


def test_t03_invalid_project_not_directory(aiosctl, fake_aios_root: Path, tmp_path: Path):
    not_dir = tmp_path / "not-a-dir.txt"
    not_dir.write_text("x", encoding="utf-8")
    with pytest.raises(NotADirectoryError):
        aiosctl.sync_project(
            fake_aios_root,
            aiosctl.SyncOptions(project=not_dir),
        )


def test_t04_missing_rules_directory_discover(aiosctl, tmp_path: Path, monkeypatch):
    scripts_dir = tmp_path / "scripts"
    scripts_dir.mkdir()
    fake_script = scripts_dir / "aiosctl.py"
    fake_script.write_text("# placeholder\n", encoding="utf-8")
    # parent.parent of scripts/aiosctl.py == tmp_path, which has no rules/
    monkeypatch.setattr(aiosctl, "__file__", str(fake_script))

    with pytest.raises(RuntimeError, match="rules directory not found"):
        aiosctl.discover_aios_root()


def test_t05_empty_rules_directory(aiosctl, fake_aios_root: Path, project_dir: Path):
    aiosctl.sync_project(
        fake_aios_root,
        aiosctl.SyncOptions(project=project_dir),
    )
    agents = project_dir / ".agents"
    assert agents.is_dir()
    assert list(agents.glob("*.md")) == [agents / "AIOS_VERSION.md"]
    assert (agents / "AIOS_VERSION.md").is_file()


def test_t06_new_file_copy(aiosctl, fake_aios_root: Path, project_dir: Path):
    write_rule(fake_aios_root / "rules", "NEW.md", "new-content\n")
    aiosctl.sync_project(
        fake_aios_root,
        aiosctl.SyncOptions(project=project_dir),
    )
    dest = project_dir / ".agents" / "NEW.md"
    assert dest.read_text(encoding="utf-8") == expected_dest_content(aiosctl, "new-content\n")


def test_t07_changed_file_update(aiosctl, fake_aios_root: Path, project_dir: Path):
    write_rule(fake_aios_root / "rules", "RULE.md", "v2\n")
    agents = project_dir / ".agents"
    agents.mkdir()
    (agents / "RULE.md").write_text(
        expected_dest_content(aiosctl, "v1\n"),
        encoding="utf-8",
    )

    aiosctl.sync_project(
        fake_aios_root,
        aiosctl.SyncOptions(project=project_dir),
    )
    assert (agents / "RULE.md").read_text(encoding="utf-8") == expected_dest_content(
        aiosctl, "v2\n"
    )


def test_t08_unchanged_hash_skip(aiosctl, fake_aios_root: Path, project_dir: Path):
    body = "stable\n"
    write_rule(fake_aios_root / "rules", "RULE.md", body)
    agents = project_dir / ".agents"
    agents.mkdir()
    dest = agents / "RULE.md"
    content = expected_dest_content(aiosctl, body)
    dest.write_text(content, encoding="utf-8")
    before_hash = sha256_text(content)

    copied = aiosctl.copy_rule(
        source=fake_aios_root / "rules" / "RULE.md",
        destination=dest,
        force=False,
        dry_run=False,
    )
    assert copied is False
    assert sha256_text(dest.read_text(encoding="utf-8")) == before_hash


def test_t09_force_overwrites_identical(aiosctl, fake_aios_root: Path, project_dir: Path):
    body = "stable\n"
    write_rule(fake_aios_root / "rules", "RULE.md", body)
    agents = project_dir / ".agents"
    agents.mkdir()
    dest = agents / "RULE.md"
    dest.write_text(expected_dest_content(aiosctl, body), encoding="utf-8")

    # Without --force, identical content must skip.
    assert (
        aiosctl.copy_rule(
            source=fake_aios_root / "rules" / "RULE.md",
            destination=dest,
            force=False,
            dry_run=False,
        )
        is False
    )

    # With --force, the write path runs even when content already matches.
    copied = aiosctl.copy_rule(
        source=fake_aios_root / "rules" / "RULE.md",
        destination=dest,
        force=True,
        dry_run=False,
    )
    assert copied is True
    assert dest.read_text(encoding="utf-8") == expected_dest_content(aiosctl, body)


def test_t10_dry_run_write_protection(aiosctl, fake_aios_root: Path, project_dir: Path):
    write_rule(fake_aios_root / "rules", "RULE.md", "dry\n")
    aiosctl.sync_project(
        fake_aios_root,
        aiosctl.SyncOptions(project=project_dir, dry_run=True),
    )
    agents = project_dir / ".agents"
    assert agents.is_dir()
    assert not (agents / "RULE.md").exists()
    assert not (agents / "AIOS_VERSION.md").exists()


def test_t11_header_generation(aiosctl, fake_aios_root: Path, project_dir: Path):
    write_rule(fake_aios_root / "rules", "RULE.md", "body\n")
    aiosctl.sync_project(
        fake_aios_root,
        aiosctl.SyncOptions(project=project_dir),
    )
    text = (project_dir / ".agents" / "RULE.md").read_text(encoding="utf-8")
    assert text.startswith(aiosctl.GENERATED_HEADER)
    assert "THIS FILE IS AUTO-GENERATED" in text
    assert "aiosctl sync" in text
    assert text.endswith("body\n") or "body\n" in text


def test_t12_orphan_preservation(aiosctl, fake_aios_root: Path, project_dir: Path):
    write_rule(fake_aios_root / "rules", "KEEP.md", "keep\n")
    agents = project_dir / ".agents"
    agents.mkdir()
    orphan = agents / "ORPHAN.md"
    orphan.write_text("orphan-content\n", encoding="utf-8")

    aiosctl.sync_project(
        fake_aios_root,
        aiosctl.SyncOptions(project=project_dir),
    )
    assert orphan.is_file()
    assert orphan.read_text(encoding="utf-8") == "orphan-content\n"
    assert (agents / "KEEP.md").is_file()


def test_t13_aios_version_created(aiosctl, fake_aios_root: Path, project_dir: Path):
    write_rule(fake_aios_root / "rules", "RULE.md", "x\n")
    aiosctl.sync_project(
        fake_aios_root,
        aiosctl.SyncOptions(project=project_dir),
    )
    version = (project_dir / ".agents" / "AIOS_VERSION.md").read_text(encoding="utf-8")
    assert version.startswith("# AIOS Rule Synchronization")
    assert "Generated:" in version
    assert "Source:" in version
    assert str(fake_aios_root) in version
    assert "aiosctl sync" in version
    assert "Do not edit manually." in version


def test_t14_aios_version_not_written_on_dry_run(
    aiosctl, fake_aios_root: Path, project_dir: Path
):
    write_rule(fake_aios_root / "rules", "RULE.md", "x\n")
    aiosctl.sync_project(
        fake_aios_root,
        aiosctl.SyncOptions(project=project_dir, dry_run=True),
    )
    assert not (project_dir / ".agents" / "AIOS_VERSION.md").exists()


def test_t15_path_handling_basename_preserved(
    aiosctl, fake_aios_root: Path, project_dir: Path
):
    # Nested-looking name is still a flat basename under rules/
    write_rule(fake_aios_root / "rules", "PATH_RULE.md", "path-ok\n")
    aiosctl.sync_project(
        fake_aios_root,
        aiosctl.SyncOptions(project=project_dir),
    )
    dest = project_dir / ".agents" / "PATH_RULE.md"
    assert dest.is_file()
    assert dest.name == "PATH_RULE.md"


def test_t16_argparse_missing_command_exit_2():
    result = run_cli()
    assert result.returncode == 2
    combined = (result.stdout or "") + (result.stderr or "")
    assert "command" in combined.lower() or "usage" in combined.lower()


def test_t02_t_runtime_failure_exit_1_missing_project(tmp_path: Path):
    missing = tmp_path / "missing-consumer"
    result = run_cli("sync", "--project", str(missing))
    assert result.returncode == 1
    combined = (result.stdout or "") + (result.stderr or "")
    assert "ERROR" in combined
    assert "Project directory not found" in combined


def test_t03_runtime_failure_exit_1_invalid_project(tmp_path: Path):
    not_dir = tmp_path / "file-not-dir.txt"
    not_dir.write_text("x", encoding="utf-8")
    result = run_cli("sync", "--project", str(not_dir))
    assert result.returncode == 1
    combined = (result.stdout or "") + (result.stderr or "")
    assert "ERROR" in combined


def test_t17_flat_glob_only(aiosctl, fake_aios_root: Path, project_dir: Path):
    write_rule(fake_aios_root / "rules", "TOP.md", "top\n")
    nested = fake_aios_root / "rules" / "nested"
    nested.mkdir()
    (nested / "NESTED.md").write_text("nested\n", encoding="utf-8")

    aiosctl.sync_project(
        fake_aios_root,
        aiosctl.SyncOptions(project=project_dir),
    )
    agents = project_dir / ".agents"
    assert (agents / "TOP.md").is_file()
    assert not (agents / "NESTED.md").exists()
    assert not (agents / "nested").exists()


def test_dry_run_counter_wording(aiosctl, fake_aios_root: Path, project_dir: Path, caplog):
    import logging

    write_rule(fake_aios_root / "rules", "RULE.md", "x\n")
    with caplog.at_level(logging.INFO, logger="AIOS"):
        aiosctl.sync_project(
            fake_aios_root,
            aiosctl.SyncOptions(project=project_dir, dry_run=True),
        )
    messages = "\n".join(caplog.messages)
    assert "Would copy :" in messages
    assert "Copied :" not in messages


def test_main_success_returns_0(aiosctl, fake_aios_root: Path, project_dir: Path, monkeypatch):
    write_rule(fake_aios_root / "rules", "RULE.md", "ok\n")
    monkeypatch.setattr(aiosctl, "discover_aios_root", lambda: fake_aios_root)
    monkeypatch.setattr(
        sys,
        "argv",
        ["aiosctl", "sync", "--project", str(project_dir)],
    )
    assert aiosctl.main() == 0
    assert (project_dir / ".agents" / "RULE.md").is_file()


def test_main_keyboard_interrupt_returns_130(aiosctl, monkeypatch):
    def boom(_args):
        raise KeyboardInterrupt()

    monkeypatch.setattr(aiosctl, "command_sync", boom)
    monkeypatch.setattr(sys, "argv", ["aiosctl", "sync", "--project", "."])
    assert aiosctl.main() == 130
