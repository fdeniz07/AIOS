"""AIOS validation package.

Shared foundation (Phase 8.1.2), Framework Structure Validation (Phase 8.2),
and Module Contract Validation (Phase 8.3).

``validate_module_contract`` is loaded lazily so importing foundation / structure
symbols does not require PyYAML until Module Contract Validation is used.
"""

from __future__ import annotations

from typing import Any

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
    "validate_module_contract",
]

__version__ = "0.1.0"


def __getattr__(name: str) -> Any:
    if name == "validate_module_contract":
        from .module_contract import validate_module_contract

        return validate_module_contract
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
