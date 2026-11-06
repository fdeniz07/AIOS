"""AIOS shared validation foundation (Phase 8.1.2).

This package provides finding models, aggregation, orchestration and reporting.
Domain validators (framework structure, Module contracts, documentation) are
registered by later phases — they are not included here.
"""

from .models import (
    EXIT_EXECUTION_FAILURE,
    EXIT_OK,
    EXIT_VALIDATION_ERROR,
    Finding,
    Severity,
    ValidationResult,
    aggregate_findings,
)
from .orchestrator import Orchestrator, ValidatorSpec
from .reporter import format_report

__all__ = [
    "EXIT_EXECUTION_FAILURE",
    "EXIT_OK",
    "EXIT_VALIDATION_ERROR",
    "Finding",
    "Orchestrator",
    "Severity",
    "ValidationResult",
    "ValidatorSpec",
    "aggregate_findings",
    "format_report",
]

__version__ = "0.1.0"
