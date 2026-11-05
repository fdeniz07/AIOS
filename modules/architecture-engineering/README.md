# Architecture Engineering

| Field | Value |
|-------|-------|
| Module id | `architecture-engineering` |
| Package version | `0.1.0` |
| Status | `draft` |
| Maturity | `experimental` |

This document is the human and agent entry point for the **Architecture Engineering** Module. Machine-readable identity and short discovery fields live in [`module.yaml`](module.yaml). Do not treat metadata as adoption or installation.

**Authority:** Module guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** constraints. Instruction precedence remains [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) §7 / [`../../AGENTS.md`](../../AGENTS.md) §2. AI recommends; humans decide. Durable architectural and product decisions belong to the Consumer.

---

## Purpose

Provide reusable, stack-agnostic guidance for **understanding**, **reviewing**, and **supporting** durable software architecture decisions — without imposing a single product architecture on consumers.

---

## Scope

In scope for this Module’s guidance surface:

- Architectural understanding before significant change
- Boundary and structure review support
- Fit of a proposed change to existing architecture
- Support for recording durable decisions as Consumer-owned ADRs (this Module does not own ADR content)

Out of scope:

- Owning or silently rewriting Consumer product architecture or ADRs
- Implementation authority, coding standards catalogs, or feature delivery orchestration
- Testing strategy, security certification, CI/CD installation, or release publication authority
- Framework Governance, L0–L7 precedence, or human approval gates (Core-owned)
- Education or Pack-specific curricula
- Automatic Module installation, adoption, or consumer repository modification

---

## When to use

- Non-trivial system boundaries, integration points, or layers exist
- A change may affect architecture, public contracts, module boundaries, data compatibility, or top-level conventions
- Architecture decisions may need durable Consumer ADRs
- Architectural understanding is incomplete and an architecture-focused assessment is requested

---

## When not to use

- Tiny single-file scripts with no lasting architecture
- Narrow edits with adequate local context and no architecture assessment requested
- The Consumer forbids external architecture frameworks by policy
- The real need is implementation, testing, security testing, DevOps, data engineering, or release operations rather than architecture guidance
- Anyone expects this Module to mandate one product architecture

---

## Draft disclosure

This Module is **`draft`** with maturity **`experimental`**.

- The package remains **`draft`** / **`experimental`** and incomplete relative to a full Architecture Engineering guidance surface.
- Included so far: `module.yaml`, this `README.md`, and one Module-local Skill (`architecture-boundary-review`, artifact lifecycle `draft`).
- Checklists, Knowledge, Prompts, Workflows, templates, examples, and tests are **not** included in this version.
- Not generally recommended for new durable Consumer adoption until the guidance surface is more complete.
- Evaluate only with this incomplete state disclosed. The Skill’s `draft` status does **not** mean the Module is adopted, installed, stable, or mandatory.

---

## Core references

Link only — do not copy Core methodology into this Module.

| Resource | Role |
|----------|------|
| [`../../methodology/architecture_first.md`](../../methodology/architecture_first.md) | Architecture-first methodology |
| [`../../methodology/rdiv.md`](../../methodology/rdiv.md) | Review → Decide → Implement → Verify |
| [`../../methodology/repository_onboarding.md`](../../methodology/repository_onboarding.md) | Starting work on an existing repository |
| [`../../methodology/ai_collaboration.md`](../../methodology/ai_collaboration.md) | Human authority with AI assistance |
| [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) | Core repository analysis Skill (**remains Core-owned**; not migrated here) |
| [`../../workflows/feature_development.md`](../../workflows/feature_development.md) | Core Feature Development Workflow (see discovery and Architecture and Design stages) |
| [`../../checklists/review.md`](../../checklists/review.md) | Core change review checklist (general; not architecture-specific) |
| [`../../prompts/review/architecture_review.md`](../../prompts/review/architecture_review.md) | Existing Core interaction prompt (not Module-local; not a Skill) |
| [`../../AGENTS.md`](../../AGENTS.md) | Agent operating manual (precedence and approval gates) |
| [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) | Framework Contract (§5 Modules, §7 precedence) |

`requires_core: "1.0.1"` in metadata is an **informational** minimum aligned with the repository root [`../../VERSION`](../../VERSION) value at authoring time (`1.0.1`). It is not a resolver, installer pin, or runtime dependency.

---

## Module capabilities

Only capabilities that exist in this package are listed. Absence of other capability types is intentional in this draft.

### Skills

| id | Title | Status | Definition |
|----|-------|--------|------------|
| `architecture-boundary-review` | Architecture Boundary Review | `draft` | [`skills/architecture_boundary_review.md`](skills/architecture_boundary_review.md) |

**Architecture Boundary Review** — evidence-based review of architectural boundaries, responsibilities, dependency direction, coupling, and structural consistency, including impact assessment for proposed structural changes. It does not impose a product architecture, does not replace Core repository analysis, and does not authorize implementation or Consumer ADR changes.

- Skill guidance remains **L6** by default unless a Consumer explicitly adopts relevant Module guidance as local policy (**L3**).
- Skill `draft` ≠ Module adoption, installation, enablement, or stability guarantee.

### Not included in this version

Checklists, Knowledge, Prompts, Workflows, templates, examples, and tests.

### Core procedures (not Module-local)

For general repository discovery and onboarding-style assessment, continue to use Core [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) (`repository-analysis`) — **Core-owned**, not migrated here. Other Core references remain in the section above.

---

## Related Modules

Companion relationships are documentation-only. Metadata v1 has no Module-to-Module `dependencies` field. Presence of a companion package does **not** install, adopt, or enable either Module.

| Module | Responsibility |
|--------|----------------|
| **This Module** | Boundaries, structural fit, and architecture decision **support** (Consumer still owns ADRs) |
| [`../development-engineering/`](../development-engineering/) | Implementation discipline within an **already agreed** scope |
| [`../testing-quality-engineering/`](../testing-quality-engineering/) | Risk-proportionate testing strategy and validation evidence (complementary; docs-only) |

This Module retains ownership of architecture boundaries and structural design concerns. Companion Modules do not take over that scope.

Do not assume Development Engineering or Testing & Quality Engineering is installed or adopted because this package references them. When implementation-scope or change-hygiene questions dominate and architecture boundaries are already clear, prefer Development Engineering. When validation strategy or evidence-honesty questions dominate, prefer Testing & Quality Engineering. Other Engineering domains may be referenced here when those packages exist — without implying hard dependencies.

---

## Relationship to `repository_analysis` (Core)

The Core Skill [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) (`id`: `repository-analysis`) remains **Core-owned**.

This Module:

- May recommend using that Skill when repository evidence is needed before architectural judgment
- Does **not** replace, fork, or migrate that Skill into this package

---

## Adoption notes

- Presence under `modules/` does **not** adopt, install, enable, or sync this Module into a Consumer repository.
- `aiosctl sync` does not install Modules.
- Explicit Consumer adoption into local policy is Consumer-owned (**L3** within adoption scope) and must not be assumed or performed silently.
- Filled ADRs and architecture decisions remain Consumer-owned (**L2**).

---

## Maintenance

- Maintained by AIOS maintainers as part of the Engineering Module Catalog.
- Package version (`module.yaml` `version`) is independent of the AIOS Framework `VERSION` and of Consumer sync markers.
- Role-based contact: see repository [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).
