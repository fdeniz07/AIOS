# Security Engineering

| Field | Value |
|-------|-------|
| Module id | `security-engineering` |
| Package version | `0.1.0` |
| Status | `draft` |
| Maturity | `experimental` |

This document is the human and agent entry point for the **Security Engineering** Module. Machine-readable identity and short discovery fields live in [`module.yaml`](module.yaml). Do not treat metadata as adoption or installation.

**Authority:** Module guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs or Consumer security policies (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** security and privacy constraints. Instruction precedence remains [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) §7 / [`../../AGENTS.md`](../../AGENTS.md) §2. AI recommends; humans decide. Durable product, architecture, and security-policy decisions—and risk acceptance—belong to the Consumer.

---

## Purpose

Provide optional, stack-agnostic guidance for **change-scoped security engineering** so Consumers can judge:

1. **Which threat / abuse and trust-boundary concerns are relevant to this change?**
2. **What secrets, dependency, and supply-chain hygiene risks appear in evidence?**
3. **What is observed versus inferred** — without claiming vulnerability, certification, or risk acceptance?

This Module **enriches** Core Review and Release security checkpoints and repository-analysis security review areas with reusable domain guidance. It does **not** replace **L0** constraints, Framework Governance, Core checklists, or Core repository analysis.

---

## Scope

In scope for this Module’s guidance surface:

- Threat and abuse-case thinking (change-scoped; no full threat-model mandate)
- Trust-boundary awareness (complementary to Architecture; no boundary ownership)
- Secrets hygiene (no secret exposure; no unauthorized secret-store access)
- Dependency and supply-chain awareness (heuristic labeling; not vulnerability guarantee)
- Security impact of implementation changes (diff/scope-oriented)
- Evidence-based security observations (Fact / Inference / Recommendation; no false vulnerability claims)

### Explicit boundaries

| Concern | Owner |
|---------|--------|
| L0 security, privacy, compliance, and related non-overridable constraints | **Core** — [`../../AGENTS.md`](../../AGENTS.md), [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) §7 |
| Framework Governance and AGENTS.md §8 | **Core** |
| Review Checklist (including secrets / L0 gates) | **Core** — [`../../checklists/review.md`](../../checklists/review.md) |
| Release Workflow and Release Checklist (including security & dependency review items) | **Core** — [`../../workflows/release.md`](../../workflows/release.md), [`../../checklists/release_checklist.md`](../../checklists/release_checklist.md) |
| Repository analysis (including security review areas) | **Core** — [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) |
| AIOS repository vulnerability-reporting policy | Root [`../../SECURITY.md`](../../SECURITY.md) — **not** this Module’s content |
| Architecture-boundary guidance and structural trust design | **Architecture Engineering** — [`../architecture-engineering/`](../architecture-engineering/) |
| Implementation discipline and change hygiene | **Development Engineering** — [`../development-engineering/`](../development-engineering/) |
| Validation strategy and evidence honesty | **Testing & Quality Engineering** — [`../testing-quality-engineering/`](../testing-quality-engineering/) |
| Consumer security policies, tool mandates, and risk acceptance | **Consumer** (**L2** / local policy) |

Out of scope:

- Replacing, relocating, or weakening **L0** security/privacy constraints or Framework Governance
- Certification, compliance attestation, formal audit authority, or penetration testing
- Approving or authorizing security risk acceptance
- Mandating security tools, scanners, or vendors
- Scanner execution authority or autonomous Consumer repository modification
- Secret exposure, secret dumping, or unauthorized secret-store access
- Inventing vulnerabilities or claiming vulnerability guarantees
- Replacing Architecture Engineering, Development Engineering, or Testing & Quality Engineering
- Migrating or forking Core `repository_analysis`, Review Checklist, Release Checklist, or root `SECURITY.md`
- Runtime, resolver, installer, registry, CLI, or auto-adoption behavior
- Module package validation ([`MODULE_VALIDATION.md`](../../docs/MODULE_VALIDATION.md)) and framework self-tests under `tests/`

---

## When to use

- A scoped change may affect trust boundaries, secrets handling, or dependency/supply-chain surface
- Security review-area identification is requested for a change under review
- Support is needed alongside Core Review or Release security/dependency checkpoints without replacing those gates
- Evidence-based security observations are needed without claiming audit or certification outcomes

---

## When not to use

- The primary need is architecture boundary redesign or structural-fit assessment — use Architecture Engineering / Core repository analysis
- The primary need is implementation scope fidelity or change hygiene — use Development Engineering
- The primary need is validation evidence honesty or test strategy — use Testing & Quality Engineering
- Penetration testing, formal audit, compliance certification, or risk-acceptance authorization is requested
- Documentation-only typos with no security-relevant surface
- The Consumer forbids external security guidance by policy
- Anyone expects this Module to run scanners, expose secrets, weaken L0, or authorize commits

---

## Draft disclosure

This Module is **`draft`** with maturity **`experimental`**.

- The package remains **`draft`** / **`experimental`** and incomplete relative to a full Security Engineering guidance surface.
- Included so far: `module.yaml` and this `README.md` only.
- Skills, Checklists, Knowledge, Prompts, Workflows, templates, examples, and tests are **not** included in this version.
- Not generally recommended for new durable Consumer adoption until the guidance surface is more complete.
- Evaluate only with this incomplete state disclosed. Module presence does **not** automatically adopt, install, enable, activate, or mandate this guidance.

---

## Core references

Link only — do not copy Core methodology, Workflow, Checklist, or repository policy bodies into this Module.

| Resource | Role |
|----------|------|
| [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) | Framework Contract (§5 Modules, §7 precedence; L0 non-overridable) |
| [`../../AGENTS.md`](../../AGENTS.md) | Agent operating manual (L0 security/privacy; approval gates) |
| [`../../checklists/review.md`](../../checklists/review.md) | Core change review checklist (L0 and secrets gates remain Core) |
| [`../../checklists/release_checklist.md`](../../checklists/release_checklist.md) | Core Release Checklist (security & dependency review items remain Core) |
| [`../../workflows/release.md`](../../workflows/release.md) | Core Release Workflow |
| [`../../workflows/feature_development.md`](../../workflows/feature_development.md) | Core Feature Development Workflow (delivery context; not replaced by this Module) |
| [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) | Core repository analysis (security review areas remain Core-owned; not pen-test/certification) |
| [`../../docs/PROCESS_DEPTH_MODEL.md`](../../docs/PROCESS_DEPTH_MODEL.md) | Process depth (including standing L0 constraints vs task exposure) |
| [`../../methodology/rdiv.md`](../../methodology/rdiv.md) | Review → Decide → Implement → Verify |
| [`../../methodology/ai_collaboration.md`](../../methodology/ai_collaboration.md) | AI assists; humans decide |
| [`../../SECURITY.md`](../../SECURITY.md) | AIOS **repository** vulnerability-reporting policy — **not** Security Engineering Module content |

`requires_core: "1.0.1"` in metadata is an **informational** minimum aligned with the repository root [`../../VERSION`](../../VERSION) value at authoring time (`1.0.1`). It is not a resolver, installer pin, or runtime dependency.

---

## Module capabilities

Only capabilities that exist in this package are listed. Absence of other capability types is intentional in this draft.

### Skills

No Module-local Skills are included in this version.

### Not included in this version

Skills, Checklists, Knowledge, Prompts, Workflows, templates, examples, and tests.

### Core procedures (not Module-local)

For general change review gates (including secrets / L0), continue to use Core [`../../checklists/review.md`](../../checklists/review.md). For release security and dependency checkpoints, continue to use Core [`../../checklists/release_checklist.md`](../../checklists/release_checklist.md) and [`../../workflows/release.md`](../../workflows/release.md). For repository security review-area inventory, continue to use Core [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md). Other Core references remain in the section above.

---

## Relationship to Architecture Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../architecture-engineering/`](../architecture-engineering/) | Boundaries, structural fit, and architecture decision **support** (Consumer still owns ADRs) |
| **This Module** | Change-scoped threat / trust-boundary **awareness** and security review-area guidance |

This Module may consider trust-boundary **awareness**. It must **not** take over architecture boundary review or structural trust design. When structural-fit or boundary-redesign questions dominate, prefer Architecture Engineering (and Core repository analysis when discovery is incomplete).

Do not assume Architecture Engineering is installed or adopted because this package references it.

---

## Relationship to Development Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../development-engineering/`](../development-engineering/) | Implementation discipline, scope fidelity, and change hygiene within an **already agreed** scope |
| **This Module** | Security impact of implementation changes; secrets and supply-chain hygiene awareness |

This Module does **not** perform plan-to-diff or change-hygiene review. When implementation-scope questions dominate, prefer Development Engineering.

Do not assume Development Engineering is installed or adopted because this package references it.

---

## Relationship to Testing & Quality Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../testing-quality-engineering/`](../testing-quality-engineering/) | Risk-proportionate validation strategy and evidence honesty |
| **This Module** | Change-scoped security observations (threat / secrets / supply-chain), not validation-run honesty |

This Module does **not** own test strategy, coverage honesty, or Stage 7 orchestration. When “were validation checks run honestly?” dominates, prefer Testing & Quality Engineering.

Do not assume Testing & Quality Engineering is installed or adopted because this package references it.

---

## Related Modules

- [`architecture-engineering`](../architecture-engineering/) — companion for architecture-boundary guidance (docs-only; not a hard dependency)
- [`development-engineering`](../development-engineering/) — companion for implementation change hygiene (docs-only; not a hard dependency)
- [`testing-quality-engineering`](../testing-quality-engineering/) — companion for validation strategy and evidence honesty (docs-only; not a hard dependency)
- [`devops-cloud-engineering`](../devops-cloud-engineering/) — companion for delivery-pipeline security hygiene and operational delivery practices (docs-only; not a hard dependency). This Module retains ownership of change-scoped threat, secrets, and supply-chain **awareness**; DevOps & Cloud addresses how security hygiene is handled **within delivery pipelines**. Core **L0** remains authoritative. No secret-store access, secret exposure, scanner execution, or security certification authority is transferred.
- [`data-engineering`](../data-engineering/) — companion for schema / lineage / data-flow engineering context (docs-only; not a hard dependency). This Module retains threat, sensitive-data, and secrets **awareness**; Data Engineering does **not** own threat modeling and does **not** authorize PII export or secret-store access. Core **L0** remains authoritative.

Documentation Engineering is not listed until a package exists.

---

## Adoption notes

- Presence under `modules/` does **not** adopt, install, enable, or sync this Module into a Consumer repository.
- `aiosctl sync` does not install Modules.
- Explicit Consumer adoption into local policy is Consumer-owned (**L3** within adoption scope) and must not be assumed or performed silently.
- Consumer-owned ADRs, security policies, tool mandates, risk acceptance, and architecture decisions remain Consumer-owned (**L2** / local process).

---

## Maintenance

- Maintained by AIOS maintainers as part of the Engineering Module Catalog.
- Package version (`module.yaml` `version`) is independent of the AIOS Framework `VERSION` and of Consumer sync markers.
- Role-based contact: see repository [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).
