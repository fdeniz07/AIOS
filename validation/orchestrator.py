"""Deterministic orchestration of registered validation callables."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Optional, Sequence

from .models import Finding, ValidationResult, aggregate_findings

ValidatorCallable = Callable[[], Sequence[Finding]]


class ValidatorAbortError(Exception):
    """Validator requests execution failure while retaining findings (exit 2)."""

    def __init__(self, message: str, findings: Sequence[Finding] = ()) -> None:
        super().__init__(message)
        self.findings: tuple[Finding, ...] = tuple(findings)


@dataclass(frozen=True)
class ValidatorSpec:
    """Named validator registration entry.

    Validators are executed in ascending ``name`` order. Names must be unique
    within one orchestrator instance.
    """

    name: str
    run: ValidatorCallable


class Orchestrator:
    """Run an explicit list of validators and aggregate their findings.

    No plugin loader, dynamic import, or external registry is used. Callers
    supply validators at construction time or via :meth:`register`.
    """

    def __init__(self, validators: Optional[Iterable[ValidatorSpec]] = None) -> None:
        self._validators: list[ValidatorSpec] = []
        if validators is not None:
            for spec in validators:
                self.register(spec.name, spec.run)

    @property
    def validator_names(self) -> tuple[str, ...]:
        return tuple(sorted(spec.name for spec in self._validators))

    def register(self, name: str, run: ValidatorCallable) -> None:
        if not name:
            raise ValueError("validator name must be non-empty")
        if any(spec.name == name for spec in self._validators):
            raise ValueError(f"duplicate validator name: {name!r}")
        self._validators.append(ValidatorSpec(name=name, run=run))

    def run(self) -> ValidationResult:
        """Execute validators in deterministic name order and aggregate findings.

        Any unexpected exception from a validator is treated as an execution
        failure (exit code 2). Findings collected before the failure are
        retained and still aggregated.
        """
        collected: list[Finding] = []
        for spec in sorted(self._validators, key=lambda item: item.name):
            try:
                batch = spec.run()
            except ValidatorAbortError as exc:
                return ValidationResult(
                    findings=aggregate_findings([*collected, *exc.findings]),
                    execution_error=str(exc),
                )
            except Exception as exc:  # noqa: BLE001 — foundation boundary
                message = f"validator {spec.name!r} failed: {type(exc).__name__}: {exc}"
                return ValidationResult(
                    findings=aggregate_findings(collected),
                    execution_error=message,
                )
            if batch is None:
                message = f"validator {spec.name!r} returned None"
                return ValidationResult(
                    findings=aggregate_findings(collected),
                    execution_error=message,
                )
            collected.extend(batch)
        return ValidationResult(findings=aggregate_findings(collected))
