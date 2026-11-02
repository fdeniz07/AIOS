# AIOS Skill & Knowledge Conventions

Version: 1.0.0

Status: Draft

Last Updated: 2026-11-02

Document type: Convention specification

This document defines **Markdown-first conventions** for AIOS Skill and Knowledge **definitions**.

It is subordinate to the Framework Contract for architecture and governance:

- Concept meanings: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §6
- Content placement: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.5
- Instruction precedence (L0–L7): [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7
- Workflow / Checklist authoring pattern (conceptual reuse only): [`WORKFLOW_CHECKLIST_CONVENTIONS.md`](WORKFLOW_CHECKLIST_CONVENTIONS.md)
- Module field / lifecycle patterns (conceptual reuse only — do not require `module.yaml` for Skills/Knowledge): [`MODULE_METADATA.md`](MODULE_METADATA.md), [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md)
- Agent operationalization: [`../AGENTS.md`](../AGENTS.md) (RDIV, human approval gates)

Illustrative Markdown structures in this document are **examples only**. They are not shipped Skill or Knowledge packages.

---

## 1. Scope and authority

### Purpose

Establish a shared, stack-agnostic way to author reusable:

- **Skills** — actionable reusable capability definitions (**how**)
- **Knowledge** — reference material (**what** / **why**)

AIOS provides the **framework**, not Consumer domain content, product backlogs, or curricula.

### Authority

| Source | Default authority |
|--------|-------------------|
| Core Skill / Knowledge | **L6** recommendation |
| Module Skill / Knowledge | **L6** until explicitly adopted into Consumer local policy → **L3** |
| Pack-contextualized Skill / Knowledge | **L5** when explicitly adopted |
| Consumer-local Skill / Knowledge | Consumer-owned (typically L3 / local process) |

Instruction precedence remains Framework Contract §7 / [`../AGENTS.md`](../AGENTS.md) §2 (**L0–L7**). Skills and Knowledge do **not** create new governance levels.

This document does **not**:

- Implement a Skill execution engine or Knowledge retrieval / RAG / indexing engine
- Require YAML frontmatter or a runtime parser
- Require `skill.yaml` or `knowledge.yaml`
- Create Module packages, Packs, or Consumer repositories
- Grant execution authority to agents or CLI tools
- Redefine concept meanings from Framework Contract §6
- Duplicate the Module metadata field dictionary

Agents may **recommend** following a Skill or consulting Knowledge. Durable actions still require applicable human / Consumer-owner approval under existing gates. AI recommends; humans decide.

---

## 2. Format rules (Markdown-first)

| Rule | Convention |
|------|------------|
| Format | Pure Markdown (`.md`) |
| Frontmatter | **Not used** |
| Machine schema / YAML | **Not required** |
| Runtime parser | **Not required** |
| Metadata | Human-readable Markdown **table** near the top of the document |
| Identifiers | Stable lowercase English `kebab-case` IDs |
| Versioning | Lightweight SemVer-style `MAJOR.MINOR.PATCH` in the metadata table (content revision only) |
| Examples | Must be labeled illustrative when not an approved shipped definition |

Do not introduce external dependencies to author or maintain these documents.

---

## 3. Conceptual boundaries

| Concept | Meaning | Owns | Does not own |
|---------|---------|------|--------------|
| **Knowledge** | Reference — **what** and **why** | Facts, concepts, rationale | Step-by-step execution |
| **Skill** | Actionable — **how** | Reusable procedures / capability definition | Multi-role orchestration; runtime engine |
| **Workflow** | Multi-step process | Stages, gates, handoffs | Single atomic how-to |
| **Checklist** | Verification list | Review / Done gates | Architecture decisions |
| **Methodology** | Engineering principles and methods | How AIOS engineering work should be approached (for example RDIV) | Skill procedure bodies; domain curricula |
| **Prompt** | Interaction-specific prompt artifact | Prompt text for a conversation / tool context | Canonical reusable capability definition |

Do not redefine these meanings here. Keep Framework Contract §6 authoritative.

**Relationships:**

- Skills may **link** to Knowledge, Methodologies, Workflows, or Checklists.
- Workflows may **reference** Skills by id/link; they must not embed full Skill procedure text.
- Knowledge must not become a disguised Skill or Workflow.
- Methodology documents under `methodology/` remain methodology guidance; do not relocate them into `knowledge/` merely for naming convenience.

---

## 4. Placement and ownership

| Layer | May provide | Must not |
|-------|-------------|----------|
| **Core** | Genuinely cross-cutting Skills under root `skills/`; genuinely Core-wide Knowledge under root `knowledge/` | Domain curricula as Core identity; Consumer-filled instances; invented Module trees |
| **Module** | Capability-specific Skills and Knowledge **inside a Module package when Modules exist** | Pack lock-in; silent Core governance override |
| **Pack** | Domain contextualization that may **reference** or extend Core/Module Skills and Knowledge | Mandatory requirement to use AIOS Core; unnecessary duplication of reusable Module capability |
| **Consumer** | Local Skill and Knowledge definitions and local adoption records | Expectation that AIOS Core stores or manages Consumer-owned filled run records |

Additional rules:

- Prefer **Module-local** Skills/Knowledge for capability-specific content when Module packages exist (Phase 7 and beyond).
- Root `skills/` and `knowledge/` are reserved for **genuinely cross-cutting Core** resources only.
- Do **not** invent fake `modules/` package paths while Module packages are not present.
- Consumer-local definitions live in the Consumer repository; ownership remains with the Consumer. AIOS Core does not manage or automatically modify them.
- Education-specific or domain curriculum material belongs in Packs or Consumer repos — not Core Skill/Knowledge identity.

---

## 5. Skill definition conventions

### 5.1 Purpose

A Skill defines a **reusable capability**: how to perform a focused engineering action in a stack-agnostic way. It is a definition for humans and agents to follow as **L6 guidance**, not an executable program.

### 5.2 Body sections

A Skill definition **should** include:

1. **Purpose** — intended outcome of the capability
2. **When to use / when not to use**
3. **Inputs** — expected inputs / context
4. **Outputs** — expected results / artifacts
5. **Procedure** — ordered, actionable steps (concise)
6. **Constraints and failure considerations** — limits, common failure modes, stop conditions
7. **Human approval and decision boundaries** — what requires owner confirmation; what the Skill must not authorize
8. **Related references** — links only (Knowledge, Methodology, Workflow, Checklist, AGENTS)

Optional: non-goals, change history.

### 5.3 Illustrative skeleton (example only — not a shipped Skill)

```markdown
## Purpose
...

## When to use
...

## When not to use
...

## Inputs
...

## Outputs
...

## Procedure
1. ...
2. ...

## Constraints and failure considerations
...

## Human approval and decision boundaries
- Follow [`../AGENTS.md`](../AGENTS.md) §8 for approval-listed operations.
- This Skill does not authorize commit, push, publish, or Consumer repository modification.

## Related references
- ...
```

### 5.4 What a Skill must not do

- Grant silent execution authority
- Replace Consumer ADRs or local policies
- Orchestrate multi-role programs (that remains Workflow territory)
- Claim an implemented runner, CLI executor, or automatic orchestrator
- Duplicate full methodology or Knowledge bodies (link instead)

---

## 6. Knowledge definition conventions

### 6.1 Purpose

Knowledge provides reusable **reference** material: concepts, rationale, and orientation (**what** / **why**). It does not execute procedures.

### 6.2 Body sections

A Knowledge definition **should** include:

1. **Purpose and scope**
2. **Information content** — the reference material itself
3. **References** — links to related docs, methodologies, or external sources where useful
4. **Source / provenance expectations** — where the material comes from when relevant (honest; no false authority)
5. **Ownership and maintenance** — who maintains the definition (role-based)
6. **Review and freshness** — when to revisit; stale-risk notes

Optional: non-goals, related Skills/Workflows (links only), change history.

### 6.3 What Knowledge must not do

- Encode step-by-step execution procedures (use a Skill)
- Own architecture or product decisions (ADRs / L2)
- Imply automated retrieval, indexing, or RAG
- Store Consumer-specific filled content inside AIOS Core

---

## 7. Metadata

Place a Markdown metadata table near the top of every Skill or Knowledge definition.

### 7.1 Fields

| Field | Required | Applies to | Description |
|-------|----------|------------|-------------|
| `id` | **yes** | Skill, Knowledge | Stable identifier (`kebab-case`) |
| `title` | **yes** | Skill, Knowledge | Human-readable name |
| `status` | **yes** | Skill, Knowledge | `draft` \| `active` \| `deprecated` |
| `version` | **yes** | Skill, Knowledge | SemVer-style **content** revision |
| `scope` | **yes** | Skill, Knowledge | `core` \| `module` \| `pack` \| `consumer-local` (informational) |
| `summary` | **yes** | Skill, Knowledge | One short paragraph for discovery |
| `owner_role` | **recommended** | Skill, Knowledge | Intended maintainer role (for example `core-maintainer`, `module-author`) — not a personal email |

Do not add Module-only fields (`maturity`, `requires_core`, `deprecation` object, etc.) unless a future PO-approved extension explicitly allows them. This keeps Skill/Knowledge authoring lighter than Module packaging.

### 7.2 Illustrative metadata table (example only)

```markdown
| Field | Value |
|-------|-------|
| `id` | `example-skill` |
| `title` | Example Skill |
| `status` | `draft` |
| `version` | `0.1.0` |
| `scope` | `core` |
| `summary` | Illustrative only — not a shipped Skill. |
| `owner_role` | `core-maintainer` |
```

---

## 8. Lifecycle

Approved lifecycle states for Skill and Knowledge **definitions**:

| Status | Meaning |
|--------|---------|
| `draft` | Work in progress; not generally recommended for new durable adoption |
| `active` | Maintained and available for evaluation / use as L6 guidance |
| `deprecated` | Not recommended for new adoption; document successor and migration notes |

Rules:

- `active` means the **definition** is maintained guidance — **not** that it is executable by an engine.
- `deprecated` does **not** imply automatic deletion or Consumer forced migration.
- Document `version` identifies content revision only. It does **not** replace AIOS Framework `VERSION`, Module package versions, or Consumer `AIOS_VERSION.md` sync markers.
- No second maturity model (for example Module `experimental` / `stable`) is introduced by this document.
- `review` and `approval` are process activities, not lifecycle status values.
- Transitions are human/process decisions. No lifecycle automation is implied.

When `status` is `deprecated`, include a short migration note (why deprecated, successor `id` if any, what consumers must not assume).

---

## 9. Governance and approvals

Unchanged by these conventions:

| Level | Rule relative to Skills / Knowledge |
|-------|-------------------------------------|
| L0 | Non-overridable — never overridden by a Skill or Knowledge document |
| L1 | Explicit user task instructions (within L0) |
| L2 | Consumer-approved ADRs and product decisions |
| L3 | Consumer local policies — including **explicitly adopted** Skill / Knowledge policy |
| L4 | AIOS Core binding operating / governance defaults |
| L5 | Explicitly adopted Pack guidance |
| L6 | Module / methodology / skill / knowledge / workflow / checklist recommendations **by default** |
| L7 | External knowledge — reference only |

Human approval gates in [`../AGENTS.md`](../AGENTS.md) §8 remain authoritative. This document creates **no** new approval authorities or governance levels.

Skills and Knowledge must not silently override ADRs, local policies, or L0 constraints. Where an operation is approval-listed, obtain confirmation **before** the operation; definitions do not grant retroactive authorization.

---

## 10. Relationship with prompts

- **Skill** is the canonical reusable capability definition.
- Files under `prompts/` remain **separate** interaction-specific prompt artifacts.
- Phase 5 does **not** migrate, rewrite, or delete existing `prompts/` content.
- Avoid maintaining two competing canonical procedures for the same capability: prefer a Skill definition and treat prompts as interaction aids that may link to the Skill.
- Prompts must not be presented as a Skill execution engine.

---

## 11. Explicit non-goals

This conventions document does **not** establish:

- Skill execution / runtime / runner
- Automatic Skill orchestration or stage bridging into Workflows
- Knowledge retrieval, RAG, or indexing engines
- Automatic Consumer repository modification
- Automatic Module installation or adoption
- Skill / Knowledge CLI commands (`list`, `show`, `validate`, `execute`)
- Mandatory YAML parser or frontmatter
- Automatic versioning or lifecycle transitions
- Fake Module directory trees
- Core Knowledge example population in Phase 5 (deferred by Product Owner decision)
- Replacement of Methodology documents under `methodology/`

---

## 12. Future work (out of this document’s authority)

Not established here:

- Further Core Skills beyond the initial Core Skill created and Product Owner–accepted in Phase 5.3 (`skills/repository_analysis.md`; artifact lifecycle remains `draft`)
- Module-packaged Skills/Knowledge (requires Module packages)
- Pack Skill/Knowledge catalogs beyond existing Pack boundaries
- CLI discovery helpers
- Any execution or retrieval infrastructure (separate approval)

---

## Document maintenance

Changes to lifecycle states, Markdown-only format rules, governance mapping, placement rules, or execution boundaries require Product Owner awareness and an update to this file. Keep Framework Contract §6 concept meanings synchronized by **reference**, not by redefinition.

End of Skill & Knowledge Conventions v1.0.0.
