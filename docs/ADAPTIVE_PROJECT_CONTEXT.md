# AIOS Adaptive Project Context

Version: 0.1.0

Status: Draft

Last Updated: 2026-11-03

Document type: Adaptive Project Intelligence design specification

This document defines the Core **Project Context** and **Task Context** models for AIOS Adaptive Project Intelligence.

It is subordinate to the Framework Contract for architecture and governance:

- Adaptive recommendation architecture: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.6
- Concept meanings and ownership: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5–§6
- Instruction precedence (L0–L7): [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7
- Agent operationalization: [`../AGENTS.md`](../AGENTS.md) (especially §4, §5, §7, §8)

This document is **conceptual design guidance**. It does not implement an adaptive runtime, discovery engine, parser, schema, API, or scoring system.

---

## 1. Purpose and Scope

### Purpose

Agents need a shared way to understand:

1. The **repository and engineering environment** (Project Context).
2. The **specific requested change or outcome** (Task Context).

These two models supply structured contextual inputs for later Adaptive Project Intelligence stages:

- Phase **6.3** — Complexity & Process Depth Model ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md))
- Phase **6.4** — Adaptive Guidance Model ([`ADAPTIVE_GUIDANCE_MODEL.md`](ADAPTIVE_GUIDANCE_MODEL.md))
- Phase **6.5** — Governance & Human Approval (interaction clarified there; existing gates already apply)
- Phase **6.6** — Reference Scenarios & Final Audit

### Scope

**In scope:**

- Conceptual definitions of Project Context and Task Context
- Information categories as possible signals (not a mandatory form)
- Evidence, inference, unknown, and conflict principles
- Mapping to existing AIOS documents and practices
- Core-only usability without populated Modules or Packs

**Out of scope:**

- Process Depth classification criteria, weights, scores, or transitions (Phase 6.3 — see [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md))
- Adaptive Guidance relevance, recommendation, and lifecycle concepts (Phase 6.4 — defined in [`ADAPTIVE_GUIDANCE_MODEL.md`](ADAPTIVE_GUIDANCE_MODEL.md); this document does **not** redefine them)
- New human-approval policies beyond referencing existing gates (Phase 6.5)
- Any executable engine, CLI, RAG, parser, or automated consumer modification

---

## 2. Architectural Positioning

| Anchor | Relationship |
|--------|----------------|
| [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.6 | Context assessment supports the first step of the adaptive recommendation pipeline (“analyze consumer / project context”). This document does **not** implement that pipeline as an engine. |
| [`../AGENTS.md`](../AGENTS.md) §4 | Project Context discovery foundation (Repository Intelligence). |
| [`../AGENTS.md`](../AGENTS.md) §5 | Task understanding and RDIV Review foundation. |
| [`../AGENTS.md`](../AGENTS.md) §7 | Adaptive Decision-Making — ceremony and recommendation posture; Process Depth criteria remain Phase 6.3. |
| [`../AGENTS.md`](../AGENTS.md) §8 | Human approval gates remain authoritative; Task Context may surface approval needs but does not grant approval. |

**Authority notes:**

- These models are **L6 design guidance** by default. They do **not** create a new governance precedence level.
- They do not replace Consumer ADRs (**L2**), adopted Consumer local policies (**L3**), or non-overridable **L0** constraints.
- **AI recommends; the human decides** ([`../methodology/ai_collaboration.md`](../methodology/ai_collaboration.md)).
- Context assessment does **not** authorize repository modification, Module/Pack adoption, or sync changes.

---

## 3. Terminology

| Term | Meaning |
|------|---------|
| **Lightweight Process Depth** | One of the four approved Process Depth levels (Lightweight, Standard, Enhanced, Critical). Criteria are defined in Phase 6.3 — not in this document. |
| **Lightweight Tooling** | Informal description of small or simple tools / tooling approaches (for example a focused CLI helper). **Not** a Process Depth level. |

These phrases share the word “Lightweight” but are **context-dependent** and must not be confused. The Process Depth level name **Lightweight** is retained; it is not renamed.

Other distinctions:

| Term | Meaning |
|------|---------|
| **Project Context** | Working model of the repository and engineering environment |
| **Task Context** | Working model of the specific requested change or outcome |
| **Process Depth** | Later ceremony/intensity level (Phase 6.3); not L0–L7 |
| **L0–L7** | Instruction precedence (Framework Contract §7 / [`../AGENTS.md`](../AGENTS.md) §2) |

---

## 4. Project Context

### Definition

**Project Context** is the working model of a **repository and its engineering environment**, built primarily from repository evidence.

It describes standing characteristics of the project, not the current user request.

### Information categories

Categories are **possible signals**, not mandatory fields. Agents gather proportionally to task need. The model is stack-agnostic and repository-type-agnostic. Repository types below are **illustrative only**.

#### 4.1 Purpose and audience

| Aspect | Guidance |
|--------|----------|
| **Represents** | Why the repository exists and who it serves |
| **Why it matters** | Prevents mismatched guidance and over-/under-ceremony |
| **Sources** | [`../AGENTS.md`](../AGENTS.md) §4; [`../methodology/repository_onboarding.md`](../methodology/repository_onboarding.md); README / product docs when present |
| **Importance** | **Essential** |
| **If missing / uncertain** | Ask or mark unknown; do not invent a product mission |

#### 4.2 Repository type

| Aspect | Guidance |
|--------|----------|
| **Represents** | Coarse shape (for example library, service, application, monorepo, documentation-only, infrastructure / DevOps) |
| **Why it matters** | Sets default expectations for structure and risk patterns |
| **Sources** | [`../ROADMAP.md`](../ROADMAP.md) Phase 6 project-type signals; repository layout evidence |
| **Importance** | **Conditional** — state only when evidence supports a label |
| **If missing / uncertain** | Prefer “unclassified” over a forced label |

#### 4.3 Structure and major components

| Aspect | Guidance |
|--------|----------|
| **Represents** | Directory layout, packages/modules, major subsystems, entry points |
| **Why it matters** | Locates where work and blast radius may land |
| **Sources** | [`../AGENTS.md`](../AGENTS.md) §4; [`../methodology/architecture_first.md`](../methodology/architecture_first.md); [`../skills/repository_analysis.md`](../skills/repository_analysis.md) |
| **Importance** | **Essential** for non-trivial work |
| **If missing / uncertain** | Limit claims to inspected paths; label assumptions |

#### 4.4 Technology stack and tooling

| Aspect | Guidance |
|--------|----------|
| **Represents** | Observed languages, frameworks, build and package tooling |
| **Why it matters** | Grounds analysis in actual stack without mandating any stack |
| **Sources** | [`../AGENTS.md`](../AGENTS.md) §4; [`../skills/repository_analysis.md`](../skills/repository_analysis.md) technology inventory |
| **Importance** | **Essential** when code or build artifacts change |
| **If missing / uncertain** | List only observed manifests; do not install packages to “discover” |

#### 4.5 Architecture and boundaries

| Aspect | Guidance |
|--------|----------|
| **Represents** | Architectural style (when evidenced), component responsibilities, API/integration boundaries |
| **Why it matters** | Preserves Architecture First and avoids parallel designs |
| **Sources** | [`../methodology/architecture_first.md`](../methodology/architecture_first.md); [`../skills/repository_analysis.md`](../skills/repository_analysis.md); Consumer ADRs when present |
| **Importance** | **Conditional** |
| **If missing / uncertain** | Infer cautiously and label as inference; do not force a style name |

#### 4.6 Conventions and practices

| Aspect | Guidance |
|--------|----------|
| **Represents** | Naming, patterns, local engineering standards |
| **Why it matters** | Consistency over novelty ([`../AGENTS.md`](../AGENTS.md) §3) |
| **Sources** | [`../AGENTS.md`](../AGENTS.md); Consumer local policies; existing code patterns |
| **Importance** | **Conditional** |
| **If missing / uncertain** | Prefer extending evident patterns; do not invent new conventions |

#### 4.7 Build, test, and validation

| Aspect | Guidance |
|--------|----------|
| **Represents** | How the project builds and checks quality |
| **Why it matters** | Informs later verification expectations |
| **Sources** | [`../AGENTS.md`](../AGENTS.md) §4; [`../skills/repository_analysis.md`](../skills/repository_analysis.md) quality/testing step |
| **Importance** | **Conditional** |
| **If missing / uncertain** | State “not found”; do not claim tests were run |

#### 4.8 CI/CD and operations

| Aspect | Guidance |
|--------|----------|
| **Represents** | Pipeline and operational configuration artifacts when present |
| **Why it matters** | Delivery and operational impact of changes |
| **Sources** | CI configs; [`../skills/repository_analysis.md`](../skills/repository_analysis.md) |
| **Importance** | **Optional** unless the task touches delivery/ops |
| **If missing / uncertain** | Mark unavailable |

#### 4.9 Security, privacy, compliance, and operational constraints

| Aspect | Guidance |
|--------|----------|
| **Represents** | Constraints that may include L0-relevant obligations |
| **Why it matters** | Safety and lawful operation; never invent L0 |
| **Sources** | [`../AGENTS.md`](../AGENTS.md) §2 L0; Consumer policies; Skill risk “review areas” practice |
| **Importance** | **Conditional** |
| **If missing / uncertain** | Escalate unknowns; do not claim “secure” without evidence |

#### 4.10 ADRs and durable consumer decisions

| Aspect | Guidance |
|--------|----------|
| **Represents** | Approved Consumer ADRs and durable product/architecture decisions (**L2**), and adopted local policies (**L3**) when present |
| **Why it matters** | Outrank generic AIOS defaults |
| **Sources** | [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.4; [`../AGENTS.md`](../AGENTS.md) §2 |
| **Importance** | **Essential when present** |
| **If missing / uncertain** | Search; if absent, state absence — do not invent ADRs |

#### 4.11 Available Core guidance

| Aspect | Guidance |
|--------|----------|
| **Represents** | Which Core Workflows, Checklists, Skills, and Methodologies exist **in this checkout** |
| **Why it matters** | Enables Core-only adaptive usefulness without Modules/Packs |
| **Sources** | [`../PROJECT_STRUCTURE.md`](../PROJECT_STRUCTURE.md); [`../AGENTS.md`](../AGENTS.md) §4 empty-directory honesty rule |
| **Importance** | **Essential** |
| **If missing / uncertain** | Do not pretend empty or absent directories are populated |

---

## 5. Task Context

### Definition

**Task Context** is the working model of the **specific requested change or outcome**.

It is distinct from Project Context. Repository size or standing “criticality” is not the same as task complexity or Process Depth.

Task Context does **not** create automatic approval.

### Information categories

#### 5.1 Requested outcome

| Aspect | Guidance |
|--------|----------|
| **Represents** | What success looks like for this request |
| **Why it matters** | Anchors scope and verification |
| **Sources** | [`../AGENTS.md`](../AGENTS.md) §5; [`../methodology/rdiv.md`](../methodology/rdiv.md); [`../workflows/feature_development.md`](../workflows/feature_development.md) Stage 1 |
| **Importance** | **Essential** |
| **If missing / uncertain** | Restate and confirm with the requester |

#### 5.2 Task type

| Aspect | Guidance |
|--------|----------|
| **Represents** | Coarse kind of work (for example fix, feature, refactor, docs, release, investigation) — illustrative labels only |
| **Why it matters** | Helps later guidance selection (Phase 6.4) |
| **Sources** | Feature Development / Release workflows |
| **Importance** | **Conditional** |
| **If missing / uncertain** | Use a plain-language description; do not force a taxonomy |

#### 5.3 Scope and affected components

| Aspect | Guidance |
|--------|----------|
| **Represents** | In-scope / out-of-scope boundaries and touched areas |
| **Why it matters** | Minimal change; prevents silent expansion |
| **Sources** | [`../workflows/feature_development.md`](../workflows/feature_development.md) Stage 1; [`../AGENTS.md`](../AGENTS.md) §4 in-scope questions |
| **Importance** | **Essential** |
| **If missing / uncertain** | Ask; refuse silent scope growth |

#### 5.4 Complexity

| Aspect | Guidance |
|--------|----------|
| **Represents** | Inherent difficulty of **this task** (not repository size) |
| **Why it matters** | Input to Process Depth (Phase 6.3) |
| **Sources** | Feature Development light vs required stage classifications |
| **Importance** | **Conditional** |
| **If missing / uncertain** | Separate explicitly from Project Context size; label uncertainty |

#### 5.5 Impact and blast radius

| Aspect | Guidance |
|--------|----------|
| **Represents** | What could break or who is affected if the change fails |
| **Why it matters** | Risk-proportional ceremony |
| **Sources** | [`../AGENTS.md`](../AGENTS.md) §4 “What would break”; Feature Development risk notes |
| **Importance** | **Essential** for non-trivial work |
| **If missing / uncertain** | State assumptions; do not minimize without evidence |

#### 5.6 Technical and operational risk

| Aspect | Guidance |
|--------|----------|
| **Represents** | Failure modes involving contracts, data, security, ops, irreversible actions |
| **Why it matters** | May intersect [`../AGENTS.md`](../AGENTS.md) §8 approval-listed operations |
| **Sources** | RDIV Review; AGENTS §8 |
| **Importance** | **Essential** when §8-adjacent or high impact |
| **If missing / uncertain** | Stop and ask before risky operations |

#### 5.7 Uncertainty and missing information

| Aspect | Guidance |
|--------|----------|
| **Represents** | Known unknowns that block safe progress |
| **Why it matters** | Prevents guessing ([`../AGENTS.md`](../AGENTS.md) §3) |
| **Sources** | AGENTS; [`../skills/repository_analysis.md`](../skills/repository_analysis.md) uncertainty handling |
| **Importance** | **Essential** |
| **If missing / uncertain** | Narrow scope, ask, or defer — do not invent |

#### 5.8 Compatibility and backward compatibility

| Aspect | Guidance |
|--------|----------|
| **Represents** | Public contracts, data compatibility, sync/consumer expectations |
| **Why it matters** | Protects consumers and durable interfaces |
| **Sources** | Architecture First; Framework Contract sync/compatibility notes |
| **Importance** | **Conditional** |
| **If missing / uncertain** | Treat unknown public-contract impact as elevated uncertainty |

#### 5.9 Dependencies and constraints

| Aspect | Guidance |
|--------|----------|
| **Represents** | Blockers, sequencing, environment or policy limits |
| **Why it matters** | Feasible planning |
| **Sources** | Feature Development planning stages; onboarding strategy steps |
| **Importance** | **Conditional** |
| **If missing / uncertain** | List unknowns explicitly |

#### 5.10 Urgency and delivery constraints

| Aspect | Guidance |
|--------|----------|
| **Represents** | Explicit time box or delivery constraint **when stated** |
| **Why it matters** | May affect scheduling and communication — **not** authority |
| **Sources** | Explicit user instructions (**L1**) |
| **Importance** | **Optional** |
| **If missing / uncertain** | Ignore if unstated. **Urgency must never waive L0 constraints or AGENTS §8 approval gates.** |

#### 5.11 Explicit user instructions and approval requirements

| Aspect | Guidance |
|--------|----------|
| **Represents** | Stated L1 instructions; known need for human/owner confirmation |
| **Why it matters** | Authority and conflict handling |
| **Sources** | [`../AGENTS.md`](../AGENTS.md) §2 L1; §8 |
| **Importance** | **Essential when present** |
| **If missing / uncertain** | Surface conflicts with standards/ADRs; do not silently override durable decisions |

---

## 6. Relationship Between Project Context and Task Context

### Why they are separate

| Dimension | Project Context | Task Context |
|-----------|-----------------|--------------|
| **Describes** | Repository / environment | This request / change |
| **Lifetime** | Relatively stable across tasks | Per request |
| **Changes when** | Repo structure, stack, policies change | User asks for different work |

Mixing them hides whether ceremony is driven by standing environment or by the current change.

### Complementarity

- Project Context without Task Context cannot judge **this** change’s blast radius or approval needs.
- Task Context without Project Context risks ignoring architecture, ADRs, and existing patterns.

Both are required inputs for later adaptive decisions.

### Combined use (conceptual — not an executable pipeline)

```text
Project Context  ──┐
                   ├──► Phase 6.3 Process Depth consideration
Task Context     ──┘              │   ([PROCESS_DEPTH_MODEL.md])
                                  └──► Phase 6.4 Adaptive Guidance recommendations
                                         ([ADAPTIVE_GUIDANCE_MODEL.md] —
                                          explainable relevance recommendations;
                                          not an automatic selection engine)
```

### Missing information and conflicts

- Prefer repository evidence for Project Context facts.
- Prefer explicit requester/owner instructions (within L0) for Task intent.
- When docs conflict with code or policies, report both with paths; ask when decision-critical.
- Label unknowns; do not invent facts to complete a template.

---

## 7. Context Assessment Principles

1. **Evidence-based** — Prefer repository and request evidence over assumptions ([`../AGENTS.md`](../AGENTS.md) §4).
2. **Proportional gathering** — Match discovery depth to task need; trivial work needs less Project Context rebuild.
3. **No mandatory full form** — Categories are signals, not a required questionnaire for every task.
4. **Reuse existing knowledge** — Reuse prior accurate Project Context in the same engagement when still valid.
5. **Avoid duplicate discovery** — Do not re-run full repository analysis when scope is already clear and evidence is fresh enough.
6. **Explicit uncertainty** — Distinguish fact, inference, unknown, and conflict (see below).
7. **Preserve consumer decisions** — ADRs and local policies remain authoritative in their scope.
8. **Core-only usability** — Context assessment and later recommendations must work using Core Workflows, Checklists, Skills, and Methodologies without populated Modules or Packs.
9. **Descriptive input only** — Context models do not authorize modifying the repository, adopting Modules/Packs, or changing sync behavior.

### Evidence labels

| Label | Meaning |
|-------|---------|
| **Verified fact** | Directly observed (path, config, ADR text, CI file, explicit user text) |
| **Reasonable inference** | Interpretation of evidence; uncertainty stated |
| **Unknown / unavailable** | Not inspected or not present |
| **Conflicting** | Sources disagree; report both |

Cite relevant file paths, and line references or ranges when available and useful; never invent line numbers ([`../skills/repository_analysis.md`](../skills/repository_analysis.md) evidence rules).

---

## 8. Relationship With Existing AIOS Components

| Component | Relationship to context |
|-----------|-------------------------|
| [`../AGENTS.md`](../AGENTS.md) §4 | Project Context discovery foundation |
| [`../AGENTS.md`](../AGENTS.md) §5 / [`../methodology/rdiv.md`](../methodology/rdiv.md) | Task Context and joint Review foundation |
| [`../skills/repository_analysis.md`](../skills/repository_analysis.md) | Optional/recommended Skill (**how**) for systematic repository evidence — not auto-executed |
| [`../methodology/repository_onboarding.md`](../methodology/repository_onboarding.md) | Project discovery methodology |
| [`../methodology/architecture_first.md`](../methodology/architecture_first.md) | Architecture understanding within Project Context |
| [`../methodology/ai_collaboration.md`](../methodology/ai_collaboration.md) | AI recommends; human decides |
| [`../workflows/feature_development.md`](../workflows/feature_development.md) | Task scope and lifecycle stages; light paths remain Workflow-owned |
| [`../workflows/release.md`](../workflows/release.md) | Task-type path when the request is a release |
| [`../checklists/review.md`](../checklists/review.md) | Verification aid after change — not a context builder |
| [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.6 | Context feeds adaptive recommendation design; no engine claimed here |
| Consumer ADRs and local policies | Authoritative constraints (L2 / adopted L3) inside Project and Task Context |
| Module metadata (`applies_when` / `avoid_when`) | Optional future enrichment when Module packages exist — **not required** for this model |
| Packs | Optional domain enrichment when explicitly adopted (**L5**) — **not required** |

This document **links**; it does not duplicate methodology, Workflow, Checklist, or Skill bodies.

---

## 9. Relationship to Process Depth

Approved Process Depth level **names** (criteria deferred to Phase 6.3):

1. **Lightweight** (Lightweight Process Depth)
2. **Standard**
3. **Enhanced**
4. **Critical**

Project Context and Task Context are **inputs** to Phase 6.3. This document does **not** define:

- Level-specific criteria
- Weights, scores, or thresholds
- Classification formulas
- Automatic escalation or de-escalation rules

**Important:** A repository’s general criticality or size does **not** automatically make every small task a **Critical** Process Depth task. Process Depth is **not** the L0–L7 precedence model; L0 still always applies.

---

## 10. Governance and Consumer Ownership

Preserved without change by this document:

- L0–L7 instruction precedence ([`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7; [`../AGENTS.md`](../AGENTS.md) §2)
- Consumer ownership of ADRs, product decisions, implementation, and local policy
- Human approval gates in [`../AGENTS.md`](../AGENTS.md) §8
- No silent Module/Pack adoption or consumer policy rewrite
- No automatic Module/Pack installation
- AI recommends; the human decides

Context models:

- Do **not** override existing governance
- Do **not** introduce new precedence levels
- Do **not** replace Consumer decisions with AIOS defaults

---

## 11. Non-Goals and Future Boundaries

This document does **not** establish or claim:

- An adaptive runtime / recommendation engine
- Automated repository discovery engine
- Numerical scoring or machine-learning classification
- Context parsers, machine schemas, APIs, or executable models
- Skill execution engine
- Workflow orchestration engine
- Knowledge retrieval / RAG
- Adaptive CLI commands
- Module/Pack catalog implementation
- Automatic consumer repository modifications
- Changes to `aiosctl sync` behavior

Future Phase 6 stages may extend related design. Implementation capabilities require separate Product Owner approval and delivery.

---

## 12. Document Maintenance

- This is a **Core** Adaptive Project Intelligence **design** document (`draft`).
- Changes must remain consistent with [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) and must not invent new governance levels.
- Related Stage 6.3+ documents ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md), [`ADAPTIVE_GUIDANCE_MODEL.md`](ADAPTIVE_GUIDANCE_MODEL.md)) should **reference** this file for Project Context and Task Context definitions rather than redefining them.
- Do not claim runtime or tooling delivery based on this document alone.

End of Adaptive Project Context v0.1.0 (`draft`).
