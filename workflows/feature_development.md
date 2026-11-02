# Feature Development Workflow

| Field | Value |
|-------|-------|
| `id` | `feature-development` |
| `title` | Feature Development Workflow |
| `status` | `draft` |
| `version` | `0.1.0` |
| `scope` | `core` |
| `summary` | A stack-agnostic workflow for analyzing, designing, implementing, validating, and handing over engineering changes. |

This document is a Core Workflow **definition**. It follows [`../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md`](../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md).

**Authority:** Core Workflow guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** constraints. Instruction precedence remains Framework Contract §7 / [`../AGENTS.md`](../AGENTS.md) §2. AI recommends; humans decide. Durable architectural and product decisions belong to the Consumer.

**RDIV relationship:** [`../methodology/rdiv.md`](../methodology/rdiv.md) remains the authoritative methodology. This Workflow **orchestrates** RDIV for Feature Development — it does not redefine or duplicate RDIV:

| RDIV phase | This Workflow |
|------------|---------------|
| Review | Stages 1–2 |
| Decide | Stages 3–5 |
| Implement | Stage 6 |
| Verify | Stages 7–9 |

Human approval gates in [`../AGENTS.md`](../AGENTS.md) §8 remain authoritative. This Workflow introduces no new approval policies or governance levels.

---

## 1. Purpose

Provide a reusable, stack-agnostic sequence for engineering changes — from understanding the request through handover — so agents and humans can apply RDIV consistently without assuming a language, framework, CI platform, or product process.

Definitions live here as Core guidance. Filled run records and Consumer-local adaptations remain Consumer-owned.

---

## 2. Prerequisites

Before starting:

- A clear task or change request is available (explicit user / owner instruction for the current work).
- Applicable Consumer ADRs, local policies, and repository constraints can be discovered or are known to be absent.
- Contributors will treat this Workflow as **L6 recommendation** unless the Consumer has explicitly adopted it as local policy (**L3**).
- No assumption that a workflow engine, CLI executor, or automated stage runner exists.

Adjust ceremony to change size: trivial documentation-only or clearly scoped fixes may use the conditional light paths below; significant or architectural work must not skip analysis merely because the task looks small ([`../AGENTS.md`](../AGENTS.md) §5).

---

## 3. Stages

### 1. Request and Scope Analysis

- **Classification:** Required
- **Intent:** Restate the request, intended outcome, in-scope / out-of-scope boundaries, and known constraints before deeper discovery.
- **Inputs:** Task description; any linked issues or owner notes; known L0 / Consumer constraints if already stated.
- **Outputs:** Explicit scope statement; out-of-scope list; initial risk / uncertainty notes.
- **Checklist references:** _(none in this version)_
- **Approval required:** no
- **Approver role:** n/a
- **Evidence expectations:** Scope and exclusions are written clearly enough that a reviewer can judge fit to the request.
- **Completion criteria:** Request restated; scope and non-goals for this change are explicit; conflicts with stated constraints are named if already visible.

### 2. Repository and Context Discovery

- **Classification:** Required for meaningful engineering work. **Conditional light / skip** only when the change is trivial (for example documentation-only typo) **and** repository risk is negligible — record a short rationale if skipping deep discovery.
- **Intent:** Understand current repository structure, relevant existing behavior, documentation, and risks before deciding (RDIV Review; see also [`../methodology/repository_onboarding.md`](../methodology/repository_onboarding.md) and [`../methodology/architecture_first.md`](../methodology/architecture_first.md)).
- **Inputs:** Scope from Stage 1; repository tree; relevant docs, tests, and prior decisions when present.
- **Outputs:** Context notes (relevant paths, patterns, constraints); risk assessment appropriate to change size.
- **Checklist references:** _(none in this version)_
- **Approval required:** no
- **Approver role:** n/a
- **Evidence expectations:** Discovery depth matches risk; assumptions are labeled as assumptions.
- **Completion criteria:** Relevant context and risks are stated; no significant implementation proceeds on unexamined repository state for non-trivial work.

### 3. Requirements and Acceptance Criteria

- **Classification:** Required for new features or behavior changes. **Optional / light** for pure refactors or small fixes when acceptance criteria are already explicit and unchanged.
- **Intent:** Make expected outcomes and acceptance checks explicit without turning Consumer product decisions into Core mandates.
- **Inputs:** Scope; repository context; Consumer requirements / ADRs when they exist.
- **Outputs:** Acceptance criteria (or pointer to Consumer-owned criteria); open questions for the owner when criteria are missing.
- **Checklist references:** _(none in this version)_
- **Approval required:** no for drafting criteria; **yes** when durable Consumer product requirements would be created or changed without an existing owner decision — then obtain authorized Consumer confirmation ([`../AGENTS.md`](../AGENTS.md) §8)
- **Approver role:** Consumer owner / authorized product decision-maker when durable requirements change
- **Evidence expectations:** Criteria are testable or reviewable; ownership of product decisions remains with the Consumer.
- **Completion criteria:** Acceptance criteria are agreed or explicitly deferred with owner awareness; Core does not invent binding product policy.

### 4. Architecture and Design

- **Classification:** **Conditional required** when the change affects architecture, public contracts, module boundaries, data compatibility, or top-level conventions. Otherwise **light or skip** with rationale (integrate with existing design; see [`../methodology/architecture_first.md`](../methodology/architecture_first.md)).
- **Intent:** Choose how the change fits the existing architecture; identify design options and impacts before coding.
- **Inputs:** Acceptance criteria; repository architecture and Consumer ADRs (**L2**).
- **Outputs:** Design approach; impact notes; ADR recommendation only when a durable architectural decision is needed (ADR content remains Consumer-owned).
- **Checklist references:** _(none in this version)_
- **Approval required:** **yes** when introducing or superseding durable architecture / public contract decisions, or when an operation on the [`../AGENTS.md`](../AGENTS.md) §8 list applies; otherwise no
- **Approver role:** Consumer owner / authorized architecture decision-maker when approval is required
- **Evidence expectations:** Fit to existing architecture is explained; conflicts with ADRs or local policy are disclosed before proceeding.
- **Completion criteria:** Design direction is clear for the planned implementation; required approvals obtained when applicable; no silent ADR override.

### 5. Implementation Planning

- **Classification:** Required for meaningful work. **Light** for small, clearly scoped fixes (short ordered step list is enough).
- **Intent:** Sequence the work, name touched areas, and confirm the plan before implementation (RDIV Decide).
- **Inputs:** Scope; acceptance criteria; design direction.
- **Outputs:** Implementation plan (steps, touched paths/components, test/validation approach at plan level).
- **Checklist references:** _(none in this version)_
- **Approval required:** no for ordinary plans; **yes** when the plan itself requires an AGENTS §8 operation (for example repository-wide restructuring) before execution
- **Approver role:** Consumer owner / authorized reviewer when approval is required
- **Evidence expectations:** Plan stays inside approved scope; unrelated refactors are excluded.
- **Completion criteria:** Ordered plan exists at a depth matching risk; ready to implement without inventing out-of-scope structure.

### 6. Implementation

- **Classification:** Required when repository changes will be made. Skip only if the Workflow stops after Decide with an explicit no-change outcome.
- **Intent:** Apply the approved plan with minimal scoped changes (RDIV Implement). Prefer existing architecture and Consumer decisions ([`../methodology/ai_collaboration.md`](../methodology/ai_collaboration.md)).
- **Inputs:** Ready implementation plan, with applicable prior approvals obtained; design constraints; repository files in scope.
- **Outputs:** Implementation changes limited to the plan; notes on deviations if any (deviations that affect durable decisions need re-approval).
- **Checklist references:** _(none in this version)_
- **Approval required:** no for executing an already authorized plan; stop and obtain approval if mid-flight work expands into AGENTS §8 territory
- **Approver role:** Consumer owner / authorized reviewer if scope expands
- **Evidence expectations:** Diff matches plan and scope; no secrets committed; no silent consumer-policy rewrite.
- **Completion criteria:** Planned changes applied (or explicitly abandoned); out-of-scope edits avoided; durable Consumer artifacts unchanged unless approved.

### 7. Testing and Validation

- **Classification:** Required for code or behavior changes. **Light** for documentation-only changes (verify docs accuracy and links as appropriate).
- **Intent:** Confirm the change meets acceptance criteria and does not break relevant consistency (RDIV Verify). Do not claim unrun tests as passed.
- **Inputs:** Implementation; acceptance criteria; existing tests or validation practices in the Consumer repository when present.
- **Outputs:** Validation results or an honest statement of what was and was not run; residual risks.
- **Checklist references:** _(none in this version)_
- **Approval required:** no
- **Approver role:** n/a
- **Evidence expectations:** Evidence matches what was actually performed; tool/stack choices remain Consumer-specific (this Workflow does not mandate a test framework).
- **Completion criteria:** Acceptance criteria addressed or gaps disclosed; validation status is truthful.

### 8. Review and Human Approval

Stage 8 is the final review and approval stage. It does not replace or defer approvals required before an operation. Any approval required by [`../AGENTS.md`](../AGENTS.md) §8 must be obtained at the relevant earlier stage, before the operation is performed. Final review does not retroactively authorize an operation performed without required prior approval.

Completion of checklist `review` means the change has been **reviewed** under that definition. It does **not** mean Release Approval, replace Release Workflow Stage 7, or grant operational authorization (commit, tag, push, publish, deploy).

- **Classification:** **Required** when any AGENTS §8 approval-listed operation applies, when durable Consumer decisions changed, or when the Consumer’s adopted review policy requires it. Otherwise **light review** (peer or owner skim appropriate to risk) without inventing a new Core approval policy.
- **Intent:** Human confirmation that the change is acceptable before treating the Workflow as complete for durable or high-impact work.
- **Inputs:** Diff; validation notes; design/ADR impacts; applicable Consumer review policy.
- **Outputs:** Review outcome; explicit approvals when required; recorded rationale for any Consumer-authorized waiver of Consumer process items (waivers must not override L0, L2 ADRs, or applicable L3 policy).
- **Checklist references:** Checklist id: `review` — Definition: [`Review Checklist`](../checklists/review.md)
- **Approval required:** **yes** when AGENTS §8 or durable Consumer decision changes apply; otherwise per Consumer policy / light review
- **Approver role:** Consumer owner / authorized reviewer (role-based, not a personal mailbox mandated by Core)
- **Evidence expectations:** Required approvals are explicit; conflicts previously disclosed are resolved or accepted by the authorized owner.
- **Completion criteria:** Required human approvals obtained when applicable; applicable Review Checklist items satisfied or validly waived when this stage uses the checklist; light-review path documented when used for low-risk work.

### 9. Completion and Handover

- **Classification:** Required (short). Artifact depth follows Consumer process.
- **Intent:** Close the loop: summarize outcome, point to evidence, and hand over residual risks or follow-ups.
- **Inputs:** Review outcome; validation notes; final diff or change description.
- **Outputs:** Completion summary; handover notes (follow-ups, known gaps); pointers to Consumer-owned records when used.
- **Checklist references:** _(none in this version)_
- **Approval required:** no unless Consumer local policy requires a formal close-out sign-off
- **Approver role:** Consumer owner when their policy requires close-out approval
- **Evidence expectations:** Summary matches what was actually done; no false claim of engine-run stages or unrun validation.
- **Completion criteria:** Outcome and residual risks are stated; Workflow run is finished from a process perspective; filled records remain Consumer-owned if created.

---

## 4. Completion criteria

The Feature Development Workflow may be treated as complete when:

1. Stages required for the change class were completed (or explicitly and justifiably light-pathed / skipped under the classifications above).
2. Acceptance criteria for the change are met or residual gaps are disclosed to the authorized owner.
3. Required human approvals under [`../AGENTS.md`](../AGENTS.md) §8 and applicable Consumer policy were obtained.
4. No L0 constraint was violated; Consumer ADRs (**L2**) and applicable local policies (**L3**) were respected or conflicts were disclosed and resolved by authorized owners.
5. Handover summary exists at a depth appropriate to the change.

Completeness of this Core **definition** does not imply an automated run, CI green claim, or Consumer release.

---

## 5. Related methodologies

Link only — do not duplicate:

- [`../methodology/rdiv.md`](../methodology/rdiv.md) — authoritative RDIV methodology (Review → Decide → Implement → Verify)
- [`../methodology/architecture_first.md`](../methodology/architecture_first.md) — understand structure before changing it
- [`../methodology/ai_collaboration.md`](../methodology/ai_collaboration.md) — AI assists; human decides
- [`../methodology/repository_onboarding.md`](../methodology/repository_onboarding.md) — starting from repository understanding
- [`../methodology/model_agnostic.md`](../methodology/model_agnostic.md) — governance independent of a single model vendor

Operational gates and precedence: [`../AGENTS.md`](../AGENTS.md).
Concept meanings and L0–L7: [`../docs/FRAMEWORK_CONTRACT.md`](../docs/FRAMEWORK_CONTRACT.md).
Authoring rules: [`../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md`](../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md).

---

## 6. Non-goals

This Workflow does **not**:

- Implement or require a workflow execution engine
- Provide automatic stage transitions or branching
- Use YAML frontmatter or a runtime parser
- Define a checklist instance schema
- Authorize automatic Consumer repository modifications
- Authorize automatic Module or Pack adoption
- Authorize dependency installation
- Authorize automatic Git commit or push
- Replace Consumer ADRs, product decisions, or existing methodologies (including RDIV)
- Mandate a programming language, framework, test tool, or CI platform
- Elevate Core Feature Development guidance above L6 unless the Consumer explicitly adopts it as local policy

---

End of Feature Development Workflow `feature-development` v0.1.0 (`draft`).
