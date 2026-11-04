# Architecture Boundary Review Skill

| Field | Value |
|-------|-------|
| `id` | `architecture-boundary-review` |
| `title` | Architecture Boundary Review |
| `status` | `draft` |
| `version` | `0.1.0` |
| `scope` | `module` |
| `summary` | An evidence-based procedure for reviewing architectural boundaries, responsibilities, dependency direction, and structural consistency without imposing a product architecture. |
| `owner_role` | `module-author` |

This document is a Module Skill **definition** for the `architecture-engineering` Module. It follows [`../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md`](../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md).

**Authority:** Module Skill guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** constraints. Instruction precedence remains Framework Contract §7 / [`../../../AGENTS.md`](../../../AGENTS.md) §2. AI recommends; humans decide. Durable architectural and product decisions belong to the Consumer.

This Skill is **analytical and advisory**. It is not a Skill runner, Workflow orchestrator, Checklist, Prompt collection, or Knowledge article. Presence of this file does not adopt, install, or enable the Module.

---

## 1. Purpose

Provide a reusable, stack-agnostic capability for reviewing **architectural boundaries**, **responsibilities**, **dependency direction**, **coupling**, and **structural consistency**, and for assessing the architectural impact of proposed structural changes — without imposing a particular product architecture on the Consumer.

---

## 2. Intended outcome

A structured **Architecture Boundary Review** report that:

- Identifies observed boundaries and responsibilities where evidence supports them
- Evaluates separation of concerns and dependency direction
- Surfaces unintended coupling and boundary-violation signals
- Checks consistency with existing architectural decisions and conventions when those artifacts exist
- Assesses architectural impact of a proposed structural change when one is in scope
- Names compatibility and integration risks supported by evidence
- Separates **facts**, **inferences**, and **recommendations**
- Supports human-owned architecture decisions without authorizing those decisions

The outcome is structured findings and advice — not repository modification and not a mandated target architecture.

---

## 3. When to use

- Non-trivial system boundaries, integration points, or layers exist
- A change may affect module boundaries, public contracts, data compatibility, or top-level structural conventions
- There is suspicion of unintended coupling, reversed dependency direction, or separation-of-concerns leakage
- Consistency with Consumer ADRs or documented architectural conventions needs evaluation
- A structural refactor, package move, or boundary change is proposed and impact should be assessed before implementation
- As supporting analysis for Feature Development Architecture and Design work without replacing the Workflow

---

## 4. When not to use

- Tiny single-file scripts with no lasting architecture
- Narrow edits with adequate local context and no boundary assessment requested
- The primary need is general repository discovery or onboarding — use Core [`../../../skills/repository_analysis.md`](../../../skills/repository_analysis.md) (`id`: `repository-analysis`) instead
- The primary need is implementation, testing strategy, security testing, DevOps/CI setup, data engineering, or release operations
- The Consumer forbids external architecture frameworks by policy
- The requester expects this Skill to mandate a single product architecture or to redesign the system unprompted

---

## 5. Inputs

- Target repository root (or an explicitly scoped subtree)
- Review goal / questions (as-is boundary review and/or proposed structural change assessment)
- When a change is in scope: a description of the proposed structural change (plan, diff summary, or equivalent) — do not invent a change
- Any known constraints (read-only requirement, time box, areas to exclude)
- Access limited to what the operator is already authorized to inspect

Optional when present (do not fabricate):

- Consumer ADRs and architecture documentation
- Prior repository analysis notes or a recent Core `repository-analysis` report
- Applicable local policies relevant to architecture

**Context sufficiency:** If repository understanding is too weak to evaluate boundaries honestly, recommend Core `repository-analysis` (or equivalent evidence gathering) first. Do not re-implement that Skill’s full discovery procedure here.

---

## 6. Outputs

Primary output: an Architecture Boundary Review report (Consumer-owned or session artifact as directed by the requester) following the structure in §9 where evidence exists.

Label each material claim as:

| Label | Meaning |
|-------|---------|
| **Fact** | Directly observed in repository evidence (path, config, code, docs, declared dependencies) |
| **Inference** | Reasonable interpretation of evidence; uncertainty stated |
| **Recommendation** | Advisory suggestion for human decision; not an implemented change and not an imposed architecture |

Unavailable sections must be marked **unavailable**, **not found**, or **unverified** — do not invent content to fill the template.

---

## 7. Procedure

Perform steps in order. Adjust depth to repository size, change risk, and requester goals. Prefer repository evidence over assumptions ([`../../../methodology/architecture_first.md`](../../../methodology/architecture_first.md)).

### Step 1 — Scope lock

- Restate the review question and whether the review is **as-is**, **change-impact**, or both
- Record in-scope and out-of-scope areas
- Name known L0 / Consumer constraints already stated
- Do not expand into opportunistic redesign

### Step 2 — Context sufficiency check

- Determine whether enough structural evidence exists to evaluate boundaries
- If not, stop or narrow: recommend Core [`../../../skills/repository_analysis.md`](../../../skills/repository_analysis.md) (or ask for missing path/context) rather than guessing
- Do not duplicate general technology inventory, onboarding, or broad repository assessment inside this Skill

### Step 3 — Identify candidate boundaries

From evidence only, identify candidate boundaries such as:

- Packages, projects, or directory modules
- Layers or declared architectural segments
- Public API / interface surfaces
- Process, service, or deployment boundaries when evidenced
- Documented responsibility boundaries (ADRs, architecture notes)

If a boundary is only assumed, label it **Inference** or mark unverified.

### Step 4 — Map responsibilities

- For each material boundary, state the observed responsibility
- Note overlaps, gaps, or leakage only with evidence
- Do not invent “intended” responsibilities that are not documented or clearly evidenced

### Step 5 — Dependency direction

- Observe dependency direction via imports, project references, call paths, messaging/config wiring, or equivalent evidence
- Flag reverse, cyclic, or layer-skipping dependency signals when supported
- Distinguish declared architecture (docs/ADRs) from observed structure when they differ — report the conflict with paths

### Step 6 — Coupling and boundary integrity

- Look for unintended coupling (shared internals leakage, cross-boundary shortcuts, unclear ownership of shared types/config)
- Assess whether boundaries are enforceable in practice or only nominal
- Keep claims proportional to evidence; do not claim a formal architecture style unless evidenced

### Step 7 — Consistency with existing decisions and conventions

- Compare findings to Consumer ADRs and architectural conventions **when present**
- If none are found, state **not found** — do not fabricate ADRs
- Disclose conflicts with L2 decisions or applicable L3 policies; do not silently override them

### Step 8 — Structural change impact (when a change is in scope)

- Identify which boundaries, responsibilities, and dependency edges would move, blur, or break
- Name compatibility and integration risks (public contracts, data shapes, consumer-facing surfaces, sync-sensitive contracts when relevant)
- If no change is in scope, mark this section **N/A**

### Step 9 — Synthesize findings and recommendations

- Prioritize findings by impact and confidence
- Keep **Fact**, **Inference**, and **Recommendation** distinct
- Present recommendations as options or advisory next steps for human owners
- Do not treat recommendations as authorized work

### Step 10 — Record limitations

- State what was not inspected
- State residual unknowns and truncated steps when time-boxed

---

## 8. Boundary and dependency evaluation criteria

Use these as evidence-oriented questions — not as a mandatory architecture standard:

- Is each material boundary observable (directory, package, API, documented responsibility) or only assumed?
- Are responsibilities coherent within a boundary, or is leakage evidenced?
- Does observed dependency direction align with documented or clearly intended direction?
- Are there cyclic, reverse, or shortcut dependency signals with concrete evidence?
- Are public contract surfaces clear enough to assess breaking risk?
- Would a proposed structural change strengthen, blur, or violate existing boundaries?
- Are compatibility / integration risks supported by paths and symbols, or only speculative?

Do **not** require microservices, monoliths, hexagonal layout, or any other single style.

---

## 9. Evidence and reporting requirements

### Recommended report structure

Include a section only when there is evidence, or explicitly mark it unavailable / N/A:

1. Executive Summary
2. Review Scope and Assumptions
3. Identified Boundaries and Responsibilities
4. Dependency Direction and Coupling Findings
5. Consistency with Existing Decisions and Conventions
6. Structural Change Impact (or N/A)
7. Compatibility and Integration Risks
8. Recommendations for Human Decision
9. Evidence Index and Limitations

### Evidence rules

- For material **facts**, cite:
  - relevant repository file paths
  - line references or ranges when available and useful
  - symbols, packages, sections, configuration keys, or other identifiers where appropriate
- Never invent line numbers
- Do not present inferences as facts
- Do not claim tests, scans, audits, or architecture certifications that were not performed
- Do not dump or paraphrase secrets, credentials, tokens, or private keys if encountered — report only that sensitive material appears present and needs human handling

---

## 10. Constraints and failure considerations

**Default mode: read-only review.**

This Skill must **not** independently:

- Modify repository files
- Apply refactors or “fix” boundary violations as part of the Skill
- Install packages or dependencies
- Change CI/CD, infrastructure, or cloud resources
- Create commits, branches, or tags
- Push, publish, or deploy
- Create or rewrite Consumer ADRs
- Impose a target architecture

Do not treat this Skill as:

- A substitute for Core `repository-analysis`
- A Workflow execution engine or Feature Development Stage replacement
- A Checklist completion authority
- A Prompt pack or a rewrite of [`../../../prompts/review/architecture_review.md`](../../../prompts/review/architecture_review.md)
- Permission to migrate or fork Core Skills

**Failure / uncertainty handling:**

- If the repository root cannot be determined, stop and ask for a path
- If access is insufficient, report blocked areas rather than guessing
- If docs and code conflict, report the conflict with paths
- If architecture style or boundary labels are unclear, say so; do not force a label
- If time-boxed, state truncated steps and residual unknowns in Evidence and Limitations

---

## 11. Human approval and decision boundaries

Human approval gates in [`../../../AGENTS.md`](../../../AGENTS.md) §8 remain authoritative. This Skill creates **no** new approval authority and no new governance level.

- Recommendations that would change durable Consumer ADRs or local policies remain recommendations until an authorized owner decides
- Operations on the AGENTS §8 list require applicable confirmation **before** the operation
- Completing or reviewing this Skill’s report does **not** authorize implementation, restructuring, commits, or publication
- Explicit Consumer adoption of Module guidance into local policy is Consumer-owned (**L3**) and must not be assumed from this Skill’s presence

---

## 12. Related references

Link only — do not duplicate methodology, Core Skill, Workflow, or Checklist bodies:

- Module entry: [`../README.md`](../README.md)
- Module metadata: [`../module.yaml`](../module.yaml)
- Conventions: [`../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md`](../../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md)
- Architecture / precedence: [`../../../docs/FRAMEWORK_CONTRACT.md`](../../../docs/FRAMEWORK_CONTRACT.md) §5–§7
- Operating manual and approvals: [`../../../AGENTS.md`](../../../AGENTS.md) (especially §8)
- Methodology: [`../../../methodology/architecture_first.md`](../../../methodology/architecture_first.md), [`../../../methodology/rdiv.md`](../../../methodology/rdiv.md), [`../../../methodology/ai_collaboration.md`](../../../methodology/ai_collaboration.md)
- Complementary Core Skill (not replaced): [`../../../skills/repository_analysis.md`](../../../skills/repository_analysis.md)
- Related Workflow (orchestration, not a substitute): [`../../../workflows/feature_development.md`](../../../workflows/feature_development.md) — especially Architecture and Design
- Related Checklist (general change review, not a substitute): [`../../../checklists/review.md`](../../../checklists/review.md)
- Related Core interaction prompt (not canonical capability; unchanged by this Skill): [`../../../prompts/review/architecture_review.md`](../../../prompts/review/architecture_review.md)

---

## Non-goals

- Skill runtime / runner / CLI execute
- Automatic remediation or authorized restructuring
- Duplicating or modifying Core `repository-analysis`
- Replacing or editing the Core architecture review prompt
- Checklist, Knowledge, Workflow, or Prompt package authoring inside this Skill
- Prescribing a mandatory product architecture style

---

## Example scenarios (illustrative)

| Scenario | Use this Skill? |
|----------|-----------------|
| Suspected reverse dependency between packages | Yes — dependency direction and coupling |
| Planned move of a public API surface across packages | Yes — structural change impact |
| Unfamiliar repository “what is this?” discovery | No — use Core `repository-analysis` |
| Documentation typo fix | No |
| Request to “split everything into microservices” as a mandate | No — may discuss trade-offs only if asked; do not impose |

---

End of Architecture Boundary Review Skill `architecture-boundary-review` v0.1.0 (`draft`).
