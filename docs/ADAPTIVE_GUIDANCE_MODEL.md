# AIOS Adaptive Guidance Model

Version: 0.1.0

Status: Draft

Last Updated: 2026-11-03

Document type: Adaptive Project Intelligence design specification

This document defines the Core **Adaptive Guidance Model** for AIOS Adaptive Project Intelligence.

It is subordinate to the Framework Contract for architecture and governance:

- Adaptive recommendation architecture: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.6
- Concept meanings and ownership: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5–§6
- Instruction precedence (L0–L7): [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7
- Agent operationalization: [`../AGENTS.md`](../AGENTS.md) (especially §2, §4, §5, §7, §8)
- Project Context and Task Context: [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md)
- Complexity Dimensions and Process Depth: [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md)

This document is **conceptual design guidance**. It does not implement an adaptive runtime, discovery engine, parser, schema, API, scoring system, registry, resolver, or autonomous classifier.

**Normative language:** In this document, **MUST**, **MUST NOT**, **SHOULD**, and **MAY** indicate requirements and recommendations for agents and authors applying this model. They do not create new L0–L7 levels or replace the Framework Contract.

---

## 1. Purpose and Scope

### Purpose

Provide a shared, explainable way for agents and humans to:

1. Identify **relevant** guidance artifacts for a specific task.
2. Qualify **usage intensity** using an already recommended Process Depth level.
3. Present recommendations for **Human Acceptance** without conflating acceptance with Consumer Adoption or AGENTS.md §8 authorization.
4. Keep AIOS Core usable **without** mandatory Modules or Packs.

### In scope

- Conceptual Adaptive Guidance model and boundaries
- Exactly six canonical Guidance Types
- Supporting resources (Prompt, Knowledge)
- Context integration and Core-first discovery order
- Process Depth intensity integration (without redefining Process Depth)
- Explainable recommendation presentation (not a metadata schema)
- Recommendation / Human Acceptance / Consumer Adoption lifecycle
- Pack versus Module adoption boundaries
- Binding versus advisory treatment under L0–L7
- Core / Module / Pack / Consumer boundaries
- Ecosystem provenance principles (conceptual)
- Illustrative reference scenarios

### Out of scope

- Adaptive runtime / recommendation engine
- Guidance registry or resolver
- New common metadata schema; mandatory `applies_when` / `avoid_when` for all types
- Numerical scoring, ranking formulas, or machine-learning classification
- Automatic Module/Pack discovery, installation, or adoption
- Skill, Workflow, or Checklist execution engines
- Knowledge retrieval / RAG
- Adaptive CLI
- Automatic Consumer repository modification
- Changes to `aiosctl sync`
- Changes to AGENTS.md §8 approval authority
- Amendments to [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.6 (deferred; see §16)
- Redefinition of Process Depth levels, D1–D12, or Feature Development Workflow stage eligibility ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §5)

### Relationship to existing contracts

| Concern | Authority |
|---------|-----------|
| L0–L7 precedence | [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7; [`../AGENTS.md`](../AGENTS.md) §2 |
| Concept meanings (Workflow, Checklist, Skill, …) | [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §6 |
| Module / Pack architecture | [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5 |
| Project / Task Context | [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md) |
| Process Depth | [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) |
| Adaptive Guidance (this document) | Conceptual extension for relevance, intensity notes, and lifecycle — **MUST NOT** weaken the rows above |

---

## 2. Architectural Principles

1. **Framework ≠ content** — AIOS provides reusable guidance; Consumers own product decisions and implementation ([`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §2, §5.4).
2. **AI recommends; humans decide** — for **advisory** guidance ([`../methodology/ai_collaboration.md`](../methodology/ai_collaboration.md); [`../AGENTS.md`](../AGENTS.md) §7).
3. **Binding constraints remain binding** — L0–L4 (and adopted L5 within scope) **MUST NOT** be presented as ordinary optional recommendations.
4. **Evidence over invention** — missing information and unknown provenance **MUST** remain visible ([`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md) §7).
5. **Proportional ceremony** — recommendations **SHOULD** scale to actual need ([`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.6).
6. **Separate concerns** — ownership ≠ precedence ≠ recommendation ≠ acceptance ≠ adoption ≠ AGENTS.md §8 authorization.
7. **No silent elevation or downgrade** — Core origin **MUST NOT** elevate L6 to L4; Recommendation **MUST NOT** downgrade L4 to L6; Acceptance **MUST NOT** create L5 for a Pack.
8. **Independence** — Core **MUST** remain usable without Modules or Packs; Modules **MUST NOT** depend on a specific Pack; Pack adoption **MUST NOT** silently adopt Modules ([`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §3, §5).
9. **Provenance ≠ suitability** — Official does not mean automatically suitable; Community does not mean automatically untrusted.
10. **Design-only pipeline** — the flows in this document are conceptual; they are not an executable engine.

---

## 3. Adaptive Guidance Conceptual Model

### Definition

**Adaptive Guidance** is the discipline of determining which **advisory** guidance artifacts are **relevant** to a task, explaining why, and qualifying **how intensely** they **SHOULD** be used given a recommended Process Depth — while continuously respecting **binding** instructions under L0–L7.

### Conceptual pipeline

```text
Binding constraints (L0–L4; Consumer L2/L3; adopted L5 within scope)
        │  (always apply; not optional recommendations)
        ▼
Project Context + Task Context
        → Complexity Dimensions → Process Depth recommendation   [intensity]
        → Adaptive Guidance recommendations                      [relevance + intensity notes]
              → Human Acceptance (advisory, current task)
              → Consumer Adoption (optional, Consumer-owned)
```

This pipeline is conceptual. It is not an executable engine. It aligns with [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md) §6 and [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §7.

### Four-layer position

| Layer | Role in Adaptive Guidance |
|-------|---------------------------|
| **Core** | Baseline discovery source for cross-cutting advisory guidance; also source of binding L4 operating/governance defaults |
| **Modules** | Optional capability guidance when present and relevant |
| **Packs** | Optional domain guidance; L5 only after explicit Consumer Adoption |
| **Consumer** | Owns Acceptance (authorized human), Adoption, ADRs, local policy, and implementation |

---

## 4. Six Guidance Types

Exactly **six** canonical Guidance Types. Meanings remain as in [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §6 and related conventions.

| Type | Responsibility | Default authority |
|------|----------------|-------------------|
| **Workflow** | Multi-step process: stages, gates, handoffs | **L6** recommendation |
| **Checklist** | Verification list at review / done gates | **L6** recommendation |
| **Skill** | Actionable reusable capability (**how**) | **L6** recommendation |
| **Methodology** | Engineering approach and principles | **L6** recommendation |
| **Module** | Reusable engineering capability package | **L6**; explicit Consumer adoption into local policy → **L3** within adoption scope |
| **Pack** | Optional domain / use-case extension | **Not adopted → L6** advisory; **explicitly adopted → L5** within approved Pack scope |

### Combined recommendations

Agents **MAY** recommend multiple Guidance Types for one task. Types **MUST NOT** be merged into a single undifferentiated blob. Example pattern: Methodology (`rdiv`) + Workflow (`feature-development`) + Checklist (`review`) + Skill (`repository-analysis`) — linked, not fused.

Workflows **MAY** reference Skills and Checklists by id/link. Skills **MUST NOT** become multi-stage Workflow substitutes. Checklists **MUST NOT** replace architecture decisions or operational authorization.

Placement conventions remain in [`WORKFLOW_CHECKLIST_CONVENTIONS.md`](WORKFLOW_CHECKLIST_CONVENTIONS.md) and [`SKILL_KNOWLEDGE_CONVENTIONS.md`](SKILL_KNOWLEDGE_CONVENTIONS.md). Module-local assets apply when Module packages exist ([`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.5).

### Education-specific guidance

Artifacts such as [`../checklists/notebook_creation.md`](../checklists/notebook_creation.md) **MUST NOT** be recommended as general Core guidance solely because they exist in the repository. Education context **MUST** be established first. Historical Education Pack material (for example [`../packs/education/AGENTS.education.md`](../packs/education/AGENTS.education.md)) **MUST NOT** be treated as automatically adopted or active for every Consumer ([`../packs/education/README.md`](../packs/education/README.md)).

---

## 5. Supporting Resources: Prompt and Knowledge

**Prompt** and **Knowledge** are **supporting resources**, not independent canonical Guidance Types.

| Resource | Role | MUST NOT |
|----------|------|----------|
| **Prompt** | Interaction-specific prompt artifact; **MAY** be referenced by Skills, Workflows, Methodologies, Modules, or Packs | Be listed as a seventh Guidance Type; replace Skill as the canonical reusable capability ([`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §6; [`SKILL_KNOWLEDGE_CONVENTIONS.md`](SKILL_KNOWLEDGE_CONVENTIONS.md)) |
| **Knowledge** | Reference material (**what** / **why**); **MAY** support recommendations across the six Guidance Types | Be treated as a seventh Guidance Type in this model; become a disguised Skill or Workflow |

Reconsidering Knowledge as an independent Guidance Type requires future real Knowledge artifacts, a clear recommendation need, and a separate Product Owner decision. Root `knowledge/` may be empty; agents **MUST NOT** invent Knowledge content ([`../PROJECT_STRUCTURE.md`](../PROJECT_STRUCTURE.md)).

---

## 6. Context Integration and Core-first Discovery

### Inputs

| Input | Role |
|-------|------|
| **Task Context** | **Primary relevance driver** — outcome, task type, scope, impact, risk, uncertainty ([`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md) §5) |
| **Project Context** | Constraints and project-specific information — structure, stack, ADRs, available Core guidance ([`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md) §4) |
| **Consumer ADRs (L2) and local policies (L3)** | **Binding constraints throughout** recommendation — not a late optional layer |
| **Existing artifact definitions** | Purpose, when to use / not use, status/version when present |
| **Modules / Packs** | Only when present, known, and relevant — **MUST NOT** be invented |

### Core-first discovery (order, not precedence)

**Core-first** means agents **SHOULD** begin by considering cross-cutting Core advisory guidance available in the checkout (Workflows, Checklists, Skills, Methodologies), because Core **MUST** remain usable without Modules or Packs.

Core-first **MUST NOT** be interpreted as:

- Giving Core advisory guidance precedence over Consumer L2/L3 decisions
- Elevating Core L6 artifacts to L4
- Skipping applicable L0–L4 (and adopted L5) constraints

### Relevance versus authorization

| Concept | Meaning |
|---------|---------|
| **Relevance** | This advisory artifact appears useful for this task |
| **Authorization** | Permission to perform durable or operational actions (Consumer authority; AGENTS.md §8; adopted policy) |

Relevance **MUST NOT** be treated as operational authorization, Consumer Adoption, or AGENTS.md §8 approval.

---

## 7. Process Depth Integration

Authoritative Process Depth definitions remain in [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md). This document **MUST NOT** redefine Lightweight, Standard, Enhanced, or Critical levels, D1–D12, or Feature Development Workflow stage classifications.

| Concern | Owner |
|---------|--------|
| Process Depth recommendation (ceremony intensity) | [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) |
| Guidance Type / artifact **relevance** | This Adaptive Guidance Model (Task Context primary; Project Context constrains) |
| Feature Development Required / Light / Skip | [`../workflows/feature_development.md`](../workflows/feature_development.md) |
| Mandatory approvals | [`../AGENTS.md`](../AGENTS.md) §8 and applicable Consumer policy |

**Rules:**

- Process Depth **MUST** affect **usage intensity** of relevant guidance only.
- Process Depth **MUST NOT** select Guidance Types or artifacts by itself.
- Process Depth **MUST NOT** override Workflow eligibility or invent new Required stages ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §5.1, §5.7).
- Process Depth **MUST NOT** be equated with Release class ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §5.2).

Illustrative intensity pattern for the **same** relevant Workflow: Lightweight → minimal proportional use; Standard → meaningful depth; Enhanced → deeper analysis/verification; Critical → maximum proportional ceremony — without changing which stages the Workflow requires.

---

## 8. Explainable Recommendation Model

Recommendations **MUST** be explainable. The following is a **conceptual presentation model**, not a mandatory metadata schema, registry field set, or machine-readable contract.

### Conceptual fields

| Field | Expectation |
|-------|-------------|
| Identity (id, title, path when known) | Essential for recommended artifacts |
| Guidance type | Essential (one of the six types) |
| Relevance to this task | Essential |
| Rationale | Essential |
| Supporting evidence | Essential when available; otherwise state unknown / not inspected |
| Usage intensity | Essential when a Process Depth level has been recommended |
| Maturity / status / version | Conditional — if absent, state **not stated** |
| Limitations / when not to use | Essential when present in the artifact |
| Ownership / adoption implications | Essential for Module and Pack; conditional for Core L6 |
| Provenance | Show when known; otherwise **explicitly unknown** |
| Trust / verification | Optional and separate from provenance |
| Missing information | Essential when gaps exist |
| Alternatives / when not to use this recommendation | Conditional |
| Authority class | Essential distinction — see below |

### Authority class in presentations

| Authority class | How to present |
|-----------------|----------------|
| **Advisory (L6)** | Suitable for Recommendation and Human Acceptance |
| **Adopted Pack (L5)** | Binding within approved scope — **MUST NOT** be offered for recurring task-level Accept/Reject |
| **Binding (L0–L4; applicable L2/L3)** | Constraint / obligation note — **MUST NOT** be labeled as an ordinary optional recommendation |

**MUST NOT** treat “located in Core” as proof of L4. **MUST NOT** treat “recommended” as Accepted, Adopted, §8-approved, or L5.

Agents **MUST NOT** invent missing metadata or present assumptions as established facts. Numerical ranking formulas **MUST NOT** be introduced by this model; when multiple advisory items are listed, qualitative ordering rationale **MAY** be stated in prose.

---

## 9. Recommendation, Human Acceptance and Consumer Adoption

Three **distinct** lifecycle stages. They **MUST NOT** be collapsed into one operation.

```text
Recommendation → Human Acceptance → Consumer Adoption
        ≠ binding L0–L4 / adopted L5 / Consumer L2–L3
        ≠ AGENTS.md §8 approval gates
        ≠ licensing / access / entitlement / purchase / distribution rights
```

### 9.1 Recommendation

| Aspect | Rule |
|--------|------|
| **Owner** | AIOS agent applying this model |
| **Meaning** | Identify and explain potentially relevant **advisory** guidance |
| **Typical authority** | L6 (including not-yet-adopted Packs) |
| **Authorizes** | Nothing beyond presenting advice |
| **MUST NOT** | Downgrade L4 (or adopted L5) to optional advice; install Modules/Packs; modify the Consumer repository; grant §8 approval; grant licensing, access, purchase, entitlement, or distribution rights |

### 9.2 Human Acceptance

| Aspect | Rule |
|--------|------|
| **Owner** | Authorized human for the current task |
| **Meaning** | Decision to **use** recommended **advisory** guidance for **this task** (accept / reject / defer / clarify) |
| **Applies to** | L6 Core guidance; L6 Module recommendations; L6 recommendations for Packs **not yet adopted** |
| **MUST NOT apply as recurring approval** | Binding L4 rules; already adopted L5 Pack guidance within scope |
| **Authorizes** | Task-level use of accepted advisory guidance within existing task authorization |
| **MUST NOT authorize** | Repository modifications beyond existing task authorization; durable Consumer ADR/policy changes; breaking changes or contract modifications; commit, push, release, publish, or deploy; any AGENTS.md §8 listed operation; licensing, access, purchase, entitlement, or distribution rights |

Human Acceptance **MUST NOT** be interpreted as blanket authorization. Human Acceptance **MUST NOT** constitute Consumer Adoption and **MUST NOT** grant L5.

### 9.3 Consumer Adoption

| Aspect | Rule |
|--------|------|
| **Owner** | Consumer |
| **Meaning** | Explicit decision to incorporate guidance into Consumer repository, policies, or durable engineering practice |
| **Recording** | Consumer-owned artifacts (for example ADR or local policy) — [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.6 spirit |
| **Effects (when explicit)** | Adopted Module / methodology / workflow / checklist / skill policy → typically **L3** within adoption scope; adopted Pack → **L5** within approved Pack scope |
| **MUST NOT** | Be assumed from Recommendation or Acceptance; silently rewrite L0–L4; activate a Pack for all Consumers merely because it exists in AIOS; override applicable licensing terms, third-party usage conditions, access restrictions, or distribution requirements |

### 9.4 AGENTS.md §8

[`../AGENTS.md`](../AGENTS.md) §8 human approval gates remain **independent and authoritative**. Lifecycle stages **MUST NOT** bypass §8. When in doubt, ask.

### 9.5 Licensing, access, entitlement and distribution rights

Keep three concerns distinct:

| Concern | Role |
|---------|------|
| **Lifecycle decisions** | Recommendation, Human Acceptance, Consumer Adoption |
| **Authority classification** | L0–L7 precedence (including binding versus advisory treatment) |
| **Legal / licensing rights** | Licensing, access, purchase, entitlement, and distribution rights under applicable law and licenses |

Licensing, access, purchase, entitlement and distribution rights are **independent of the Adaptive Guidance lifecycle stages**. That independence **MUST NOT** be read as placing licensing or legal constraints outside the L0–L7 authority model. Applicable licensing and legal restrictions remain authoritative under **L0** ([`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7; [`../AGENTS.md`](../AGENTS.md) §2).

| Action | Licensing / access / entitlement / purchase / distribution rights |
|--------|-------------------------------------------------------------------|
| **Recommendation** | **MUST NOT** grant these rights |
| **Human Acceptance** | **MUST NOT** grant these rights |
| **Consumer Adoption** | **MUST NOT** grant these rights; **MUST NOT** override applicable licensing terms, third-party usage conditions, access restrictions, or distribution requirements |
| **Pack or Module Adoption** | **MUST NOT** automatically establish a right to install, redistribute, sublicense, or commercially use included content |

These rights also remain separate from AGENTS.md §8 authorization: satisfying or skipping a lifecycle stage **MUST NOT** be treated as a license grant or entitlement.

---

## 10. Pack Adoption vs. Module Adoption

### Pack states

#### A. Pack not yet adopted

- A known Pack **MAY** be presented as an **L6** advisory recommendation when relevant.
- Human Acceptance **MAY** authorize using that guidance for the **current task** within existing task authorization.
- That use **MUST NOT** constitute Consumer Adoption.
- That use **MUST NOT** grant **L5** precedence.

#### B. Pack explicitly adopted by the Consumer

- Explicit Consumer Adoption establishes **L5** within the **approved Pack scope** ([`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7; [`../AGENTS.md`](../AGENTS.md) §2).
- Applicable binding Pack guidance within that scope **MUST NOT** be presented as an ordinary optional recommendation.
- It **MUST NOT** be offered for repeated task-level Accept/Reject.
- Human Acceptance **MUST NOT** downgrade, override, or make binding L5 guidance optional.
- Adopted Pack guidance remains subject to **L0–L4** and all applicable constraints.

### Modules and Pack composition

- Adopting a Pack **MUST NOT** implicitly mean that every Module referenced or included by that Pack has been independently adopted.
- Module ownership, dependencies, licensing, and adoption remain governed by Module rules ([`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5; [`MODULE_METADATA.md`](MODULE_METADATA.md); [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md)).
- If a Pack adoption scope explicitly includes Modules, that inclusion **MUST** be visible and approved — **MUST NOT** be inferred.
- Pack or Module Adoption (including explicit Module inclusion in a Pack scope) **MUST NOT** automatically establish a right to install, redistribute, sublicense, or commercially use included content; see §9.5.

---

## 11. L0–L7 Precedence and Binding vs. Advisory Guidance

Authoritative definitions: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7 and [`../AGENTS.md`](../AGENTS.md) §2. This section **applies** them to Adaptive Guidance; it **MUST NOT** redefine levels.

| Level | Meaning (summary) | Adaptive Guidance treatment |
|-------|-------------------|----------------------------|
| **L0** | Non-overridable safety, legal, security, privacy, licensing, compliance | Always binding; **MUST NOT** be optionalized |
| **L1** | Current explicit task instructions | Binding within L0 |
| **L2** | Consumer-approved ADRs and product decisions | Binding constraints throughout recommendation |
| **L3** | Consumer local policies (including explicitly adopted Module guidance as policy) | Binding within scope |
| **L4** | AIOS Core **binding** operating and governance defaults | Binding; **MUST NOT** be presented as ordinary optional recommendations; Recommendation **MUST NOT** downgrade L4 |
| **L5** | Explicitly adopted Pack guidance within scope | Binding within scope; **MUST NOT** be recurring Accept/Reject; subject to L0–L4 |
| **L6** | Module, methodology, workflow, checklist, skill recommendations by default; **not-yet-adopted Pack** recommendations | Advisory Recommendation / Acceptance candidates; Core origin **MUST NOT** auto-elevate to L4 |
| **L7** | External knowledge | Reference only |

**Conflict rule preserved:** Recommendations never silently override binding instructions ([`../AGENTS.md`](../AGENTS.md) §2).

---

## 12. Core / Module / Pack / Consumer Boundaries

| Boundary | Rule |
|----------|------|
| Core usability | Core **MUST** remain independently usable without Modules or Packs |
| Core advisory guidance | **MUST NOT** require Module or Pack dependencies |
| Modules | Independently distributable; **MUST NOT** depend on a specific Pack; Module-to-Module dependency fields are not part of metadata v1 ([`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.9) |
| Packs | **MAY** compose Modules per existing contracts; composition ≠ silent Module adoption |
| Consumer | Retains Adoption and implementation authority; third-party guidance **MUST NOT** silently modify Consumer decisions |
| Sync | `aiosctl sync` does not transfer ownership of Consumer ADRs or product decisions ([`../AGENTS.md`](../AGENTS.md) §12) |

---

## 13. Ecosystem and Provenance

Adaptive Guidance **SHOULD** remain capable of describing Official, Community, and Third-party Modules and Packs conceptually.

| Concept | Meaning |
|---------|---------|
| **Provenance** | Who develops and maintains an artifact (for example Official, Community, Third-party) |
| **Trust / verification** | What validation or review has taken place (separate from provenance) |

- Provenance **SHOULD** be shown when known; otherwise state **unknown**.
- Official **MUST NOT** be assumed suitable solely because it is Official.
- Community / Third-party **MUST NOT** be assumed untrusted solely because of provenance label.
- Provenance and ecosystem labels **MUST NOT** be treated as licensing, access, entitlement, purchase, or distribution grants; those rights remain independent (see §9.5).
- This document does **not** implement a marketplace, registry, package manager, licensing engine, entitlement system, or distribution infrastructure.

---

## 14. Reference Scenarios

Scenarios are **illustrative**. They are not automatic rules. Hypothetical future artifacts are labeled as such. Do not invent repository artifacts that do not exist.

This section remains the **Adaptive Guidance–focused** illustrative set. The integrated cross-model suite is [`ADAPTIVE_REFERENCE_SCENARIOS.md`](ADAPTIVE_REFERENCE_SCENARIOS.md) (documentation validation references; not new policies). Section 14 content is preserved and is not replaced by that suite.

### 14.1 Trivial documentation fix (Core-only)

- **Context:** Single README typo; negligible risk.
- **Relevance:** A full Feature Development Workflow recommendation is **not** automatic. Targeted verification or a short scope confirmation **MAY** suffice.
- **Process Depth:** If Lightweight, intensity is minimal; Depth does not force Workflow selection.
- **Acceptance:** Optional acceptance of the narrow advisory approach.
- **Adoption:** Not required.
- **Binding:** Applicable L4 / §8 remain constraints, not Accept/Reject items.

### 14.2 Feature Development — Standard Process Depth

- **Context:** Small API bug fix; meaningful code change.
- **Relevant (L6 examples):** [`../workflows/feature_development.md`](../workflows/feature_development.md), [`../checklists/review.md`](../checklists/review.md), [`../methodology/rdiv.md`](../methodology/rdiv.md); conditional [`../skills/repository_analysis.md`](../skills/repository_analysis.md).
- **Intensity:** Standard expectations per [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §5.
- **Acceptance:** Use of accepted L6 guidance for this task.
- **§8:** Independent; apply when listed operations apply.

### 14.3 Feature Development — Enhanced Process Depth

- **Context:** Public contract / higher blast radius.
- **Relevance:** Same Core L6 set may remain relevant; [`../methodology/architecture_first.md`](../methodology/architecture_first.md) often relevant. Stage 4 eligibility remains Workflow-owned.
- **Intensity:** Enhanced — deeper discovery, design, and verification notes.
- **Acceptance:** Does **not** authorize ADR changes or contract breaks.
- **§8 / L2:** Independent when durable decisions or listed operations apply.

### 14.4 Release task

- **Relevant (L6):** [`../workflows/release.md`](../workflows/release.md), [`../checklists/release_checklist.md`](../checklists/release_checklist.md).
- Feature Development completion does **not** authorize release.
- Release decision and publication authorization are **not** Human Acceptance of guidance.
- Process Depth ≠ Release class.

### 14.5 Multiple Guidance Types

- Example set: RDIV + Feature Development + Repository Analysis + Review Checklist.
- Present as related L6 items with distinct responsibilities.
- Knowledge, if present, **MAY** support; it is not a seventh type.

### 14.6 Optional Module (hypothetical)

- **Hypothetical future Module** (for example security-engineering). No Module packages are required to exist today.
- Recommend as **L6** after Core baseline discovery when relevant.
- Acceptance ≠ Consumer Adoption (L3 policy).
- No automatic install.

### 14.7 Pack — not adopted versus adopted

**Not adopted (L6):**

- Education Pack known but not adopted → advisory L6 recommendation when Education context is real.
- Acceptance → task-level use only; **no L5**.
- `notebook_creation.md` only with Education context.
- Constituent Modules not silently adopted.

**Explicitly adopted (L5):**

- Binding within approved Pack scope; no recurring Accept/Reject.
- Still subject to L0–L4.
- Module inclusion still requires visible approved scope — not inference.

### 14.8 Community or Third-party Module (hypothetical)

- State provenance (or **unknown**); keep trust/verification separate.
- Treat as L6 advisory unless Consumer Adoption creates L3 policy.
- **MUST NOT** silently override Consumer L2/L3.

### 14.9 Incomplete or missing guidance information

- Missing status, metadata, or provenance → state **not stated** / **unknown**.
- Prefer clarify or defer over invention.
- Gaps **MUST NOT** be used to invent L4 or L5 authority.

### 14.10 Accepted but not adopted

- Human Acceptance of L6 (including not-adopted Pack) authorizes task-level use only.
- Without Consumer Adoption, no durable L3/L5 elevation.
- Guidance **MAY** be recommended again on a later task.
- §8 and implementation authorization remain separate.

---

## 15. Risks, Limitations and Non-goals

### Risks and limitations

- Heterogeneous artifact maturity (many definitions remain `draft`).
- Module catalog not populated — Module scenarios are often hypothetical.
- Misreading Core-first as precedence.
- Misreading Pack Acceptance as L5 Adoption.
- Misreading Acceptance as §8 authorization.
- Education residuals mistaken for general Core guidance.
- Pressure to turn explainable fields into a mandatory schema — resisted by this document.

### Non-goals (reaffirmed)

This document does **not** establish or claim: adaptive engine; registry; resolver; scoring/ML; automatic Module/Pack discovery/installation/adoption; marketplace or package manager; licensing/entitlement engine; Skill/Workflow execution; Knowledge RAG; Adaptive CLI; automatic Consumer repository modification; `aiosctl sync` changes; AGENTS.md §8 redesign; Framework Contract §5.6 text changes.

---

## 16. Future Considerations

Governance interactions with existing precedence and Human Approval Gates are defined in [`ADAPTIVE_GOVERNANCE_MODEL.md`](ADAPTIVE_GOVERNANCE_MODEL.md). This document remains the canonical source for Guidance Lifecycle semantics (§9); the Governance Model explains interactions and does **not** change [`../AGENTS.md`](../AGENTS.md) §8 authority.

Phase **6.6** reference scenarios and documentation-level audit specifications are delivered in [`ADAPTIVE_REFERENCE_SCENARIOS.md`](ADAPTIVE_REFERENCE_SCENARIOS.md) and [`ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md`](ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md). This document remains the canonical source for Guidance Lifecycle semantics (§9); those Phase 6.6 documents do **not** redefine them.

Items below require **separate** Product Owner scope and approval:

- Evaluation of whether [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.6 should be clarified to name all six Guidance Types and the Acceptance versus Adoption split (**deferred**; not decided here)
- Phase 7 Module catalog population enabling non-hypothetical Module recommendations
- Any runtime, registry, distribution, or verification infrastructure

---

## 17. Source References

| Document | Relevance |
|----------|-----------|
| [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §3, §5–§7 | Layers, Module/Pack, §5.6, concept meanings, L0–L7 |
| [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md) | Project Context, Task Context, Core-only usability |
| [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) | Process Depth, intensity mapping, ownership vs Workflow |
| [`../AGENTS.md`](../AGENTS.md) §2, §7, §8 | Precedence operationalization, adaptive posture, approval gates |
| [`WORKFLOW_CHECKLIST_CONVENTIONS.md`](WORKFLOW_CHECKLIST_CONVENTIONS.md) | Workflow/Checklist authority and placement |
| [`SKILL_KNOWLEDGE_CONVENTIONS.md`](SKILL_KNOWLEDGE_CONVENTIONS.md) | Skill/Knowledge/Prompt boundaries |
| [`MODULE_METADATA.md`](MODULE_METADATA.md), [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md), [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md) | Module metadata and lifecycle (packages may be absent) |
| [`../packs/education/README.md`](../packs/education/README.md) | Pack adoption and L5 |
| [`../workflows/feature_development.md`](../workflows/feature_development.md), [`../workflows/release.md`](../workflows/release.md) | Core Workflow examples |
| [`../checklists/review.md`](../checklists/review.md), [`../checklists/release_checklist.md`](../checklists/release_checklist.md) | Core Checklist examples |
| [`../skills/repository_analysis.md`](../skills/repository_analysis.md) | Core Skill example |
| [`../methodology/`](../methodology/) | Core Methodologies |
| [`../ROADMAP.md`](../ROADMAP.md) Phase 6 | Adaptive Project Intelligence direction; engine non-goal |
| [`../PROJECT_STRUCTURE.md`](../PROJECT_STRUCTURE.md) | Actual layout and maturity |

---

## Document maintenance

- This is a Core Adaptive Project Intelligence **design** document (`draft`).
- Changes **MUST** remain consistent with [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md), [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md), [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md), and [`../AGENTS.md`](../AGENTS.md).
- Do not claim runtime or tooling delivery based on this document alone.
- Phase 6 reference scenarios and documentation-level audit materials are maintained in `ADAPTIVE_REFERENCE_SCENARIOS.md` and `ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md`, respectively.

End of Adaptive Guidance Model v0.1.0 (`draft`).
