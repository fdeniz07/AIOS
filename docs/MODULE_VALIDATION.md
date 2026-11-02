# AIOS Module Validation Strategy

Version: 1.0.0

Status: Approved

Last Updated: 2026-11-02

Document type: Module validation expectations

This document defines **future validation requirements and architecture** for AIOS Modules.

It does **not** implement validators, schemas, tests, CLI commands, or CI workflows.

Related authorities:

- Architecture: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5
- Precedence (L0–L7): [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7
- Metadata field model: [`MODULE_METADATA.md`](MODULE_METADATA.md)
- Lifecycle governance: [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md)
- Sync compatibility: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §9

---

## 1. Purpose

Ensure that when Modules exist, they can be checked against approved contracts in a proportionate way:

- Mechanical checks for objective contract compliance.
- Human architecture review for subjective quality and integration judgment.

Validation never installs, adopts, or modifies consumer repositories.

---

## 2. Validation layers

Seven layers. Distinguish **mechanical validation** from **human architecture review**.

| # | Layer | Primary mode |
|---|-------|--------------|
| 1 | Structural validation | Mechanical (+ human for proportionality) |
| 2 | Metadata validation | Mechanical |
| 3 | Lifecycle validation | Mechanical (+ human for subjective completeness) |
| 4 | Dependency validation | Mechanical for v1 bans; human/deferred for cycles |
| 5 | Governance validation | Mixed (see §7) |
| 6 | Documentation validation | Mixed (heading presence mechanical; quality human) |
| 7 | Core / Module / Pack integration review | Primarily human |

---

## 3. Active Module minimum requirements

An **`active`** Module requires:

- `module.yaml`
- `README.md`
- All five required metadata fields valid per [`MODULE_METADATA.md`](MODULE_METADATA.md): `id`, `version`, `title`, `summary`, `status`

Missing `applies_when` or `avoid_when` produces a **Warning**, not an Error.

Optional directories (`knowledge/`, `skills/`, `workflows/`, `checklists/`, `templates/`, `examples/`, `tests/`) must **not** become mandatory merely because they appear in an illustrative layout. Absence of optional directories is not an Error.

`draft` Modules may be incomplete; disclosure expectations follow [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md). Do not treat draft incompleteness as an Error by default.

---

## 4. Metadata validation

Authoritative field specification: [`MODULE_METADATA.md`](MODULE_METADATA.md).

Documented checks:

| Check | Severity |
|-------|----------|
| Required fields present and non-empty | Error if missing/invalid |
| Optional fields valid when present | Error if present but invalid enum/format |
| `id` lowercase English kebab-case; Pack-independent | Error if invalid |
| `version` SemVer (`MAJOR.MINOR.PATCH`, valid pre-release allowed) | Error if invalid |
| `status` ∈ {`draft`, `active`, `deprecated`} | Error if invalid |
| `maturity` ∈ {`experimental`, `stable`} when present | Error if invalid |
| `requires_core` SemVer minimum string when present | Error if invalid format |
| `deprecation` only when `status: deprecated` | Error if inconsistent |
| Unknown fields | **Warning** initially |
| `dependencies` key present in metadata v1 | **Error** |

Unknown-field policy may be reviewed in future metadata/validator versions. Do not introduce new metadata fields via validation.

---

## 5. Lifecycle validation

Authoritative lifecycle rules: [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md).

Preserve:

- Status: `draft`, `active`, `deprecated` only.
- Optional maturity: `experimental`, `stable`.
- Deprecated Modules normally omit maturity (Warning if present).
- Deprecated Modules require README migration guidance.

**Standard migration heading (mandatory for deprecated):**

```markdown
## Migration
```

A deprecated Module without a README section titled exactly `## Migration` is **invalid** (**Error**).

Do not make subjective documentation quality an Error (use Warning or Informational).

---

## 6. Dependency validation

Preserve Phase 2.4 decisions:

| Rule | Validation |
|------|------------|
| Metadata v1 has no Module dependency field | — |
| `dependencies` in metadata v1 | **Error** |
| Circular Module dependencies conceptually forbidden | Cycle checks **deferred** until an approved machine-readable relationship model exists |
| Companion relationships | Documentation-only; not hard dependency Errors |
| Pack composition | Not a Module dependency |
| Module → Pack dependency | Forbidden (human review / future checks); never encode Pack lock-in in Module metadata |
| Resolver / installer | Do not exist; validation must not assume them |

---

## 7. Governance validation

Preserve L0–L7 meanings. Validation does not change precedence.

| Rule | Notes |
|------|-------|
| Module guidance **L6** by default | Docs/metadata must not claim binding Core override |
| Explicit adoption into consumer local policy → **L3** | Consumer-owned recording |
| Consumer-approved ADRs → **L2** | Module does not own ADRs |
| Explicitly adopted Pack guidance → **L5** (unless incorporated into consumer local policy → L3) | Module must not redefine Pack authority |
| Metadata never implies adoption or installation | Mechanical + language checks |
| No silent modification of consumer-owned artifacts | Error if Module instructs silent overwrite |

### Mechanical vs human (governance)

| More mechanical | Human review |
|-----------------|--------------|
| Explicit “installed/adopted/enabled by metadata” claims | Nuanced L6/L3 wording quality |
| Explicit “silently overwrite consumer ADR/policy” instructions | Whether advice pressures ownership boundaries |
| Forbidden metadata keys (`dependencies` in v1) | Pack coupling / Core duplication judgment |

---

## 8. Severity model

### Error

Objectively violates an approved contract.

Examples:

- Missing required metadata field or required files for `active`
- Invalid required field, SemVer, status/maturity value
- `dependencies` present in metadata v1
- Deprecated Module without `## Migration`
- Explicit claims that metadata means installed or adopted
- Instructions to silently overwrite consumer-owned decisions

### Warning

Recommended quality or completeness is missing.

Examples:

- Missing `applies_when` or `avoid_when`
- Unknown metadata fields
- Thin README documentation
- Missing useful Core methodology references
- Incomplete experimental Module disclosures
- Maturity present on deprecated Module

### Informational

Optional improvements.

Examples:

- Suggested companion Modules
- Additional checklist recommendations
- Non-blocking documentation improvements

Do **not** classify subjective architectural preferences (for example “must use microservices”) as Errors.

---

## 9. Mechanical versus human review matrix

| Mechanical | Human architecture review |
|------------|---------------------------|
| File presence (`module.yaml`, `README.md`) | Core methodology duplication |
| YAML parsing | Pack coupling / Module→Pack lock-in |
| Required fields | Architecture trade-off quality |
| Enum values | Proportionality of Module scope |
| SemVer syntax | Whether a change warrants MAJOR |
| ID naming | ADR advice quality |
| `requires_core` format | Overreaching security claims |
| Unknown fields (warn) | |
| Deprecation field consistency | |
| `## Migration` heading presence when deprecated | |

---

## 10. Future CI policy

Approved future behavior (not implemented by this document):

- CI **fails on Errors only**.
- Warnings and Informational findings remain visible.
- **No Module CI** before actual Modules exist.
- Future Module validation must remain **separate** from `aiosctl sync`.
- Existing sync behavior and compatibility must **not** change.
- Phase 8 may introduce broader automated contract tests.

Do not implement CI workflows or CLI commands in this specification. A future `aiosctl module validate` (or equivalent) must not alter sync paths, filenames, or prune semantics.

---

## 11. Documentation validation expectations

| Topic | Mode | Typical severity if weak |
|-------|------|--------------------------|
| Purpose and scope | Human (+ structure) | Warning |
| `applies_when` / `avoid_when` | Mechanical presence | Warning if missing |
| Usage guidance | Human | Warning |
| Trade-offs | Human | Warning / Info |
| Core references | Human (+ link checks later) | Warning |
| Pack independence | Human | Warning / Error if Pack-required |
| Related Modules (companions) | Human / Info | Informational |
| Deprecation / `## Migration` | Mechanical when deprecated | Error if missing |
| Maintenance information | Human | Informational / Warning |

---

## 12. Core / Module / Pack integration review

Human-led checks for:

- Duplicate Core methodology content that should remain a Core reference.
- Pack-specific Module coupling.
- Module-to-Pack dependencies.
- Governance duplication or conflicting precedence claims.
- Unnecessary technology, IDE, agent, or LLM vendor lock-in.

---

## 13. Boundaries and non-goals

Validation **cannot** prove:

- An architecture recommendation is universally correct.
- A consumer should adopt a Module.
- An ADR is optimal.
- A system is secure merely because validation passed.
- Stable maturity guarantees permanent compatibility.
- Metadata implies adoption or installation.

Consumer adoption decisions remain **outside** Module validation.

Additional non-goals:

- Implementing validators, schemas, or tests in this document’s authority alone
- Using sync to install Modules
- Autonomous adaptive selection via validation tooling
- Expanding metadata v1 field set through validation rules

---

## Document maintenance

Changes to severity policy, active minimums, migration heading, or CI fail rules require Product Owner awareness and an update to this file. Keep Framework Contract references synchronized.

End of Module Validation Strategy v1.0.0.
