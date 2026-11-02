# AIOS Module Lifecycle & Governance

Version: 1.0.0

Status: Approved

Last Updated: 2026-11-02

Document type: Module lifecycle governance

This document defines **lifecycle and governance rules** for AIOS Modules.

Related authorities:

- Architecture and boundaries: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5
- Instruction precedence (L0–L7): [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7
- Module metadata field model: [`MODULE_METADATA.md`](MODULE_METADATA.md)
- Agent operationalization: [`../AGENTS.md`](../AGENTS.md) §2

This document does **not**:

- Create or populate Modules
- Implement lifecycle automation, validators, or CLI commands
- Change L0–L7 precedence
- Imply adoption or installation of a Module by a consumer
- Add fields to metadata v1

---

## 1. Lifecycle status

Exactly **three** lifecycle states exist. Do not introduce `archived`, `proposed`, `retired`, or other additional states without a separate Product Owner decision.

Conceptual flow (not software-enforced):

```text
draft → active → deprecated
```

Transitions are human/process decisions. No autonomous lifecycle engine is implied or authorized.

### 1.1 `draft`

- Work in progress.
- May be incomplete.
- **Not generally recommended** for new durable consumer adoption.
- May be evaluated or used only with **explicit disclosure** of its incomplete state.

### 1.2 `active`

- Maintained and available for consumer **evaluation**.
- Must provide a usable entry point through `README.md` and required metadata (`id`, `version`, `title`, `summary`, `status`).
- May carry optional maturity `experimental` or `stable`.
- **Active does not mean adopted or installed.**

### 1.3 `deprecated`

- No longer recommended for **new** adoption.
- Must include a README section with the **exact** Markdown heading `## Migration` (see §5).
- Must preserve existing consumer ownership of ADRs, local policies, and implementation.
- Does **not** trigger automatic consumer changes, Module deletion, or successor installation.

---

## 2. Draft versus active expectations

| Topic | Draft | Active |
|-------|-------|--------|
| Completeness | May be incomplete | Usable entry point required |
| Durable new adoption | Not generally recommended | Allowed as L6 recommendation; consumer may adopt to L3 |
| Disclosure | Incomplete state must be clear | Scope and applicability should be clear |
| Catalog posture | In progress / design | Available for discovery |
| Adoption implication | None | None — still not installed by metadata |

---

## 3. Maturity (optional)

Allowed values (metadata v1):

- `experimental`
- `stable`

Maturity is **independent** of lifecycle `status`.

When `status` is `deprecated`, maturity should normally be **omitted**.

### 3.1 Experimental expectations

| Area | Expectation |
|------|-------------|
| Documentation | Purpose clear; gaps allowed if disclosed |
| Scope clarity | May still sharpen |
| Applicability | `applies_when` / `avoid_when` strongly recommended |
| Validation | Manual / light; no warranty |
| Compatibility claims | Cautious; honest `requires_core` if present |
| Change risk | Higher; more frequent SemVer bumps expected |
| Maintenance | Evolving / best-effort |

### 3.2 Stable expectations

| Area | Expectation |
|------|-------------|
| Documentation | Purpose, scope, and adoption notes reasonably complete |
| Scope clarity | Boundaries and non-goals clear |
| Applicability | `applies_when` / `avoid_when` expected |
| Validation | Manual and, when available later, tooling — still not a warranty |
| Compatibility claims | Honest minimum Core claim; tested notes in README |
| Change risk | Prefer SemVer discipline; avoid surprise breaks |
| Maintenance | Intended ongoing care while `status` remains `active` |

### 3.3 What “stable” does **not** guarantee

- Permanent compatibility
- SLA or mandatory support commitment
- Automatic adoption or installation
- Freedom from future breaking changes (breaking changes use MAJOR)

---

## 4. Guidance-oriented SemVer policy

Module `version` follows SemVer (`MAJOR.MINOR.PATCH`, including valid pre-releases).

This policy applies to **guidance-based Modules**, not only software APIs.

| Bump | Meaning for Modules |
|------|---------------------|
| **MAJOR** | Breaking change to adopted engineering guidance or Module contract; removed or reversed recommendations that invalidate prior consumer adoption; incompatible required structures; Module identity (`id`) changes |
| **MINOR** | Backward-compatible new guidance; new sections or optional capabilities |
| **PATCH** | Corrections, clarifications, non-breaking examples, typo fixes |

### Version independence

| Version kind | Meaning |
|--------------|---------|
| **Module version** | Version of the Module package / guidance surface (`module.yaml` `version`) |
| **AIOS Framework version** | Core / framework distribution version |
| **Consumer integration version** | Consumer record of what was integrated (for example sync metadata today) |

Do not conflate these three (see Framework Contract §10).

---

## 5. Deprecation and migration governance

When `status` is `deprecated`:

### 5.1 Metadata (`deprecation` object)

Per [`MODULE_METADATA.md`](MODULE_METADATA.md):

- `reason` — recommended
- `successor` — optional Module `id` when a successor exists
- `sunset` — optional ISO date `YYYY-MM-DD`

### 5.2 README migration section (mandatory)

Deprecated Modules **must** include a README section whose heading is exactly:

```markdown
## Migration
```

That section must describe:

- Why the Module is deprecated
- Whether a successor exists (and which Module `id`, if applicable)
- Recommended migration steps
- What existing consumers should **not** assume

This heading convention is aligned with [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md). A deprecated Module without the exact `## Migration` heading is invalid for validation purposes.

The structured metadata `deprecation` object (see [`MODULE_METADATA.md`](MODULE_METADATA.md)) is separate from this human-readable README section.

### 5.3 What deprecation does **not** do

Deprecation does **not**:

- Delete the Module automatically
- Rewrite consumer ADRs
- Rewrite consumer local policies
- Modify consumer code
- Automatically install a successor

Any consumer-side migration requires **consumer-owner approval**. AIOS and agents may disclose deprecation and propose changes; they must not silently apply them.

Prefer deprecate-before-remove. Physical removal of Module content requires separate Product Owner approval and migration planning (Framework Contract §12 principles).

---

## 6. Ownership and maintenance

- Do **not** add owner or maintainer fields to metadata v1.
- Do **not** require personal email addresses or individual identities in Module contracts.
- When actual Modules are created, a README **Maintenance** section is **recommended**.
- Prefer **role-based** ownership descriptions (for example “AIOS maintainers”, project team alias, or pointer to `CONTRIBUTING.md`).
- No SLA or mandatory support commitment is implied by `active` or `stable`.

---

## 7. Relationship with L0–L7 governance

Lifecycle and maturity signals do **not** change instruction precedence.

| Level | Unchanged rule |
|-------|----------------|
| L0 | Non-overridable constraints |
| L1 | Explicit user instructions (with durable-decision safeguards) |
| L2 | Consumer-approved ADRs and product decisions |
| L3 | Consumer local policies (including explicitly adopted Module guidance) |
| L4 | AIOS Core binding operating/governance defaults |
| L5 | Explicitly adopted Pack guidance |
| L6 | Module and methodology recommendations **by default** |
| L7 | External knowledge |

- Module guidance remains **L6** regardless of `draft` / `active` / `deprecated` (deprecation affects **recommendation posture**, not a new precedence level).
- Explicit consumer adoption into local policy remains **L3**.
- Metadata never implies adoption or installation.
- Deprecated Modules must not be used as a pretext to silently alter consumer-owned artifacts.

---

## 8. Explicit non-goals

- Lifecycle automation or state machines in tooling (unless separately approved later)
- Additional lifecycle states beyond the three approved values
- Owner/maintainer fields in metadata v1
- Guaranteed compatibility, SLA, or automatic adoption via `stable`
- Autonomous migration of consumer repositories
- Package-manager install/uninstall of Modules via `aiosctl sync`
- Equating Framework version bumps with Module version bumps

---

## Document maintenance

Changes to lifecycle states, maturity expectations, SemVer policy, or deprecation/migration rules require Product Owner awareness and an update to this file. Keep cross-references from the Framework Contract and Module Metadata specification synchronized.

End of Module Lifecycle & Governance v1.0.0.
