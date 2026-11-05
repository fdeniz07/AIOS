# Data Engineering

| Field | Value |
|-------|-------|
| Module id | `data-engineering` |
| Package version | `0.1.0` |
| Status | `draft` |
| Maturity | `experimental` |

This document is the human and agent entry point for the **Data Engineering** Module. Machine-readable identity and short discovery fields live in [`module.yaml`](module.yaml). Do not treat metadata as adoption or installation.

**Authority:** Module guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs or Consumer data architecture / data policies (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** constraints. Instruction precedence remains [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) §7 / [`../../AGENTS.md`](../../AGENTS.md) §2. AI recommends; humans decide. Durable product, architecture, and data-policy decisions—and risk acceptance—belong to the Consumer. Explicit Consumer adoption of Module guidance into local policy is Consumer-owned (**L3** within the adoption scope) and must not be assumed.

---

## Purpose

Provide optional, stack-agnostic guidance for **change-scoped data engineering** so Consumers can judge:

1. **Which data-model, schema, transformation, lineage, and quality concerns are relevant to this change?**
2. **What schema / data-contract and blast-radius risks appear in evidence?**
3. **What is observed versus inferred** — without migration execution, database access, PII export, vendor mandates, or Consumer data-architecture ownership?

This Module **enriches** Core Feature Development data-compatibility checkpoints, Process Depth data-integrity considerations, AGENTS approval gates for data/irreversibility, and repository-analysis data/persistence inventory with reusable domain guidance. It does **not** replace Framework Governance, Core Workflows, Core Skills, or sibling Module surfaces.

---

## Scope

In scope for this Module’s guidance surface (guidance areas — not Module-local Skills in this version):

### Data modeling

- Entity and relationship clarity as evidenced in the change
- Distinguishing application models from storage representations
- Change impact on existing models without imposing a Consumer canonical model

### Schema design and evolution

- Additive versus breaking change awareness
- Compatibility and consumer-impact considerations for schema/data contracts
- Schema-impact **review** of existing evidence (see Inspection versus execution)

### Data transformation

- Mapping completeness and silent-coercion risks
- Idempotency awareness for transform logic (conceptual)
- No ETL/ELT tool or vendor mandate

### Data pipeline semantics

- Job boundaries, dependency order, retry and idempotency **concepts**
- Semantic failure modes for data jobs
- Distinct from DevOps delivery / CI/CD pipelines (see glossary below)

### Data quality awareness

- What data-quality questions to ask (completeness, consistency, freshness as concepts)
- Criteria awareness only — not test strategy or validation-run ownership

### Data lineage and provenance

- Source-to-consumer impact awareness
- Blast-radius considerations for schema or data-contract changes
- No lineage-platform mandate; no production data tracing access

### Data lifecycle

- Retention, archive, and delete **awareness** only
- No legal retention sign-off or compliance certification

### Storage and access patterns

- Read/write path and consistency tradeoff **awareness** from repository evidence
- No database administration; no live database sessions; no engine/vendor selection authority

### Data integration and interoperability

- Cross-service data-contract drift awareness
- Complements Architecture boundary guidance without taking ownership of structural redesign

### Analytical versus operational data considerations

- Conceptual separation of operational versus analytical concerns
- No warehouse, lake, or analytics-platform mandate

### Data pipeline glossary

| Term | Meaning in this Module |
|------|------------------------|
| **Data pipeline (semantics)** | Data job, transform, and orchestration **meaning and contracts** — boundaries, dependencies, retry/idempotency concepts, semantic failure modes |
| **Delivery pipeline (DevOps)** | CI/CD structure, environment promotion, build/publish, and operational readiness — owned as guidance by [`../devops-cloud-engineering/`](../devops-cloud-engineering/) |

**Data pipeline semantics ≠ DevOps CI/CD pipeline ownership.**

### Inspection versus execution

**Inspection of existing evidence does not authorize execution or generation of new operational plans.**

Allowed as guidance:

- Inspecting existing migration **files** and **diffs**
- Inspecting already available migration **plans or outputs** when present as evidence
- Reviewing data job definitions, contracts, and documented lineage for impact awareness
- Separating observed facts from inferred risks (Fact / Inference / Recommendation)

Not authorized by this Module:

- Running migration tooling to **generate** a new operational plan
- Applying migrations or changing a database
- Triggering or executing data pipelines/jobs
- Direct database access or database administration
- Reading, exporting, or dumping production or PII data

### Explicit boundaries

| Concern | Owner |
|---------|--------|
| Framework Governance and L0–L7 precedence | **Core** — [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) §7 / [`../../AGENTS.md`](../../AGENTS.md) §2 |
| AGENTS.md §8 approval gates (including changes that break data; irreversible work) | **Core** — [`../../AGENTS.md`](../../AGENTS.md) |
| AGENTS.md §9 safety | **Core** — [`../../AGENTS.md`](../../AGENTS.md) |
| Feature Development Workflow (including Stage 4 data-compatibility triggers) | **Core** — [`../../workflows/feature_development.md`](../../workflows/feature_development.md) |
| Process Depth (including D6 data integrity & reversibility) | **Core** — [`../../docs/PROCESS_DEPTH_MODEL.md`](../../docs/PROCESS_DEPTH_MODEL.md) |
| Repository analysis (including Step 4 Data and persistence inventory) | **Core** — [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) — **reference and enrich; never fork, copy, relocate, or replace** |
| Architecture boundaries and structural fit | **Architecture Engineering** — [`../architecture-engineering/`](../architecture-engineering/) |
| Implementation scope and change hygiene | **Development Engineering** — [`../development-engineering/`](../development-engineering/) |
| Test strategy and validation evidence honesty | **Testing & Quality Engineering** — [`../testing-quality-engineering/`](../testing-quality-engineering/) |
| Threat, sensitive-data, and secrets awareness | **Security Engineering** — [`../security-engineering/`](../security-engineering/) |
| Delivery pipeline, environment promotion, IaC inspection, operational readiness | **DevOps & Cloud Engineering** — [`../devops-cloud-engineering/`](../devops-cloud-engineering/) |
| Consumer data architecture, ADRs, data policies, technology/vendor selection, retention decisions, and risk acceptance | **Consumer** (**L2** / local policy) |
| Reusable change-scoped data engineering guidance | **This Module** (**L6**) |

Out of scope:

- Database administration and direct database access
- Migration execution or applying schema/database changes
- Running migration tooling to generate a new operational plan
- Infrastructure or data-change execution
- Production/PII reading, exporting, or dumping
- Secret-store access or secret exposure
- Autonomous pipeline/job triggering or execution
- Owning or rewriting Consumer data architecture or ADRs
- Vendor or stack mandates (illustrative examples may appear; mandates are forbidden)
- Compliance certification and legal retention sign-off
- Replacing Architecture, Development, Testing & Quality, Security, or DevOps & Cloud owned surfaces
- Forking, copying, relocating, or replacing Core `repository_analysis`, Feature/Release Workflows, or Framework Governance
- Runtime, resolver, installer, registry, CLI, or auto-adoption behavior
- Module package validation ([`MODULE_VALIDATION.md`](../../docs/MODULE_VALIDATION.md)) and framework self-tests under `tests/`

---

## When to use

- A scoped change affects schemas, migrations, data contracts, persistence models, or data transformation/job definitions
- Schema-evolution, lineage/blast-radius, or data-quality **criteria** awareness is requested for a scoped change
- Support is needed alongside Core data-compatibility or irreversibility checkpoints without replacing those gates
- Evidence-based data-engineering observations are needed without claiming migration, DB, or pipeline execution authority

---

## When not to use

- The primary need is architecture boundary redesign or structural-fit assessment — use Architecture Engineering / Core repository analysis
- The primary need is implementation scope fidelity or change hygiene — use Development Engineering
- The primary need is validation evidence honesty or test strategy — use Testing & Quality Engineering
- The primary need is threat, sensitive-data, or secrets **awareness** — use Security Engineering
- The primary need is CI/CD, environment promotion, IaC, or operational readiness — use DevOps & Cloud Engineering
- Migration execution, live database access, production/PII export, or autonomous data-job execution is requested
- Documentation-only typos with no data or persistence surface
- The Consumer forbids external data-engineering guidance by policy
- Anyone expects this Module to migrate databases, run jobs, access production data, weaken L0, or authorize commits

---

## Draft disclosure

This Module is **`draft`** with maturity **`experimental`**.

- The package remains **`draft`** / **`experimental`** and incomplete relative to a full Data Engineering guidance surface.
- Included so far: `module.yaml` and this `README.md` only.
- Skills, Checklists, Knowledge, Prompts, Workflows, templates, examples, and tests are **not** included in this version.
- The package is **not** a complete data-platform playbook.
- Not generally recommended for new durable Consumer adoption until the guidance surface is more complete.
- Evaluate only with this incomplete state disclosed. Module presence does **not** automatically adopt, install, enable, activate, or mandate this guidance.

---

## Core references

Link only — do not copy Core methodology, Workflow, Checklist, or Skill bodies into this Module.

| Resource | Role |
|----------|------|
| [`../../docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) | Framework Contract (§5 Modules, §7 precedence; L0 non-overridable) |
| [`../../AGENTS.md`](../../AGENTS.md) | Agent operating manual (§8 approval gates including data/irreversibility; §9 safety) |
| [`../../workflows/feature_development.md`](../../workflows/feature_development.md) | Core Feature Development Workflow (Stage 4 data-compatibility triggers remain Core; not replaced) |
| [`../../docs/PROCESS_DEPTH_MODEL.md`](../../docs/PROCESS_DEPTH_MODEL.md) | Process depth (D6 data integrity & reversibility; Process Depth ≠ operational authorization) |
| [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md) | Core repository analysis (Step 4 Data and persistence inventory remains Core-owned; enrich only — never fork) |
| [`../../methodology/rdiv.md`](../../methodology/rdiv.md) | Review → Decide → Implement → Verify |
| [`../../methodology/ai_collaboration.md`](../../methodology/ai_collaboration.md) | AI assists; humans decide |
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

For data/persistence inventory, continue to use Core [`../../skills/repository_analysis.md`](../../skills/repository_analysis.md). For Feature Development data-compatibility and related stages, continue to use Core [`../../workflows/feature_development.md`](../../workflows/feature_development.md). For integrity/reversibility depth signals, continue to use [`../../docs/PROCESS_DEPTH_MODEL.md`](../../docs/PROCESS_DEPTH_MODEL.md). For AGENTS approval and safety gates, continue to use [`../../AGENTS.md`](../../AGENTS.md) §8 / §9. Other Core references remain in the section above.

---

## Relationship to Architecture Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../architecture-engineering/`](../architecture-engineering/) | Boundaries, structural fit, and architecture decision **support** (Consumer still owns ADRs) |
| **This Module** | Data-domain fit, schema/data-contract impact, and lineage/blast-radius **awareness** |

This Module may discuss data-compatibility implications. It must **not** own system boundary redesign or Consumer data architecture ADRs. When structural-fit or boundary-redesign questions dominate, prefer Architecture Engineering.

Do not assume Architecture Engineering is installed or adopted because this package references it.

---

## Relationship to Development Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../development-engineering/`](../development-engineering/) | Implementation discipline, scope fidelity, and change hygiene within an **already agreed** scope |
| **This Module** | Schema/data-change **intent and impact** guidance; data pipeline **semantics** |

**Development Engineering retains implementation-change hygiene.** This Module does **not** replace plan-to-diff or change-hygiene review. When implementation-scope questions dominate, prefer Development Engineering.

Do not assume Development Engineering is installed or adopted because this package references it.

---

## Relationship to Testing & Quality Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../testing-quality-engineering/`](../testing-quality-engineering/) | Risk-proportionate validation strategy and evidence honesty |
| **This Module** | Data-quality **criteria awareness** (what questions to ask) — not test strategy or validation-run honesty |

**Data quality criteria awareness ≠ Testing & Quality test strategy ownership.** This Module does **not** own Feature Development Stage 7, coverage honesty, or test execution. When “were validation checks run honestly?” dominates, prefer Testing & Quality Engineering.

Do not assume Testing & Quality Engineering is installed or adopted because this package references it.

---

## Relationship to Security Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../security-engineering/`](../security-engineering/) | Change-scoped threat, sensitive-data, secrets, and supply-chain **awareness** |
| **This Module** | Data-flow / lineage context for engineering impact — without threat-model or secrets ownership |

**Security Engineering retains threat, sensitive-data, and secrets awareness.** This Module does **not** authorize PII export, secret-store access, or security certification. Core **L0** remains authoritative. When threat / secrets review dominates, prefer Security Engineering.

Do not assume Security Engineering is installed or adopted because this package references it.

---

## Relationship to DevOps & Cloud Engineering

Companion relationship is **documentation-only**. Metadata v1 has no Module-to-Module `dependencies` field.

| Module | Responsibility |
|--------|----------------|
| [`../devops-cloud-engineering/`](../devops-cloud-engineering/) | Delivery pipeline hygiene, environment promotion, IaC inspection, and operational readiness |
| **This Module** | **Data pipeline semantics** (job/transform meaning and contracts) — not CI/CD or deployment ownership |

**Data pipeline semantics ≠ DevOps CI/CD pipeline ownership.** Guidance about data pipeline semantics is in scope; **triggering or executing** pipelines/jobs is **not** authorized by this Module. Operational execution and deployment authority remain Consumer-owned. DevOps & Cloud retains delivery-pipeline and operational guidance boundaries. When deploy/CI/IaC/ops questions dominate, prefer DevOps & Cloud Engineering.

Do not assume DevOps & Cloud Engineering is installed or adopted because this package references it.

---

## Related Modules

- [`architecture-engineering`](../architecture-engineering/) — companion for architecture-boundary guidance (docs-only; not a hard dependency)
- [`development-engineering`](../development-engineering/) — companion for implementation change hygiene (docs-only; not a hard dependency). Development Engineering retains implementation-change hygiene; this Module does not replace it.
- [`testing-quality-engineering`](../testing-quality-engineering/) — companion for validation strategy and evidence honesty (docs-only; not a hard dependency). Data-quality criteria awareness does not transfer test-strategy ownership.
- [`security-engineering`](../security-engineering/) — companion for threat, sensitive-data, and secrets awareness (docs-only; not a hard dependency)
- [`devops-cloud-engineering`](../devops-cloud-engineering/) — companion for delivery-pipeline and operational practices (docs-only; not a hard dependency). Data pipeline semantics remain distinct from CI/CD ownership; no job/pipeline execution authority is transferred.

Documentation Engineering is not listed until a package exists.

---

## Adoption notes

- Presence under `modules/` does **not** adopt, install, enable, or sync this Module into a Consumer repository.
- `aiosctl sync` does not install Modules.
- Explicit Consumer adoption into local policy is Consumer-owned (**L3** within adoption scope) and must not be assumed or performed silently.
- Consumer-owned ADRs, data architecture, data policies, technology/vendor selection, retention decisions, risk acceptance, and operational database authority remain Consumer-owned (**L2** / local process).

---

## Maintenance

- Maintained by AIOS maintainers as part of the Engineering Module Catalog.
- Package version (`module.yaml` `version`) is independent of the AIOS Framework `VERSION` and of Consumer sync markers.
- Role-based contact: see repository [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).
