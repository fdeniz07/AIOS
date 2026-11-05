# DevOps & Cloud Engineering

| Field | Value |
|-------|-------|
| Module id | `devops-cloud-engineering` |
| Package version | `0.1.0` |
| Status | `draft` |
| Maturity | `experimental` |

This document is the human and agent entry point for the **DevOps & Cloud Engineering** Module. Machine-readable identity and short discovery fields live in [`module.yaml`](module.yaml). Do not treat metadata as adoption or installation.

**Authority:** Module guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs or Consumer infrastructure / deployment policies (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** security and privacy constraints. Instruction precedence remains [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) §7 / [`../../AGENTS.md`](../../AGENTS.md) §2. AI recommends; humans decide. Durable product, architecture, infrastructure, deployment, and operational-acceptance decisions belong to the Consumer.

---

## Purpose

Provide optional, stack-agnostic guidance for **change-scoped delivery and operational (DevOps & Cloud) engineering** so Consumers can judge:

1. **How does this change affect CI/CD, environments, infrastructure-as-code, containers, or operational readiness?**
2. **What delivery, promotion, and infrastructure hygiene risks appear in evidence?**
3. **What is observed versus inferred** — without claiming deployment authority, cloud access, uptime guarantees, or vendor mandates?

This Module **enriches** Core Release publication/verification practice and repository-analysis CI/ops review areas with reusable domain guidance. It covers **both DevOps and Cloud Engineering** concerns — not CI/CD alone. It does **not** replace Core Release Workflow or Checklist, AIOS repository CI, Framework Governance, or Core repository analysis.

---

## Scope

In scope for this Module’s guidance surface (guidance areas — not Module-local Skills in this version):

### CI/CD pipeline hygiene

- Pipeline structure and maintainability
- Change-scoped pipeline review
- Honest interpretation of pipeline gates and results
- Separation of validation, publication, and deployment concerns

No CI/CD platform or vendor mandate. The AIOS repository’s own [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml) remains **Core repository maintenance**, not this Module’s content.

### Environment separation and promotion

- Environment separation principles
- Configuration separation
- Promotion paths
- Environment-specific operational risks

Consumer ownership of environment topology, infrastructure choices, and deployment policies is preserved. No cloud account, cluster, or production environment access.

### Build artifact and publication discipline

Guidance that **complements** Core Release Stage 8 (tagging and publication). This Module does **not** grant authority to create tags, push artifacts, publish packages, deploy applications, or approve releases. Core Release Workflow and Release Checklist remain authoritative.

### Infrastructure-as-Code review heuristics

**Inspection is not execution.**

Allowed as guidance:

- Reviewing existing IaC diffs
- Reviewing already available plan output (when present as evidence)
- Identifying scope and blast-radius concerns
- Discussing configuration drift evidence
- Highlighting potentially destructive changes
- Separating observed facts from inferred risks

Not authorized by this Module:

- Running `terraform plan` / `terraform apply` or equivalent commands
- Generating a plan by executing provisioning tools
- Modifying Consumer infrastructure
- Accessing cloud accounts
- Executing deployment or provisioning tools

An existing plan output may be inspected as evidence. This Module does **not** authorize generating a plan by executing commands. All infrastructure decisions remain Consumer-owned.

### Container and image hygiene

- Base-image awareness
- Image and dependency hygiene
- Configuration surface
- Container lifecycle concerns
- Operational implications of container changes

No Docker, Kubernetes, registry, or other vendor/tool mandate. No registry access or container runtime execution authority.

### Observability and operational readiness

- Logs, metrics, and traces as operational signals
- Operational readiness considerations
- Monitoring and alerting design considerations
- Failure visibility and diagnosability
- Evidence-based operational observations

Consumer-owned: SLOs and SLIs, alert thresholds, monitoring platforms, operational acceptance criteria, and production readiness / go-live decisions. No uptime guarantees or operational certification claims.

### Operational safety, blast-radius, and rollback awareness

- Blast-radius awareness
- Change reversibility
- Failure impact
- Rollback considerations (awareness and review support only)
- Operational risk disclosure

Rollback guidance is **awareness only**. This Module does **not** invent or claim authority over Core rollback systems, automated runbooks, or Consumer operational procedures.

### Secrets-in-pipeline hygiene

Delivery-pipeline handling guidance only.

- **Security Engineering** owns threat, secrets, and supply-chain **awareness**.
- **This Module** addresses how security hygiene is handled **within delivery pipelines**.
- **Core L0** security and privacy constraints remain authoritative.

No secret values, secret dumping, unauthorized secret-store access, secret retrieval, or scanner execution authority.

### Explicit boundaries

| Concern | Owner |
|---------|--------|
| Framework Governance and L0–L7 precedence | **Core** — [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) §7 / [`../../AGENTS.md`](../../AGENTS.md) §2 |
| AGENTS.md §8 approval gates | **Core** — [`../../AGENTS.md`](../../AGENTS.md) |
| AGENTS.md §9 safety | **Core** — [`../../AGENTS.md`](../../AGENTS.md) |
| L0 security and privacy constraints | **Core** |
| Feature Development Workflow | **Core** — [`../../workflows/feature_development.md`](../../workflows/feature_development.md) |
| Release Workflow and Release Checklist | **Core** — [`../../workflows/release.md`](../../workflows/release.md), [`../../checklists/release_checklist.md`](../../checklists/release_checklist.md) |
| Repository analysis and CI/ops inventory | **Core** — [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) |
| AIOS repository CI | **Core** maintainers — [`../../.github/workflows/ci.yml`](../../.github/workflows/ci.yml) |
| Phase 8 framework self-tests and Module validation CI direction | **Core** |
| `aiosctl sync` contract | **Core** |
| Architecture boundaries and structural fit | **Architecture Engineering** — [`../architecture-engineering/`](../architecture-engineering/) |
| Implementation scope and change hygiene | **Development Engineering** — [`../development-engineering/`](../development-engineering/) |
| Validation strategy and evidence honesty | **Testing & Quality Engineering** — [`../testing-quality-engineering/`](../testing-quality-engineering/) |
| Threat, secrets, and supply-chain awareness | **Security Engineering** — [`../security-engineering/`](../security-engineering/) |
| Consumer infrastructure decisions, deployment policies, SLOs, and tool mandates | **Consumer** (**L2** / local policy) |
| Reusable delivery and operational engineering guidance | **This Module** (**L6**) |

Out of scope:

- Consumer deployment or go-live authority
- Cloud account, cluster, or production access
- Secret-store access or secret exposure
- Autonomous infrastructure or CI/CD changes
- IaC plan/apply command execution authority
- Deployment execution authority
- Vendor or tool mandates
- Certification or uptime guarantees
- Runtime, resolver, installer, registry, CLI, or auto-adoption
- Replacement of Core Release Workflow or Release Checklist
- Replacement of AIOS repository CI
- Modification of Consumer infrastructure without explicit Consumer authorization
- Forking or migrating Core `repository_analysis`, Release artifacts, or Framework Governance
- Inventing Core rollback automation or runbooks
- Module package validation ([`MODULE_VALIDATION.md`](../../docs/MODULE_VALIDATION.md)) and framework self-tests under `tests/`

---

## When to use

- A scoped change affects CI/CD pipelines, environments, infrastructure-as-code, containers, or operational readiness
- Delivery, environment promotion, or infrastructure **review** guidance is requested
- Support is needed alongside Core Release publication/deploy steps without replacing those gates
- Operational readiness or blast-radius awareness is needed without claiming go-live authority

---

## When not to use

- The primary need is architecture boundary redesign or structural-fit assessment — use Architecture Engineering / Core repository analysis
- The primary need is implementation scope fidelity or change hygiene — use Development Engineering
- The primary need is validation evidence honesty or test strategy — use Testing & Quality Engineering
- The primary need is threat, secrets, or supply-chain **awareness** (not pipeline handling) — use Security Engineering
- Cloud account access, production deployment execution, or infrastructure apply is requested
- Documentation-only typos with no delivery or operational surface
- The Consumer forbids external DevOps or Cloud guidance by policy
- Anyone expects this Module to deploy, apply IaC, access cloud accounts, expose secrets, weaken L0, or authorize commits

---

## Draft disclosure

This Module is **`draft`** with maturity **`experimental`**.

- The package remains **`draft`** / **`experimental`** and incomplete relative to a full DevOps & Cloud Engineering guidance surface.
- Included so far: `module.yaml` and this `README.md` only.
- Skills, Checklists, Knowledge, Prompts, Workflows, templates, examples, and tests are **not** included in this version.
- The package is **not** a complete operational playbook.
- Not generally recommended for new durable Consumer adoption until the guidance surface is more complete.
- Evaluate only with this incomplete state disclosed. Module presence does **not** automatically adopt, install, enable, activate, or mandate this guidance.

---

## Core references

Link only — do not copy Core methodology, Workflow, Checklist, or repository CI bodies into this Module.

| Resource | Role |
|----------|------|
| [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) | Framework Contract (§5 Modules, §7 precedence; L0 non-overridable) |
| [`../../AGENTS.md`](../../AGENTS.md) | Agent operating manual (§8 approval gates; §9 safety; L0 security/privacy) |
| [`../../workflows/release.md`](../../workflows/release.md) | Core Release Workflow (Stage 8–9 publication/verification remain Core; this Module enriches ops analysis only) |
| [`../../checklists/release_checklist.md`](../../checklists/release_checklist.md) | Core Release Checklist (readiness/decision/closure; no deploy authority) |
| [`../../workflows/feature_development.md`](../../workflows/feature_development.md) | Core Feature Development Workflow (delivery context; not replaced) |
| [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) | Core repository analysis (CI/CD and Operations inventory remains Core-owned) |
| [`../../docs/PROCESS_DEPTH_MODEL.md`](../../docs/PROCESS_DEPTH_MODEL.md) | Process depth (operational authorization vs Process Depth; Release class boundary) |
| [`../../methodology/rdiv.md`](../../methodology/rdiv.md) | Review → Decide → Implement → Verify |
| [`../../methodology/ai_collaboration.md`](../../methodology/ai_collaboration.md) | AI assists; humans decide |
| [`../../.github/workflows/ci.yml`](../../.github/workflows/ci.yml) | AIOS **repository** CI — Core maintenance; **not** DevOps & Cloud Module content |
| [`../../VERSION`](../../VERSION) | Framework version source at authoring time |

`requires_core: "1.0.1"` in metadata is an **informational** minimum aligned with the repository root [`../../VERSION`](../../VERSION) value at authoring time (`1.0.1`). It is not a resolver, installer pin, or runtime dependency.

---

## Module capabilities

Only capabilities that exist in this package are listed. Absence of other capability types is intentional in this draft.

### Skills

No Module-local Skills are included in this version.

### Not included in this version

Skills, Checklists, Knowledge, Prompts, Workflows, templates, examples, and tests.

### Core procedures (not Module-local)

For release readiness, human release decision, and publication authorization, continue to use Core [`../../workflows/release.md`](../../workflows/release.md) and [`../../checklists/release_checklist.md`](../../checklists/release_checklist.md). For repository CI/ops inventory, continue to use Core [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md). For AGENTS approval and safety gates, continue to use [`../../AGENTS.md`](../../AGENTS.md) §8 / §9. Other Core references remain in the section above.

---

## Relationship to Architecture Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../architecture-engineering/`](../architecture-engineering/) | Boundaries, structural fit, and architecture decision **support** (Consumer still owns ADRs) |
| **This Module** | Delivery/ops practice; environment promotion and operational implications |

This Module may discuss operational implications. It must **not** own cloud topology or architecture decisions. When structural-fit or boundary-redesign questions dominate, prefer Architecture Engineering.

Do not assume Architecture Engineering is installed or adopted because this package references it.

---

## Relationship to Development Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../development-engineering/`](../development-engineering/) | Implementation discipline, scope fidelity, and change hygiene within an **already agreed** scope |
| **This Module** | Delivery pipeline, infrastructure, and operational **domain** practices |

This Module does **not** replace implementation-change-hygiene or plan-to-diff review. When implementation-scope questions dominate, prefer Development Engineering.

Do not assume Development Engineering is installed or adopted because this package references it.

---

## Relationship to Testing & Quality Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../testing-quality-engineering/`](../testing-quality-engineering/) | Risk-proportionate validation strategy and evidence honesty (CI testing meaning ≠ pipeline ownership) |
| **This Module** | Pipeline structure, promotion, and operational readiness — not test strategy or validation-run honesty |

This Module does **not** own test strategy, coverage honesty, or Feature Development Stage 7. When “were validation checks run honestly?” dominates, prefer Testing & Quality Engineering.

Do not assume Testing & Quality Engineering is installed or adopted because this package references it.

---

## Relationship to Security Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../security-engineering/`](../security-engineering/) | Change-scoped threat, secrets, and supply-chain **awareness** |
| **This Module** | How security hygiene is handled **within delivery pipelines** (secrets-in-pipeline hygiene) |

This Module does **not** own threat modeling, secret-store access, secret exposure, or scanner execution. Core L0 remains authoritative. When threat / supply-chain awareness dominates (rather than pipeline handling), prefer Security Engineering.

Do not assume Security Engineering is installed or adopted because this package references it.

---

## Related Modules

- [`architecture-engineering`](../architecture-engineering/) — companion for architecture-boundary guidance (docs-only; not a hard dependency)
- [`development-engineering`](../development-engineering/) — companion for implementation change hygiene (docs-only; not a hard dependency)
- [`testing-quality-engineering`](../testing-quality-engineering/) — companion for validation strategy and evidence honesty (docs-only; not a hard dependency)
- [`security-engineering`](../security-engineering/) — companion for threat, secrets, and supply-chain awareness (docs-only; not a hard dependency)

Other Engineering domains are not listed here until packages exist.

---

## Adoption notes

- Presence under `modules/` does **not** adopt, install, enable, or sync this Module into a Consumer repository.
- `aiosctl sync` does not install Modules.
- Explicit Consumer adoption into local policy is Consumer-owned (**L3** within adoption scope) and must not be assumed or performed silently.
- Consumer-owned ADRs, infrastructure decisions, deployment policies, SLOs, tool mandates, and architecture decisions remain Consumer-owned (**L2** / local process).

---

## Maintenance

- Maintained by AIOS maintainers as part of the Engineering Module Catalog.
- Package version (`module.yaml` `version`) is independent of the AIOS Framework `VERSION` and of Consumer sync markers.
- Role-based contact: see repository [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).
