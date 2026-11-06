"""Finding model and aggregation tests."""

from __future__ import annotations

import pytest

from validation.models import (
    EXIT_EXECUTION_FAILURE,
    EXIT_OK,
    EXIT_VALIDATION_ERROR,
    Finding,
    Severity,
    ValidationResult,
    aggregate_findings,
)


def test_finding_valid_construction():
    finding = Finding(
        code="F001",
        severity=Severity.WARNING,
        category="foundation",
        message="example",
        path="docs/x.md",
        rule="found.example",
        suggestion="fix it",
    )
    assert finding.code == "F001"
    assert finding.severity is Severity.WARNING
    assert finding.suggestion == "fix it"


def test_severity_values():
    assert {s.value for s in Severity} == {"ERROR", "WARNING", "INFO"}


def test_optional_fields_default_none():
    finding = Finding(
        code="F002",
        severity=Severity.INFO,
        category="foundation",
        message="minimal",
    )
    assert finding.path is None
    assert finding.rule is None
    assert finding.suggestion is None


def test_stable_serialization_roundtrip():
    finding = Finding(
        code="F003",
        severity=Severity.ERROR,
        category="foundation",
        message="broken",
        path="a/b",
        rule="r1",
        suggestion="repair",
    )
    data = finding.to_dict()
    assert list(data.keys()) == [
        "code",
        "severity",
        "category",
        "message",
        "path",
        "rule",
        "suggestion",
    ]
    assert data["severity"] == "ERROR"
    restored = Finding.from_dict(data)
    assert restored == finding


def test_aggregate_multiple_and_deterministic_order():
    findings = [
        Finding("c", Severity.INFO, "cat", "m3", path="p2", rule="r2"),
        Finding("a", Severity.ERROR, "cat", "m1", path="p1", rule="r1"),
        Finding("b", Severity.WARNING, "cat", "m2", path="p0", rule="r0"),
    ]
    first = aggregate_findings(findings)
    second = aggregate_findings(list(reversed(findings)))
    assert first == second
    assert [f.severity for f in first] == [
        Severity.ERROR,
        Severity.WARNING,
        Severity.INFO,
    ]


def test_duplicate_suppression_same_rule_and_path():
    findings = [
        Finding("a", Severity.INFO, "cat", "one", path="x", rule="dup"),
        Finding("b", Severity.INFO, "cat", "two", path="x", rule="dup"),
    ]
    result = aggregate_findings(findings)
    assert len(result) == 1


def test_same_rule_different_paths_preserved():
    findings = [
        Finding("a", Severity.WARNING, "cat", "m", path="a.md", rule="r"),
        Finding("a", Severity.WARNING, "cat", "m", path="b.md", rule="r"),
    ]
    assert len(aggregate_findings(findings)) == 2


def test_different_rules_same_path_preserved():
    findings = [
        Finding("a", Severity.WARNING, "cat", "m", path="a.md", rule="r1"),
        Finding("a", Severity.WARNING, "cat", "m", path="a.md", rule="r2"),
    ]
    assert len(aggregate_findings(findings)) == 2


def test_duplicate_keeps_higher_severity():
    findings = [
        Finding("a", Severity.INFO, "cat", "soft", path="x", rule="dup"),
        Finding("b", Severity.ERROR, "cat", "hard", path="x", rule="dup"),
        Finding("c", Severity.WARNING, "cat", "mid", path="x", rule="dup"),
    ]
    result = aggregate_findings(findings)
    assert len(result) == 1
    assert result[0].severity is Severity.ERROR
    assert result[0].code == "b"


def test_duplicate_equal_severity_is_deterministic():
    a = Finding("a", Severity.WARNING, "cat", "alpha", path="x", rule="dup")
    b = Finding("z", Severity.WARNING, "cat", "zeta", path="x", rule="dup")
    assert aggregate_findings([a, b]) == aggregate_findings([b, a])


@pytest.mark.parametrize(
    "findings,execution_error,expected",
    [
        ((), None, EXIT_OK),
        (
            (Finding("w", Severity.WARNING, "c", "m", rule="r", path="p"),),
            None,
            EXIT_OK,
        ),
        (
            (Finding("i", Severity.INFO, "c", "m", rule="r", path="p"),),
            None,
            EXIT_OK,
        ),
        (
            (Finding("e", Severity.ERROR, "c", "m", rule="r", path="p"),),
            None,
            EXIT_VALIDATION_ERROR,
        ),
        ((), "boom", EXIT_EXECUTION_FAILURE),
        (
            (Finding("e", Severity.ERROR, "c", "m", rule="r", path="p"),),
            "boom",
            EXIT_EXECUTION_FAILURE,
        ),
    ],
)
def test_exit_codes(findings, execution_error, expected):
    result = ValidationResult(findings=findings, execution_error=execution_error)
    assert result.exit_code() == expected
