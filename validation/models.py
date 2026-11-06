"""Shared finding and result models for the AIOS validation foundation."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Optional, Sequence


class Severity(str, Enum):
    """Finding severity. Only ERROR fails validation (exit code 1)."""

    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


# Lower rank sorts first / wins duplicate severity ties toward stricter outcome.
SEVERITY_RANK: Mapping[Severity, int] = {
    Severity.ERROR: 0,
    Severity.WARNING: 1,
    Severity.INFO: 2,
}

EXIT_OK = 0
EXIT_VALIDATION_ERROR = 1
EXIT_EXECUTION_FAILURE = 2


@dataclass(frozen=True)
class Finding:
    """Domain-agnostic validation finding.

    Duplicate identity for aggregation is ``(rule, path)`` — see
    :func:`aggregate_findings`.
    """

    code: str
    severity: Severity
    category: str
    message: str
    path: Optional[str] = None
    rule: Optional[str] = None
    suggestion: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        """Stable JSON-friendly serialization."""
        return {
            "code": self.code,
            "severity": self.severity.value,
            "category": self.category,
            "message": self.message,
            "path": self.path,
            "rule": self.rule,
            "suggestion": self.suggestion,
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> Finding:
        return cls(
            code=str(data["code"]),
            severity=Severity(str(data["severity"])),
            category=str(data["category"]),
            message=str(data["message"]),
            path=_optional_str(data.get("path")),
            rule=_optional_str(data.get("rule")),
            suggestion=_optional_str(data.get("suggestion")),
        )


@dataclass(frozen=True)
class ValidationResult:
    """Aggregated outcome of one orchestration run."""

    findings: tuple[Finding, ...] = field(default_factory=tuple)
    execution_error: Optional[str] = None

    @property
    def has_errors(self) -> bool:
        return any(f.severity is Severity.ERROR for f in self.findings)

    def exit_code(self) -> int:
        if self.execution_error is not None:
            return EXIT_EXECUTION_FAILURE
        if self.has_errors:
            return EXIT_VALIDATION_ERROR
        return EXIT_OK

    def to_dict(self) -> dict[str, Any]:
        return {
            "findings": [f.to_dict() for f in self.findings],
            "execution_error": self.execution_error,
            "exit_code": self.exit_code(),
        }


def _optional_str(value: Any) -> Optional[str]:
    if value is None:
        return None
    return str(value)


def _identity(finding: Finding) -> tuple[str, str]:
    """Approved duplicate key: same rule and same path."""
    return (finding.rule or "", finding.path or "")


def _finding_sort_key(finding: Finding) -> tuple[Any, ...]:
    return (
        SEVERITY_RANK[finding.severity],
        finding.rule or "",
        finding.path or "",
        finding.code,
        finding.category,
        finding.message,
        finding.suggestion or "",
    )


def _prefer_finding(current: Finding, challenger: Finding) -> Finding:
    """When identities collide, keep higher severity; never drop stricter signal.

    Equal severity: prefer the lexicographically smaller deterministic key so
    outcome does not depend on encounter order.
    """
    cur_rank = SEVERITY_RANK[current.severity]
    chal_rank = SEVERITY_RANK[challenger.severity]
    if chal_rank < cur_rank:
        return challenger
    if chal_rank > cur_rank:
        return current
    if _finding_sort_key(challenger) < _finding_sort_key(current):
        return challenger
    return current


def aggregate_findings(findings: Sequence[Finding]) -> tuple[Finding, ...]:
    """Deduplicate by (rule, path) and return a deterministically ordered tuple.

    Ordering: severity (ERROR → WARNING → INFO), then rule, path, code,
    category, message, suggestion. Validator execution order does not affect
    the final order.
    """
    winners: dict[tuple[str, str], Finding] = {}
    for finding in findings:
        key = _identity(finding)
        existing = winners.get(key)
        if existing is None:
            winners[key] = finding
        else:
            winners[key] = _prefer_finding(existing, finding)
    ordered = sorted(winners.values(), key=_finding_sort_key)
    return tuple(ordered)
