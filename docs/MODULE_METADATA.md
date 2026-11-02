# AIOS Module Metadata Specification

Version: 1.1.0

Status: Approved

Last Updated: 2026-11-02

Document type: Module metadata contract

This document defines the **approved field model** for Module metadata (`module.yaml` when a Module exists).

It is subordinate to the Framework Contract for architecture and governance:

- Architecture and boundaries: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5
- Instruction precedence (L0–L7): [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7
- Module lifecycle and governance: [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md)
- Agent operationalization: [`../AGENTS.md`](../AGENTS.md) §2

This specification does **not**:

- Create or populate Modules
- Implement parsers, validators, or CLI commands
- Change L0–L7 precedence
- Imply that a Module has been adopted or installed by a consumer

Metadata is **descriptive**. Adoption remains a consumer-owned decision (Module guidance **L6** by default; explicit adoption into local policy → **L3**).

---

## 1. Purpose

`module.yaml` provides machine-readable identity, short discovery information, lifecycle signals, applicability hints, and optional minimum Core compatibility for an AIOS Module.

Detailed narrative belongs in the Module `README.md`, not in metadata.

---

## 2. Metadata versus README

| Concern | `module.yaml` | `README.md` |
|---------|---------------|-------------|
| Machine-readable identity | Yes | Optional restatement |
| Short discovery information | Yes (`summary`, tags, hints) | Expanded narrative |
| Lifecycle signal | Yes (`status`, optional `maturity`) | Deprecation explanation |
| Applicability hints | Short lists (`applies_when`, `avoid_when`) | Detailed scenarios and rationale |
| Minimum Core compatibility | Optional `requires_core` | Compatibility and testing notes |
| Purpose and scope | One-line / short summary only | Full purpose and scope |
| Usage guidance | No | Yes |
| Examples | No | Yes |
| Trade-offs | No | Yes |
| Adoption guidance | No | Yes (how a consumer may adopt into L3 policy) |

**Rules:**

- Metadata must **not** state or imply that a consumer has adopted, installed, enabled, or synced the Module.
- Metadata must **not** redefine Core governance or L0–L7.
- Do not duplicate the full README into YAML.

---

## 3. Approved field model (metadata v1)

### 3.1 Required fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Stable Module identifier. Lowercase English **kebab-case**. Must not be tied to a specific Pack. |
| `version` | string | Module package version. **SemVer** `MAJOR.MINOR.PATCH`, including valid pre-release identifiers. |
| `title` | string | Human-readable display name. |
| `summary` | string | Short purpose for discovery (one or a few sentences). |
| `status` | enum | Lifecycle publication state (see §4). |

### 3.2 Optional fields

| Field | Type | Description |
|-------|------|-------------|
| `maturity` | enum | Optional quality/stability signal, independent of `status` (see §4). |
| `applies_when` | list of strings | Short hints for when the Module is relevant. |
| `avoid_when` | list of strings | Short hints for when the Module is disproportionate or inappropriate. |
| `tags` | list of strings | Discovery labels (lowercase kebab-case recommended). |
| `provides` | list of strings | Coarse capability labels (not a substitute for README). |
| `requires_core` | string | Optional **minimum** supported AIOS Core/Framework version (SemVer). |
| `deprecation` | object | Only when `status` is `deprecated` (see §5). |

### 3.3 Explicitly excluded from metadata v1

- **`dependencies`** — not included. Do not add an empty or reserved `dependencies` key. Phase 2.4 dependency and compatibility **design** is **completed**: metadata v1 intentionally contains no Module-to-Module dependency fields. Future machine-readable Module relationship metadata remains deferred until a concrete use case justifies an approved additive extension.
- Tested Core version ranges and compatibility algorithms — not included.
- Adoption, installation, or sync state — not included.
- IDE, agent, or LLM vendor pins — not allowed.

---

## 4. Status and maturity

Field enums and independence rules live here. Full lifecycle definitions, draft/active expectations, experimental/stable expectations, SemVer governance, and migration rules live in [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md).

### Status (required)

Allowed values (exactly three — no additional states in metadata v1):

- `draft`
- `active`
- `deprecated`

`status` is the publication / lifecycle signal.

Semantics (summary; authoritative detail in [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md)):

- `draft` — work in progress; not generally recommended for new durable adoption.
- `active` — maintained and available for evaluation; not adopted/installed by metadata alone.
- `deprecated` — not recommended for new adoption; README must include the exact heading `## Migration` (see §5 and [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md)).

### Maturity (optional)

Allowed values:

- `experimental`
- `stable`

`maturity` is independent of `status`.

When `status` is `deprecated`, `maturity` should normally be **omitted**.

Examples of valid combinations:

| status | maturity | Meaning (informational) |
|--------|----------|-------------------------|
| `draft` | `experimental` | Early design |
| `active` | `experimental` | Usable; expect change |
| `active` | `stable` | Default “mature” signal |
| `deprecated` | *(omit)* | Prefer successor / reason in `deprecation` |

---

## 5. Deprecation object

Applicable **only** when `status: deprecated`.

| Field | Required? | Description |
|-------|-----------|-------------|
| `reason` | Recommended | Short deprecation rationale. |
| `successor` | Optional | Successor Module `id`, if any. |
| `sunset` | Optional | Planned removal or end-of-support date as ISO date `YYYY-MM-DD`. |

Do not use `deprecation` when status is `draft` or `active`.

**Metadata versus README (deprecation):**

- The metadata `deprecation` block holds **structured** deprecation information (`reason`, optional `successor`, optional `sunset`).
- The Module `README.md` holds **human-readable** migration guidance.
- These are separate artifacts; one does not replace the other.

**Lifecycle / validation requirement:** when `status` is `deprecated`, the Module `README.md` **must** include a section with the **exact** Markdown heading:

```markdown
## Migration
```

That section must cover why the Module is deprecated, successor where applicable, migration steps, and assumptions consumers must not make. See [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md) §5 and [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md). Deprecation never silently rewrites consumer-owned artifacts.

---

## 6. Core compatibility (`requires_core`)

- Optional.
- SemVer-based **minimum** version string.
- Example: `requires_core: "1.0.0"`
- Meaning: minimum supported AIOS Core/Framework version (informational).
- Do **not** encode tested ranges or resolver algorithms in metadata v1.
- Detailed compatibility notes belong in `README.md`.

---

## 7. Naming and format conventions

| Topic | Rule |
|-------|------|
| Module `id` | Lowercase English `kebab-case`; stable; Pack-independent |
| `version` | SemVer `MAJOR.MINOR.PATCH` (+ valid pre-release if needed) |
| YAML | UTF-8; prefer 2-space indent; quote strings when needed |
| Lists | YAML sequences of short strings |
| Unknown fields | Future validation should initially **warn**, not immediately reject. No validator is implemented by this document. |

---

## 8. Governance relationship

Unchanged by this specification:

- Module guidance = **L6** by default.
- Explicit consumer adoption into local policy = **L3**.
- Pack guidance = **L5** when explicitly adopted.
- Consumer ownership of product decisions and artifacts.
- Core / Module / Pack boundaries per Framework Contract §5.
- L0–L7 precedence per Framework Contract §7.
- Adaptive recommendation architecture remains **design only** (not an implemented engine).

Metadata does not change governance precedence.

---

## 9. Illustrative example

The following is an **example only**. It is **not** an implemented schema file, **not** a shipped Module, and **not** evidence that any Module exists in the repository.

```yaml
# ILLUSTRATIVE EXAMPLE ONLY — not an implemented module.yaml
id: architecture-engineering
version: 0.1.0
title: Architecture Engineering
summary: >
  Guidance for structuring and reviewing software architecture decisions
  without imposing a single product architecture on consumers.

status: draft
maturity: experimental

applies_when:
  - Non-trivial system boundaries or integration points exist
  - Architecture decisions need durable consumer ADRs
avoid_when:
  - Tiny single-file scripts with no lasting architecture
  - The consumer forbids external architecture frameworks by policy

tags:
  - architecture
  - design
provides:
  - architecture-review-guidance
  - adr-oriented-decision-support

requires_core: "1.0.0"

# Example deprecation shape (only if status were deprecated):
# deprecation:
#   reason: "Superseded by a revised architecture guidance Module"
#   successor: architecture-engineering
#   sunset: "2027-12-31"
```

---

## 10. Completed Phase 2 decisions versus deferred work

**Completed (do not restate as open):**

- Phase 2.4 dependency and compatibility **design** — completed. Metadata v1 has no dependency fields; `dependencies` is forbidden. Conceptual constraints (for example no Module→Pack dependency; Pack composition ≠ Module dependency; no resolver/installer) remain binding as documented in the Framework Contract and Module Validation expectations.
- Phase 2.6 conceptual Reference Module design — completed (illustrative only; no Module package shipped by this specification).
- Phase 2.7 Module validation **strategy** — completed in [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md).

**Deferred future work (distinct from the completed design above):**

- Machine-readable Module-to-Module relationship metadata and any approved additive metadata extension that would encode relationship graphs (until a concrete use case justifies it)
- Validation **tooling**, schemas, CLI validate commands, and Module CI (future implementation — not Phase 2.7 design)
- Module catalog population (Phase 7)
- Adaptive engine implementation (separate future approval)

Lifecycle governance beyond the field enums is defined in [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md) and is not deferred here.

---

## Document maintenance

Changes to the approved field model, enums, or naming rules require Product Owner awareness and an update to this file. Keep the Framework Contract and [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md) references synchronized when authority relationships change.

End of Module Metadata Specification v1.1.0.
