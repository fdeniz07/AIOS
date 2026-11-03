# AIOS Adaptive Reference Scenarios

Version: 0.1.0

Status: Draft

Last Updated: 2026-11-03

Document type: Phase 6.6 Adaptive Project Intelligence reference scenario specification

This document defines the **canonical integrated reference scenario suite** for AIOS Adaptive Project Intelligence.

It is subordinate to existing authorities and **MUST NOT** redefine them:

- Project Context and Task Context: [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md)
- Process Depth: [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md)
- Adaptive Guidance (including Guidance Lifecycle semantics): [`ADAPTIVE_GUIDANCE_MODEL.md`](ADAPTIVE_GUIDANCE_MODEL.md)
- Adaptive Governance interactions: [`ADAPTIVE_GOVERNANCE_MODEL.md`](ADAPTIVE_GOVERNANCE_MODEL.md)
- Framework architecture and L0–L7: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md)
- Agent operationalization and Human Approval Gates: [`../AGENTS.md`](../AGENTS.md) (especially §2, §7, §8)
- Feature Development and Release stage eligibility: [`../workflows/feature_development.md`](../workflows/feature_development.md), [`../workflows/release.md`](../workflows/release.md)

Scenarios in this document are **illustrative validation references**. They are **not** new policies, Human Approval Gates, Process Depth levels, Guidance Types, Workflow stage classifications, Release classes, or AGENTS.md §8 rules.

This document does **not** implement a runtime, engine, registry, resolver, scoring system, schema, or automated scenario runner.

---

## 1. Purpose and Scope

### Purpose

Provide one integrated, auditable suite of reference scenarios that exercise Adaptive Project Intelligence **across** context, Process Depth, guidance lifecycle, precedence, authorization, Workflow, and Release distinctions — without inventing new architecture.

### In scope

- Fourteen mandatory scenarios **RS-01** through **RS-14**
- RS-12 subcases **RS-12a** and **RS-12b** (not independent scenario IDs)
- Cross-model validation criteria and model references
- Traceability to model-specific examples in AGM §14 and PDM §4.7

### Out of scope

- New architectural or governance decisions
- Changes to AGENTS.md §8 or Framework Contract §5.6
- Runtime tests, CI automation, or executable verification
- Rewriting or removing AGM §14 or PDM §4.7 content
- Cross-document discoverability alignment (Phase **6.6.4**)
- Claiming Phase 6 or Phase 6.6 completion

---

## 2. Non-policy disclaimer

| These scenarios | They are not |
|-----------------|--------------|
| Illustrate how existing models interact | Binding Consumer or Core policies |
| Support documentation-level audit | New §8 approval operations |
| Clarify expected agent reasoning | Automatic Workflow stage skip rules |
| Label unknowns and hypotheticals | Proof that Modules/Packs exist in the catalog |

Completing a scenario walkthrough **MUST NOT** be treated as Human Acceptance, Consumer Adoption, §8 authorization, Release Approval, or publication authorization.

---

## 3. Relationship to existing models

| Model | Owns | This suite |
|-------|------|------------|
| [`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md) | Project Context and Task Context | Supplies initial context; does not redefine |
| [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) | Process Depth intensity; §4.7 depth-focused examples | Applies intensity; does not change levels |
| [`ADAPTIVE_GUIDANCE_MODEL.md`](ADAPTIVE_GUIDANCE_MODEL.md) | Six Guidance Types; lifecycle; §14 model-specific examples | Applies lifecycle; does not change semantics |
| [`ADAPTIVE_GOVERNANCE_MODEL.md`](ADAPTIVE_GOVERNANCE_MODEL.md) | Precedence × Lifecycle × Authorization interactions | Applies interaction rules |
| Feature Development / Release Workflows | Stage Required / Light / Skip; Release Approval vs publication | Eligibility remains Workflow-owned |
| [`../AGENTS.md`](../AGENTS.md) §8 | Human Approval Gates | Unchanged; scenarios apply them |

**Three independent dimensions** appear in every scenario and **MUST NOT** be conflated:

1. **Agent behavior** — what the agent may recommend or refuse to assume
2. **Human decision** — task-level Acceptance, rejection, Consumer Adoption, or durable Consumer decisions
3. **Operational authorization** — permission for §8-listed or otherwise gated operations (commit, tag, push, publish, deploy, etc.)

Process Depth is **usage intensity only**. It is **not** instruction precedence, authorization, Workflow eligibility, or Release class ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §5).

---

## 4. Common scenario format

Each scenario uses the following documentation fields (not a mandatory metadata schema or runtime structure):

1. **ID and title**
2. **Purpose**
3. **Initial context** (Project Context and Task Context; unknowns explicit)
4. **Relevant instructions and constraints** (L0–L7 / Consumer)
5. **Illustrative task classification**
6. **Process Depth and rationale** (where applicable)
7. **Guidance and lifecycle state**
8. **Expected agent behavior**
9. **Required human decision** (where applicable)
10. **Operational authorization boundary**
11. **Expected outcome**
12. **Model references**
13. **Validation criteria**

Hypothetical Modules or Packs are labeled **Hypothetical**. Missing facts use **unknown** or **not stated**.

---

## 5. Scenario suite

### RS-01 — Lightweight routine (Core-only)

**Purpose:** Show proportional low ceremony for a trivial Core-only task without treating Lightweight Process Depth as Workflow stage-skip authority.

**Initial context**

- **Project Context:** Small documentation-oriented repository; standing risk negligible for the touched path; Core Workflows/Checklists available.
- **Task Context:** Correct a single README typo; no behavior change.
- **Unknowns:** None material for scope; Consumer review policy **not stated** beyond ordinary defaults.

**Relevant instructions and constraints**

- Applicable L4 Core operating defaults remain constraints, not Accept/Reject items.
- AGENTS.md §8 applies only if a listed operation appears (not expected here).
- No adopted Pack required.

**Illustrative task classification:** Documentation fix / typo.

**Process Depth and rationale:** **Lightweight** — low blast radius; trivial documentation-only change; negligible repository risk ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §4; illustrative affinity with PDM §4.7 Scenario A).

**Guidance and lifecycle state**

- Full Feature Development Workflow recommendation is **not** automatic.
- Narrow advisory approach (short scope confirmation / targeted verification) **MAY** suffice.
- Human Acceptance optional; Consumer Adoption not required.

**Expected agent behavior**

- Recommend proportionate ceremony; do not invent architecture work.
- **MUST NOT** treat Lightweight Process Depth alone as authorization to skip Feature Development Stage 2 or any other Workflow stage.
- Stage 2 conditional light/skip remains owned solely by [`../workflows/feature_development.md`](../workflows/feature_development.md): only when the change is trivial (for example documentation-only typo) **and** repository risk is negligible, with a short rationale if deep discovery is skipped ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §5.3, §5.5).
- Do not invent new eligibility criteria.

**Required human decision:** Optional task-level Acceptance of the narrow advisory approach.

**Operational authorization boundary:** No commit/push/publish assumed. Lightweight Depth and optional Acceptance do **not** grant operational authorization.

**Expected outcome:** Proportionate Core-only handling; Workflow eligibility preserved; no Adoption; no false §8 waiver.

**Model references:** APC; PDM §4–§5 (esp. §5.3, §5.5); AGM §9, §14.1; Governance §4–§5; Feature Development Workflow Stage 2.

**Validation criteria**

- Depth is not equated with Workflow Light/Skip.
- Stage 2 skip, if described, cites existing Workflow eligibility only.
- L4 / §8 are not presented as recurring Accept/Reject items.

---

### RS-02 — Standard feature development

**Purpose:** Show default meaningful engineering intensity with explainable multi-type Core L6 recommendations.

**Initial context**

- **Project Context:** Ordinary service or library; tests and docs present.
- **Task Context:** Small API bug fix with meaningful code/behavior change; limited blast radius.
- **Unknowns:** Consumer-specific review SLAs **not stated**.

**Relevant instructions and constraints**

- Consumer L2/L3 **not stated** as conflicting.
- L6 Core advisory guidance applicable; L4 constraints remain.
- §8 independent if listed operations arise.

**Illustrative task classification:** Bug fix / small feature correction.

**Process Depth and rationale:** **Standard** — meaningful ordinary work; not trivial; no material Enhanced/Critical drivers ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §4; affinity with PDM §4.7 Scenario B).

**Guidance and lifecycle state**

- Relevant L6 examples: [`../workflows/feature_development.md`](../workflows/feature_development.md), [`../checklists/review.md`](../checklists/review.md), [`../methodology/rdiv.md`](../methodology/rdiv.md); conditional [`../skills/repository_analysis.md`](../skills/repository_analysis.md).
- Present as related but distinct Guidance Types (affinity with AGM §14.5).
- Recommendation → optional Human Acceptance for this task; Adoption not required for task-level use.

**Expected agent behavior**

- Recommend Core L6 guidance with rationale; keep types distinct.
- Scale intensity to Standard per PDM; do not use Depth to select Guidance Types.
- Surface §8 only when applicable operations appear.

**Required human decision:** May Accept advisory guidance for this task.

**Operational authorization boundary:** Acceptance does not authorize §8-listed operations, commit, push, publish, or deploy.

**Expected outcome:** Explainable Standard-depth Core recommendation path; lifecycle and §8 remain independent.

**Model references:** APC; PDM §4–§5; AGM §4–§5, §9, §14.2, §14.5; Governance §5–§6.

**Validation criteria**

- Process Depth ≠ Guidance Type picker.
- Multi-type set is linked, not fused.
- §8 remains independent of Acceptance.

---

### RS-03 — Enhanced multi-component / public contract

**Purpose:** Show deeper intensity for higher blast radius without equating Acceptance with durable contract or §8 authority.

**Initial context**

- **Project Context:** Public API or multi-component surface exists.
- **Task Context:** Public contract field rename or similar managed contract change; elevated blast radius.
- **Unknowns:** Exact dependent Consumer count **unknown** until discovery.

**Relevant instructions and constraints**

- Possible L2 ADR / public-contract impact.
- L4 Core defaults and §8 may apply for public-contract or durable-decision changes.
- L6 advisory guidance remains advisory until accepted for the task; Adoption separate.

**Illustrative task classification:** Public-contract / multi-component change.

**Process Depth and rationale:** **Enhanced** — public-contract significance and wider impact; not automatically Critical if managed/reversible ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §4; affinity with PDM §4.7 Scenario C).

**Guidance and lifecycle state**

- Core L6 set may remain relevant; [`../methodology/architecture_first.md`](../methodology/architecture_first.md) often relevant.
- Feature Development Stage 4 eligibility remains Workflow-owned.
- Human Acceptance of advisory guidance does **not** authorize ADR changes or contract breaks.

**Expected agent behavior**

- Recommend deeper discovery, design, and verification notes at Enhanced intensity.
- Disclose contract/ADR impacts; do not silently rewrite L2.
- Do not claim Acceptance authorizes public-contract breaks.

**Required human decision:** Task Acceptance of advisory path if used; durable ADR/contract decisions require Consumer owner under existing rules.

**Operational authorization boundary:** Enhanced Depth and Acceptance do not grant §8 authorization or publication rights.

**Expected outcome:** Enhanced ceremony with clear separation of Accept, durable Consumer decision, and §8.

**Model references:** APC; PDM §4–§5; AGM §9, §14.3; Governance §5–§7, §10; Feature Development Workflow Stage 4.

**Validation criteria**

- Accept ≠ ADR rewrite or contract break.
- Stage eligibility remains Workflow-owned.
- §8 / L2 treated as independent constraints.

---

### RS-04 — Critical high-impact / irreversible

**Purpose:** Show Critical Process Depth for severe task hazards without treating Depth or §8 labels as interchangeable.

**Initial context**

- **Project Context:** Production data or irreversible migration surface exists.
- **Task Context:** Irreversible production data migration or equivalent severe integrity hazard.
- **Unknowns:** Full rollback feasibility may be **unknown** until assessed.

**Relevant instructions and constraints**

- L0 integrity / safety constraints where applicable.
- AGENTS.md §8 likely applicable (irreversible destruction risk; public/data impact).
- Consumer policy review-approval may apply independently.

**Illustrative task classification:** High-impact / irreversible operations.

**Process Depth and rationale:** **Critical** — severe reversibility and integrity drivers; **not** because the repository is labeled “critical” and **not** solely because §8 applies ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §4; affinity with PDM §4.7 Scenario D).

**Guidance and lifecycle state**

- Recommend maximum proportional ceremony and hazard-aware verification.
- Lifecycle stages do not authorize the irreversible operation.

**Expected agent behavior**

- Classify Critical from task hazards, not repository marketing labels.
- State that §8 approval requirement does **not** automatically equal Critical Depth, and Critical Depth does **not** authorize the operation.
- Stop for authorized approval before §8-listed actions.

**Required human decision:** Authorized actor under AGENTS.md §8 / Consumer authority before irreversible operations; separate from advisory Acceptance.

**Operational authorization boundary:** Depth label never authorizes the operation; only authorized approval does.

**Expected outcome:** Critical intensity with independent §8 path; no Depth-as-authorization confusion.

**Model references:** APC; PDM §4; AGM §9; Governance §6–§7; [`../AGENTS.md`](../AGENTS.md) §8.

**Validation criteria**

- “Needs §8 ⇒ Critical” is rejected as automatic rule.
- Critical Depth ≠ operational authorization.

---

### RS-05 — Incomplete / ambiguous Project Context

**Purpose:** Show honest handling of missing repository or Consumer facts.

**Initial context**

- **Project Context:** Partial tree inspected; architecture docs incomplete; standing constraints **unknown** / **not stated**.
- **Task Context:** Requested change stated at high level; blast radius **unknown**.
- **Unknowns:** Consumer ADRs, adopted Packs/Modules, review policy, licensing entitlements — **not stated**.

**Relevant instructions and constraints**

- Do not invent L2/L3 content.
- Do not invent L5 adopted Pack scope.
- L0–L7 known constraints still apply when evidenced.

**Illustrative task classification:** Insufficiently specified change.

**Process Depth and rationale:** Depth assessment remains provisional; uncertainty alone **MUST NOT** automatically force Critical ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md)). Prefer disclose unknowns and proportionate discovery.

**Guidance and lifecycle state**

- Prefer clarify or defer over invention (affinity with AGM §14.9).
- Missing status/provenance → **not stated** / **unknown**.
- Gaps **MUST NOT** invent L4 or L5 authority.

**Expected agent behavior**

- Label unknowns explicitly.
- **MUST NOT** infer missing Consumer decisions, policies, adopted guidance, or authorization.
- Expand discovery proportionally or ask; do not fabricate Project Context.

**Required human decision:** Clarification from Consumer/owner when decision-critical facts are missing.

**Operational authorization boundary:** Unknowns never authorize operations.

**Expected outcome:** Transparent uncertainty; no invented authority.

**Model references:** APC §7; PDM uncertainty rules; AGM §14.9; Governance §11.

**Validation criteria**

- Uses `unknown` / `not stated` language.
- No inferred Adoption, L5, or §8 grant.

---

### RS-06 — Task vs Consumer constraint conflict

**Purpose:** Show binding Consumer instructions prevailing over advisory recommendations.

**Initial context**

- **Project Context:** Consumer has an approved ADR or local policy (L2/L3) constraining approach A.
- **Task Context:** User request prefers approach A (conflicts with that ADR/policy).
- **Unknowns:** Whether the owner intends to supersede the ADR — **not stated** until asked.

**Relevant instructions and constraints**

- Binding Consumer L2/L3 within scope.
- L6 advisory recommendations **MUST NOT** silently override binding instructions ([`../AGENTS.md`](../AGENTS.md) §2; Governance §10).
- Superseding a durable Consumer decision requires confirmation from the authorized Consumer owner. AGENTS.md §8 applies independently when the proposed operation falls within its defined approval requirements.

**Illustrative task classification:** Conflicted implementation request.

**Process Depth and rationale:** Assessed from actual task hazards after conflict disclosure; Depth does not resolve precedence.

**Guidance and lifecycle state**

- Agent may explain alternatives as L6.
- Acceptance of L6 that conflicts with binding L2/L3 is not available as silent override.

**Expected agent behavior**

- Disclose the conflict; name the ADR/policy.
- Do not impose conflicting L6.
- Ask the authorized owner before durable override.

**Required human decision:** Authorized Consumer owner confirmation if durable decision would change; otherwise follow binding constraint.

**Operational authorization boundary:** Conflict disclosure does not itself authorize the override operation.

**Expected outcome:** Precedence preserved; no silent L2/L3 rewrite.

**Model references:** Contract §7; AGENTS §2, §8; Governance §10; APC ownership.

**Validation criteria**

- Binding Consumer instructions prevail within scope.
- L6 is not treated as higher authority.

---

### RS-07 — Advisory recommendation rejected

**Purpose:** Show the reject/defer path for advisory guidance.

**Initial context**

- **Project Context:** Ordinary Core-capable repository.
- **Task Context:** Meaningful change where Feature Development Workflow is recommended as L6.
- **Unknowns:** None material.

**Relevant instructions and constraints**

- L6 recommendation only; no L5 Pack in play.
- Rejection does not alter L0–L4.

**Illustrative task classification:** Feature or fix with declined process advice.

**Process Depth and rationale:** As assessed for the task (illustrative: Standard); rejection does not change Depth classification rules.

**Guidance and lifecycle state**

- Recommendation issued → Human **rejects** or defers the advisory guidance.
- No Consumer Adoption.
- Guidance **MAY** be recommended again on a later task.

**Expected agent behavior**

- Accept the rejection; do not coerce Adoption or re-label guidance as binding.
- Continue only within remaining authorized task scope and binding constraints.

**Required human decision:** Explicit reject or defer of the advisory recommendation.

**Operational authorization boundary:** Rejection grants no operational rights; Acceptance was never granted.

**Expected outcome:** Clear reject path without policy mutation.

**Model references:** AGM §9; Governance §5, §11.

**Validation criteria**

- Reject ≠ durable policy change.
- No implied Adoption or §8 effect.

---

### RS-08 — Human Acceptance without Adoption

**Purpose:** Show task-level Acceptance without durable Consumer Adoption.

**Initial context**

- **Project Context:** Core guidance available; optional Pack **not** adopted (see also RS-09 patterns).
- **Task Context:** Human Accepts recommended L6 Core (or not-adopted Pack) guidance for **this task only**.
- **Unknowns:** Future Adoption intent **not stated**.

**Relevant instructions and constraints**

- Human Acceptance authorizes task-level use of that advisory guidance within existing task authorization only ([`ADAPTIVE_GUIDANCE_MODEL.md`](ADAPTIVE_GUIDANCE_MODEL.md) §9).
- Without Consumer Adoption: no durable L3/L5 elevation.

**Illustrative task classification:** Task using accepted advisory guidance.

**Process Depth and rationale:** Independent of Acceptance vs Adoption distinction (illustrative: Standard).

**Guidance and lifecycle state**

- Recommend → **Human Acceptance** → **no** Consumer Adoption (affinity with AGM §14.10).
- Later tasks may need a fresh recommendation/Acceptance.

**Expected agent behavior**

- Treat guidance as task-level L6 use only.
- **MUST NOT** claim L3 policy or L5 Pack authority from Acceptance alone.
- Keep §8 and implementation authorization separate.

**Required human decision:** Human Acceptance for current task; Adoption explicitly absent.

**Operational authorization boundary:** Acceptance does not authorize commit, push, publish, deploy, install, or §8-listed operations.

**Expected outcome:** Accept ≠ Adopt demonstrated.

**Model references:** AGM §9–§10, §14.10; Governance §5–§7.

**Validation criteria**

- No L3/L5 elevation from Acceptance alone.
- §8 remains independent.

---

### RS-09 — Pack L6 vs L5; Module ≠ automatic L3

**Purpose:** Distinguish not-adopted Pack advice, adopted Pack scope, Pack vs Module adoption, and Module vs L3 policy.

**Initial context**

- **Project Context:** Education-related Consumer work **or** clearly labeled hypothetical future Module catalog entry.
- **Task Context:** Consider Pack guidance and/or Module guidance relevance.
- **Unknowns:** Unless stated, Pack adoption status and Module adoption status are **not stated**.

**Relevant instructions and constraints**

- **Not-adopted Pack:** advisory **L6** when Education (or Pack) context is real ([`ADAPTIVE_GUIDANCE_MODEL.md`](ADAPTIVE_GUIDANCE_MODEL.md) §9.2, §10).
- **Explicitly adopted Pack:** **L5** within approved Pack scope; still subject to L0–L4; no recurring Accept/Reject for in-scope adopted Pack rules.
- Pack adoption **MUST NOT** implicitly adopt constituent Modules.
- **Module adoption does not automatically elevate all Module content to L3** Consumer local policy ([`ADAPTIVE_GOVERNANCE_MODEL.md`](ADAPTIVE_GOVERNANCE_MODEL.md) §3).
- Education residuals (for example notebook checklists) are not general Core guidance without Education context.
- **Hypothetical** future Modules (for example a future security-engineering Module) are labeled Hypothetical and are **not** claimed as existing AIOS packages.

**Illustrative task classification:** Pack- or Module-touching advisory task.

**Process Depth and rationale:** Independent of Pack L6/L5 state (Depth ≠ adoption).

**Guidance and lifecycle state**

| State | Lifecycle meaning |
|-------|-------------------|
| Pack not adopted | L6 recommend → Accept = task use only; **no L5** |
| Pack explicitly adopted | L5 within approved scope |
| Module recommended | L6 until Consumer Adoption / local policy decision |
| Module “adopted” without L3 policy decision | Do **not** treat all Module content as automatic L3 |

**Expected agent behavior**

- State Pack adoption state or mark **not stated**.
- Keep Pack and Module adoption separate.
- Label Hypothetical Modules clearly; do not invent catalog presence.
- Do not present fictional artifacts as existing Core components.

**Required human decision:** Task Acceptance and/or explicit Consumer Adoption with approved scope — distinct decisions.

**Operational authorization boundary:** Neither Pack Acceptance nor Module recommendation installs packages or modifies Consumer repositories automatically. Licensing/access remain L0 (see RS-13).

**Expected outcome:** L6 vs L5 vs L3 boundaries preserved; Pack ≠ Module; Module ≠ auto-L3.

**Model references:** AGM §9–§10, §14.6–§14.7; Governance §3, §5; Framework Contract §5.2; Education Pack docs when Education context applies.

**Validation criteria**

- Not-adopted Pack ≠ L5.
- Pack adoption ≠ Module adoption.
- Module adoption ≠ automatic L3 for all content.
- Hypothetical labeling present where Modules are not in catalog.

---

### RS-10 — Precedence conflict (binding vs advisory)

**Purpose:** Show Instruction Precedence constraining advisory Guidance Lifecycle without merging the dimensions.

**Initial context**

- **Project Context:** Binding L4 Core default and/or adopted L5 Pack scope and/or Consumer L3 policy present.
- **Task Context:** Agent considers an L6 recommendation that would conflict with binding guidance.
- **Unknowns:** None for the binding rule itself.

**Relevant instructions and constraints**

- Instruction Precedence L0–L7 ([`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7; [`../AGENTS.md`](../AGENTS.md) §2).
- Recommendations **MUST NOT** silently override binding instructions.
- Core origin of an artifact **MUST NOT** automatically elevate L6 advisory guidance to L4.

**Illustrative task classification:** Advice vs binding rule.

**Process Depth and rationale:** Independent; Depth does not resolve precedence.

**Guidance and lifecycle state**

- Lifecycle may still describe Recommendation/Acceptance for **non-conflicting** advisory items.
- Binding L4 / in-scope adopted L5 are not recurring Accept/Reject targets for those binding rules.

**Expected agent behavior**

- Disclose binding conflict; do not present conflicting L6 as optional override of L4/L5/L2/L3.
- Keep Precedence, Lifecycle, and Authorization as separate dimensions ([`ADAPTIVE_GOVERNANCE_MODEL.md`](ADAPTIVE_GOVERNANCE_MODEL.md) §4).

**Required human decision:** Authorized owner only if a durable binding change is in scope; otherwise follow binding guidance.

**Operational authorization boundary:** Precedence resolution is not operational authorization.

**Expected outcome:** Binding wins; dimensions remain independent.

**Model references:** Contract §7; AGENTS §2; Governance §3–§4, §10; AGM §9.2.

**Validation criteria**

- No silent binding override.
- Core presence ≠ automatic L4 elevation of advisory content.

---

### RS-11 — Acceptance without §8 authorization

**Purpose:** Show Human Acceptance does not grant AGENTS.md §8 authorization.

**Initial context**

- **Project Context:** Ordinary repository.
- **Task Context:** Human Accepts L6 advisory guidance for the task; the planned work would also include an AGENTS.md §8-listed operation (for example large multi-component refactor or public-contract break).
- **Unknowns:** Whether the Accepting person is the §8-authorized actor — **not stated** / must not be assumed.

**Relevant instructions and constraints**

- [`../AGENTS.md`](../AGENTS.md) §8 remains authoritative and unchanged.
- Human Acceptance ≠ §8 authorization ([`ADAPTIVE_GOVERNANCE_MODEL.md`](ADAPTIVE_GOVERNANCE_MODEL.md) §6–§7).

**Illustrative task classification:** Accepted advice plus gated operation.

**Process Depth and rationale:** As warranted by hazards; §8 need does not automatically set Critical.

**Guidance and lifecycle state**

- Recommendation → Human Acceptance for advisory use.
- §8 authorization still missing until an authorized actor grants it.

**Expected agent behavior**

- Allow task-level use of accepted advisory guidance only within existing task authorization.
- **MUST NOT** proceed with the §8-listed operation until authorized.
- **MUST NOT** assume the person who Accepted guidance is the §8-authorized actor.

**Required human decision**

- Human Acceptance (advisory) — possibly already given.
- Separate §8 authorization from an **authorized** actor.

**Operational authorization boundary:** Only the authorized actor may grant §8 authorization; Acceptance never substitutes.

**Expected outcome:** Clear Accept ≠ §8 split.

**Model references:** AGENTS §8; Governance §6–§7; AGM §9.

**Validation criteria**

- Acceptance and §8 are separate decisions.
- No automatic authority by reviewer title alone.

---

### RS-12 — Review / Release vs publication

**Purpose:** Preserve Workflow review, Release Approval, and operational authorization as distinct decisions.

RS-12 contains exactly two subcases. **RS-12a** and **RS-12b** are **not** independent scenario IDs.

#### RS-12a — Feature Development review vs operational authorization

**Purpose:** Show Feature Development Stage 8 / checklist `review` completion means reviewed — not operational authorization.

**Initial context**

- **Project Context:** Feature Development Workflow in use.
- **Task Context:** Change has completed Stage 8 review path appropriate to risk.
- **Unknowns:** Operational authorization for commit/tag/push/publish/deploy — **not stated** unless separately granted.

**Relevant instructions and constraints**

- [`../workflows/feature_development.md`](../workflows/feature_development.md) Stage 8: completion of checklist `review` means the change has been **reviewed**; it does **not** mean Release Approval, replace Release Workflow Stage 7, or grant operational authorization (commit, tag, push, publish, deploy).
- Applicable §8 approvals must be obtained before the relevant operation, not retroactively.

**Illustrative task classification:** Feature Development close-out review.

**Process Depth and rationale:** Independent of review-vs-ops distinction.

**Guidance and lifecycle state:** Review completion is not Human Acceptance of advisory guidance and not Consumer Adoption.

**Expected agent behavior**

- Record review outcome truthfully.
- **MUST NOT** treat review completion as authorization to commit, tag, push, publish, or deploy.

**Required human decision:** Review outcome / light-review path as applicable; separate ops authorization when operations proceed.

**Operational authorization boundary:** Review ≠ operational authorization.

**Expected outcome:** Reviewed change without implied publish/commit authority.

**Model references:** Feature Development Stage 8; [`../checklists/review.md`](../checklists/review.md); Governance §8; AGM §14.4 (partial).

**Validation criteria**

- Review completion does not authorize commit/tag/push/publication/deployment.
- §8 prior-approval timing preserved.

#### RS-12b — Release Approval vs publication authorization

**Purpose:** Show Release Stage 7 go/no-go/defer ≠ Stage 8 operational publication actions.

**Initial context**

- **Project Context:** Release Workflow in scope.
- **Task Context:** Stage 7 human release decision recorded (go / no-go / defer).
- **Unknowns:** Explicit Stage 8 operational authorization for each tag/push/publish/deploy action — **not stated** unless granted.

**Relevant instructions and constraints**

- [`../workflows/release.md`](../workflows/release.md): Stage 7 Release Approval is distinct from Stage 8 operational authorization.
- Completing Stage 7 does **not** mark Stage 8 authorized.
- Feature Development completion does **not** authorize release (affinity with AGM §14.4).
- Process Depth ≠ Release class ([`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md) §5.2).

**Illustrative task classification:** Release decision / publication path.

**Process Depth and rationale:** Not mapped to Release class.

**Guidance and lifecycle state:** Release decision and publication authorization are **not** Human Acceptance of guidance.

**Expected agent behavior**

- Treat go decision as release decision only.
- **MUST NOT** perform or assume tag, push, publish, or deploy without prior operational authorization.
- Skip Stage 8 on explicit no-publish paths.

**Required human decision:** Stage 7 release decision; separate Stage 8 operational authorizations when publication is in scope.

**Operational authorization boundary:** Stage 7 ≠ Stage 8.

**Expected outcome:** Clear Release Approval vs publication split.

**Model references:** Release Workflow Stages 7–8; [`../checklists/release_checklist.md`](../checklists/release_checklist.md); Governance §8; AGM §14.4; PDM §5.2.

**Validation criteria**

- Go/no-go/defer does not itself authorize Stage 8 actions.
- Depth is not equated with Release class.

---

### RS-13 — Licensing / access as L0

**Purpose:** Keep licensing, legal, access, entitlement, and distribution restrictions under Instruction Precedence L0 — not as a fourth governance dimension and not as lifecycle grants.

**Initial context**

- **Project Context:** Third-party or entitlement-bearing content **may** apply; exact license terms might be **unknown**.
- **Task Context:** Recommendation or Adoption of Pack/Module-like guidance is considered.
- **Unknowns:** Entitlement status **unknown** unless evidenced.

**Relevant instructions and constraints**

- Applicable licensing/legal/access/entitlement/distribution restrictions are **L0** where applicable ([`ADAPTIVE_GOVERNANCE_MODEL.md`](ADAPTIVE_GOVERNANCE_MODEL.md) §12; [`ADAPTIVE_GUIDANCE_MODEL.md`](ADAPTIVE_GUIDANCE_MODEL.md) §9.5).
- Recommendation, Human Acceptance, and Consumer Adoption **MUST NOT** grant licensing, access, purchase, entitlement, or distribution rights.
- Consumer Adoption **MUST NOT** override applicable licensing terms.

**Illustrative task classification:** Guidance use involving rights-sensitive content.

**Process Depth and rationale:** Independent of licensing grants.

**Guidance and lifecycle state**

- Lifecycle decisions may proceed only as advice/acceptance/adoption **records** — never as license grants.
- Blocking unknown rights → do not proceed with restricted use.

**Expected agent behavior**

- Separate lifecycle talk from rights talk.
- Mark entitlement unknowns; do not invent license grants.
- Treat applicable restrictions as L0 constraints.

**Required human decision:** Compliance / procurement decisions under Consumer and legal process — outside Acceptance semantics.

**Operational authorization boundary:** Lifecycle stages do not authorize redistribution or entitled install.

**Expected outcome:** L0 rights model preserved; no fourth axis.

**Model references:** AGM §9.5; Governance §4, §12; Contract §7.

**Validation criteria**

- Licensing remains under L0.
- Accept/Adopt ≠ rights grant.

---

### RS-14 — Urgent task; governance gates still apply

**Purpose:** Show urgency does not reduce Process Depth or waive L0 / §8 requirements.

**Initial context**

- **Project Context:** Production pressure or deadline narrative present.
- **Task Context:** Urgent request that still implicates meaningful risk and possibly §8-listed operations.
- **Unknowns:** None required for the urgency rule itself.

**Relevant instructions and constraints**

- Urgency **MUST NEVER** waive L0 constraints or AGENTS.md §8 gates ([`ADAPTIVE_PROJECT_CONTEXT.md`](ADAPTIVE_PROJECT_CONTEXT.md); [`PROCESS_DEPTH_MODEL.md`](PROCESS_DEPTH_MODEL.md)).
- Urgency must not reduce Process Depth or waive applicable Consumer mandatory controls.

**Illustrative task classification:** Time-critical change.

**Process Depth and rationale:** Assessed from actual dimensional hazards — **not** lowered solely because the request is urgent.

**Guidance and lifecycle state**

- Advisory lifecycle may continue.
- Lifecycle completion does not waive gates.

**Expected agent behavior**

- Acknowledge urgency without lowering Depth solely for speed theater.
- Still surface §8 / L0 requirements.
- Refuse to treat urgency as authorization.

**Required human decision:** Same authorized approvals as without urgency when gates apply.

**Operational authorization boundary:** Urgency grants no operational authorization.

**Expected outcome:** Gates and Depth integrity under pressure.

**Model references:** APC urgency rules; PDM urgency rules; Governance §10; AGENTS §8.

**Validation criteria**

- Urgency does not auto-reduce Depth.
- Urgency does not waive L0 or §8.

---

## 6. Hypothetical and unknown handling

| Situation | Required treatment |
|-----------|-------------------|
| Missing Consumer ADR/policy/adoption/auth | `unknown` or `not stated` — do not infer |
| Future Module packages | Label **Hypothetical**; not existing catalog facts |
| Education Pack residuals | Require real Education context; not automatic general Core guidance |
| Incomplete guidance metadata | Prefer clarify/defer; no invented L4/L5 |

---

## 7. Traceability to AGM §14 and PDM §4.7

AGM §14 and PDM §4.7 remain **model-specific illustrative examples**. This suite provides **integrated cross-model** scenarios. Existing examples are **not** copied, removed, or rewritten here. Discoverability pointers in those documents are deferred to Phase **6.6.4**.

| Existing example | Primary RS mapping |
|------------------|-------------------|
| PDM §4.7 Scenario A — README typo | RS-01 |
| PDM §4.7 Scenario B — Ordinary bug fix | RS-02 |
| PDM §4.7 Scenario C — Public API rename | RS-03 |
| PDM §4.7 Scenario D — Irreversible data migration | RS-04 |
| AGM §14.1 Trivial documentation fix | RS-01 |
| AGM §14.2 Feature Development — Standard | RS-02 |
| AGM §14.3 Feature Development — Enhanced | RS-03 |
| AGM §14.4 Release task | RS-12 (esp. RS-12b); related RS-12a |
| AGM §14.5 Multiple Guidance Types | RS-02 |
| AGM §14.6 Optional Module (hypothetical) | RS-09 |
| AGM §14.7 Pack not adopted vs adopted | RS-09 |
| AGM §14.8 Community/Third-party Module | RS-09 (provenance themes; Hypothetical) |
| AGM §14.9 Incomplete guidance information | RS-05 |
| AGM §14.10 Accepted but not adopted | RS-08 |

---

## 8. Non-goals

This document does **not** establish or claim:

- Adaptive engine, registry, resolver, scoring, or ML classification
- Automatic Module/Pack installation or Consumer repository modification
- New Human Approval Policies or AGENTS.md §8 changes
- Framework Contract §5.6 rewrite (remains deferred)
- Replacement of AGM §14 or PDM §4.7
- `aiosctl sync` behavior changes
- Phase 6 or Phase 6.6 completion

---

## 9. Document maintenance

- Status remains `Draft` until Product Owner accepts Phase 6.6 documentation delivery.
- Cross-document alignment (ROADMAP, PROJECT_STRUCTURE, Related entry points, APC/AGM/PDM/Governance pointers) belongs to Phase **6.6.4**.
- When Guidance Lifecycle semantics change, update [`ADAPTIVE_GUIDANCE_MODEL.md`](ADAPTIVE_GUIDANCE_MODEL.md) first; then align scenarios.
- When Process Depth or Workflow eligibility changes, update PDM / Workflows first; then align RS-01 and related scenarios.

End of Adaptive Reference Scenarios v0.1.0 (`Draft`).
