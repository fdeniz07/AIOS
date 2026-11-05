# Development Engineering

| Field | Value |
|-------|-------|
| Module id | `development-engineering` |
| Package version | `0.1.0` |
| Status | `draft` |
| Maturity | `experimental` |

This document is the human and agent entry point for the **Development Engineering** Module. Machine-readable identity and short discovery fields live in [`module.yaml`](module.yaml). Do not treat metadata as adoption or installation.

**Authority:** Module guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** constraints. Instruction precedence remains [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) §7 / [`../../AGENTS.md`](../../AGENTS.md) §2. AI recommends; humans decide. Durable architectural and product decisions belong to the Consumer.

---

## Purpose

Provide optional, stack-agnostic engineering guidance for **disciplined implementation** within an **already agreed scope** — without replacing Core workflows, imposing a coding-standard catalog, or redesigning Consumer architecture.

---

## Scope

In scope for this Module’s guidance surface:

- Implementation discipline
- Change scope and change hygiene
- Maintainability-oriented implementation practices
- Implementation-focused review guidance

### Explicit boundaries

| Concern | Owner |
|---------|--------|
| Feature Development Workflow | **Core** — [`../../workflows/feature_development.md`](../../workflows/feature_development.md) |
| RDIV methodology | **Core** — [`../../methodology/rdiv.md`](../../methodology/rdiv.md) |
| AI Collaboration methodology | **Core** — [`../../methodology/ai_collaboration.md`](../../methodology/ai_collaboration.md) |
| Framework Governance and AGENTS.md §8 | **Core** |
| Architecture-boundary guidance | **Architecture Engineering** — [`../architecture-engineering/`](../architecture-engineering/) |
| Product architecture, ADRs, coding standards | **Consumer** (**L2** / local policy) |
| Testing strategy | Not this Module — [`../testing-quality-engineering/`](../testing-quality-engineering/) (Testing & Quality Engineering) |
| Security Engineering | Not this Module — Security Engineering does not provide certification, penetration-testing, or formal audit authority |
| Release Workflow | **Core** — [`../../workflows/release.md`](../../workflows/release.md) |

Out of scope:

- Copying or relocating Core Feature Development / Release Workflows into this package
- Owning or rewriting Consumer ADRs or product architecture
- Mandating a single coding style, language, or framework
- Automatic Module installation, adoption, or consumer repository modification

---

## When to use

- Scoped code or behavior changes are being planned or implemented
- Diff fidelity to an agreed plan/scope needs reinforcement
- Opportunistic refactors or drive-by edits are a material risk
- Implementation-focused review support is requested (without replacing Core review)

---

## When not to use

- The primary need is architecture boundary or structural-fit assessment — use Architecture Engineering / Core analysis
- The work is release, publish, tag, or deploy oriented — use Core Release Workflow
- Documentation-only typos with no implementation surface
- The Consumer forbids external development guidance by policy
- Anyone expects this Module to replace Feature Development Workflow or to authorize commits

---

## Draft disclosure

This Module is **`draft`** with maturity **`experimental`**.

- The package remains **`draft`** / **`experimental`** and incomplete relative to a full Development Engineering guidance surface.
- Included so far: `module.yaml`, this `README.md`, and one Module-local Skill (`implementation-change-hygiene`, artifact lifecycle `draft`).
- Checklists, Knowledge, Prompts, Workflows, templates, examples, and tests are **not** included in this version.
- Not generally recommended for new durable Consumer adoption until the guidance surface is more complete.
- Evaluate only with this incomplete state disclosed. The Skill’s `draft` status does **not** mean the Module is adopted, installed, enabled, stable, active, or mandatory. Module presence does **not** automatically adopt or activate its guidance.

---

## Core references

Link only — do not copy Core methodology or Workflow bodies into this Module.

| Resource | Role |
|----------|------|
| [`../../workflows/feature_development.md`](../../workflows/feature_development.md) | Core Feature Development Workflow (orchestration remains Core; especially implementation planning and implementation stages) |
| [`../../methodology/rdiv.md`](../../methodology/rdiv.md) | Review → Decide → Implement → Verify |
| [`../../methodology/ai_collaboration.md`](../../methodology/ai_collaboration.md) | AI assists; humans decide |
| [`../../methodology/architecture_first.md`](../../methodology/architecture_first.md) | Understand structure before changing it |
| [`../../checklists/review.md`](../../checklists/review.md) | Core general change review checklist |
| [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) | Core repository analysis (not an implementation Skill) |
| [`../../AGENTS.md`](../../AGENTS.md) | Agent operating manual (precedence and approval gates) |
| [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) | Framework Contract (§5 Modules, §7 precedence) |

`requires_core: "1.0.1"` in metadata is an **informational** minimum aligned with the repository root [`../../VERSION`](../../VERSION) value at authoring time (`1.0.1`). It is not a resolver, installer pin, or runtime dependency.

---

## Module capabilities

Only capabilities that exist in this package are listed. Absence of other capability types is intentional in this draft.

### Skills

| id | Title | Status | Definition |
|----|-------|--------|------------|
| `implementation-change-hygiene` | Implementation Change Hygiene | `draft` | [`skills/implementation_change_hygiene.md`](skills/implementation_change_hygiene.md) |

**Implementation Change Hygiene** — evidence-based review of implementation **scope fidelity**, **change hygiene**, and **plan-to-diff consistency**. It is analytical and advisory: it does not replace the Core Feature Development Workflow, does not replace the Core Review Checklist, does not impose coding standards, and does not authorize repository modifications, commits, or releases.

- Skill guidance remains **L6** by default unless a Consumer explicitly adopts relevant Module guidance as local policy (**L3**).
- Skill `draft` ≠ Module adoption, installation, enablement, or stability guarantee.
- Consumer-owned ADRs, architecture, and product decisions remain **L2** / Consumer-owned.

### Not included in this version

Checklists, Knowledge, Prompts, Workflows, templates, examples, and tests.

### Core procedures (not Module-local)

For delivery orchestration, continue to use Core [`../../workflows/feature_development.md`](../../workflows/feature_development.md). For general change review gates, continue to use Core [`../../checklists/review.md`](../../checklists/review.md). Other Core references remain in the section above.

---

## Relationship to Architecture Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../architecture-engineering/`](../architecture-engineering/) | Boundaries, structural fit, and architecture decision **support** (Consumer still owns ADRs) |
| **This Module** | Implementation discipline within an **already agreed** scope |

This Module must **not** redesign architecture under the guise of implementation. When boundary or structural-fit questions dominate, prefer Architecture Engineering (and Core repository analysis when discovery is incomplete).

Do not assume Architecture Engineering is installed or adopted because this package references it.

---

## Related Modules

Companion relationships are **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field. Presence of a companion package does **not** install, adopt, or enable either Module.

- [`architecture-engineering`](../architecture-engineering/) — companion for architecture-boundary guidance (docs-only; not a hard dependency). This Module retains ownership of implementation discipline and change hygiene.
- [`testing-quality-engineering`](../testing-quality-engineering/) — complementary companion for risk-proportionate testing strategy and validation evidence (docs-only; not a hard dependency). This Module does **not** own testing strategy or validation methodology.
- [`devops-cloud-engineering`](../devops-cloud-engineering/) — companion for delivery-pipeline, infrastructure, and operational domain practices (docs-only; not a hard dependency). This Module does **not** own reusable delivery/ops guidance and does **not** replace Core Feature Development Workflow; DevOps & Cloud does **not** replace implementation-change-hygiene.

Do not assume companion Modules are installed or adopted because this package references them. Other Engineering domains are not listed here until packages exist.

---

## Adoption notes

- Presence under `modules/` does **not** adopt, install, enable, or sync this Module into a Consumer repository.
- `aiosctl sync` does not install Modules.
- Explicit Consumer adoption into local policy is Consumer-owned (**L3** within adoption scope) and must not be assumed or performed silently.
- Consumer-owned ADRs, coding standards, and architecture decisions remain Consumer-owned (**L2** / local process).

---

## Maintenance

- Maintained by AIOS maintainers as part of the Engineering Module Catalog.
- Package version (`module.yaml` `version`) is independent of the AIOS Framework `VERSION` and of Consumer sync markers.
- Role-based contact: see repository [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).
