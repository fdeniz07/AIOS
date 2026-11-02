# Repository Analysis Skill

| Field | Value |
|-------|-------|
| `id` | `repository-analysis` |
| `title` | Repository Analysis Skill |
| `status` | `draft` |
| `version` | `0.1.0` |
| `scope` | `core` |
| `summary` | A technology-agnostic procedure for inspecting software repositories and producing evidence-based architectural and engineering assessments. |
| `owner_role` | `core-maintainer` |

This document is a Core Skill **definition**. It follows [`../docs/SKILL_KNOWLEDGE_CONVENTIONS.md`](../docs/SKILL_KNOWLEDGE_CONVENTIONS.md).

**Authority:** Core Skill guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** constraints. Instruction precedence remains Framework Contract §7 / [`../AGENTS.md`](../AGENTS.md) §2. AI recommends; humans decide.

This Skill is **analytical and advisory**. It is not a Skill runner, Workflow orchestrator, Checklist, Prompt collection, or Knowledge article.

---

## 1. Purpose

Provide a reusable, stack-agnostic capability for systematically inspecting a software repository and producing an evidence-based architectural and engineering assessment.

The procedure is intended to work across diverse repositories (for example JVM / Spring, .NET / ASP.NET Core, Python, JavaScript / TypeScript, frontend or backend apps, monoliths or distributed systems, and infrastructure / DevOps repos). Those stacks are **illustrative only** — none is mandatory.

---

## 2. Intended outcome

A structured analysis report that:

- Summarizes repository purpose and shape from evidence
- Inventories technologies and tooling that were actually observed
- Describes architecture and boundaries only where evidence supports the claim
- Separates **facts**, **inferences**, and **recommendations**
- Names residual risks, gaps, and human follow-ups
- Cites relevant repository file paths, line references or ranges when available and useful, and symbols, sections, configuration keys or other identifiers where appropriate — without inventing line numbers

The outcome is understanding and advice — not repository modification.

---

## 3. When to use

- Before significant change work, when repository understanding is incomplete
- During onboarding to an unfamiliar codebase
- When preparing architecture, risk, or quality assessments for human review
- As supporting analysis inside Feature Development discovery stages (see Related references) without replacing the Workflow
- When a Product Owner or Consumer asks for a technology-agnostic repository assessment

---

## 4. When not to use

- As authorization to modify code, configs, CI, infrastructure, or dependencies
- As a substitute for Workflow orchestration or Checklist verification
- As a security penetration test, formal audit, or compliance certification
- When the task is already a narrowly scoped edit with adequate local context and no assessment was requested
- To invent Module packages, domain curricula, or Consumer product decisions

---

## 5. Inputs

- Target repository root (or clear path to analyze)
- Analysis goal / questions from the requester (scope, depth, focus areas)
- Any known constraints (read-only requirement, time box, areas to exclude)
- Access limited to what the operator is already authorized to inspect

Optional: existing ADRs, architecture docs, prior reports, or Consumer policies — use when present; do not fabricate them.

---

## 6. Outputs

Primary output: an analysis report (Consumer-owned or session artifact as directed by the requester) following the recommended structure in §8 where evidence exists.

Each material claim should be labeled as:

| Label | Meaning |
|-------|---------|
| **Fact** | Directly observed in repository evidence (path, config, code, CI, docs) |
| **Inference** | Reasonable interpretation of evidence; uncertainty stated |
| **Recommendation** | Advisory suggestion; not an implemented change |

Unavailable sections must be marked **unavailable**, **not found**, or **unverified** — do not invent content to fill the template.

---

## 7. Analysis procedure

Perform steps in order. Adjust depth to repository size and requester goals. Prefer repository evidence over assumptions ([`../AGENTS.md`](../AGENTS.md); [`../methodology/architecture_first.md`](../methodology/architecture_first.md)).

### Step 1 — Repository discovery

- Identify the repository root and VCS context when available
- Inspect top-level and relevant nested directory structure
- Identify project and configuration manifests (build, package, workspace, environment samples)
- Identify documentation and architectural guidance (README, docs/, ADRs, architecture notes)

### Step 2 — Technology inventory

- Languages and frameworks **observed**
- Build and package tooling
- Runtime and deployment configuration artifacts
- External services and integrations referenced in config or code
- Dependency inventory sources (lockfiles, manifests) — list what exists; do not install packages

### Step 3 — Architecture analysis

- Identify architectural style **only where evidence supports it**
- Identify major components / modules and stated or evident responsibilities
- Examine dependency direction and boundaries where structure reveals them
- Identify entry points and major execution paths
- Examine API and integration boundaries (HTTP, messaging, CLIs, jobs, etc.)

### Step 4 — Data and persistence

- Identify persistence technologies and storage clients when present
- Identify data access patterns from code/layout evidence
- Identify migrations and schema artifacts where available
- Distinguish confirmed persistence facts from inferred domain models

### Step 5 — Quality and testing

- Identify test types and frameworks when present
- Examine CI/CD configuration as evidence of quality gates
- Review static analysis and quality tooling configuration when present
- Identify observability and operational practices reflected in the repo

### Step 6 — Risk assessment

- Architectural risks supported by evidence
- Maintainability concerns
- Dependency and security **review areas** (flag for human review; do not claim a vulnerability merely because a dependency or config exists)
- Testing gaps relative to critical paths
- Potential technical debt signals

### Step 7 — Findings and recommendations

- Prioritize findings by impact and confidence
- Explain impact and cite evidence
- Keep facts, inferences, and recommendations visually distinct
- Provide relevant repository file paths; add line references or ranges when available and useful; include symbols, sections, configuration keys or other identifiers where appropriate; never invent line numbers
- Identify areas requiring human investigation or approval before action

---

## 8. Evidence and reporting requirements

### Recommended report structure

Include a section only when there is evidence, or explicitly mark it unavailable:

1. Executive Summary
2. Repository Overview
3. Technology Inventory
4. Architecture Overview
5. Component and Dependency Relationships
6. API and Integration Overview
7. Data and Persistence
8. Testing and Quality
9. CI/CD and Operations
10. Risks and Technical Debt
11. Recommendations
12. Evidence and Limitations

### Evidence rules

- For material **facts**, cite:
  - relevant repository file paths
  - line references or line ranges whenever available and useful
  - symbols, sections, configuration keys or other identifiers where appropriate
- If line references cannot be established, do **not** invent them; still provide file paths and any available identifiers
- Keep a clear distinction between directly observed evidence (**facts**) and interpretation (**inferences**)
- State what was **not** inspected when scope was limited
- Do not present inferences as facts
- Do not claim tests, scans, or audits that were not run
- Do not dump or paraphrase secrets, credentials, tokens, or private keys if encountered — report only that sensitive material appears present and needs human handling

---

## 9. Constraints and safety boundaries

**Default mode: read-only inspection.**

This Skill must **not** independently:

- Modify repository files
- Generate or apply code fixes as part of the Skill
- Install packages or dependencies
- Execute database or schema migrations
- Change infrastructure or cloud resources
- Modify CI/CD pipelines
- Create commits, branches, or tags
- Push or publish changes
- Access secret stores beyond incidental file sighting, or expose sensitive values in reports

Do not treat this Skill as:

- A Workflow execution engine
- A Checklist completion authority
- A Prompt pack
- A Knowledge document
- Permission to create a `modules/` tree or Module packages

Stack examples (Java, .NET, Python, JS/TS, etc.) are non-mandatory illustrations of applicability.

---

## 10. Human approval requirements

Human approval gates in [`../AGENTS.md`](../AGENTS.md) §8 remain authoritative. This Skill creates **no** new approval authority.

If deeper investigation would require a potentially destructive, externally impactful, or approval-listed operation (for example repository-wide restructuring, public contract breaks, or irreversible actions), **stop** and request applicable human / Consumer-owner authorization **before** proceeding.

Analysis recommendations that would change durable Consumer ADRs or local policies must be framed as recommendations only until an authorized owner decides.

Final review of analysis does not retroactively authorize repository modifications.

---

## 11. Failure and uncertainty handling

- If the repository root cannot be determined, stop and ask for a path
- If access is insufficient, report blocked areas rather than guessing
- If evidence conflicts (docs vs code), report the conflict with paths
- If architecture style is unclear, say so; do not force a label
- If security concerns are only heuristic, label them as review areas — not confirmed vulnerabilities
- If time-boxed, state truncated steps and residual unknowns in Evidence and Limitations

---

## 12. Related references

Link only — do not duplicate methodology or workflow bodies:

- Conventions: [`../docs/SKILL_KNOWLEDGE_CONVENTIONS.md`](../docs/SKILL_KNOWLEDGE_CONVENTIONS.md)
- Concept meanings / precedence: [`../docs/FRAMEWORK_CONTRACT.md`](../docs/FRAMEWORK_CONTRACT.md) §6–§7
- Operating manual and approvals: [`../AGENTS.md`](../AGENTS.md) (especially §8)
- Methodology: [`../methodology/rdiv.md`](../methodology/rdiv.md), [`../methodology/architecture_first.md`](../methodology/architecture_first.md), [`../methodology/repository_onboarding.md`](../methodology/repository_onboarding.md), [`../methodology/ai_collaboration.md`](../methodology/ai_collaboration.md)
- Related Workflow (orchestration, not a substitute): [`../workflows/feature_development.md`](../workflows/feature_development.md)
- Related Checklist (verification after change, not a substitute): [`../checklists/review.md`](../checklists/review.md)

---

## Non-goals

- Skill runtime / runner / CLI execute
- Automatic remediation or “fix the findings” authority
- Knowledge article authoring inside this Skill
- Prompt migration or replacement of `prompts/`
- Module catalog creation

---

End of Repository Analysis Skill `repository-analysis` v0.1.0 (`draft`).
