"""Reporter and ``python -m validation`` CLI tests."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from validation.models import Finding, Severity, ValidationResult
from validation.reporter import format_report
from validation import __main__ as validation_main

REPO_ROOT = Path(__file__).resolve().parents[2]


def test_format_report_all_severities_and_suggestion():
    result = ValidationResult(
        findings=(
            Finding(
                "E1",
                Severity.ERROR,
                "cat",
                "err msg",
                path="a.py",
                rule="r.e",
                suggestion="fix me",
            ),
            Finding(
                "W1",
                Severity.WARNING,
                "cat",
                "warn msg",
                path="b.py",
                rule="r.w",
            ),
            Finding(
                "I1",
                Severity.INFO,
                "cat",
                "info msg",
                rule="r.i",
            ),
        )
    )
    text = format_report(result)
    assert "[ERROR] code=E1 category=cat rule=r.e path=a.py" in text
    assert "  err msg" in text
    assert "  suggestion: fix me" in text
    assert "[WARNING] code=W1" in text
    assert "[INFO] code=I1" in text
    assert "path=-" in text  # missing path rendered stably
    assert text.endswith("exit_code=1\n")


def test_format_report_stable_for_identical_results():
    finding = Finding("c", Severity.INFO, "cat", "m", rule="r", path="p")
    a = format_report(ValidationResult(findings=(finding,)))
    b = format_report(ValidationResult(findings=(finding,)))
    assert a == b


def test_format_report_execution_failure():
    text = format_report(ValidationResult(execution_error="validator 'x' failed"))
    assert text.startswith("[EXECUTION_FAILURE] validator 'x' failed\n")
    assert "exit_code=2\n" in text


def test_cli_main_registers_framework_structure_no_misleading_claims(capsys):
    code = validation_main.main(["--root", str(REPO_ROOT)])
    captured = capsys.readouterr()
    assert code == 0
    assert "framework-structure" in captured.out
    assert "module-contract" in captured.out
    assert "documentation-integrity" in captured.out
    assert "Framework Structure Validation" in captured.out
    assert "Module Contract Validation" in captured.out
    assert "Documentation Integrity Validation" in captured.out
    assert "Pack validation" in captured.out
    assert "NOT performed" in captured.out
    assert "No domain validators are registered" not in captured.out
    assert "No findings." in captured.out
    assert "exit_code=0" in captured.out
    assert "validation passed" not in captured.out.lower()
    assert "all checks" not in captured.out.lower()


def test_python_m_validation_subprocess():
    proc = subprocess.run(
        [sys.executable, "-m", "validation", "--root", str(REPO_ROOT)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0
    assert "framework-structure" in proc.stdout
    assert "module-contract" in proc.stdout
    assert "documentation-integrity" in proc.stdout
    assert "Framework Structure Validation" in proc.stdout
    assert "Module Contract Validation" in proc.stdout
    assert "Documentation Integrity Validation" in proc.stdout
    assert "NOT performed" in proc.stdout
    assert "exit_code=0" in proc.stdout
