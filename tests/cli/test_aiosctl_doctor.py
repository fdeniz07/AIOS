"""
Phase 3.3.4 doctor command tests.

Uses temporary fake repositories only for structural diagnostics.
Does not modify consumer repositories or Module infrastructure.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
AIOSCTL_PATH = REPO_ROOT / "scripts" / "aiosctl.py"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(AIOSCTL_PATH), *args],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )


def build_healthy_root(base: Path) -> Path:
    root = base / "healthy_aios"
    (root / "rules").mkdir(parents=True)
    (root / "docs").mkdir(parents=True)
    (root / "methodology").mkdir(parents=True)
    (root / "VERSION").write_text("1.0.1\n", encoding="utf-8")
    (root / "rules" / "SAMPLE.md").write_text("# sample\n", encoding="utf-8")
    (root / "AGENTS.md").write_text("# agents\n", encoding="utf-8")
    (root / "MANIFEST.md").write_text("# manifest\n", encoding="utf-8")
    (root / "ROADMAP.md").write_text("# roadmap\n", encoding="utf-8")
    (root / "docs" / "FRAMEWORK_CONTRACT.md").write_text(
        "# contract\n", encoding="utf-8"
    )
    (root / "aiosctl.yaml").write_text("# documentary\n", encoding="utf-8")
    return root


def severities(findings) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in findings:
        counts[item.severity] = counts.get(item.severity, 0) + 1
    return counts


def test_d01_live_doctor_healthy_exit_zero():
    result = run_cli("doctor")
    combined = (result.stdout or "") + (result.stderr or "")
    assert result.returncode == 0
    assert "AIOS Doctor" in combined
    assert "[PASS] Python runtime" in combined
    assert "[PASS] Repository root" in combined
    assert "[PASS] Framework version" in combined
    assert "[PASS] CLI script" in combined
    assert "[PASS] Rules directory" in combined
    assert "[PASS] Framework contract" in combined
    assert "Errors   : 0" in combined
    assert "AIOS environment is healthy." in combined
    assert "modules/" not in combined.lower()


def test_d02_healthy_fake_root(aiosctl, tmp_path: Path):
    root = build_healthy_root(tmp_path)
    findings = aiosctl.collect_doctor_findings(root)
    assert severities(findings).get(aiosctl.SEVERITY_ERROR, 0) == 0
    titles = {item.title for item in findings}
    assert "Python runtime" in titles
    assert "Framework version" in titles
    assert "Configuration" in titles
    assert not any("modules" in item.title.lower() for item in findings)


def test_d03_missing_version_is_error(aiosctl, tmp_path: Path, monkeypatch):
    root = build_healthy_root(tmp_path)
    (root / "VERSION").unlink()
    findings = aiosctl.collect_doctor_findings(root)
    version_findings = [f for f in findings if f.title == "Framework version"]
    assert version_findings
    assert version_findings[0].severity == aiosctl.SEVERITY_ERROR

    monkeypatch.setattr(aiosctl, "locate_repository_root", lambda: root)
    monkeypatch.setattr(sys, "argv", ["aiosctl", "doctor"])
    assert aiosctl.main() == 1


def test_d04_unspecified_version_is_error(aiosctl, tmp_path: Path):
    root = build_healthy_root(tmp_path)
    (root / "VERSION").write_text("\n", encoding="utf-8")
    findings = aiosctl.collect_doctor_findings(root)
    version_findings = [f for f in findings if f.title == "Framework version"]
    assert version_findings[0].severity == aiosctl.SEVERITY_ERROR


def test_d05_missing_rules_is_error(aiosctl, tmp_path: Path):
    root = build_healthy_root(tmp_path)
    # Remove rules tree
    for child in (root / "rules").iterdir():
        child.unlink()
    (root / "rules").rmdir()
    findings = aiosctl.collect_doctor_findings(root)
    rules = [f for f in findings if f.title == "Rules directory"]
    assert rules[0].severity == aiosctl.SEVERITY_ERROR


def test_d06_empty_rules_is_warning_not_error(aiosctl, tmp_path: Path, monkeypatch):
    root = build_healthy_root(tmp_path)
    (root / "rules" / "SAMPLE.md").unlink()
    findings = aiosctl.collect_doctor_findings(root)
    assert severities(findings).get(aiosctl.SEVERITY_ERROR, 0) == 0
    warnings = [f for f in findings if f.severity == aiosctl.SEVERITY_WARNING]
    assert any(f.title == "Rules content" for f in warnings)

    monkeypatch.setattr(aiosctl, "locate_repository_root", lambda: root)
    monkeypatch.setattr(sys, "argv", ["aiosctl", "doctor"])
    assert aiosctl.main() == 0


def test_d07_missing_required_docs_are_errors(aiosctl, tmp_path: Path):
    root = build_healthy_root(tmp_path)
    (root / "AGENTS.md").unlink()
    (root / "docs" / "FRAMEWORK_CONTRACT.md").unlink()
    findings = aiosctl.collect_doctor_findings(root)
    by_title = {f.title: f for f in findings}
    assert by_title["AGENTS.md"].severity == aiosctl.SEVERITY_ERROR
    assert by_title["Framework contract"].severity == aiosctl.SEVERITY_ERROR


def test_d08_missing_methodology_is_info(aiosctl, tmp_path: Path):
    root = build_healthy_root(tmp_path)
    (root / "methodology").rmdir()
    findings = aiosctl.collect_doctor_findings(root)
    method = [f for f in findings if f.title == "Methodology directory"]
    assert method[0].severity == aiosctl.SEVERITY_INFO
    assert "Not present" in method[0].detail


def test_d09_aiosctl_yaml_documentary_info(aiosctl, tmp_path: Path):
    root = build_healthy_root(tmp_path)
    findings = aiosctl.collect_doctor_findings(root)
    config = [f for f in findings if f.title == "Configuration"]
    assert config[0].severity == aiosctl.SEVERITY_INFO
    assert "not consumed" in config[0].detail


def test_d10_missing_aiosctl_yaml_is_info(aiosctl, tmp_path: Path):
    root = build_healthy_root(tmp_path)
    (root / "aiosctl.yaml").unlink()
    findings = aiosctl.collect_doctor_findings(root)
    config = [f for f in findings if f.title == "Configuration"]
    assert config[0].severity == aiosctl.SEVERITY_INFO
    assert "not present" in config[0].detail


def test_d11_no_modules_requirement(aiosctl, tmp_path: Path):
    root = build_healthy_root(tmp_path)
    assert not (root / "modules").exists()
    findings = aiosctl.collect_doctor_findings(root)
    assert severities(findings).get(aiosctl.SEVERITY_ERROR, 0) == 0
    joined = " ".join(f"{f.title} {f.detail}" for f in findings).lower()
    assert "modules/" not in joined
    assert "module package" not in joined


def test_d12_doctor_is_read_only(aiosctl, tmp_path: Path, monkeypatch):
    root = build_healthy_root(tmp_path)
    before = {
        path.relative_to(root): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }
    monkeypatch.setattr(aiosctl, "locate_repository_root", lambda: root)
    assert aiosctl.command_doctor() == 0
    after = {
        path.relative_to(root): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }
    assert before == after


def test_d13_unavailable_root_exits_one(aiosctl, monkeypatch):
    monkeypatch.setattr(aiosctl, "locate_repository_root", lambda: None)
    monkeypatch.setattr(sys, "argv", ["aiosctl", "doctor"])
    assert aiosctl.main() == 1


def test_d14_python_below_minimum_is_error(aiosctl, tmp_path: Path, monkeypatch):
    from types import SimpleNamespace

    root = build_healthy_root(tmp_path)
    fake_version = SimpleNamespace(major=3, minor=9, micro=0)
    monkeypatch.setattr(aiosctl.sys, "version_info", fake_version)

    findings = aiosctl.collect_doctor_findings(root)
    python_findings = [f for f in findings if f.title == "Python runtime"]
    assert python_findings
    assert python_findings[0].severity == aiosctl.SEVERITY_ERROR
    assert "3.9.0" in python_findings[0].detail

    monkeypatch.setattr(aiosctl, "locate_repository_root", lambda: root)
    monkeypatch.setattr(sys, "argv", ["aiosctl", "doctor"])
    assert aiosctl.main() == 1


def test_d15_missing_manifest_is_error(aiosctl, tmp_path: Path, monkeypatch):
    root = build_healthy_root(tmp_path)
    (root / "MANIFEST.md").unlink()

    findings = aiosctl.collect_doctor_findings(root)
    manifest = [f for f in findings if f.title == "MANIFEST.md"]
    assert manifest
    assert manifest[0].severity == aiosctl.SEVERITY_ERROR
    assert "Missing or unreadable" in manifest[0].detail

    monkeypatch.setattr(aiosctl, "locate_repository_root", lambda: root)
    monkeypatch.setattr(sys, "argv", ["aiosctl", "doctor"])
    assert aiosctl.main() == 1


def test_d16_missing_roadmap_is_error(aiosctl, tmp_path: Path, monkeypatch):
    root = build_healthy_root(tmp_path)
    (root / "ROADMAP.md").unlink()

    findings = aiosctl.collect_doctor_findings(root)
    roadmap = [f for f in findings if f.title == "ROADMAP.md"]
    assert roadmap
    assert roadmap[0].severity == aiosctl.SEVERITY_ERROR
    assert "Missing or unreadable" in roadmap[0].detail

    monkeypatch.setattr(aiosctl, "locate_repository_root", lambda: root)
    monkeypatch.setattr(sys, "argv", ["aiosctl", "doctor"])
    assert aiosctl.main() == 1
