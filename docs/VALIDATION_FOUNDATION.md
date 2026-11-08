# AIOS Validation Foundation

Status: current shared contract (originated in Phase 8.1.2; updated for the current package state)
Package: `validation/`
CLI: `python -m validation`

---

## Purpose and scope

This document describes the **shared validation infrastructure** used by AIOS repository validators.

### Historical Phase 8.1.2 scope

Phase 8.1.2 originally delivered only the foundation:

- Shared finding model
- Deterministic aggregation and duplicate suppression
- Severity / exit-code contract
- Explicit orchestrator interface
- Deterministic reporter
- Independent CLI entry point with an **empty** default registry

At that time the foundation did **not** implement framework structure rules, Module contract rules, documentation-link checks, governance checks, or CI wiring.

### Current package state

Later Phase 8 work registered domain validators on the same foundation. The current package still owns the shared model and CLI, and now also hosts:

- Framework Structure Validation (Phase 8.2)
- Module Contract Validation (Phase 8.3)
- Documentation Integrity Validation (Phase 8.4)

GitHub Actions CI integration for those validators was added in Phase 8.5. This document remains the contract for shared models, aggregation, orchestration, reporting, and exit codes. Domain rule details live in the Phase 8.2 / 8.3 design documents and the Documentation Integrity implementation.

---

## Package architecture

```text
validation/
├── __init__.py                 # public exports (lazy Module / Docs validators)
├── __main__.py                 # python -m validation
├── models.py                   # Finding, Severity, ValidationResult, aggregation
├── orchestrator.py             # Orchestrator, ValidatorSpec, ValidatorAbortError
├── reporter.py                 # format_report()
├── framework_structure.py      # Framework Structure Validation
├── module_contract.py          # Module Contract Validation
└── documentation_integrity.py  # Documentation Integrity Validation
```

### Public API

Exported symbols include:

- `Finding`, `Severity`, `ValidationResult`, `aggregate_findings`
- `EXIT_OK`, `EXIT_VALIDATION_ERROR`, `EXIT_EXECUTION_FAILURE`
- `Orchestrator`, `ValidatorSpec`, `ValidatorAbortError`
- `format_report`
- `validate_framework_structure`
- `validate_module_contract` (lazy)
- `validate_documentation_integrity` (lazy)

The shared `Finding` contract is domain-agnostic. Domain validators add rules without changing this model.

This package is independent of `scripts/aiosctl.py` and of `DiagnosticFinding` used by `aiosctl doctor`.

---

## Finding model

| Field | Type | Notes |
|-------|------|--------|
| `code` | `str` | Machine-oriented finding code |
| `severity` | `Severity` | `ERROR`, `WARNING`, or `INFO` |
| `category` | `str` | Logical grouping (for example `structure`, `module`, `documentation-integrity`) |
| `message` | `str` | Human-readable description |
| `path` | `str \| None` | Location identity for reporting and aggregation (see below) |
| `rule` | `str \| None` | Stable rule identifier used for duplicate identity |
| `suggestion` | `str \| None` | Optional remediation hint |

Serialization: `Finding.to_dict()` / `Finding.from_dict()` produce stable key sets suitable for tests and tooling.

### `Finding.path` semantics

- Prefer a **repository-relative** source path when a single filesystem path is sufficient.
- Individual validators may populate `path` with a **composite identity** so that multiple findings that share the same rule and source file are not collapsed by aggregation.
- Aggregation identity remains **`(rule, path)`** (missing values treated as empty string). Consumers that need a filesystem path should treat composite values as opaque identities or parse only the leading path segment before the first `#`.

Examples used by current validators:

| Validator | Example `path` | Meaning |
|-----------|----------------|---------|
| Framework Structure | `README.md` | Plain repository-relative path |
| Module Contract | `modules/sample/module.yaml#status` | Same YAML file, distinct field identity |
| Documentation Integrity | `docs/a.md#L3#missing.md` | Source file + optional line + link/image target |

Human-readable locations may also appear in `message` (for example `docs/a.md:3`). That does not change the aggregation key.

---

## Severity and exit-code contract

| Exit code | Meaning |
|-----------|---------|
| `0` | Successful validation: no `ERROR` findings and no execution failure |
| `1` | Validation errors: at least one `ERROR` finding |
| `2` | Execution or configuration failure |

`WARNING` and `INFO` never produce exit code `1`.

Execution failures (validator exceptions, invalid validator return values, or `ValidatorAbortError`) are distinct from ordinary contract violations and use exit code `2`.

---

## Aggregation and duplicate suppression

- Duplicate identity: **same `rule` and same `path`** (missing values treated as empty string).
- Distinct findings are preserved when `rule` or `path` differs.
- When duplicates collide, the finding with the **higher severity** is kept (`ERROR` > `WARNING` > `INFO`). Equal severity ties break by a deterministic lexicographic key of finding fields so encounter order does not change the winner.
- Final ordering is deterministic: severity rank, then `rule`, `path`, `code`, `category`, `message`, `suggestion`.

---

## Orchestration interface

Callers construct an `Orchestrator` and register named callables:

```python
from validation import Finding, Orchestrator, Severity

def example_validator():
    return [
        Finding(
            code="EX001",
            severity=Severity.INFO,
            category="example",
            message="illustrative only",
            rule="example.rule",
            path="README.md",
        )
    ]

orch = Orchestrator()
orch.register("example", example_validator)
result = orch.run()
```

- Validators run in ascending **name** order (deterministic execution order).
- Duplicate registration names raise `ValueError`.
- No plugin system, dynamic discovery, or external registry is provided.

### Current default CLI registry

`python -m validation` registers and runs, in execution order:

1. `documentation-integrity`
2. `framework-structure`
3. `module-contract`

Pack validation is **not** registered and is explicitly reported as not performed.

### `ValidatorAbortError` and early abort

Domain runners raise `ValidatorAbortError` when a validator completes with an `execution_error` (exit-code `2` semantics) while still carrying findings.

Orchestrator behavior:

- Stops further validators after the abort.
- Aggregates findings already collected from earlier validators together with findings attached to the abort.
- Sets `ValidationResult.execution_error` and therefore exit code `2`.

Findings collected before the execution failure are preserved. Unexpected exceptions and `None` validator returns are also treated as execution failures.

---

## Reporter responsibilities

`format_report(result)` emits stable text:

- Severity label per finding
- `code`, `category`, `rule`, `path`, message
- `suggestion` when present
- `execution_error` when present
- Trailing `exit_code=N`

Reporting stays separate from validation logic.

---

## CLI behavior

```powershell
python -m validation
```

Independent of:

```powershell
python scripts/aiosctl.py
```

Current default behavior:

- Prints a banner listing the three registered domain validators in execution order
- States that Pack validation is **not** performed
- Runs the registered validators through the Orchestrator
- Prints the deterministic report and exits with `0` / `1` / `2`

Optional:

```powershell
python -m validation --root <path>
```

---

## Extension model for additional validators

Later approved domains may:

1. Implement domain validator functions returning `Sequence[Finding]`
2. Register them on an `Orchestrator` by stable name
3. Reuse `format_report` and `ValidationResult.exit_code()`

---

## Current implementation boundaries

Implemented in the current package:

- Shared models, aggregation, orchestrator, reporter, CLI
- Framework Structure, Module Contract, and Documentation Integrity validators
- Unit/integration tests under `tests/validation_foundation/`, `tests/validation_structure/`, `tests/validation_module_contract/`, and `tests/validation_documentation/`
- CI jobs `framework-validation-tests` and `framework-validation-cli` (Phase 8.5)

Still out of scope for this foundation contract:

- Pack validation
- `aiosctl validate` (or any new `aiosctl` command)
- Automatic remediation
- Plugin loading
- Consumer repository modification

---

## Explicit non-goals

- Changing Framework Contract or Module governance rules
- Replacing or wrapping `aiosctl doctor`
- Treating a successful empty historical registry as a full AIOS validation pass
- Claiming Pack validation or Consumer adoption checks
