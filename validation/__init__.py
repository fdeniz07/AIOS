"""AIOS validation package.

Shared foundation (Phase 8.1.2) plus Framework Structure Validation (Phase 8.2).
"""

from .framework_structure import validate_framework_structure
from .models import (
    EXIT_EXECUTION_FAILURE,
    EXIT_OK,
    EXIT_VALIDATION_ERROR,
    Finding,
    Severity,
    ValidationResult,
    aggregate_findings,
)
from .orchestrator import Orchestrator, ValidatorAbortError, ValidatorSpec
from .reporter import format_report

__all__ = [
    "EXIT_EXECUTION_FAILURE",
    "EXIT_OK",
    "EXIT_VALIDATION_ERROR",
    "Finding",
    "Orchestrator",
    "Severity",
    "ValidationResult",
    "ValidatorAbortError",
    "ValidatorSpec",
    "aggregate_findings",
    "format_report",
    "validate_framework_structure",
]

__version__ = "0.1.0"
