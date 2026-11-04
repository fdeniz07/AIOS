# Implementation Change Hygiene Skill

| Field | Value |
|-------|-------|
| `id` | `implementation-change-hygiene` |
| `title` | Implementation Change Hygiene |
| `status` | `draft` |
| `version` | `0.1.0` |
| `scope` | `module` |
| `summary` | An evidence-based procedure for reviewing implementation scope fidelity, change hygiene, and plan-to-diff consistency without authorizing changes or imposing coding standards. |
| `owner_role` | `module-author` |

This document is a Module Skill **definition** for the `development-engineering` Module. It follows [`../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md`](../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md).

**Authority:** Module Skill guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** constraints. Instruction precedence remains Framework Contract §7 / [`../../../AGENTS.md`](../../../AGENTS.md) §2. AI recommends; humans decide. Durable architectural and product decisions belong to the Consumer.

This Skill is **analytical and advisory**. It is not a Skill runner, Workflow orchestrator, Checklist, Prompt collection, or Knowledge article. Presence of this file does not adopt, install, or enable the Module.

---

## 1. Purpose

Provide a reusable, stack-agnostic capability for reviewing **implementation scope fidelity**, **change hygiene**, and **diff-to-plan consistency** — so humans can judge whether an implementation stayed inside an agreed scope without opportunistic churn.

This Skill does **not** orchestrate feature delivery, rewrite implementation plans, impose coding standards, redesign architecture, or authorize repository modifications.

---

## 2. Intended outcome

A structured **Implementation Change Hygiene Report** presented in the assistant response by default that:

- Compares agreed scope against observed changes
- Surfaces unrelated, opportunistic, or disproportionate edits when evidence supports the finding
- Distinguishes necessary supporting changes from unlabeled scope expansion
- Compares an available implementation plan to the actual diff when a plan exists
- Separates **facts**, **inferences**, and **recommendations**
- Names missing context honestly

The Skill must **not** independently create, save, or modify report files in a Consumer repository. Persisting a report as a file requires a separate explicit request and applicable authorization.

The outcome is advisory findings — not automatic fixes and not Stage 8 checklist completion.

---

## 3. When to use

- Scoped code or behavior implementation is in progress or recently completed
- Diff fidelity to an agreed scope or plan needs reinforcement
- Opportunistic refactors, drive-by formatting, or unrelated structural edits are a material risk
- As supporting analysis for Feature Development implementation or review stages **without** replacing the Workflow or Core Review Checklist

---

## 4. When not to use

- The primary need is architecture boundary or structural-fit assessment — use [`../../architecture-engineering/skills/architecture_boundary_review.md`](../../architecture-engineering/skills/architecture_boundary_review.md)
- The primary need is general repository discovery — use Core [`../../../skills/repository_analysis.md`](../../../skills/repository_analysis.md)
- Release, publish, tag, or deploy work — use Core Release Workflow
- No agreed scope and no inspectable change/diff can be obtained
- The requester expects automatic fixes, commits, or coding-style enforcement
- The Consumer forbids external development guidance by policy

---

## 5. Inputs

- Agreed scope statement (and explicit non-goals when stated)
- Inspectable change evidence (diff, patch, PR description with file list, or equivalent) that the operator is authorized to view
- Review questions / focus from the requester
- Any known constraints (read-only requirement, time box, paths to exclude)

Optional when present (**do not invent**):

- Implementation plan (from Feature Development Stage 5 or equivalent)
- Acceptance criteria
- Notes on prior approvals already obtained
- Consumer coding standards or local policy relevant to the change (for conflict disclosure only)

**Missing context:** If scope cannot be determined, stop and ask. If no plan is available, record **plan unavailable** and continue only with scope↔diff review — never fabricate a plan. If no diff/change evidence is available, stop and ask for evidence.

---

## 6. Outputs

Primary output: an **Implementation Change Hygiene Report** in the assistant response (unless the requester separately authorizes a Consumer-owned file artifact).

Label each material claim as:

| Label | Meaning |
|-------|---------|
| **Fact** | Directly observed in scope text, plan text, or change/diff evidence |
| **Inference** | Reasonable interpretation; uncertainty stated |
| **Recommendation** | Advisory suggestion for human decision; not an implemented fix and not authorization |

Unavailable sections must be marked **unavailable**, **not found**, or **unverified** — do not invent content to fill the template.

### Recommended report structure

1. Executive Summary
2. Agreed Scope and Plan Status
3. Evidence Examined
4. Scope Fidelity Findings
5. Change Hygiene Findings
6. Plan-to-Diff Consistency
7. Recommendations for Human Decision
8. Limitations and Missing Context

---

## 7. Procedure

Perform steps in order. Adjust depth to change size and requester goals. Prefer evidence over assumptions. **Default mode: read-only review.**

### Step 1 — Scope lock

- Restate the agreed scope and stated non-goals
- Record in-scope / out-of-scope boundaries for this review
- If scope is missing or contradictory, stop and ask — do not invent scope

### Step 2 — Plan intake

- If an implementation plan is provided or clearly present, record it as an input
- If none is available, mark **plan unavailable** and proceed without inventing one
- Do not redefine or silently rewrite the plan

### Step 3 — Diff and evidence intake

- Inspect only authorized change evidence
- List material paths/hunks examined at a depth matching risk
- Cite file paths; add line references or ranges when available and useful
- **Never invent line numbers** or unobserved hunks

### Step 4 — Scope fidelity review

- Map observed changes to agreed scope
- Identify unrelated or opportunistic edits when evidence supports the claim
- Distinguish **necessary supporting changes** from **scope expansion**; label supporting-necessary claims as **Inference** unless explicitly documented in scope/plan
- Do not claim a change is out of scope without pointing to scope text and change evidence

### Step 5 — Change hygiene review

- Look for potentially unnecessary refactoring relative to stated outcome
- Detect unrelated formatting-only or structural churn when evidenced
- Evaluate proportionality: is the change set sized to the request?
- Note unintended behavior-change signals only when supported by evidence (do not claim runtime proof that was not observed)
- Do not call a change “unnecessary” without sufficient evidence; prefer “unexplained relative to stated scope/plan”

### Step 6 — Plan-to-diff consistency review

- When a plan exists: identify missing plan items, unexpected additions, and unexplained deviations
- When plan is unavailable: mark this section **N/A — plan unavailable** (scope fidelity may still apply)
- Do not invent plan steps to force a consistency narrative

### Step 7 — Findings synthesis

- Prioritize findings by impact and confidence
- Keep **Fact**, **Inference**, and **Recommendation** distinct
- Present recommendations as options for human owners
- Do not treat recommendations as authorized work

### Step 8 — Limitations and missing context

- State what was not inspected
- State missing scope, plan, or diff evidence
- State truncated steps when time-boxed

---

## 8. Review criteria

Use these as evidence-oriented questions — not as a coding-standard law:

- Is each material change traceable to agreed scope or an explicit plan step?
- Are there unrelated files or behaviors relative to the stated outcome?
- Is a “supporting” change justified with evidence, or is it unlabeled scope expansion?
- Do wide refactors or formatting-only sweeps lack a stated need?
- When a plan exists, are plan items omitted without disclosure?
- Do secrets or durable Consumer artifact edits appear without clear approval evidence?

Do **not** require a numerical quality score or 1–10 rating. Do **not** mandate a language, framework, or style guide.

---

## 9. Evidence rules

- For material **facts**, cite relevant repository paths and line references/ranges when available and useful
- Never invent line numbers, hunks, test results, or approval records
- Do not present inferences as facts
- Do not claim tests, scans, or security certifications that were not performed
- If secrets, credentials, tokens, or private keys appear in the change set: report that sensitive material appears present and needs human handling — do **not** dump or paraphrase secret values

---

## 10. Constraints and failure considerations

**Default mode: read-only review.**

This Skill must **not** independently:

- Modify repository files
- Apply automatic fixes or refactors as part of the Skill
- Create, save, or overwrite Consumer report files without a separate explicit request and authorization
- Install packages or dependencies
- Create commits, branches, or tags
- Push, publish, or deploy
- Rewrite Consumer ADRs, coding standards, or architecture decisions
- Impose a coding style or target architecture

Do not treat this Skill as:

- A substitute for Core Feature Development Workflow orchestration
- A replacement for Core [`../../../checklists/review.md`](../../../checklists/review.md)
- A substitute for Architecture Boundary Review
- A Skill runner, CLI executor, or automatic adoption mechanism
- Security approval or compliance certification

**Failure / uncertainty handling:**

- If scope cannot be established, stop and ask
- If change evidence cannot be inspected, stop and ask
- If plan is missing, mark unavailable — do not invent
- If “unnecessary” cannot be evidenced, say unexplained / unverified instead
- If time-boxed, state truncated steps in Limitations

---

## 11. Security signals and human approval boundaries

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
- Authorize implementation, commits, pushes, publishes, or releases

Recommendations that would change durable Consumer ADRs or local policies remain recommendations until an authorized owner decides. Completing this Skill’s report does **not** authorize any repository modification. Explicit Consumer adoption of Module guidance into local policy is Consumer-owned (**L3**) and must not be assumed from this Skill’s presence.

---

## 12. Related references

Link only — do not duplicate methodology, Workflow, Checklist, or Core Skill bodies:

- Module entry: [`../README.md`](../README.md)
- Module metadata: [`../module.yaml`](../module.yaml)
- Conventions: [`../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md`](../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md)
- Architecture / precedence: [`../../../docs/FRAMEWORK_CONTRACT.md`](../../../docs/FRAMEWORK_CONTRACT.md) §5–§7
- Operating manual and approvals: [`../../../AGENTS.md`](../../../AGENTS.md) (especially §8)
- Core Feature Development Workflow (orchestration remains Core): [`../../../workflows/feature_development.md`](../../../workflows/feature_development.md) — especially Implementation Planning and Implementation
- Methodology: [`../../../methodology/rdiv.md`](../../../methodology/rdiv.md), [`../../../methodology/ai_collaboration.md`](../../../methodology/ai_collaboration.md)
- Core Review Checklist (not replaced): [`../../../checklists/review.md`](../../../checklists/review.md)
- Core repository analysis (not replaced): [`../../../skills/repository_analysis.md`](../../../skills/repository_analysis.md)
- Architecture Boundary Review (companion Module Skill; not replaced): [`../../architecture-engineering/skills/architecture_boundary_review.md`](../../architecture-engineering/skills/architecture_boundary_review.md)

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

---

## Example scenarios (illustrative)

| Scenario | Use this Skill? |
|----------|-----------------|
| PR adds feature files plus unrelated renames across the tree | Yes — scope fidelity / hygiene |
| Plan lists three steps; diff omits one and adds an unexplained module | Yes — plan-to-diff consistency |
| Architecture boundary / dependency direction question | No — Architecture Boundary Review |
| Unfamiliar repo “what is this?” discovery | No — Core `repository-analysis` |
| Request to auto-fix formatting and commit | No — Skill does not modify or authorize commits |

---

End of Implementation Change Hygiene Skill `implementation-change-hygiene` v0.1.0 (`draft`).
