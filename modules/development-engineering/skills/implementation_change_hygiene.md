# Implementation Change Hygiene Skill

| Field | Value |
|-------|-------|
| `id` | `implementation-change-hygiene` |
| `title` | Implementation Change Hygiene |
| `status` | `draft` |
| `version` | `0.2.0` |
| `scope` | `module` |
| `summary` | Advisory guidance for scope fidelity, change hygiene, and plan-to-diff consistency during and after AI-assisted implementation — without authorizing out-of-scope edits or replacing Core workflows. |
| `owner_role` | `module-author` |

This document is a Module Skill **definition** for the `development-engineering` Module. It follows [`../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md`](../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md).

**Authority:** Module Skill guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** constraints. Instruction precedence remains Framework Contract §7 / [`../../../AGENTS.md`](../../../AGENTS.md) §2. AI recommends; humans decide. Durable architectural and product decisions belong to the Consumer.

This Skill is **analytical and advisory**. It is not a Skill runner, Workflow orchestrator, Checklist, Prompt collection, or Knowledge article. Presence of this file does not adopt, install, or enable the Module.

---

## 1. Purpose

Provide a reusable, stack-agnostic capability that helps humans and agents keep AI-assisted implementation **inside an already approved scope**, maintain **plan-to-diff traceability**, and practice **change hygiene** — without opportunistic churn and without silent scope expansion.

This Skill does **not** orchestrate feature delivery, define or rewrite implementation plans, impose coding standards, redesign architecture, or authorize repository modifications.

---

## 2. Intended outcome

Depending on mode (see §4):

- **active-hygiene:** lightweight advisory escort while an already authorized in-scope implementation proceeds — fidelity monitoring, discovery classification, honest close-out.
- **review:** a structured **Implementation Change Hygiene Report** in the assistant response (default) that compares approved scope/plan to observed changes.

Both modes:

- Separate **facts**, **inferences**, and **recommendations**
- Classify discoveries as **F1 / F2 / F3** (see §3)
- Name missing context honestly
- Never independently authorize additional changes

The Skill must **not** independently create, save, or modify report files in a Consumer repository. Persisting a report as a file requires a separate explicit request and applicable authorization.

The outcome is advisory findings — not automatic fixes and not Core Review Checklist completion.

---

## 3. Authority model

| Layer | Meaning for this Skill |
|-------|------------------------|
| **L1** | Explicit task authorization for the **current** task, limited to the **approved task scope**. |
| **L6** | This Skill’s advisory guidance. It grants **no** additional authority. |
| **L0 / AGENTS §8** | Non-overridable safety and listed approval boundaries. Applicable stop behavior when crossed. |

**L1 does not authorize changes outside the approved task scope.**

This Skill never independently authorizes additional edits, commits, pushes, publishes, deployments, installs, or scope expansions.

### Finding classification (F1 / F2 / F3)

| Class | Definition | Required behavior |
|-------|------------|-------------------|
| **F1 — Unrelated, non-blocking** | Observation unrelated to the approved task that does **not** block safe/valid completion of that task | **Disclose** it. Do **not** silently expand scope. **Continue** the original authorized in-scope task when doing so remains safe and valid. |
| **F2 — Blocking for approved task** | Missing/contradictory scope or plan, or other issue that prevents safe or correct completion of the approved task | **Clarify or escalate**. Do **not** claim completion while unresolved. |
| **F3 — Authorization or safety boundary** | Crosses L0, AGENTS §8, secrets handling, durable Consumer artifact edits without approval evidence, publish/deploy, or similar | Apply the **applicable stop** behavior. Do not proceed with the forbidden operation. |

---

## 4. Operating modes

### `active-hygiene`

Lightweight **advisory** guidance accompanying an **already authorized** implementation task (L1 within approved scope).

- Does **not** grant file modification authority
- Does **not** execute changes independently
- Does **not** replace Core Feature Development Stage 5 (Implementation Planning) or Stage 6 (Implementation)
- Does **not** introduce another approval layer for already authorized **in-scope** work
- **Does** monitor scope fidelity and change hygiene during implementation
- **Does** classify discoveries as F1/F2/F3 and apply §3

### `review`

**Read-only** review of existing change evidence against approved scope and plan (when available).

- Default mode when the requester asks for hygiene / plan-to-diff review
- Does not modify the repository as part of the Skill

---

## 5. When to use

- Scoped code or behavior implementation is in progress or recently completed
- Diff fidelity to an approved scope or plan needs reinforcement
- Opportunistic refactors, drive-by formatting, or unrelated structural edits are a material risk
- As supporting analysis for Feature Development implementation or review stages **without** replacing the Workflow or Core Review Checklist

---

## 6. When not to use

- The primary need is architecture boundary or structural-fit assessment — use [`../../architecture-engineering/skills/architecture_boundary_review.md`](../../architecture-engineering/skills/architecture_boundary_review.md)
- The primary need is general repository discovery — use Core [`../../../skills/repository_analysis.md`](../../../skills/repository_analysis.md)
- Release, publish, tag, or deploy work — use Core Release Workflow
- No approved scope can be obtained and inventing one would be required
- The requester expects automatic fixes, commits, coding-style enforcement, or out-of-scope edits “because L1 said implement”
- The Consumer forbids external development guidance by policy

---

## 7. Scope ownership

This Skill **consumes** the approved scope and implementation plan from the **Core Feature Development Workflow** (especially Stage 1 scope outputs and Stage 5 plan outputs, or equivalent Consumer-provided artifacts).

It **must not**:

- Recreate Feature Development Stage 1
- Independently define or expand scope
- Rewrite the approved implementation plan
- Override Core Workflow decisions

It **may**:

- Check whether approved scope and plan are available
- Identify contradictions or missing information (**F2** when blocking)
- Track plan-to-diff fidelity
- Report deviations

---

## 8. Inputs

Required (as available; do not invent):

- Approved scope statement (and explicit non-goals when stated) — **consumed**, not authored here
- For `review`: inspectable change evidence (diff, patch, PR file list, or equivalent) the operator is authorized to view
- Review questions / focus from the requester
- Known constraints (read-only requirement, time box, paths to exclude)

Optional when present (**do not invent**):

- Implementation plan (Core Stage 5 or equivalent)
- Acceptance criteria
- Notes on prior approvals already obtained
- Consumer coding standards or local policy (conflict disclosure only)

**Missing context:**

- If scope cannot be determined → **F2**: stop and ask; do not invent scope
- If plan is missing → mark **plan unavailable**; continue with scope↔change review only; never fabricate a plan
- If `review` mode and no diff/change evidence → stop and ask

---

## 9. Outputs

Primary output: an **Implementation Change Hygiene Report** in the assistant response (unless the requester separately authorizes a Consumer-owned file artifact), and/or during `active-hygiene` a concise close-out covering the same honesty rules.

Label each material claim as:

| Label | Meaning |
|-------|---------|
| **Fact** | Directly observed in scope text, plan text, or change/diff evidence |
| **Inference** | Reasonable interpretation; uncertainty stated |
| **Recommendation** | Advisory suggestion for human decision; not an implemented fix and not authorization |

Unavailable sections must be marked **unavailable**, **not found**, or **unverified** — do not invent content to fill the template.

### Recommended report structure

1. Executive Summary (include F1/F2/F3 findings if any)
2. Approved Scope and Plan Status (consumed inputs)
3. Evidence Examined / Change Ownership Notes
4. Scope Fidelity Findings
5. Change Hygiene Findings
6. Plan-to-Diff Consistency
7. Accidental / Unexpected Change Handling
8. Recommendations for Human Decision
9. Limitations and Missing Context
10. Validation Disclosure (what was run vs unrun; **unrun ≠ passed**)

---

## 10. Operating principles (`active-hygiene`)

Keep these lightweight — do **not** duplicate Core Stage 5–6 procedure bodies:

1. Bind work to the **consumed** approved scope and plan.
2. Prefer minimal in-scope edits; avoid opportunistic refactors and unrelated formatting sweeps.
3. Keep a mental/plan-step → path trace for material edits.
4. On discovery, classify **F1 / F2 / F3** before acting.
5. Close with honest changed-path and validation disclosure.

---

## 11. Procedure (`review` — canonical)

Perform steps in order. Adjust depth to change size and requester goals. Prefer evidence over assumptions. **Default mode: read-only review.**

### Step 1 — Scope intake (consume)

- Restate the **approved** scope and stated non-goals from Core/Consumer inputs
- Record in-scope / out-of-scope boundaries for this review
- If scope is missing or contradictory, classify **F2** and ask — do not invent scope

### Step 2 — Plan intake (consume)

- If an implementation plan is provided or clearly present, record it as an input
- If none is available, mark **plan unavailable** and proceed without inventing one
- Do not redefine or silently rewrite the plan

### Step 3 — Diff and evidence intake

- Inspect only authorized change evidence
- Distinguish, when possible: changes made by the **current agent** vs **pre-existing / externally supplied** changes in the inspected diff
- List material paths/hunks examined at a depth matching risk
- Cite file paths; add line references or ranges when available and useful
- **Never invent line numbers** or unobserved hunks

### Step 4 — Scope fidelity review

- Map observed changes to approved scope
- Identify unrelated or opportunistic edits when evidence supports the claim
- Distinguish **necessary supporting changes** from **scope expansion**; label supporting-necessary claims as **Inference** unless explicitly documented in scope/plan
- Do not claim a change is out of scope without pointing to scope text and change evidence

### Step 5 — Change hygiene review

- Look for potentially unnecessary refactoring relative to stated outcome
- Detect unrelated formatting-only or structural churn when evidenced
- Evaluate proportionality: is the change set sized to the request?
- Note unintended behavior-change signals only when supported by evidence (do not claim runtime proof that was not observed)
- Prefer “unexplained relative to approved scope/plan” over unsupported “unnecessary”

### Step 6 — Plan-to-diff consistency review

- When a plan exists: identify missing plan items, unexpected additions, and unexplained deviations
- When plan is unavailable: mark this section **N/A — plan unavailable** (scope fidelity may still apply)
- Do not invent plan steps to force a consistency narrative

### Step 7 — Accidental out-of-scope change handling

See §12.

### Step 8 — Findings synthesis

- Prioritize findings by impact and confidence
- Tag material discoveries **F1 / F2 / F3**
- Keep **Fact**, **Inference**, and **Recommendation** distinct
- Present recommendations as options for human owners
- Do not treat recommendations as authorized work

### Step 9 — Limitations, missing context, validation disclosure

- State what was not inspected
- State missing scope, plan, or diff evidence
- State truncated steps when time-boxed
- State which validations were **run** vs **unrun**; never represent unrun checks as passed

---

## 12. Accidental out-of-scope changes

Explicitly distinguish:

| Source | Meaning |
|--------|---------|
| **Current-agent change** | Edit introduced by the current agent under the present task |
| **Pre-existing / external** | Already present in an inspected diff or supplied by another party |

Rules:

- Do **not** silently retain, expand, or automatically revert unexpected changes.
- If the **current agent** made an out-of-scope change:
  1. **Disclose** it (Fact: path + known change).
  2. **Avoid further unauthorized changes**.
  3. **Restore** only when ownership is unambiguous, restoration is safe, and doing so cannot overwrite pre-existing or user work.
  4. Otherwise **stop** the affected operation and request direction (**F2** or **F3** as applicable).
- If the unexpected change is **pre-existing/external**, disclose and recommend human direction; do not claim authorship or auto-revert.

---

## 13. Review criteria

Use as evidence-oriented questions — not as a coding-standard law:

- Is each material change traceable to approved scope or an explicit plan step?
- Are there unrelated files or behaviors relative to the stated outcome?
- Is a “supporting” change justified with evidence, or unlabeled scope expansion?
- Do wide refactors or formatting-only sweeps lack a stated need?
- When a plan exists, are plan items omitted without disclosure?
- Do secrets or durable Consumer artifact edits appear without clear approval evidence?
- Were F1 findings disclosed without unnecessary interruption of valid in-scope work?
- Were F2/F3 handled with clarify/stop rather than silent continuation?

Do **not** require a numerical quality score. Do **not** mandate a language, framework, or style guide.

---

## 14. Evidence rules

- For material **facts**, cite relevant repository paths and line references/ranges when available and useful
- Never invent line numbers, hunks, test results, or approval records
- Do not present inferences as facts
- Do not claim tests, scans, or certifications that were not performed
- **Unrun ≠ passed**
- If secrets, credentials, tokens, or private keys appear: report that sensitive material appears present and needs human handling — do **not** dump or paraphrase secret values

---

## 15. Constraints and failure considerations

This Skill must **not** independently:

- Grant file modification authority (including in `active-hygiene`)
- Modify repository files as part of the Skill definition’s authority
- Apply automatic fixes or refactors as part of the Skill
- Create, save, or overwrite Consumer report files without separate explicit request and authorization
- Install packages or dependencies
- Create commits, branches, or tags
- Push, publish, or deploy
- Rewrite Consumer ADRs, coding standards, or architecture decisions
- Impose a coding style or target architecture
- Independently authorize additional changes

Do not treat this Skill as:

- A substitute for Core Feature Development Workflow orchestration
- A replacement for Core [`../../../checklists/review.md`](../../../checklists/review.md)
- A substitute for Architecture Boundary Review
- A general code-review framework or testing framework
- A Skill runner, CLI executor, or automatic adoption mechanism
- Security approval or compliance certification

**Failure / uncertainty handling:**

- Scope cannot be established → **F2**, ask
- Change evidence cannot be inspected in `review` → ask
- Plan missing → mark unavailable; do not invent
- “Unnecessary” cannot be evidenced → say unexplained / unverified
- Time-boxed → state truncated steps in Limitations

---

## 16. Human approval and decision boundaries

Human approval gates in [`../../../AGENTS.md`](../../../AGENTS.md) §8 remain authoritative. This Skill creates **no** new approval authority and no new governance level.

This Skill **may identify and report** (as Fact/Inference with evidence):

- Potential secret exposure in the change set
- Edits to durable Consumer artifacts (for example ADRs or local policy files)
- Missing or unclear approval evidence relative to stated durable decisions
- Changes that appear to fall under AGENTS §8-listed operations

This Skill must **not**:

- Grant security approval
- Decide whether authorization is legally or organizationally sufficient
- Override or reinterpret AGENTS.md §8
- Perform protected operations
- Authorize implementation outside approved scope, commits, pushes, publishes, or releases

Recommendations that would change durable Consumer ADRs or local policies remain recommendations until an authorized owner decides. Completing this Skill’s report does **not** authorize any repository modification. Explicit Consumer adoption of Module guidance into local policy is Consumer-owned (**L3**) and must not be assumed from this Skill’s presence.

`active-hygiene` does **not** add an extra approval gate for work that is already authorized and **in-scope**.

---

## 17. Related references

Link only — do not duplicate methodology, Workflow, Checklist, or Core Skill bodies:

- Module entry: [`../README.md`](../README.md)
- Module metadata: [`../module.yaml`](../module.yaml)
- Conventions: [`../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md`](../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md)
- Architecture / precedence: [`../../../docs/FRAMEWORK_CONTRACT.md`](../../../docs/FRAMEWORK_CONTRACT.md) §5–§7
- Operating manual and approvals: [`../../../AGENTS.md`](../../../AGENTS.md) (especially §2 and §8)
- Core Feature Development Workflow (orchestration remains Core): [`../../../workflows/feature_development.md`](../../../workflows/feature_development.md) — especially Stages 1, 5, and 6
- Methodology: [`../../../methodology/rdiv.md`](../../../methodology/rdiv.md), [`../../../methodology/ai_collaboration.md`](../../../methodology/ai_collaboration.md)
- Core Review Checklist (not replaced): [`../../../checklists/review.md`](../../../checklists/review.md)
- Core repository analysis (not replaced): [`../../../skills/repository_analysis.md`](../../../skills/repository_analysis.md)
- Architecture Boundary Review (companion Module Skill; not replaced): [`../../architecture-engineering/skills/architecture_boundary_review.md`](../../architecture-engineering/skills/architecture_boundary_review.md)
- Adoption example (illustrative): [`../../../examples/02-module-guided-adoption/README.md`](../../../examples/02-module-guided-adoption/README.md)

---

## Non-goals

- Automatic file modifications, fixes, or refactoring
- Mandatory numerical score or 1–10 rating
- Coding-style enforcement or language-specific mandates
- Architecture redesign or ADR authorship
- Testing strategy ownership or security certification
- Skill runtime / runner / CLI execute
- Automatic Module adoption or installation
- Replacing Feature Development Workflow, Release Workflow, or Core `review` checklist completion
- Recreating Stage 1 scope definition or Stage 5 plan authorship

---

## Illustrative scenarios

| Scenario | Use this Skill? | Expected class / behavior |
|----------|-----------------|---------------------------|
| Clearly scoped implementation; only planned paths change | Yes — `active-hygiene` or `review` | Continue in-scope; honest close-out |
| Nearby unrelated typo discovered; approved task still completable | Yes | **F1** — disclose; continue authorized task |
| Missing API contract blocks correct completion | Yes | **F2** — clarify/escalate; no “complete” claim |
| Secret appears in diff | Yes | **F3** — applicable stop; no secret dump |
| Plan lists three steps; diff omits one and adds unexplained rename | Yes — `review` | Plan-to-diff mismatch report |
| Architecture boundary / dependency direction question | No | Architecture Boundary Review |
| Unfamiliar repo discovery | No | Core `repository-analysis` |
| Request to auto-fix formatting and commit | No | Skill does not modify or authorize commits |

### Scenario 1 — Clearly scoped implementation

- **Context:** Approved scope names one behavior change and listed non-goals; plan names the target paths.
- **Behavior:** Bind to consumed scope/plan; avoid drive-by edits; keep path↔plan trace.
- **Reporting:** Changed paths; plan mapping; validation run/unrun honesty.
- **Boundary:** No opportunistic package-wide refactor.

### Scenario 2 — Newly discovered out-of-scope issue

- **Context:** During in-scope work, an unrelated defect or concern appears.
- **Behavior:** Classify F1/F2/F3. F1 → disclose and continue. F2 → clarify. F3 → stop.
- **Reporting:** Finding class, evidence, options for human decision (defer / explicit expansion / separate task).
- **Boundary:** No silent scope expansion.

### Scenario 3 — Plan-to-diff mismatch

- **Context:** Approved plan exists; inspected diff omits a plan step and/or adds unexplained paths.
- **Behavior (`review`):** Fact paths; Inference on unexplained additions; Recommendations (justify, revert, or obtain expansion).
- **Reporting:** Missing plan items; unexpected additions; no auto-fix.
- **Boundary:** Does not complete Core Review Checklist by itself.

---

## Representative diff-review exercise (illustrative)

Stack-agnostic documentation exercise — not an executable test.

| Field | Example content |
|-------|-----------------|
| **Approved scope** | Add a null-guard in the invoice creation entry point when `customerId` is null; update only the unit test for that method. Non-goals: billing-package refactor; API version change. |
| **Expected plan** | (1) Guard in invoice creation entry point (2) Adjust the matching unit test null case |
| **Actual changed paths** | Invoice creation source; matching unit test; **unexpected** private helper rename in a mapper file; **unexpected** unrelated docs wording edit |
| **Mismatch** | Plan steps 1–2 present; mapper rename and docs edit unexplained vs scope/plan |

**Expected Skill-guided report (abbreviated):**

- **Fact:** Listed changed paths observed in evidence.
- **Fact:** Mapper rename and docs edit are not named in approved scope/plan.
- **Inference:** Unexplained / opportunistic relative to approved outcome (uncertainty stated if authorship unclear).
- **F1** (example): docs wording may be non-blocking if the authorized null-guard task remains safely completable — disclose; do not expand scope.
- **Recommendation:** Human chooses justify-with-expansion, revert unexpected paths, or split work — Skill does not authorize extra edits.
- **Validation disclosure:** State tests run vs unrun; unrun ≠ passed.

---

## Change history

| Version | Notes |
|---------|-------|
| `0.1.0` | Initial draft Skill (review-oriented hygiene procedure) |
| `0.2.0` | Pilot maturation: L1/L6/F1–F3 authority model; scope ownership (consume Core plan/scope); `active-hygiene` vs `review`; accidental out-of-scope handling; scenarios + diff-review exercise |

---

End of Implementation Change Hygiene Skill `implementation-change-hygiene` v0.2.0 (`draft`).
