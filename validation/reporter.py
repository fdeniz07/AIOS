"""Deterministic text reporting for validation results."""

from __future__ import annotations

from .models import Severity, ValidationResult

_SEVERITY_LABEL = {
    Severity.ERROR: "ERROR",
    Severity.WARNING: "WARNING",
    Severity.INFO: "INFO",
}


def format_report(result: ValidationResult) -> str:
    """Render a stable, CI-friendly multi-line report.

    Finding order matches :attr:`ValidationResult.findings` (already
    aggregated and sorted). Output does not depend on locale or wall clock.
    """
    lines: list[str] = []

    if result.execution_error is not None:
        lines.append(f"[EXECUTION_FAILURE] {result.execution_error}")

    if not result.findings and result.execution_error is None:
        lines.append("No findings.")
    else:
        for finding in result.findings:
            label = _SEVERITY_LABEL[finding.severity]
            rule = finding.rule if finding.rule is not None else "-"
            path = finding.path if finding.path is not None else "-"
            lines.append(
                f"[{label}] code={finding.code} category={finding.category} "
                f"rule={rule} path={path}"
            )
            lines.append(f"  {finding.message}")
            if finding.suggestion:
                lines.append(f"  suggestion: {finding.suggestion}")

    lines.append(f"exit_code={result.exit_code()}")
    return "\n".join(lines) + "\n"
