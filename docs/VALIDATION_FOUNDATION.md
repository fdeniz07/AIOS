# AIOS Validation Foundation

Status: draft foundation (Phase 8.1.2)
Package: `validation/`
CLI: `python -m validation`

---

## Purpose and scope

This document describes the **shared validation infrastructure** used by future AIOS repository validators.

Phase 8.1.2 delivers only the foundation:

- Shared finding model
- Deterministic aggregation and duplicate suppression
- Severity / exit-code contract
- Explicit orchestrator interface
- Deterministic reporter
- Independent CLI entry point

It does **not** implement framework structure rules, Module contract rules, documentation-link checks, governance checks, or CI wiring.

---

## Package architecture

```text
validation/
├── __init__.py       # public exports
├── __main__.py       # python -m validation
├── models.py         # Finding, Severity, ValidationResult, aggregation
├── orchestrator.py   # Orchestrator, ValidatorSpec
└── reporter.py       # format_report()
```

The shared `Finding` contract is domain-agnostic. Future validators add rules without changing this model.

This package is independent of `scripts/aiosctl.py` and of `DiagnosticFinding` used by `aiosctl doctor`.

---

## Finding model

| Field | Type | Notes |
|-------|------|--------|
| `code` | `str` | Machine-oriented finding code |
| `severity` | `Severity` | `ERROR`, `WARNING`, or `INFO` |
| `category` | `str` | Logical grouping (for example `structure`, `module`) |
| `message` | `str` | Human-readable description |
| `path` | `str \| None` | Repository-relative path when applicable |
| `rule` | `str \| None` | Stable rule identifier used for duplicate identity |
| `suggestion` | `str \| None` | Optional remediation hint |

Serialization: `Finding.to_dict()` / `Finding.from_dict()` produce stable key sets suitable for tests and tooling.

---

## Severity and exit-code contract

| Exit code | Meaning |
|-----------|---------|
| `0` | No `ERROR` findings and no execution failure |
| `1` | At least one `ERROR` finding |
| `2` | Execution or configuration failure |

`WARNING` and `INFO` never produce exit code `1`.

Execution failures (validator exceptions, invalid validator return values) are distinct from ordinary contract violations and use exit code `2`.

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

- Validators run in ascending **name** order.
- Duplicate registration names raise `ValueError`.
- No plugin system, dynamic discovery, or external registry is provided.
- Phase 8.1.2 default CLI registry is **empty**.

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

With no registered validators (Phase 8.1.2 default):

- Prints an explicit banner that **no domain validators are registered**
- States that framework structure and Module contract validation were **not** performed
- Runs an empty orchestration
- Reports `No findings.` and `exit_code=0`
- Must **not** be interpreted as comprehensive repository validation success

---

## Extension model for future validators

Later phases may:

1. Implement domain validator functions returning `Sequence[Finding]`
2. Register them on an `Orchestrator` by stable name
3. Reuse `format_report` and `ValidationResult.exit_code()`

Expected future domains (not implemented here):

- Framework structure validation (Phase 8.2)
- Module contract validation (Phase 8.3)
- Documentation integrity
- Additional approved domains

---

## Current implementation boundaries

Implemented:

- Shared models, aggregation, orchestrator, reporter, CLI
- Unit tests under `tests/validation_foundation/`
- This foundation document

Not implemented:

- Domain rule packs
- Module discovery / YAML metadata validation
- Markdown link or anchor validation
- CI job integration
- `aiosctl validate` (or any new `aiosctl` command)
- Automatic remediation
- Plugin loading

---

## Explicit non-goals

- Changing Framework Contract or Module governance rules
- Replacing or wrapping `aiosctl doctor`
- Consumer repository modification
- Claiming Phase 8.2 / 8.3 completion
- Treating an empty validator registry as a full AIOS validation pass
