# AIOS Process Depth Model

Version: 0.1.0

Status: Draft

Last Updated: 2026-11-03

Document type: Adaptive Project Intelligence design specification

This document defines the Core **Complexity Dimensions** and **Process Depth Classification** models for AIOS Adaptive Project Intelligence.

It is subordinate to the Framework Contract for architecture and governance:

- Adaptive recommendation architecture: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.6
- Concept meanings and ownership: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5–§6
- Instruction precedence (L0–L7): [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7
- Agent operationalization: [`../AGENTS.md`](../AGENTS.md) (especially §2, §4, §5, §7, §8)
- Project Context and Task Context: [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md)

This document is **conceptual design guidance**. It does not implement an adaptive runtime, discovery engine, parser, schema, API, scoring system, or autonomous classifier.

---

## 1. Purpose / Scope / Non-goals

### Purpose

Provide a shared, qualitative way for agents and humans to:

1. Interpret **Complexity Dimensions** (D1–D12) derived from Project Context and Task Context.
2. Recommend an appropriate **Process Depth** level for a specific task.
3. Keep ceremony proportional while preserving existing AIOS governance.

### Scope

**In scope:**

- Complexity Dimensions taxonomy and roles
- Four Process Depth levels and qualitative classification reasoning
- Conceptual relationship to Feature Development Workflow
- Concise Release Workflow clarification
- Governance invariants related to Process Depth

**Out of scope:**

- Detailed Feature Development stage-by-stage normative mapping (Phase **6.3.4**)
- Adaptive Guidance selection of Workflows, Checklists, Skills, Modules, or Packs (Phase **6.4**)
- Numerical scores, weights, thresholds, formulas, or automatic escalation
- Runtime engines, parsers, schemas, APIs, RAG, Skill/Workflow executors, adaptive CLI
- Automatic Module/Pack discovery, installation, adoption, or consumer repository modification

### Non-goals

AIOS Core provides the **framework**, not Consumer domain content. This document does not authorize consumer repository changes, operational Git/publish/deploy actions, or silent adoption of Modules or Packs.

---

## 2. Terminology

| Term | Meaning |
|------|---------|
| **Project Context** | Working model of the repository and engineering environment ([`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md)) |
| **Task Context** | Working model of the specific requested change or outcome |
| **Complexity Dimension** | One of D1–D12 qualitative inputs, constraints, or modifiers used in Process Depth reasoning |
| **Process Depth** | Recommended engineering ceremony intensity for a **task** — one of Lightweight, Standard, Enhanced, Critical |
| **Lightweight Process Depth** | The lowest Process Depth level |
| **Workflow light/skip paths** | Stage-level shortcuts in Feature Development or Release Workflows — **not** the same as Lightweight Process Depth |
| **Lightweight Tooling** | Informal description of small/simple tools — **not** a Process Depth level |
| **Release class** | Nature of a release and its applicable release procedure — **not** Process Depth |
| **Input** | Dimension that qualitatively informs Process Depth recommendation |
| **Constraint** | Binding obligation independent of Process Depth |
| **Contextual modifier** | Adjusts expectations; does not independently select Process Depth |

These terms are **not interchangeable**.

---

## 3. Complexity Dimensions

Complexity Dimensions provide qualitative inputs to Process Depth Classification. They reuse Project Context and Task Context from [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md).

### 3.1 Interpretation principles

- **Task Context** is the primary classification driver.
- **Project Context** provides constraints and contextual information; it does not independently determine Process Depth.
- Not every dimension is relevant to every task.
- Primary drivers are typically **1–3**, with **no hard maximum** — all materially relevant drivers may be documented.
- Avoid double-counting correlated risks (name the primary hazard once).
- Urgency is **not** a depth input; it may affect priority/communication only and must not reduce mandatory controls or required Process Depth.

### 3.2 Dimension roles

| Role | Meaning | Members |
|------|---------|---------|
| **Input** | Qualitatively informs Process Depth | D1–D4, D5 task exposure, D6–D10 |
| **Constraint** | Binding independently of Process Depth | D5 standing constraints, D12, applicable [`../AGENTS.md`](../AGENTS.md) §8 gates, applicable Consumer ADR/policy review-approval requirements |
| **Contextual modifier** | Sets expectations; does not auto-select depth | D11; urgency (priority only) |

### 3.3 Taxonomy (D1–D12)

#### D1 — Task complexity

| Aspect | Guidance |
|--------|----------|
| **Definition** | Intrinsic difficulty of **this task** (not repository size) |
| **Ownership** | Task Context |
| **Role** | Input |
| **Must not infer** | Large or “critical” repository ⇒ high task complexity |

#### D2 — Scope & affected components

| Aspect | Guidance |
|--------|----------|
| **Definition** | In-scope / out-of-scope boundaries and touched components |
| **Ownership** | Task Context (Project structure informs) |
| **Role** | Input |
| **Must not infer** | File count alone ⇒ wide blast radius or Critical depth |

#### D3 — Impact & blast radius

| Aspect | Guidance |
|--------|----------|
| **Definition** | Who or what is affected if the change fails |
| **Ownership** | Task Context (Project topology informs) |
| **Role** | Input |
| **Must not infer** | Critical product ⇒ every small task is Critical Process Depth |

#### D4 — Technical & operational risk

| Aspect | Guidance |
|--------|----------|
| **Definition** | Technical and operational failure modes for this change |
| **Ownership** | Task Context |
| **Role** | Input |
| **Must not infer** | Presence of risk ⇒ operational authorization already granted |

#### D5 — Security, privacy & compliance exposure

One conceptual dimension with **two aspects that must not be conflated**:

| Aspect | Meaning | Role |
|--------|---------|------|
| **Standing constraints** | Applicable **L0** (non-overridable framework constraint layer) **and** project-specific security, privacy, and compliance obligations | **Constraint** |
| **Task exposure** | How the **current task** interacts with those areas | **Input** |

| Aspect | Guidance |
|--------|----------|
| **Ownership** | Standing constraints: recorded via Project Context; **L0 is not owned, redefined, or overridden by Project Context**. Task exposure: Task Context |
| **Must not infer** | Heuristic “review area” ⇒ confirmed vulnerability; standing constraints may be ignored at Lightweight |

#### D6 — Data integrity & reversibility

| Aspect | Guidance |
|--------|----------|
| **Definition** | Data/schema integrity impact and difficulty of reversal |
| **Ownership** | Task Context |
| **Role** | Input |
| **Must not infer** | Presence of migration artifacts ⇒ authority to execute migrations |

#### D7 — Architectural impact

| Aspect | Guidance |
|--------|----------|
| **Definition** | Impact on architecture, boundaries, layers, or top-level conventions |
| **Ownership** | Task Context |
| **Role** | Input |
| **Must not infer** | Any new directory ⇒ Enhanced by default |

#### D8 — Public API & backward compatibility

| Aspect | Guidance |
|--------|----------|
| **Definition** | Impact on external contracts, sync compatibility, or breaking changes |
| **Ownership** | Task Context |
| **Role** | Input |
| **Must not infer** | Internal refactor ⇒ public contract break |

#### D9 — Dependencies & uncertainty

| Aspect | Guidance |
|--------|----------|
| **Definition** | Task dependencies and known unknowns |
| **Ownership** | Task Context |
| **Role** | Input |
| **Must not infer** | Uncertainty alone ⇒ Critical Process Depth |

#### D10 — Verification difficulty

| Aspect | Guidance |
|--------|----------|
| **Definition** | Cost and difficulty of verifying the change |
| **Ownership** | Task Context (Project test/CI maturity informs) |
| **Role** | Input |
| **Must not infer** | Unrun checks ⇒ passed |

#### D11 — Project type, size & maturity

| Aspect | Guidance |
|--------|----------|
| **Definition** | Standing repository type, scale, and maturity |
| **Ownership** | Project Context |
| **Role** | Contextual modifier |
| **Must not infer** | Platform/large repo ⇒ every task is Critical Process Depth |

#### D12 — Existing ADRs & consumer policies

| Aspect | Guidance |
|--------|----------|
| **Definition** | Consumer ADRs (**L2**) and adopted local policies (**L3**) that constrain the task |
| **Ownership** | Project Context constrains Task Context |
| **Role** | Constraint |
| **Must not infer** | Generic AIOS defaults override durable Consumer decisions |

### 3.4 Ownership summary

| ID | Project Context | Task Context |
|----|-----------------|--------------|
| D1–D4, D6–D10 | Informs where noted | Owner |
| D5 standing | Records applicable obligations (does not own L0) | — |
| D5 exposure | Informs | Owner |
| D11 | Owner | — |
| D12 | Owner (constraint) | Must respect |

### 3.5 Interaction and double-counting

- D2 vs D3: many components ≠ wide blast radius.
- D7 vs D8: architectural change ≠ automatic public break.
- D5 standing vs exposure: record separately.
- D5 vs D6: name the primary hazard when overlapping.
- D9 vs D10: do not inflate the same gap twice.
- D11 vs D3/D4: repository criticality ≠ task risk.
- Urgency vs controls: urgency does not lower Process Depth or waive L0 / §8 / Consumer mandatory controls.

### 3.6 Evidence and uncertainty (dimensions)

Use evidence labels aligned with [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md): verified fact, reasonable inference, unknown/unavailable, conflicting.

- Identify missing information explicitly.
- Request additional analysis or clarification when needed.
- Disclose assumptions in provisional assessments.
- Uncertainty alone must not automatically classify a task as Critical.
- No numerical scoring, weights, thresholds, or automatic escalation.

---

## 4. Process Depth Classification

### 4.1 Approved levels

1. **Lightweight**
2. **Standard**
3. **Enhanced**
4. **Critical**

Process Depth is **not** the L0–L7 precedence model. L0 always applies.

### 4.2 Qualitative classification reasoning

1. Build Task Context.
2. Apply Project Context constraints and standing obligations.
3. Select relevant D1–D12 dimensions for this task.
4. Separate inputs, constraints, and modifiers.
5. Identify primary drivers (typically 1–3; no hard maximum).
6. Check independent approval obligations ([`../AGENTS.md`](../AGENTS.md) §8 and applicable Consumer ADR/policy review-approval requirements).
7. Recommend a Process Depth based on **task** dimensions (complexity, impact, risk, architecture, data integrity, and other relevant inputs).
8. Check Lightweight eligibility (including unresolved mandatory approval bar).
9. Explain why the selected level is appropriate and why adjacent levels are less suitable when that distinction matters.
10. If provisional, disclose missing information, assumptions used, and required clarification or additional analysis.

**Analysis is always required**; its depth is proportional to the task.

### 4.3 Approval requirements vs Process Depth

**Established rule:**

Approval requirements may affect **Lightweight eligibility** and impose **independent governance obligations**, but they **do not independently determine** Process Depth.

- A required Consumer Policy review does **not** automatically make a task Enhanced or Critical.
- An [`../AGENTS.md`](../AGENTS.md) §8 approval requirement does **not** automatically make a task Critical.
- Recommended depth is driven by actual task complexity, impact, risk, architecture, data integrity, and other relevant dimensions.
- Mandatory approval requirements remain binding **independently** of the recommended level.
- Obtaining approval does **not** automatically determine Process Depth.
- Process Depth **never** grants operational authorization.
- Review requirements and operational authorization remain distinct.

### 4.4 Level definitions

#### Lightweight

| Aspect | Guidance |
|--------|----------|
| **Purpose** | Lowest ceremony for trivial, clearly bounded, negligible-risk, small-impact work |
| **Typical tasks** | Documentation typo; isolated micro-fix with no behavior or contract impact |
| **Relevant dimensions** | Low D1–D4; no meaningful D5 exposure / D6–D8; low D9–D10; standing constraints scanned |
| **Analysis** | Targeted analysis **always** required — not analysis-free |
| **Planning / design** | Minimal or short step list |
| **Implementation / verification** | Minimal scoped change; proportionate verification |
| **Review / documentation** | Light review unless Consumer policy requires more |
| **Eligibility** | Trivial + clearly bounded + negligible risk + small impact + **no unresolved mandatory approval requirement** |
| **Inappropriate when** | Meaningful architectural, public-contract, or data impact; coordinated multi-component risk; unresolved mandatory approval; meaningful security/data/reversibility risk; unresolved critical-path uncertainty |

Unresolved mandatory approval requirements (applicable §8 and/or applicable Consumer ADR/policy review-approval) make a task **ineligible for Lightweight**. Applicable §8 gates remain mandatory whenever they apply. §8 is **not** an automatic Critical classification mechanism.

#### Standard

| Aspect | Guidance |
|--------|----------|
| **Purpose** | **Default** for meaningful ordinary engineering work |
| **Typical tasks** | Ordinary bug fixes; small or medium features; normal refactoring; regular documentation changes |
| **Relevant dimensions** | Moderate D1–D4; limited or absent D7–D8; low D5 exposure; manageable D9–D10 |
| **Analysis** | Meaningful discovery proportionate to the change |
| **Planning / design** | Short plan; deeper design only when architecture/contract triggers apply |
| **Implementation / verification** | Scoped implementation; relevant validation with honest unrun disclosure |
| **Review / documentation** | Normal review as applicable |
| **Inappropriate when** | Purely trivial (Lightweight more proportionate) or material Enhanced/Critical drivers are present |
| **Insufficient when** | Material D7 / D8 / D6 impact; coordinated wide D2 + D3 scope/impact; elevated D5 task exposure; severe D9 / D10 complexity or verification difficulty with high downside — consider Enhanced or Critical based on actual task hazards (no automatic classification) |

#### Enhanced

| Aspect | Guidance |
|--------|----------|
| **Purpose** | Significant engineering work requiring deeper discovery, design, and verification |
| **Typical tasks** | Architectural changes; public contract or backward-compatibility changes; important data-model changes; coordinated multi-component work; substantial dependency or verification complexity |
| **Relevant dimensions** | Often D7, D8, D6, D2+D3, D9, D10; D5 exposure when relevant |
| **Analysis** | Deep discovery; Architecture First; ADR/policy conflict scan |
| **Planning / design** | Explicit design direction when architecture/contracts are affected |
| **Implementation / verification** | Careful sequencing; stronger validation; residual risks recorded |
| **Review / documentation** | Structured review; durable decision changes follow owner path |
| **Inappropriate when** | Ordinary/trivial work (overkill) or Critical-class irreversible/severe hazards dominate |
| **Must not auto-apply** | Every multi-component change or ADR touch; required Consumer Policy review alone |

#### Critical

| Aspect | Guidance |
|--------|----------|
| **Purpose** | Very high-impact work; serious security or data-integrity risk; difficult reversibility; critical operational consequences |
| **Typical tasks** | Destructive production data migration; severe compliance/security exposure; wide irreversible public break |
| **Relevant dimensions** | Strong D3/D4/D5 exposure/D6; often D8; high downside under D9 |
| **Analysis / design / verify / review** | Maximum proportional ceremony; human gates where independently required |
| **Inappropriate when** | Justified only by “repository is critical”; uncertainty alone; urgency theater; “needs §8 therefore Critical” |
| **Must not auto-apply** | Repository criticality alone; §8 approval requirement alone |

**Critical Process Depth** is not the same as a **critical repository**.

### 4.5 Default and boundary rules

| Rule | Statement |
|------|-----------|
| Default | **Standard** for meaningful ordinary engineering work |
| Lightweight | Only when all eligibility conditions hold |
| Enhanced | Requires material dimensional evidence — not approval labels alone |
| Critical | Reserved for severe task hazards — not repository labels alone |
| Conflicting signals | Prefer constraint-preserving reading; disclose conflicts; ask when decision-critical |
| Missing information | Identify gaps; request clarification; use provisional recommendation when needed |
| Urgency | Must not reduce Process Depth or waive L0 / §8 / applicable Consumer mandatory controls |

### 4.6 Provisional recommendations

When a Process Depth recommendation is **provisional**, explicitly disclose:

- What information is missing
- Which assumptions are being used
- What clarification or additional analysis is required

No fixed mandatory sentence or template is required. No separate appendix is required.

A provisional recommendation does **not** authorize actions that require human approval.

Uncertainty alone must not automatically result in Critical.

### 4.7 Illustrative scenarios (non-binding)

Scenarios illustrate the model; they do not create new binding rules.

#### Scenario A — README typo

- **Drivers:** Low D1–D4; standing constraints scanned.
- **Recommended:** Lightweight.
- **Not Standard:** Disproportionate ceremony.
- **Approval:** None expected unless Consumer policy unusually requires it.

#### Scenario B — Ordinary single-module bug fix

- **Drivers:** Moderate D1–D4; no D7/D8.
- **Recommended:** Standard.
- **Not Lightweight:** Behavior change / non-trivial.
- **Not Enhanced:** No architectural or public-contract impact.
- **Approval:** Independent Consumer review policy, if any, does not by itself force Enhanced.

#### Scenario C — Public API field rename

- **Drivers:** D8 primary; elevated D3; possible D7.
- **Recommended:** Enhanced.
- **Not Standard:** Public-contract significance.
- **Not auto-Critical:** Managed/reversible contract change may remain Enhanced; Critical only if severity warrants.
- **Approval:** Owner path for durable contract/ADR changes may apply independently; depth does not authorize.

#### Scenario D — Irreversible production data migration

- **Drivers:** Strong D6/D3/D4; possible D5 exposure.
- **Recommended:** Critical.
- **Not Enhanced:** Reversibility and integrity severity.
- **Approval:** Likely applicable §8 irreversible/data gates and Consumer policy — **independent** of the depth label. Depth still does not authorize the operation.

---

## 5. Workflow notes

### 5.1 Feature Development Workflow (conceptual)

- Process Depth **recommends** engineering ceremony intensity.
- The Feature Development Workflow **owns** stage-level Required / light / skip classifications ([`../workflows/feature_development.md`](../workflows/feature_development.md)).
- Detailed stage-by-stage normative mapping belongs to Phase **6.3.4** and is **not** defined here.

Do not treat as interchangeable:

- Lightweight Process Depth
- Workflow light/skip paths
- Lightweight tooling

### 5.2 Release Workflow clarification (mandatory)

- Complexity Dimensions **may inform** Release assessment.
- **Process Depth** and **Release class** are **separate concepts**.
- Process Depth describes engineering process intensity for a **task**.
- Release class describes the nature of a **release** and its applicable procedure ([`../workflows/release.md`](../workflows/release.md)).
- There is **no automatic equivalence or mapping** between Process Depth and Release class.

This clarification is concise by design. It does **not** create a separate Release classification model.

---

## 6. Governance

Preserved without creating new precedence levels:

- **L0** applies at every Process Depth.
- **L1** cannot silently rewrite durable **L2/L3** Consumer decisions.
- [`../AGENTS.md`](../AGENTS.md) **§8** remains mandatory whenever applicable.
- Applicable Consumer ADRs and Consumer Policies remain binding.
- Review requirements are not operational authorization.
- Process Depth is not operational authorization.
- AI recommends; humans decide.
- Urgency does not waive mandatory controls or justify reducing required Process Depth.
- Analysis is always required and proportional to the task.
- A critical repository does not mean a Critical task.
- Approval requirements do not independently determine Process Depth.
- No autonomous Module/Pack adoption, installation, or consumer repository modification.
- No silent consumer policy rewrite.

Human approval gates and instruction precedence remain as defined in [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7 and [`../AGENTS.md`](../AGENTS.md) §2 / §8.

---

## 7. Relationship to Adaptive Project Context / Phase 6.4

| Artifact | Relationship |
|----------|----------------|
| [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md) | Defines Project Context and Task Context — inputs to this model |
| This document | Interprets dimensions and recommends Process Depth |
| Phase **6.3.4** | Detailed Feature Development (and related) stage mapping |
| Phase **6.4** | Adaptive Guidance Model — selecting Workflows, Checklists, Skills, and optional Modules/Packs |
| [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.6 | Adaptive recommendation architecture (design only; not an engine) |

```text
Project Context + Task Context
        → Complexity Dimensions (D1–D12)
        → Process Depth recommendation
        → (Phase 6.4) Adaptive Guidance recommendations
```

This pipeline is conceptual. It is not an executable engine.

---

## Document maintenance

- This is a Core Adaptive Project Intelligence **design** document (`draft`).
- Changes must remain consistent with [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) and [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md).
- Do not claim runtime or tooling delivery based on this document alone.
- Related Phase 6.3.4+ work should reference this file rather than redefine Process Depth levels or D1–D12.

End of Process Depth Model v0.1.0 (`draft`).
