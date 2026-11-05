# Testing & Quality Engineering

| Field | Value |
|-------|-------|
| Module id | `testing-quality-engineering` |
| Package version | `0.1.0` |
| Status | `draft` |
| Maturity | `experimental` |

This document is the human and agent entry point for the **Testing & Quality Engineering** Module. Machine-readable identity and short discovery fields live in [`module.yaml`](module.yaml). Do not treat metadata as adoption or installation.

**Authority:** Module guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs or Consumer testing policies (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** constraints. Instruction precedence remains [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) §7 / [`../../AGENTS.md`](../../AGENTS.md) §2. AI recommends; humans decide. Durable product, architecture, and testing-policy decisions belong to the Consumer.

---

## Purpose

Provide optional, stack-agnostic guidance for **risk-proportionate testing and quality engineering** so Consumers can judge:

1. **What should be tested?** — given change scope, risk, and critical paths
2. **How much validation is appropriate?** — proportionate depth without mandating tools or thresholds
3. **What evidence supports validation claims?** — honest distinction between checks that were run and those that were not

This Module **enriches** Core Feature Development **Stage 7 (Testing and Validation)** with reusable domain guidance. It does **not** replace that Workflow stage, the Core Review Checklist, RDIV Verify, or any Core release validation path.

---

## Scope

In scope for this Module’s guidance surface:

- Test strategy and planning
- Risk- and change-based test selection
- Conceptual test-level selection (unit, integration, end-to-end)
- Regression test selection heuristics
- Testability and critical-path considerations (without taking over architecture review)
- Test coverage limitations and metric honesty
- Validation evidence and unrun-check disclosure
- Lightweight defect analysis and reporting structure
- Conceptual CI testing considerations (what validation means in CI — not pipeline ownership)

### Explicit boundaries

| Concern | Owner |
|---------|--------|
| Feature Development Workflow (including Stage 7 orchestration) | **Core** — [`../../workflows/feature_development.md`](../../workflows/feature_development.md) |
| Review Checklist | **Core** — [`../../checklists/review.md`](../../checklists/review.md) |
| Release Workflow and Release Checklist | **Core** — [`../../workflows/release.md`](../../workflows/release.md), [`../../checklists/release_checklist.md`](../../checklists/release_checklist.md) |
| RDIV Verify | **Core** — [`../../methodology/rdiv.md`](../../methodology/rdiv.md) |
| Repository analysis (including test/CI inventory) | **Core** — [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) |
| Framework Governance and AGENTS.md §8 | **Core** |
| Architecture-boundary guidance | **Architecture Engineering** — [`../architecture-engineering/`](../architecture-engineering/) |
| Implementation discipline and change hygiene | **Development Engineering** — [`../development-engineering/`](../development-engineering/) |
| Testing policies, coverage thresholds, mandatory tools | **Consumer** (**L2** / local policy) |
| Security certification / penetration testing | Not this Module — Security Engineering does not provide certification, penetration-testing, or formal audit authority |
| CI/CD pipeline structure and delivery/operational guidance | Not this Module — see [DevOps & Cloud Engineering](../devops-cloud-engineering/) (does not grant platform setup, deployment execution, or tool-selection authority) |

Out of scope:

- Replacing or relocating Core Feature Development Stage 7, Review Checklist, Release Workflow/Checklist, or RDIV Verify
- Migrating or forking Core `repository_analysis`
- Owning or rewriting Consumer ADRs, product decisions, or testing policies
- Mandating a language, test framework, coverage percentage, or CI vendor
- Security certification, penetration testing, or security approval authority
- Automatic test execution, test runners, coverage engines, or Consumer repository modification
- Education Pack content (for example root `QUALITY_CONTROL.md`)
- Module package validation ([`MODULE_VALIDATION.md`](../../docs/MODULE_VALIDATION.md)) and framework self-tests under `tests/`

---

## When to use

- A scoped change needs risk-proportionate test planning or validation depth advice
- Validation claims need honest evidence versus unrun checks
- Regression or critical-path selection guidance is requested
- Support is needed alongside Feature Development Stage 7 without replacing the Workflow

---

## When not to use

- The primary need is architecture boundary or structural-fit assessment — use Architecture Engineering / Core repository analysis
- The primary need is implementation scope fidelity or change hygiene — use Development Engineering
- The work is release publish, tag, or deploy platform setup — use Core Release Workflow / [`devops-cloud-engineering`](../devops-cloud-engineering/) for delivery and operational engineering guidance (this Module does **not** own pipeline structure, environment promotion, or operational readiness)
- Documentation-only typos with no behavior or validation surface
- The Consumer forbids external testing guidance by policy
- Anyone expects this Module to run tests, set coverage gates, or authorize commits

---

## Draft disclosure

This Module is **`draft`** with maturity **`experimental`**.

- The package remains **`draft`** / **`experimental`** and incomplete relative to a full Testing & Quality Engineering guidance surface.
- Included so far: `module.yaml` and this `README.md` only.
- Skills, Checklists, Knowledge, Prompts, Workflows, templates, examples, and tests are **not** included in this version.
- Not generally recommended for new durable Consumer adoption until the guidance surface is more complete.
- Evaluate only with this incomplete state disclosed. Module presence does **not** automatically adopt, install, enable, activate, or mandate this guidance.

---

## Core references

Link only — do not copy Core methodology, Workflow, or Checklist bodies into this Module.

| Resource | Role |
|----------|------|
| [`../../workflows/feature_development.md`](../../workflows/feature_development.md) | Core Feature Development Workflow — Stage 7 Testing and Validation remains Core orchestration; this Module enriches it |
| [`../../checklists/review.md`](../../checklists/review.md) | Core change review checklist (validation considered; unrun ≠ passed) |
| [`../../workflows/release.md`](../../workflows/release.md) | Core Release Workflow (release validation / post-release verification) |
| [`../../checklists/release_checklist.md`](../../checklists/release_checklist.md) | Core Release Checklist |
| [`../../methodology/rdiv.md`](../../methodology/rdiv.md) | Review → Decide → Implement → Verify |
| [`../../methodology/ai_collaboration.md`](../../methodology/ai_collaboration.md) | AI assists; humans decide |
| [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) | Core repository analysis (test/CI inventory remains Core-owned) |
| [`../../AGENTS.md`](../../AGENTS.md) | Agent operating manual (precedence and approval gates) |
| [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) | Framework Contract (§5 Modules, §7 precedence) |

`requires_core: "1.0.1"` in metadata is an **informational** minimum aligned with the repository root [`../../VERSION`](../../VERSION) value at authoring time (`1.0.1`). It is not a resolver, installer pin, or runtime dependency.

---

## Module capabilities

Only capabilities that exist in this package are listed. Absence of other capability types is intentional in this draft.

### Skills

No Module-local Skills are included in this version.

### Not included in this version

Skills, Checklists, Knowledge, Prompts, Workflows, templates, examples, and tests.

### Core procedures (not Module-local)

For delivery orchestration and Stage 7, continue to use Core [`../../workflows/feature_development.md`](../../workflows/feature_development.md). For general change review gates, continue to use Core [`../../checklists/review.md`](../../checklists/review.md). For repository test/CI inventory, continue to use Core [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md). Other Core references remain in the section above.

---

## Relationship to Architecture Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../architecture-engineering/`](../architecture-engineering/) | Boundaries, structural fit, and architecture decision **support** (Consumer still owns ADRs) |
| **This Module** | Risk-proportionate validation strategy and evidence honesty |

This Module may consider **testability** and critical-path exposure. It must **not** take over architecture boundary review. When structural-fit questions dominate, prefer Architecture Engineering (and Core repository analysis when discovery is incomplete).

Do not assume Architecture Engineering is installed or adopted because this package references it.

---

## Relationship to Development Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../development-engineering/`](../development-engineering/) | Implementation discipline, scope fidelity, and change hygiene within an **already agreed** scope |
| **This Module** | What to validate, how much validation is proportionate, and what evidence supports claims |

This Module does **not** perform plan-to-diff or change-hygiene review. When implementation-scope questions dominate, prefer Development Engineering.

Do not assume Development Engineering is installed or adopted because this package references it.

---

## Related Modules

- [`architecture-engineering`](../architecture-engineering/) — companion for architecture-boundary guidance (docs-only; not a hard dependency)
- [`development-engineering`](../development-engineering/) — companion for implementation change hygiene (docs-only; not a hard dependency)
- [`devops-cloud-engineering`](../devops-cloud-engineering/) — companion for CI/CD pipeline structure, environment promotion, and operational readiness (docs-only; not a hard dependency). This Module retains ownership of risk-proportionate test strategy and validation evidence honesty; DevOps & Cloud does **not** own test strategy, test execution policy, coverage interpretation, or Feature Development Stage 7.

Other Engineering domains are not listed here until packages exist.

---

## Adoption notes

- Presence under `modules/` does **not** adopt, install, enable, or sync this Module into a Consumer repository.
- `aiosctl sync` does not install Modules.
- Explicit Consumer adoption into local policy is Consumer-owned (**L3** within adoption scope) and must not be assumed or performed silently.
- Consumer-owned ADRs, testing policies, thresholds, tool mandates, and architecture decisions remain Consumer-owned (**L2** / local process).

---

## Maintenance

- Maintained by AIOS maintainers as part of the Engineering Module Catalog.
- Package version (`module.yaml` `version`) is independent of the AIOS Framework `VERSION` and of Consumer sync markers.
- Role-based contact: see repository [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).
