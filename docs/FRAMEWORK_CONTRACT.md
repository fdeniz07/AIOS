# AIOS Framework Contract

Version: 1.4.0

Status: Approved

Last Updated: 2026-11-02

Document type: Architecture contract

This document defines architectural boundaries, responsibilities, consumption models, ownership rules, and compatibility principles for AIOS.

It is not an implementation plan, roadmap substitute, or marketing overview.

Phase 2.2 extends Section 5 with the **Module Architecture Contract** (conceptual architecture). Phase 2.3 adds the Module metadata field model in [`MODULE_METADATA.md`](MODULE_METADATA.md). Phase 2.5 adds Module lifecycle governance in [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md). Phase 2.7 adds future Module validation expectations in [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md). This contract does not implement Modules, metadata parsers, validators, CLI commands, lifecycle automation, or an adaptive engine.

Related entry points:

- Product overview: [`../README.md`](../README.md)
- Product manifest: [`../MANIFEST.md`](../MANIFEST.md)
- Actual repository layout: [`../PROJECT_STRUCTURE.md`](../PROJECT_STRUCTURE.md)
- Agent operating manual: [`../AGENTS.md`](../AGENTS.md)
- Evolution phases: [`../ROADMAP.md`](../ROADMAP.md)
- Module metadata field model: [`MODULE_METADATA.md`](MODULE_METADATA.md)
- Module lifecycle and governance: [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md)
- Module validation expectations: [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md)
- Workflow and checklist authoring conventions: [`WORKFLOW_CHECKLIST_CONVENTIONS.md`](WORKFLOW_CHECKLIST_CONVENTIONS.md)

---

## 1. Purpose and Scope

### Purpose

Establish a shared contract so that:

- contributors know what belongs in AIOS Core versus packs, modules, or consumer repositories
- coding agents apply AIOS guidance without owning consumer product decisions
- existing sync consumers are not silently broken
- planned capabilities are not mistaken for implemented ones
- adaptive module recommendations stay distinct from autonomous consumer changes

### In scope

- Architectural boundaries and component responsibilities
- Module Architecture Contract (conceptual; Section 5)
- Reference to the approved Module metadata field model ([`MODULE_METADATA.md`](MODULE_METADATA.md))
- Reference to Module lifecycle and governance ([`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md))
- Reference to future Module validation expectations ([`MODULE_VALIDATION.md`](MODULE_VALIDATION.md))
- Adaptive module recommendation principles (design contract, not runtime)
- Consumer ownership and precedence
- Supported consumption models
- Current `aiosctl sync` compatibility surface
- Versioning terminology and migration principles
- Implementation-status vocabulary

### Out of scope for this document

- Implementing adaptive module selection or recommendation engines in code
- Populating `modules/`, shipping a Module catalog, or implementing metadata parsers/validators
- Duplicating the full Module metadata, lifecycle, or validation specifications (see [`MODULE_METADATA.md`](MODULE_METADATA.md), [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md), [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md))
- Implementing Module validators, schemas, or CI jobs (expectations only in [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md))
- Implementing selective sync, pack sync, module sync, or prune behavior
- Moving or rewriting files under `rules/`
- Changing `scripts/aiosctl.py`
- Modifying any consumer repository
- Recording consumer product ADRs, backlogs, or roadmaps inside AIOS
- Dependency resolvers, installers, or package-manager runtimes

---

## 2. Product Identity and Principles

### Identity

| Field | Value |
|-------|-------|
| Name | AIOS (Artificial Intelligence Operating System) |
| Definition | Open-Source AI Software Engineering Framework |
| Slogan | Engineer the workspace, not the prompt. |
| Guiding principle | AIOS provides the framework, not the content. |

AIOS is a **repository-centered** engineering framework that works **with** coding agents.

AIOS is **not**:

- an IDE
- an LLM
- an AI wrapper
- a simple code-generation tool

### Principles

1. **Repository-driven engineering** — durable context lives in the repository.
2. **Architecture First** — understand before changing.
3. **RDIV** — Review → Decide → Implement → Verify (`methodology/rdiv.md`).
4. **Model- and agent-agnostic governance** — rules outlive any single tool.
5. **Human-in-the-loop** — conflicts are disclosed; approvals are respected.
6. **Minimal change** — preserve useful work; avoid unnecessary rewrites.
7. **Adaptive to project context** — recommendations scale with size, stack, risk, and capacity.
8. **Framework ≠ content** — Core stays reusable; domain content stays in packs or consumers.
9. **Honest status** — never claim validation or capability that was not performed or implemented.
10. **Consumer authority with non-overridable limits** — approved consumer ADRs and product decisions prevail over generic AIOS defaults, except where applicable **safety, legal, security, privacy, licensing, compliance** or other justified non-overridable obligations apply. Ordinary technical preferences are not L0.
11. **Recommend, do not impose** — AIOS explains options; it must not silently overwrite consumer decisions or autonomously restructure consumer repositories.

---

## 3. Architectural Boundaries

### Logical architecture tree

```text
AIOS
├── Core                         # common engineering foundation
│   ├── AGENTS.md
│   ├── MANIFEST.md / PROJECT_STRUCTURE.md / README.md / ROADMAP.md
│   ├── rules/                   # current sync source (includes legacy education rules)
│   ├── methodology/
│   ├── prompts/                 # partial; discovery and some review assets
│   └── scripts/aiosctl.py       # sync CLI (current)
│
├── Packs                        # optional domain / use-case extensions
│   └── education/               # partial; preserved education AGENTS today
│
├── Modules                      # planned reusable engineering capabilities
│   └── <module-id>/             # not populated yet
│
├── Shared capability areas      # mostly planned at repository root
│   ├── knowledge/
│   ├── skills/
│   ├── workflows/
│   ├── templates/
│   ├── checklists/
│   └── tests/
│
├── Integrations                 # planned guidance for external tools/agents
├── docs/                        # framework documentation (this contract)
├── lab/                         # demo only
└── examples/                    # planned adoption examples
```

### Core / Module / Pack (approved distinction)

| Layer | Meaning | Examples |
|-------|---------|----------|
| **Core** | Common engineering foundation and cross-domain principles | Governance, RDIV, Architecture First, generic `AGENTS.md` |
| **Module** | Reusable engineering capability | Architecture, Development, Testing & Quality, Security Engineering, DevOps & Cloud, Data Engineering |
| **Pack** | Optional domain- or use-case-specific extension | Education; other specialized domains |

Relationship rules:

- A **Pack may use** one or more Modules.
- A **Module must not** become tied to one specific Pack unless explicitly justified and documented.
- Core must remain usable without any Pack.
- Modules and Packs are optional relative to Core adoption.

### Boundary rules

| Layer | May contain | Must not contain |
|-------|-------------|------------------|
| Core | Cross-domain governance and methodology | Product roadmaps, consumer ADRs, pack-only curricula as Core identity |
| Pack | Domain/use-case extensions that may reference modules | Mandatory requirement to use AIOS Core |
| Module | Stack-agnostic engineering capability assets | Single-product decisions; silent Pack lock-in |
| Consumer | Requirements, ADRs, backlog, implementation, local policy | Expectation that AIOS owns product decisions |

### Existing versus proposed

| Topic | Existing today | Approved design in this contract | Future (not implemented) |
|-------|----------------|----------------------------------|--------------------------|
| Core identity docs | Present | Authoritative for framework intent | Continual refinement |
| `rules/` contents | Mixed generic + education | Education items are migration candidates, not permanent Core identity | Pack-based education rules after approved migration |
| Modules | Not populated; no `modules/` tree | Module Architecture Contract (Section 5); metadata field model in [`MODULE_METADATA.md`](MODULE_METADATA.md); adaptive recommend ≠ auto-apply | Populated modules, parsers/validators, catalog, tooling |
| Adaptive selection | Manual/human+agent judgment via docs | Architectural recommendation pipeline (Section 5) | Optional assisted discovery — not autonomous apply; engine needs separate approval |
| Content placement | Root `methodology/` active; root `workflows/` holds initial Core Workflow definitions (Phase 4 MVP); root `checklists/` holds initial Core Checklist definitions; root `knowledge/` / `skills/` still empty | Module-local assets by default; root shared only for genuine cross-cutting Core resources | Broader knowledge/skills population and further workflow/checklist content under later phases / explicit approval |
| Pack manifests | None required | Packs may later use an optional manifest; **not** mandatory in this contract | Evaluate `pack.yaml` need; schema deferred |

---

## 4. AIOS Core

### Responsibility

AIOS Core is the common, **technology-agnostic** engineering foundation every adoption path may rely on.

Core provides universal operating and governance defaults, cross-cutting engineering principles, shared conventions that genuinely apply across domains, and common framework-level capabilities.

Core **must not** become a container for every methodology, technology, workflow, or domain-specific resource. Capability-specific assets belong in Modules (or Packs when domain-specific). Root shared directories are reserved for genuinely cross-cutting Core resources.

### Core includes (conceptual)

- Generic agent operating guidance (`AGENTS.md`)
- Product and structure manifests (`MANIFEST.md`, `PROJECT_STRUCTURE.md`)
- Engineering methodologies under `methodology/` — **Core-owned reference content**, **L6 by default** (not automatically L4 binding rules)
- Syncable governance rules under `rules/` **as they exist today** (L4 operating/governance defaults in an AIOS adoption context, subject to L0–L3)
- Lightweight tooling entry point (`scripts/aiosctl.py`) — currently `sync` only
- Framework documentation such as this contract

### Core does not include

- Consumer product ADRs, roadmaps, or backlogs
- Full educational curricula or vocabulary databases as Core identity
- Claimed runtime engines that are only documentation
- Lock-in to one IDE, LLM, cloud, vendor agent, or language stack
- Automatic imposition of Modules or Packs
- Every specialized engineering capability that can live as a Module

### Current implementation note

`rules/` currently also contains education-oriented files used by historical synced consumers. They remain for compatibility. They are **not** permanent Core identity; see Section 12. This contract does not migrate them.

---

## 5. Module Architecture Contract

This section is the **Module Architecture Contract**. It defines conceptual architecture, boundaries, ownership, composition, content placement, adaptive recommendation rules, and constraints for Modules and Packs.

**Status:** Approved architectural design. **Not** an implemented Module catalog, metadata runtime, installer, resolver, or adaptive engine.

**Architectural ownership versus governance precedence:** This section answers *where things live and who owns them*. Section 7 answers *which instruction wins when guidance conflicts* (L0–L7). Ownership does not rewrite precedence; precedence does not move files or ownership.

### 5.1 Composition model

```text
Core          → common foundation (governance + cross-cutting principles)
Modules       → reusable engineering capabilities (optional, recommendable)
Packs         → optional domain / use-case extensions (may compose Modules)
Consumer      → product ownership, ADRs, local policy, implementation
```

- Core provides the foundation.
- Modules provide reusable engineering capabilities.
- Packs compose or contextualize Modules for specific domains or use cases.
- Consumers decide what to reference, adopt, or integrate.

A **Module must not depend on a specific Pack**. Pack-to-Module composition is supported **conceptually**; packaging and manifest mechanics are deferred.

### 5.2 Modules

A **Module** is a reusable, independently understandable engineering capability (for example Architecture, Development, Testing & Quality, Security Engineering, DevOps & Cloud, Data Engineering).

A Module:

- Has a clearly defined responsibility and scope.
- May contain knowledge, skills, workflows, checklists, templates, examples, and tests.
- Can be recommended based on project context.
- Is independent of any particular Pack.
- Must explain when it applies and when it should not be used.
- Must not silently impose architectural decisions on consumers.

**Governance:** Module guidance is **non-binding by default (L6)**. When a consumer **explicitly adopts** Module guidance into its own local policy, that adopted policy is **consumer-owned at L3** within the adoption scope. Adoption must not be assumed or performed silently by AIOS.

**Implementation status:** Modules are an approved architectural concept. No Module packages are populated by this document revision. No `modules/` tree is required to exist for this contract to be valid.

#### Illustrative Module layout (proposal only — not a shipped tree)

```text
modules/<module-id>/
├── module.yaml      # field model: MODULE_METADATA.md (no Module packages populated yet)
├── README.md        # human/agent entry point (expected when a Module exists)
├── knowledge/       # optional — Module-specific
├── skills/          # optional — Module-specific
├── workflows/       # optional — Module-specific
├── checklists/      # optional
├── templates/       # optional
├── examples/        # optional
└── tests/           # optional
```

Not every Module needs every directory. The approved **`module.yaml` field model** is defined in [`MODULE_METADATA.md`](MODULE_METADATA.md). Module **lifecycle and governance** are defined in [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md). **Future Module validation expectations** (layers, severities, CI fail-on-Error, sync separation) are defined in [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md) — not implemented as tooling by this contract. Phase 2.4 dependency and compatibility **design** is completed and embedded (see Section 5.9); machine-readable Module relationship metadata and catalog population remain deferred.

### 5.3 Packs

A **Pack** is an optional domain- or use-case-specific extension.

| Aspect | Definition |
|--------|------------|
| Purpose | Extend AIOS for a domain without forcing that domain into Core |
| Example | Education (`packs/education/`) |
| Adoption | Explicit opt-in by the consumer / project owner |
| May use Modules | Yes — a Pack may compose or reference one or more Modules |
| Status today | Partial — Education Pack README + preserved historical AGENTS |

A Pack:

- Provides contextual guidance for a particular domain or use case.
- May compose or reference Modules; must not duplicate reusable Module capabilities unnecessarily.
- Must not redefine Core governance or the L0–L7 model.
- Applies only when **explicitly adopted** by the consumer.

**Governance:** Explicitly adopted Pack guidance operates at **L5** within adopted scope and cannot override L0–L4. If a consumer further copies Pack guidance into its own local policy, that consumer-owned policy is **L3**. Pack presence in the AIOS repository does not activate the Pack for every consumer.

Packs are not required to use AIOS Core. Education content must not be automatically migrated into Core or Modules.

#### Optional Pack manifest (`pack.yaml`)

An optional Pack manifest may become useful later to declare identity, Module composition, and adoption hints. This contract **does not** require `pack.yaml`, does **not** define its schema, and does **not** authorize tooling that assumes a Pack manifest exists. Evaluate need in subsequent design work; keep Pack-to-Module composition valid with documentation-only references until then.

### 5.4 Consumer ownership

The consumer repository remains the owner of:

- Product requirements and decisions
- Approved ADRs
- Product architecture
- Implementation and source code
- Local engineering policies
- Roadmaps and project-specific artifacts

AIOS must not silently overwrite, replace, or modify consumer-owned decisions or artifacts.

AIOS provides reusable engineering guidance, not ownership of the consumer product. Synced `.agents/` files remain AIOS-derived artifacts; sync does not transfer ownership of consumer ADRs or product decisions (see Sections 7–9).

### 5.5 Content organization

Default architectural direction:

| Asset kind | Default placement |
|------------|-------------------|
| Module-specific knowledge | Inside the respective Module |
| Module-specific skills | Inside the respective Module |
| Module-specific workflows | Inside the respective Module |
| Cross-cutting resources that genuinely serve multiple Modules or the whole framework | Core / root shared directories |
| Root `methodology/` | **Core-owned** reference content; **L6 by default** |

This contract does **not** migrate existing root content, templates, prompts, or Education assets. Migration requires separate approval (Section 12).

### 5.6 Adaptive recommendation architecture

**Status:** Approved architectural model. **Not implemented** as an autonomous discovery, selection, installation, adoption, or consumer-modification engine.

Pipeline:

1. Analyze consumer / project context (goals, stack, architecture, requirements, maturity, constraints).
2. Identify relevant engineering needs.
3. Recommend applicable Modules or Packs.
4. Explain the recommendation, rationale, trade-offs, and when **not** to use it.
5. Request human / consumer-owner approval for durable adoption.
6. Record adoption in **consumer-owned** artifacts or policies (ADR or local policy).
7. Apply adopted guidance only within its approved scope (L3 for adopted Module policy; L5 for adopted Pack scope).

Keep recommendations proportional to actual need. Scale ceremony down for small or low-risk work.

| Allowed | Not allowed |
|---------|-------------|
| Analyze and recommend Modules/Packs | Automatically impose patterns, Modules, or Packs |
| Explain trade-offs and alternatives | Silently overwrite consumer ADRs or policies |
| Wait for owner approval before structural adoption | Autonomously restructure the consumer repository |
| Treat recommendations as L6 advice | Claim an implemented autonomous discovery/selection engine |
| Record adoption only after explicit consumer decision | Install or “apply” Modules via sync without a separate approved mechanism |

### 5.7 Architecture constraints

- Avoid unnecessary coupling between Modules.
- Avoid circular Module dependencies.
- Avoid Pack-specific Module implementations (a Module must remain usable without that Pack).
- Avoid duplicating Core operating/governance rules inside Modules.
- Avoid turning Core into a domain-specific content repository.
- Avoid mandatory adoption of Modules or Packs.
- Avoid IDE-, agent-, or LLM-vendor-specific architectural dependencies.
- Avoid premature runtime, resolver, installer, or package-manager assumptions.

Dependency versioning algorithms, compatibility matrices, and automated resolution tooling remain **out of scope** for this section. Phase 2.4 conceptual design is completed (Section 5.9); machine-readable relationship metadata and resolvers remain deferred future work.

### 5.8 Relationship to L0–L7

This Module Architecture Contract **does not change** the approved precedence model in Section 7.

| Level | Role relative to Modules / Packs |
|-------|----------------------------------|
| L0 | Non-overridable constraints — never overridden by Modules or Packs |
| L1 | Explicit user task instructions — within L0; do not silently rewrite durable consumer decisions |
| L2 | Consumer-approved ADRs / product decisions — outrank generic AIOS defaults |
| L3 | Consumer local policies — including **explicitly adopted** Module guidance |
| L4 | AIOS Core binding operating and governance defaults — not ordinary methodologies |
| L5 | Explicitly adopted Pack guidance — within scope only |
| L6 | Module and methodology recommendations **by default** |
| L7 | External knowledge — reference only |

### 5.9 Completed Phase 2 decisions versus deferred work

**Decided elsewhere (do not re-litigate here):**

- Approved Module metadata field model, required/optional fields, `status` / `maturity` enums, `requires_core`, deprecation object, and unknown-field warning policy — [`MODULE_METADATA.md`](MODULE_METADATA.md)
- Module lifecycle and governance (draft/active/deprecated expectations, maturity expectations, guidance-oriented SemVer, deprecation/migration, ownership outside metadata) — [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md)
- Module validation expectations (layers, severities, active minimums, `## Migration`, CI fail-on-Error, sync separation) — [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md)

**Phase 2.4 dependency and compatibility design — completed:**

- Conceptual design is **completed**. Do not describe Phase 2.4 design itself as still open or deferred.
- Metadata v1 has **no** Module-to-Module dependency fields; a `dependencies` key is **forbidden** (validation Error).
- Circular Module dependencies remain conceptually forbidden (Section 5.7).
- Pack-to-Module composition is **not** a Module dependency; Module-to-Pack dependencies remain **forbidden**.
- Companion recommendations remain README-only; required/optional dependency semantics are documented design decisions, not metadata v1 fields.
- No resolver, installer, or package-manager runtime exists or is authorized.
- A separate `MODULE_DEPENDENCY.md` is **intentionally not required**; decisions are embedded here and in Module Metadata / Validation docs.

**Still deferred (future work — distinct from completed Phase 2.4 design):**

- Machine-readable Module-to-Module relationship metadata and any additive metadata extension that would enable relationship graphs (until a concrete use case justifies Product Owner approval)
- Circular-dependency **tooling** checks that require such a machine-readable relationship graph
- Implementation of Module validators, schemas, CLI validate commands, or Module CI jobs (no Modules yet; sync unchanged)
- Actual Module catalog population (Phase 7)
- Pack manifest schema (`pack.yaml`)
- Adaptive engine implementation
- Migration of Education content or other existing resources

---

## 6. Knowledge, Skills, Agents, and Workflows

| Concept | Meaning | Owns | Does not own |
|---------|---------|------|--------------|
| **Knowledge** | Reference — **what** and **why** | Facts, concepts, rationale | Step-by-step execution |
| **Skill** | Actionable — **how** | Procedures | Multi-role orchestration |
| **Agent** | Role / responsibility profile | Duty boundaries | Product backlog ownership |
| **Workflow** | Multi-step process | Stages, gates, handoffs | Single atomic how-to |
| **Integration** | External tool/agent guidance | Compatibility notes | Replacing the external tool |
| **Template** | Artifact skeleton | Starting structure | Consumer-filled content |
| **Checklist** | Verification list | Review / Done gates | Architecture decisions |
| **Validation** | Contract conformance checks | Structure/contract checks | Claiming unrun tests as passed |

Authoring conventions for Workflow and Checklist **definitions** (Markdown-first metadata tables, lifecycle `draft` / `active` / `deprecated`, stage and checklist reference rules, definition-versus-instance boundary, and execution non-authority) are specified in [`WORKFLOW_CHECKLIST_CONVENTIONS.md`](WORKFLOW_CHECKLIST_CONVENTIONS.md). That document does not change the meanings in the table above and does not implement an execution engine.

### Related existing areas

| Area | Path | Status today |
|------|------|--------------|
| Methodologies | `methodology/` | Active |
| Agent operating manual | `AGENTS.md` | Active |
| Agent mode rules | `rules/AGENT_RULES.md` | Active (education-leaning content present) |
| Prompts | `prompts/` | Partial |
| Templates | `templates/` | Placeholder |
| Checklists | `checklists/` | Implemented (initial Core set: `review`, `release`; education-specific notebook checklist remains separate) |
| Workflows | `workflows/` | Implemented (Phase 4 MVP: Feature Development, Release) |
| Knowledge | `knowledge/` | Planned |
| Skills | `skills/` | Planned |
| Validation suite | `tests/` | Planned |
| Demo tests | `lab/aios-demo-api/` | Demo |

Default placement follows Section 5.5: Module-specific knowledge, skills and workflows live **inside Modules**; root shared directories hold only genuinely cross-cutting Core resources. Templates and checklists may live in shared root areas and/or inside Packs or Modules. They must not store consumer-specific filled documents.

Integrations today: README-level compatibility notes only. Dedicated adapters are not implemented.

Validation today: CI report + demo API tests — not a full framework contract validator. `aiosctl validate` is not implemented.

---

## 7. Consumer Ownership and Precedence

### Ownership table

| Concern | Owner |
|---------|-------|
| Product requirements | Consumer |
| ADRs and architecture decisions | Consumer |
| Roadmap and backlog | Consumer |
| Implementation and runtime systems | Consumer |
| Project-specific instructions and policies | Consumer |
| Generic governance and methodologies | AIOS |
| Optional packs / recommended modules | AIOS (source) + consumer (adoption choice) |
| Synced copies under consumer `.agents/` | AIOS (source for generated copies); consumer (whether to keep syncing) |

### Precedence (L0–L7)

This section defines the **authoritative architectural precedence model**.

Root [`AGENTS.md`](../AGENTS.md) §2 **operationalizes** this model for AI agents. Following Phase 1.4.1, the Contract and root AGENTS are **aligned**. They are complementary authorities (meta-document vs operating manual), not competing hierarchy levels.

Section 5 (Module Architecture Contract) defines **architectural ownership and placement**. This section defines **instruction precedence**. Do not conflate the two.

When guidance conflicts, apply:

#### L0 – Non-overridable constraints

Applicable **safety, legal, security, privacy, licensing and compliance** obligations, plus other justified non-overridable obligations where applicable.

These cannot be overridden by user instructions, consumer ADRs, local policies, AIOS Core, Packs, Modules or external knowledge.

Do **not** classify ordinary technical preferences or architectural recommendations as L0.

#### L1 – Explicit user instructions

Explicit instructions from the user for the current task.

Binding within L0. They do not silently amend durable consumer ADRs or local policies: disclose conflicts, obtain authorized confirmation, and record durable changes in consumer-owned artifacts.

#### L2 – Consumer-approved ADRs and product decisions

Explicitly approved consumer-specific architecture and product decisions.

These take precedence over generic AIOS defaults. Do not silently replace them.

#### L3 – Consumer local policies

Consumer-owned project instructions, repository policies and local engineering standards.

Binding within scope, subject to L0 and applicable L2.

#### L4 – AIOS Core binding defaults

AIOS Core operating instructions, governance rules and adopted engineering defaults.

Apply in an AIOS adoption context; **must not override L0–L3**.

#### L5 – Explicitly adopted Pack guidance

Domain- or use-case-specific Pack guidance.

Binding **only** within explicitly adopted scope. Cannot override L0–L4.

#### L6 – Module and methodology recommendations

Adaptive Module recommendations, skills, workflows and methodology guidance offered as advice.

**Recommendations by default**, not mandatory instructions.

Explicit consumer adoption of a Module recommendation as local policy moves that policy to **L3**.

#### L7 – External knowledge

External documentation, articles, examples and general knowledge.

Non-binding reference only.

### Conflict-resolution rules

1. Higher-level applicable constraints take precedence over lower-level instructions.
2. L0 constraints cannot be overridden.
3. Explicit user instructions govern the current task within L0 boundaries, but do not silently amend durable consumer decisions.
4. Consumer-approved ADRs and product decisions take precedence over generic AIOS defaults.
5. More specific or newer same-level decisions win only when the newer decision explicitly supersedes the older one or the relationship is otherwise unambiguous.
6. If same-level binding instructions conflict and no clear supersession exists, stop and ask the authorized decision owner.
7. Recommendations never silently override binding instructions.
8. AIOS-synced files in a consumer repository remain AIOS-derived artifacts. Sync does not give AIOS ownership of consumer ADRs or product decisions.
9. Document precedence (this section / `AGENTS.md` §2) and decision-quality priorities (`rules/DECISION_RULES.md`) are separate concepts.

### Historical note (dated context)

Before Phase 1.4.1, root `AGENTS.md` used an older instruction-priority list that could place some AIOS documents above consumer documents. That current-tension status is **resolved**: root `AGENTS.md` §2 now operationalizes this L0–L7 model. Retain this note only as historical context, not as an active discrepancy.

### Named repositories (classification only)

| Repository | Classification | Notes |
|------------|----------------|-------|
| GitHub-DevOps-Learning-Path | Legacy synced consumer | Historical `.agents/` sync; preserve artifacts; no ongoing AIOS integration required |
| Python3_Kurs | Not an active AIOS consumer | No verified integration; no planned AIOS integration |
| DigitalParentHub | Active reference-only consumer | Read-only overlay; consumer ADRs authoritative; AIOS must not write into or own its decisions |

Do not modify these repositories unless the product owner explicitly requests a separate consumer-side task.

---

## 8. Consumption Models

Supported models:

1. **Reference-only**
2. **Synced**
3. **Hybrid** = combination of (1) and (2), not a separate runtime or implementation engine

### Comparison

| Dimension | Reference-only | Synced |
|-----------|----------------|--------|
| Mechanism | Reference AIOS guidance without copying AIOS-managed files | Copy AIOS-managed artifacts under the sync contract |
| AIOS from consumer work | Read-only | Sync writes only to designated generated paths |
| Typical local AIOS material | Policy/feedback only | Generated `.agents/*.md` (today) |
| Update | Refresh AIOS reference (clone/pull) | Run `aiosctl sync` when desired |
| Example posture | DigitalParentHub | Legacy GitHub-DevOps-Learning-Path |

### Reference-only

- No requirement to copy Core files into the consumer.
- Consumer keeps full ownership of local policies and decisions.
- Mismatches should be captured on the consumer side and proposed to AIOS separately.

### Synced

- Selected AIOS-managed artifacts are copied into the consumer.
- Generated files are derived; manual edits conflict with future sync.
- Consumer product ADRs still govern product decisions.

### Hybrid

Reference-only guidance plus synced artifacts may coexist. That is still reference-only + synced, not a third engine.

---

## 9. Sync Compatibility Contract

Describes **existing** behavior of `scripts/aiosctl.py`. Do not break without an explicit migration plan.

### Implemented behavior

| Item | Current behavior |
|------|------------------|
| Command | `python scripts/aiosctl.py sync --project <path>` |
| Source | `rules/*.md` (flat glob only) |
| Destination | `<project>/.agents/` |
| Filenames | Basename preserved |
| Generated header | AUTO-GENERATED warning prepended |
| Change detection | SHA-256 over header + content; skip unless `--force` |
| Version marker | `<project>/.agents/AIOS_VERSION.md` (timestamp + source path) |
| Deleted source rules | Not auto-deleted from consumer `.agents/` |
| Project selection | `--project` only |
| `aiosctl.yaml` | Not read by the CLI |
| Extra flags | `--force`, `--dry-run` |

### Compatibility surface

- `rules/` top-level `*.md` source
- `.agents/` destination
- Existing rule basenames for legacy synced consumers
- Generated header semantics
- Non-deletion default for orphan destination files

### Not implemented

- Selective sync, pack sync, module sync
- Automatic pruning
- Semantic version pinning in `AIOS_VERSION.md`
- Reading `aiosctl.yaml`
- Adaptive module installation via sync

### Future sync evolution (proposal only)

Selective profiles, pack-aware sync, opt-in prune, richer version metadata — none implemented by this contract.

---

## 10. Versioning and Backward Compatibility

### Versioning terminology

| Term | Meaning | Current implementation | Future (proposed, not implemented) |
|------|---------|------------------------|------------------------------------|
| **AIOS Framework Version** | Version of the AIOS framework distribution / Core contract surface | Git tags/releases exist; docs may carry their own version fields; not a single enforced machine schema | Clear semver policy for Core + sync compatibility |
| **Module / Pack Version** | Version of an individual Module or Pack package | Not implemented as populated versioned packages | `module.yaml` / pack manifest versions |
| **Consumer Integration Version** | Record of what a consumer integrated and when | Partial: synced consumers get `AIOS_VERSION.md` (timestamp + source path only) | Richer pin of Framework / Module / Pack versions |

Do not treat these three as already fully implemented mechanisms.

### Compatibility principles

1. Breaking changes to sync paths, filenames, or artifact contracts require explicit migration planning.
2. Existing consumers must not be silently broken.
3. Automatic deletion of consumer artifacts must never be the default.
4. Separate Framework Version, Module/Pack Version, and Consumer Integration Version in documentation and tooling design.
5. Document versions, git tags, and sync metadata must not be conflated.

### Compatibility expectations

| Change type | Expectation |
|-------------|-------------|
| Additive Core docs | Compatible |
| Clarifying this contract without behavior change | Compatible |
| Renaming/moving synced rule basenames | Breaking — migration required |
| Changing `.agents/` destination | Breaking — migration required |
| Default prune | Disallowed |
| `rules/` subdirectories without flat mirror | Breaking for current glob — dual-publish or migration required |

---

## 11. Implementation Status Policy

| Status | Meaning |
|--------|---------|
| **implemented** / **active** | Present, usable, truthful for the claim |
| **partial** | Present but incomplete |
| **planned** | Intended; may exist as empty reservation |
| **placeholder** | Empty stub / reserved name |
| **demo** | Sample only (for example `lab/`) |

Rules:

- Do not present planned or placeholder items as implemented.
- Do not imply automated enforcement where only documentation exists.
- Adaptive module selection is an approved **design** principle, not an implemented selector service.
- When unsure, use the weaker status label.

`PROJECT_STRUCTURE.md` inventories actual paths. This contract defines vocabulary and meaning.

---

## 12. Migration and Deprecation Principles

1. Prefer dual-publish or shims before removing a synced surface.
2. Document consumer impact before migrations.
3. Provide a rollback path.
4. Require product-owner approval for sync-affecting migrations.
5. Deprecate before delete; never silently delete consumer-side derived artifacts by default.

### Education rules migration (process only)

Education-oriented files under `rules/` remain in the live sync source.

Migration to `packs/education/` requires: classification, compatibility analysis, dual-publish or explicit strategy, consumer impact assessment, rollback plan, and separate product-owner approval.

This contract does not move, rename, delete, or modify any file under `rules/`.

### Consumption relationship classes

- Legacy synced consumers may retain historical artifacts without ongoing integration.
- Active reference-only consumers keep consumer ADR authority.
- Non-integrated repositories are not AIOS consumers.

---

## 13. Non-Goals

- Owning consumer roadmaps, backlogs, or ADRs
- Imposing the same heavy architecture on every project
- Forcing microservices, DDD, CQRS, or similar patterns by default
- Autonomous modification of consumer repositories under the guise of “adaptive selection”
- Replacing coding agents or IDEs
- Shipping domain curricula as mandatory Core content
- Treating empty directories as completed subsystems
- Silent breaking changes to `aiosctl sync`
- Default automatic deletion of consumer `.agents/` files
- Claiming selective sync, pack sync, prune, semver pin, or adaptive auto-apply as current features

---

## 14. Future Evolution

Direction: [`../ROADMAP.md`](../ROADMAP.md). Expectations only:

| Theme | Expectation |
|-------|-------------|
| Contract maintenance | Update this file when boundaries change |
| `AGENTS.md` alignment | Keep §2 operationalization synchronized with this Section 7 L0–L7 model |
| Education migration | Only under Section 12 gates |
| Module Architecture Contract | Section 5 remains conceptual architecture; metadata / lifecycle / validation docs are referenced, not duplicated |
| Module metadata | Field model approved; parsers and real `module.yaml` files not implemented |
| Module lifecycle | Governance approved in [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md); no lifecycle automation implemented |
| Module validation | Expectations approved in [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md); no validator/CI/Module tooling implemented yet |
| Module deps / catalog / CLI | Phase 2.4 **design** completed (no metadata v1 deps; conceptual constraints binding); machine-readable relationship metadata deferred; catalog (7) and CLI (3) remain future work; sync preserved |
| Modules (implementation) | Populate later under approved contracts; keep adaptive recommend ≠ auto-apply; no autonomous selection engine unless separately approved and documented |
| CLI | Preserve sync; Module validation must stay separate from sync; add Module-aware commands only when implemented |
| Versioning | Formalize Framework / Module-Pack / Consumer Integration versions |
| Framework validation (Phase 8) | Broader automated contract tests may complement Module validation |

Always separate:

- **Existing implementation**
- **Approved design**
- **Future implementation**

---

## Component Responsibility Summary

| Component | Responsibility | Status today |
|-----------|----------------|--------------|
| AIOS Core | Common engineering foundation | Active (mixed rules legacy) |
| Packs | Optional domain/use-case extensions | Partial |
| Modules | Reusable engineering capabilities | Architecture approved (Section 5); metadata / lifecycle / validation docs approved; packages not populated |
| Adaptive selection | Context-based recommend/explain pipeline | Approved design; not automated; engine not implemented |
| Knowledge | What / why | Planned |
| Skills | How | Planned |
| Agents | Role profiles | Partial |
| Workflows | Multi-step processes | Implemented (Phase 4 MVP; RDIV remains methodology guidance) |
| Integrations | External tool guidance | Partial |
| Templates | Artifact skeletons | Placeholder |
| Checklists | Verification lists | Implemented (initial Core set; not an exhaustive catalog) |
| Module validation | Future Module checks | Expectations in [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md); not implemented |
| Framework validation | Contract / CI checks | Demo API CI today; broader tests planned (Phase 8) |

---

## Document Maintenance

Changes that alter boundaries, precedence, adaptive rules, or sync compatibility require:

- an update to this file
- consumer/contributor impact notes
- product-owner awareness for compatibility-sensitive changes

End of Framework Contract v1.4.0 (Module Architecture in §5; metadata, lifecycle, and validation expectations referenced via dedicated docs).
