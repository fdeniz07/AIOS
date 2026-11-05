# AIOS Roadmap

Status: Active

Last Updated: 2026-11-05

This is the **AIOS framework** product roadmap.

It describes proposed evolutionary phases, not fixed delivery dates and not guaranteed release version numbers.

Consumer-project roadmaps, ADRs and backlogs belong in those repositories — not here.

Authoritative governance and precedence: [`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md) §7 (operationalized in [`AGENTS.md`](AGENTS.md) §2).

---

## Guiding Constraints

- Remain an open-source AI Software Engineering Framework
- Stay reusable across projects and technology stacks
- Support beginners through senior engineers and teams
- Prefer incremental change over rewrites
- Avoid unnecessary complexity
- Preserve useful Git history and consumer sync compatibility
- Provide the framework, not the domain content
- Do not present planned capabilities (module runtime, discovery engine, automated apply of recommendations, a fully populated multi-domain Module catalog, new CLI commands, etc.) as already implemented — a draft first Module package does not mean the catalog is complete
- Protect the existing `aiosctl sync` contract (`rules/*.md` → consumer `.agents/`) unless a versioned migration is explicitly approved

---

## Phase 0 — Foundation and Identity

**Intent:** Align AIOS identity and documentation with reality.

**Completed:**

- Generic `AGENTS.md`
- Honest README capability status
- Complete `MANIFEST.md` and `PROJECT_STRUCTURE.md` (Phase 0 baseline)
- Framework `ROADMAP.md`
- Minimal OSS docs (`CONTRIBUTING`, `SECURITY`, `CODE_OF_CONDUCT`)
- Preserve education operating manual under `packs/education/`
- Keep `rules/` sync contract unchanged for consumers

**Status:** Completed

---

## Phase 1 — Framework Contract and Governance Alignment

**Intent:** Make adoption unambiguous and align Core documentation with the approved contract.

**Status:** Completed

### Closure note

- Formally approved by the Product Owner.
- Final validation: Phase 1.7 – **PASS**.
- Governance Foundation acceptance criteria satisfied.

### Completed Phase 1 objectives

- Framework Contract created and approved (`docs/FRAMEWORK_CONTRACT.md`)
- L0–L7 governance / precedence model established (Contract §7)
- Root `AGENTS.md` aligned to operationalize L0–L7
- L4/L6 methodology authority clarified (Core methodologies remain L6 recommendations by default; explicit consumer adoption → L3)
- Relevant Core governance documents aligned (`rules/PROJECT_RULES.md`, `rules/DECISION_RULES.md`, `rules/AGENT_RULES.md`)
- `README.md` and `MANIFEST.md` aligned with the Contract
- Education Pack README created (`packs/education/README.md`) as domain-agnostic Education & Learning Engineering overview
- Framework Contract precedence correction (L0–L7 explicit; outdated AGENTS “tension” removed)
- Repository documentation refresh of `PROJECT_STRUCTURE.md`, `ROADMAP.md` and `CONTRIBUTING.md`
- Governance consistency and regression validation (Phase 1.5.x)

### Phase 1 exit summary

The **governance foundation is complete**: authoritative Framework Contract, operational L0–L7 model, Core document alignment, Education Pack entry-point documentation, and sync-compatible Core rules surface.

Items listed below remain **Product Owner–approved deferrals** as **future work**. They are **not** Phase 1 blockers and do not reopen Phase 1.

### Explicitly deferred beyond Phase 1 (Product Owner decisions)

1. **Education-rule migration**
   - Keep education-specific rules in their current `rules/` locations.
   - Preserve the existing flat `rules/*.md` → consumer `.agents/` sync contract.
   - Do not migrate, rename, remove, or reorganize these rules as part of Phase 1.
   - Handle migration as a separately scoped future task with compatibility analysis and explicit approval.
   - Education content must not be automatically migrated into Core or Modules.

2. **Skills / workflows contribution standards**
   - Defer detailed contribution paths and standards to later capability phases (see Phases 4, 5, 7 and 9).
   - Do not imply that skills/workflows execution infrastructure already exists.

3. **Release documentation hygiene**
   - Defer the Phase 1 `CHANGELOG.md` update to a separate release-hygiene task.
   - Not a Phase 1 exit blocker.

4. **Implementation status labeling**
   - Remains ongoing documentation hygiene as placeholders fill in.
   - Not a Phase 1 exit blocker.

### Outside Phase 1 scope (future capabilities)

These remain later-phase direction only — **not implemented** and not Phase 1 incomplete work:

- Architecture & Module Foundation (Phase 2)
- CLI growth beyond `aiosctl sync` (Phase 3)
- Populated `workflows/`, `skills/`, `knowledge/` and related content (Phases 4–5)
- Adaptive recommendation design (Phase 6) and any future adaptive **engine** (separate approval)
- Engineering Module catalog / packaging (Phase 7; see that section for current partial progress)
- Broader validation/automation and ecosystem samples (Phases 8–9)

---

## Phase 2 — Architecture & Module Foundation

**Intent:** Define the reusable Module architecture and its contracts with Core, Packs, methodologies, consumers and future adaptive capabilities — **before** CLI growth or catalog population.

**Status:** Completed

### Closure note

- Architecture & Module Foundation contracts are approved and documented.
- Final review: Phase 2.8 – PASS WITH FINDINGS (closure adjustments applied).
- No Module packages, validators, CLI growth, or adaptive engine were implemented in this phase.

### Architectural direction (approved for this phase)

- Root `methodology/` remains **Core-owned L6 reference** content (not automatically L4).
- **Module-local** knowledge, skills and workflows are the default placement for Module assets.
- Root shared directories (`knowledge/`, `skills/`, `workflows/`, etc.) are reserved for genuinely **cross-cutting Core** resources.
- Pack-to-Module composition must remain possible.
- `pack.yaml` is **not** mandatory; optional Pack manifests remain deferred.
- Consumer adoption remains a **consumer-owned** ADR or local policy (adopt → L3 for Modules; Pack adopt → L5).
- Education content must not be automatically migrated into Core or Modules.
- Module **status** and **maturity** are separate metadata concepts (see `docs/MODULE_METADATA.md` and `docs/MODULE_LIFECYCLE.md`).

### Sub-phases

| ID | Title | Status | Focus |
|----|-------|--------|--------|
| **2.1** | Architecture Discovery | **Completed** | Read-only audit of current architecture and Module foundation gaps |
| **2.2** | Module Architecture Contract | **Completed** | Boundaries, optional directories, Core/Pack/Module interaction; `pack.yaml` not mandatory |
| **2.3** | Module Metadata Specification | **Completed** | Approved `module.yaml` field model (`docs/MODULE_METADATA.md`) |
| **2.4** | Dependency & Compatibility Model | **Completed** | Design completed; decisions embedded (see note below) |
| **2.5** | Module Lifecycle & Governance | **Completed** | Lifecycle, SemVer, deprecation/migration (`docs/MODULE_LIFECYCLE.md`) |
| **2.6** | Reference Module Design | **Completed** | Conceptual `architecture-engineering` design only (no Module package) |
| **2.7** | Validation Strategy | **Completed** | Future validation expectations (`docs/MODULE_VALIDATION.md`) |
| **2.8** | Final Review | **Completed** | Consistency review and closure adjustments |

### Phase 2.4 note (dependency & compatibility)

- Dependency and compatibility **design** is completed.
- Approved decisions are **embedded** in the Framework Contract, Module Metadata, and Module Validation documentation (for example: no `dependencies` field in metadata v1; presence of `dependencies` is a validation Error; circular Module dependencies remain conceptually forbidden; Pack composition is not a Module dependency; no resolver/installer).
- A separate `MODULE_DEPENDENCY.md` is **intentionally not required**.
- Future machine-readable Module relationship metadata remains **deferred** until a concrete use case justifies it.

### In scope for Phase 2 (completed)

- Architecture, contracts, metadata, dependency/compatibility **design**, lifecycle and reference Module **design**
- Documentation amendments that align with the Framework Contract (without silently changing approved L0–L7 authority)
- Distinguishing design / planned / implemented language

### Out of scope for Phase 2

- Populated multi-module catalog (see Phase 7)
- CLI implementation beyond today’s `sync` (see Phase 3)
- Autonomous adaptive recommendation or selection **engine** (Phase 6 is design-only; engine needs separate future approval)
- Breaking or replacing `aiosctl sync`
- Education-rule migration or automatic Education → Core/Module moves
- Module dependency **resolver** runtime
- Separate `MODULE_DEPENDENCY.md` (intentionally deferred)

---

## Phase 3 — CLI Improvements

**Intent:** Grow `aiosctl` beyond rule sync — carefully — **after** Module Foundation contracts exist.

**Depends on:** Phase 2 Module contracts (especially metadata and validation strategy) for any Module-aware commands.

Current (implemented): `aiosctl sync` copies `rules/*.md` → `<project>/.agents/`

Proposed commands (**planned, not implemented**):

- `validate`
- `doctor`
- `init`
- `version`
- Future Module-oriented discovery/validation helpers (for example list/info/validate) — only after Phase 2 schemas are approved

Also planned: decide whether `aiosctl.yaml` should become a real config surface.

**Compatibility rule:** do not break existing sync paths without a versioned migration. Sync behavior remains protected.

---

## Phase 4 — Workflow and Checklist System

**Intent:** Provide a small set of stack-agnostic workflows and usable checklists.

**Status:** Completed

Completed means Product Owner–accepted Phase 4 deliverables are implemented in the working tree. It does **not** imply they have already been committed or pushed.

**Conventions (Phase 4.2):** [`docs/WORKFLOW_CHECKLIST_CONVENTIONS.md`](docs/WORKFLOW_CHECKLIST_CONVENTIONS.md) — Markdown-first Workflow and Checklist definition conventions (no execution engine; no YAML frontmatter requirement). Document lifecycle status remains `Draft` until conventions themselves are separately approved.

**Accepted deliverables:**

- Workflow and Checklist authoring conventions
- Core Feature Development Workflow (`workflows/feature_development.md`)
- Core Release Workflow (`workflows/release.md`)
- Core Review Checklist (`checklists/review.md`)
- Core Release Checklist (`checklists/release_checklist.md`)
- Workflow–Checklist integration (Feature Development Stage 8 → `review`; Release Stages 7 and 9 → `release`)

**Historical objectives (satisfied):**

- Establish Workflow and Checklist authoring conventions (Phase 4.2)
- Populate `workflows/` with canonical engineering flows where they are genuinely cross-cutting Core resources; prefer Module-local workflows when capability-specific
- Complete release / review checklists
- Keep ceremony adaptive to project size

Does not implement a workflow or checklist execution engine.

---

## Phase 5 — Skills and Knowledge

**Intent:** Add reusable engineering knowledge without shipping consumer content.

**Status:** Completed

Completed means Product Owner–accepted Phase 5 deliverables are implemented in the working tree. It does **not** imply they have already been committed or pushed. It does **not** promote Skill or conventions lifecycles, populate Knowledge, or deliver Skill execution / retrieval infrastructure.

### Accepted progress

| Step | Outcome |
|------|---------|
| **5.1** Discovery | Accepted — Skill/Knowledge boundaries, Markdown-first approach, and placement rules clarified |
| **5.2** Conventions | [`docs/SKILL_KNOWLEDGE_CONVENTIONS.md`](docs/SKILL_KNOWLEDGE_CONVENTIONS.md) created and Product Owner–accepted; document lifecycle remains **Draft** (Markdown-first; no YAML frontmatter; definition lifecycle `draft` / `active` / `deprecated`; no Skill execution or Knowledge retrieval engine) |
| **5.3** Core Skill | Repository Analysis Skill (`skills/repository_analysis.md`, `id` `repository-analysis`) created and Product Owner–accepted; artifact lifecycle remains **`draft`** (`version` `0.1.0`); directory population ≠ active lifecycle or complete Skill catalog |
| **5.4** Documentation alignment | Framework Contract, ROADMAP, and PROJECT_STRUCTURE updated to reflect the above maturity without changing artifact lifecycles |
| **5.5** Final audit | PASS WITH FINDINGS — foundation sufficient to close; illustrative conventions path and ROADMAP closure wording corrected in this closure step |

**Knowledge:** remains **Planned** — no Core Knowledge example in Phase 5; `knowledge/` stays empty.

**Approved Phase 5 decisions:**

- Pure Markdown Skill and Knowledge definitions with metadata tables
- One Core Skill definition in Phase 5.3; **no** Core Knowledge example in Phase 5
- Prefer Module-local Skills when Module packages exist; root `skills/` / `knowledge/` only for genuinely cross-cutting Core resources
- Existing `prompts/` remain separate interaction artifacts (no migration/deletion); Skill is the canonical reusable capability definition
- Domain content (architecture, testing, security, DevOps, data, documentation) may later feed Phase 7 Module packaging — not Core identity dumps

**Historical objectives (preserved):**

- Skill schema and examples — prefer Module-local skills; root `skills/` / `knowledge/` only for cross-cutting Core resources
- Shared reference material under root `knowledge/` only when truly Core-wide
- Domains such as architecture, testing, security, DevOps, data, documentation (content may later feed Phase 7 packaging)

**Non-goals (preserved):** Does not implement a skills execution infrastructure, Knowledge retrieval/RAG/indexing engine, or Skill/Knowledge CLI.

**Closure note:** Phase 5 is **Completed**. Conventions remain **Draft**; the initial Core Skill remains **`draft`** (`0.1.0`, scope `core`); Knowledge remains **Planned** and empty. Skill Runner, discovery/runtime, RAG, CLI integration, automated installation, and Module/domain-specific Skill catalogs remain out of scope (later phases / separate approval).

---

## Phase 6 — Adaptive Project Intelligence

**Intent:** Define how agents assess repository and task context, adapt process depth, and recommend relevant guidance — **architecture and recommendation design**, not an autonomous runtime engine.

**Status:** Completed

Completed means Product Owner–accepted Phase 6 Adaptive Project Intelligence **documentation and design** deliverables are present in the working tree, with documentation-level final audit outcome **PASS WITH FINDINGS**. It does **not** imply they have already been committed or pushed. It does **not** deliver an adaptive engine, runtime, registry, resolver, scoring system, or automatic Consumer modification.

**Canonical design documents:**

- [`docs/ADAPTIVE_PROJECT_CONTEXT.md`](docs/ADAPTIVE_PROJECT_CONTEXT.md)
- [`docs/PROCESS_DEPTH_MODEL.md`](docs/PROCESS_DEPTH_MODEL.md)
- [`docs/ADAPTIVE_GUIDANCE_MODEL.md`](docs/ADAPTIVE_GUIDANCE_MODEL.md)
- [`docs/ADAPTIVE_GOVERNANCE_MODEL.md`](docs/ADAPTIVE_GOVERNANCE_MODEL.md)
- [`docs/ADAPTIVE_REFERENCE_SCENARIOS.md`](docs/ADAPTIVE_REFERENCE_SCENARIOS.md)
- [`docs/ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md`](docs/ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md)

**Explicit boundary:** Actual adaptive **engine** implementation requires a **separate future scope and Product Owner approval**. Phase 6 must not claim that engine as delivered.

Out of scope for Phase 6 (unless separately approved later):

- Autonomous Module discovery, selection, installation, or adoption
- Autonomous consumer repository modification
- Skill or Workflow execution engines
- Knowledge retrieval / RAG
- Adaptive CLI
- Numerical scoring or machine-learning classification

### Approved substages

| Stage | Title | Status |
|-------|-------|--------|
| **6.1** | Adaptive Intelligence Discovery | Completed |
| **6.2** | Repository Context Model | Completed — [`docs/ADAPTIVE_PROJECT_CONTEXT.md`](docs/ADAPTIVE_PROJECT_CONTEXT.md) |
| **6.3** | Complexity & Process Depth Model | Completed — [`docs/PROCESS_DEPTH_MODEL.md`](docs/PROCESS_DEPTH_MODEL.md) |
| **6.4** | Adaptive Guidance Model | Completed — [`docs/ADAPTIVE_GUIDANCE_MODEL.md`](docs/ADAPTIVE_GUIDANCE_MODEL.md) (conceptual design specification; not an adaptive engine) |
| **6.5** | Governance & Human Approval | Completed — conceptual design in [`docs/ADAPTIVE_GOVERNANCE_MODEL.md`](docs/ADAPTIVE_GOVERNANCE_MODEL.md) (governance interactions only; no new approval policies; not a runtime) |
| **6.6** | Reference Scenarios & Final Audit | Completed — [`docs/ADAPTIVE_REFERENCE_SCENARIOS.md`](docs/ADAPTIVE_REFERENCE_SCENARIOS.md) (illustrative validation references; not policies); [`docs/ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md`](docs/ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md) (documentation-level audit **PASS WITH FINDINGS**; not a runtime test) |

#### Phase 6.6 substages

| Stage | Title | Status |
|-------|-------|--------|
| **6.6.1** | Read-only Discovery | Completed |
| **6.6.2** | Scenario & Audit Design | Completed |
| **6.6.3** | Reference Scenarios & Audit Documentation | Completed — [`docs/ADAPTIVE_REFERENCE_SCENARIOS.md`](docs/ADAPTIVE_REFERENCE_SCENARIOS.md); [`docs/ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md`](docs/ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md) |
| **6.6.4** | Documentation Alignment & Phase Closure | Completed |

#### Phase 6.5 substages

| Stage | Title | Status |
|-------|-------|--------|
| **6.5.1** | Read-only Discovery | Completed |
| **6.5.2** | Governance Design Proposal | Completed |
| **6.5.3** | Adaptive Governance Model Documentation | Completed — [`docs/ADAPTIVE_GOVERNANCE_MODEL.md`](docs/ADAPTIVE_GOVERNANCE_MODEL.md) (conceptual design specification; not a runtime; AGENTS.md §8 unchanged) |
| **6.5.4** | Documentation & Roadmap Alignment | **Completed** |

#### Phase 6.4 substages

| Stage | Title | Status |
|-------|-------|--------|
| **6.4.1** | Read-only Documentation Alignment Discovery | Completed |
| **6.4.2** | Adaptive Guidance Design Proposal | Completed |
| **6.4.3** | Adaptive Guidance Model Implementation | Completed — [`docs/ADAPTIVE_GUIDANCE_MODEL.md`](docs/ADAPTIVE_GUIDANCE_MODEL.md) (conceptual design specification; not a runtime) |
| **6.4.4** | Documentation & Roadmap Alignment | Completed |

#### Phase 6.3 substages

| Stage | Title | Status |
|-------|-------|--------|
| **6.3.1** | Complexity & Process Depth Discovery | Completed |
| **6.3.2** | Complexity Dimensions Model | Completed — consolidated in [`docs/PROCESS_DEPTH_MODEL.md`](docs/PROCESS_DEPTH_MODEL.md) |
| **6.3.3** | Process Depth Classification Model | Completed — [`docs/PROCESS_DEPTH_MODEL.md`](docs/PROCESS_DEPTH_MODEL.md) |
| **6.3.4** | Feature Development Workflow Mapping | Completed — [`docs/PROCESS_DEPTH_MODEL.md`](docs/PROCESS_DEPTH_MODEL.md) §5 |

#### Phase 6.3.4 substages

| Stage | Title | Status |
|-------|-------|--------|
| **6.3.4.1** | Read-only Discovery | Completed |
| **6.3.4.2** | Design Proposal | Completed |
| **6.3.4.3** | Implementation | Completed — [`docs/PROCESS_DEPTH_MODEL.md`](docs/PROCESS_DEPTH_MODEL.md) §5 |
| **6.3.4.4** | Documentation & Roadmap Alignment | Completed |

### Approved design directions

- Keep **Project Context** and **Task Context** separate; both inform Process Depth and guidance recommendations
- Use exactly four Process Depth levels: **Lightweight**, **Standard**, **Enhanced**, **Critical** (distinct from L0–L7; distinct from “lightweight tooling”)
- Remain useful with **Core-only** guidance (Workflows, Checklists, Skills, methodologies); Modules and Packs may enrich later but are not mandatory
- Documentation/convention-first unless/until tooling is separately proven and approved

### Preserved historical intent

- Project-type and repository signals as part of Project Context (for example library, service, monorepo, docs-only)
- Explainable guidance recommendations based on Project Context, Task Context, existing artifact definitions, and human judgment / acceptance where applicable — not an automatic resolver, scoring system, or runtime selection engine ([`docs/ADAPTIVE_GUIDANCE_MODEL.md`](docs/ADAPTIVE_GUIDANCE_MODEL.md))
- No autonomous module discovery, selection, or consumer-modification engine in this phase

---

## Phase 7 — Engineering Module Catalog / Packaging

**Intent:** Populate reusable engineering Module packages using the Phase 2 contracts.

This phase carries forward the **implementation / packaging** slice formerly associated with “Engineering Modules,” after architecture was moved into Phase 2.

**Status:** In progress — Module catalog foundation established; catalog not fully populated.

### Completed so far (Phase 7.1–7.30)

| ID | Title | Status | Outcome |
|----|-------|--------|---------|
| **7.1** | Module Catalog Discovery | **Completed** | Read-only inventory and first-Module recommendation |
| **7.2** | Module Catalog Architecture | **Completed** | Catalog conventions; root modules/; PO decisions on IDs/prompts/index |
| **7.3** | Architecture Engineering Module Design | **Completed** | Design-only for `architecture-engineering` |
| **7.4** | Initial Module Skeleton | **Completed** | `modules/README.md`; `architecture-engineering` `module.yaml` + README |
| **7.5** | First Module Skill + doc alignment | **Completed** | Module-local Skill `architecture-boundary-review` (`draft`); Module/catalog README alignment |
| **7.6** | Roadmap and Project Structure Alignment | **Completed** | ROADMAP and PROJECT_STRUCTURE aligned to the Module catalog foundation; Product Owner accepted |
| **7.7** | Next-domain prioritization | **Completed** | Candidate Engineering domains evaluated; Development Engineering selected as the next packaged domain |
| **7.8** | Development Engineering Module | **Completed** | `development-engineering` (`draft` / `experimental` / `0.1.0`); Module-local Skill `implementation-change-hygiene` (`draft`); Module README alignment |
| **7.9** | Catalog Documentation Alignment | **Completed** | Align ROADMAP, PROJECT_STRUCTURE, and Architecture Related Modules to both existing draft Modules |
| **7.15** | Testing & Quality Engineering Discovery | **Completed** | Read-only inventory; T&Q next-domain recommendation |
| **7.16** | Testing & Quality Engineering Module Design | **Completed** | Design-only; PO approved `testing-quality-engineering` skeleton-first |
| **7.17** | Testing & Quality Engineering Skeleton | **Completed** | `module.yaml` + README; catalog index row; no Skills |
| **7.18** | Catalog Documentation Alignment | **Completed** | Align ROADMAP and PROJECT_STRUCTURE to three draft Modules (`architecture-engineering`, `development-engineering`, `testing-quality-engineering`) |
| **7.26** | Next-domain discovery | **Completed** | Candidate remaining domains evaluated; Security Engineering recommended as next packaged domain |
| **7.27** | Security Engineering Module Design | **Completed** | Design-only; PO approved `security-engineering` skeleton-first |
| **7.28** | Security Engineering Skeleton | **Completed** | `module.yaml` + README; catalog index row; four draft Modules; no Module-local Skills |
| **7.29** | DevOps & Cloud Engineering Domain Discovery | **Completed** | Read-only inventory; DevOps & Cloud recommended as next packaged domain |
| **7.30** | DevOps & Cloud Engineering Module Design | **Completed** | Design-only; PO approved `devops-cloud-engineering` skeleton-first |

### Phase 7.31–7.36 (completed)

| ID | Title | Status | Outcome |
|----|-------|--------|---------|
| **7.31** | DevOps & Cloud Engineering Skeleton | **Completed** | `module.yaml` + README; catalog index row; five draft Modules; no Module-local Skills |
| **7.32** | Companion Module README Alignment | **Completed** | Documentation-only alignment of Architecture, Development, Testing & Quality and Security companion references for DevOps & Cloud Engineering; no Core or Module authority changes. |
| **7.33** | Final Pre-Commit Review and Publication | **Completed** | Nine-file Phase 7.31–7.32 change set reviewed, staged, committed and pushed (`f014c2e`). |
| **7.34** | Engineering Module Catalog Gap Assessment | **Completed** | Read-only; Data Engineering justified as next Module; Documentation Engineering not yet justified as Module |
| **7.35** | Data Engineering Domain Discovery | **Completed** | Read-only; Data Engineering justified; proceed to Module design |
| **7.36** | Data Engineering Module Design | **Completed** | Design-only; PO approved `data-engineering` skeleton-first (mandatory migration-inspection and pipeline-execution clarifications) |

### Phase 7.37 (current)

| ID | Title | Status | Outcome |
|----|-------|--------|---------|
| **7.37** | Data Engineering Skeleton | **In Progress** | `module.yaml` + README; catalog index row; six draft Modules; no Module-local Skills |

### Present today (not a full catalog)

- Catalog index: `modules/README.md` (thin index; not a registry/resolver)
- Draft Module packages:
  - `architecture-engineering` — `status: draft`, `maturity: experimental`, `version: 0.1.0`; informational `requires_core: "1.0.1"` (not a runtime pin); Module-local Skill `architecture-boundary-review` (`draft`, `scope: module`)
  - `development-engineering` — `status: draft`, `maturity: experimental`, `version: 0.1.0`; informational `requires_core: "1.0.1"` (not a runtime pin); Module-local Skill `implementation-change-hygiene` (`draft`, `scope: module`)
  - `testing-quality-engineering` — `status: draft`, `maturity: experimental`, `version: 0.1.0`; informational `requires_core: "1.0.1"` (not a runtime pin); skeleton only (`module.yaml` + README); no Module-local Skills in this version
  - `security-engineering` — `status: draft`, `maturity: experimental`, `version: 0.1.0`; informational `requires_core: "1.0.1"` (not a runtime pin); skeleton only (`module.yaml` + README); no Module-local Skills in this version
  - `devops-cloud-engineering` — `status: draft`, `maturity: experimental`, `version: 0.1.0`; informational `requires_core: "1.0.1"` (not a runtime pin); skeleton only (`module.yaml` + README); no Module-local Skills in this version
  - `data-engineering` — `status: draft`, `maturity: experimental`, `version: 0.1.0`; informational `requires_core: "1.0.1"` (not a runtime pin); skeleton only (`module.yaml` + README); no Module-local Skills in this version
- Guidance remains **L6** by default; explicit Consumer adoption → Consumer-owned **L3**
- Framework Governance remains Core-owned; Consumer architecture/ADRs, Consumer testing policies, Consumer security policies / risk acceptance, Consumer infrastructure / deployment policies / SLOs, and Consumer data architecture / data policies / retention / risk acceptance remain Consumer-owned (**L2**)

### Catalog targets (not all packaged)

Intended Engineering Module domains (six draft packages present today; catalog not complete):

- Architecture Engineering — **present** (`architecture-engineering`, draft)
- Development Engineering — **present** (`development-engineering`, draft)
- Testing & Quality Engineering — **present** (`testing-quality-engineering`, draft)
- Security Engineering — **present** (`security-engineering`, draft)
- DevOps & Cloud Engineering — **present** (`devops-cloud-engineering`, draft)
- Data Engineering — **present** (`data-engineering`, draft)
- Documentation Engineering — not packaged (narrowed from “Documentation & Governance”; Framework Governance stays Core)

Education materials remain optional **Packs**, not Core identity and not an automatic Module migration.

### Remaining Phase 7 direction (not claimed done)

- Additional Module packages for the domains above (when designed and approved)
- Further Module-local capabilities only with explicit approval
- Do **not** treat draft Modules/Skills as stable, active, installed, adopted, or mandatory

**Out of scope unless separately approved:** dependency resolver runtime; auto-install into consumer repositories; Module registry/discovery engine; adaptive recommendation **engine**; breaking sync; new metadata/lifecycle fields.

---

## Phase 8 — Validation and Automation

**Intent:** Verify framework integrity in CI and structural tests.

- Populate `tests/` for structure and contract checks
- Strengthen CI beyond demo API smoke tests
- Validate docs references and required entry points
- Complement (do not replace) any local CLI validation from Phase 3

---

## Phase 9 — Ecosystem and Integrations

**Intent:** Improve adoption across coding agents and host projects.

- Adoption examples under `examples/` (pointers or minimal samples)
- Integration notes for major coding assistants
- Community contribution of skills, workflows and Modules under approved contracts

---

## Explicit Non-Goals for This Roadmap

- Hosting a single company's product backlog inside AIOS Core
- Replacing general-purpose coding assistants
- Building a large runtime “AI OS kernel” before the documentation contract is solid
- Breaking `aiosctl sync` consumers for cosmetic folder moves
- Claiming planned Modules, adaptive tooling, module resolvers, or new CLI commands as shipped Core features
- Treating Phase 6 adaptive **design** as delivery of an adaptive **engine**

---

## How to Use This Document

Contributors and agents should treat later phases as **direction**, not unfinished work to invent in one pass.

Prefer completing earlier phases with small, reviewable changes.

Changes that affect architecture, governance, compatibility or consumer ownership must respect [`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md) and applicable approval gates.
