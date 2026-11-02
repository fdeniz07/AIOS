# AIOS Workflow & Checklist Conventions

Version: 1.0.0

Status: Draft

Last Updated: 2026-11-02

Document type: Convention specification

This document defines **Markdown-first conventions** for AIOS Workflow and Checklist **definitions**.

It is subordinate to the Framework Contract for architecture and governance:

- Concept meanings: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §6
- Content placement: [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5.5
- Instruction precedence (L0–L7): [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §7
- Module field / lifecycle patterns (conceptual reuse only): [`MODULE_METADATA.md`](MODULE_METADATA.md), [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md)
- Agent operationalization: [`../AGENTS.md`](../AGENTS.md) (RDIV, human approval gates)

This document does **not**:

- Implement a workflow or checklist execution engine
- Require YAML frontmatter or a runtime parser
- Create Module packages, Packs, or consumer repositories
- Grant execution authority to agents or CLI tools
- Redefine Workflow or Checklist meanings from Framework Contract §6
- Duplicate the Module metadata field dictionary

Illustrative Markdown structures in this document are **examples only**. They are not shipped Workflow or Checklist packages.

---

## 1. Purpose

Establish a shared, stack-agnostic way to author reusable:

- **Workflows** — multi-step engineering process definitions (stages, gates, handoffs)
- **Checklists** — verification lists used at review / done gates

Reusable definitions live in the AIOS repository (or future Module / Pack packages).  
**Consumer-local** Workflow and Checklist **definitions** may live in the Consumer repository; ownership remains with the Consumer. AIOS Core does not manage or automatically modify them.  
**Execution records** (filled checklists, run logs) remain **consumer-owned**.

---

## 2. Format rules (Markdown-first)

| Rule | Convention |
|------|------------|
| Format | Pure Markdown (`.md`) |
| Frontmatter | **Not used** |
| Machine schema / YAML | **Not required** |
| Runtime parser | **Not required** for this phase |
| Metadata | Human-readable Markdown **table** near the top of the document |
| Identifiers | Stable lowercase English `kebab-case` IDs |
| Versioning | Lightweight SemVer-style `MAJOR.MINOR.PATCH` in the metadata table |
| Examples | Must be labeled illustrative when not an approved shipped definition |

Do not introduce external dependencies to author or maintain these documents.

---

## 3. Governance and authority

Unchanged by these conventions:

| Level | Rule relative to Workflows / Checklists |
|-------|------------------------------------------|
| L0 | Non-overridable constraints — never overridden by a workflow or checklist |
| L1 | Explicit user task instructions (within L0) |
| L2 | Consumer-approved ADRs and product decisions |
| L3 | Consumer local policies — including **explicitly adopted** workflow / checklist policy |
| L4 | AIOS Core binding operating / governance defaults |
| L5 | Explicitly adopted Pack guidance |
| L6 | Module / methodology / workflow / checklist recommendations **by default** |
| L7 | External knowledge |

| Source | Default authority |
|--------|-------------------|
| Core workflow / checklist | **L6** recommendation |
| Module workflow / checklist | **L6** until explicitly adopted into consumer local policy → **L3** |
| Pack-contextualized guidance | **L5** when explicitly adopted |
| Consumer-local workflow / filled instance | Consumer-owned (typically L3 / local process) |

Human approval gates in [`../AGENTS.md`](../AGENTS.md) remain authoritative.  
Workflow and checklist text must not silently override ADRs, local policies, or L0 constraints.

---

## 4. Execution boundaries

A Workflow or Checklist **definition** does **not** authorize:

- Automatic file modifications
- Dependency installation
- Consumer repository changes
- Automatic Module or Pack adoption
- External service operations
- Git commits or pushes
- Autonomous stage transitions

Agents and tools may **recommend** following a workflow. Durable actions still require applicable human / consumer-owner approval under existing gates.

---

## 5. Placement and ownership

| Layer | May provide | Must not |
|-------|-------------|----------|
| **Core** | Cross-cutting engineering workflows under root `workflows/`; generic checklists under root `checklists/` | Domain curricula as Core identity; consumer-filled instances |
| **Module** | Capability-specific workflows and checklists inside the Module tree | Pack lock-in; silent Core governance override |
| **Pack** | Domain contextualization that may **reference** Core/Module workflows and checklists | Mandatory requirement to use AIOS Core; duplicate reusable Module capability unnecessarily |
| **Consumer** | Local adoption, localization, **consumer-local Workflow / Checklist definitions**, and **execution records** | Expectation that AIOS stores filled checklist instances or manages consumer-local definitions |

Additional placement rules:

- Root `workflows/` is reserved for **genuinely cross-cutting Core** workflows.
- Capability-specific flows prefer **Module-local** placement (when Modules exist).
- Education-specific content such as `checklists/notebook_creation.md` must **not** be promoted to Core identity.
- Do not store consumer-specific filled documents under AIOS Core `checklists/` or `workflows/`.
- Consumer-local Workflow and Checklist definitions, when used, live in the Consumer repository and remain Consumer-owned; AIOS Core does not manage or automatically modify them.

---

## 6. Shared lifecycle

Approved lifecycle states for Workflow and Checklist **definitions**:

| Status | Meaning |
|--------|---------|
| `draft` | Work in progress; not generally recommended for new durable adoption |
| `active` | Maintained and available for evaluation / use as L6 guidance |
| `deprecated` | Not recommended for new adoption; document successor and migration notes |

`review` and `approval` are **process activities**, not lifecycle status values.

Transitions are human/process decisions. No lifecycle automation is implied.

When `status` is `deprecated`, include a short migration note (why deprecated, successor `id` if any, what consumers must not assume).

---

## 7. Workflow conventions

### 7.1 Required metadata table

Place near the top of every Workflow definition:

| Field | Description |
|-------|-------------|
| `id` | Stable workflow identifier (`kebab-case`) |
| `title` | Human-readable name |
| `status` | `draft` \| `active` \| `deprecated` |
| `version` | SemVer-style document version |
| `scope` | `core` \| `module` \| `pack` \| `consumer-local` (informational) |
| `summary` | One short paragraph for discovery |

### 7.2 Body sections

A Workflow definition **should** include:

1. **Purpose** — why the workflow exists  
2. **Prerequisites** — what must be true before starting  
3. **Stages** — ordered stages (see §7.3)  
4. **Completion criteria** — when the whole workflow is considered complete  
5. **Related methodologies** — links only (for example RDIV); do not duplicate methodology text  

Optional: non-goals, related workflows, change history.

### 7.3 Stage conventions

Each stage **should** document:

| Element | Description |
|---------|-------------|
| Stage name | Short heading |
| Required / optional | Whether the stage is required for workflow completion |
| Intent | What the stage achieves |
| Inputs | Expected inputs |
| Outputs | Expected outputs / artifacts |
| Checklist references | Zero or more checklist `id`s (see §9) |
| Approval required | `yes` / `no` |
| Approver role | Role-based (for example “consumer owner”, “reviewer”) — not personal email |
| Evidence expectations | What evidence is expected if approval or verification applies |
| Completion criteria | When this stage is done |

**Conditional stages:** describe conditions in natural language under the stage (for example “Skip if the change is documentation-only”).  
No automatic branching engine is authorized.

**Illustrative stage skeleton (example only — not a shipped workflow):**

```markdown
## Stages

### 1. Analysis (required)

- Intent: Understand request, repository context, and risks.
- Inputs: Task description; relevant repository paths.
- Outputs: Short understanding notes; identified constraints.
- Checklists: _(none)_
- Approval required: no
- Completion criteria: Risks and scope are stated explicitly.

### 2. Review gate (required)

- Intent: Human confirmation before durable structural change.
- Checklists: `review` _(illustrative id only)_
- Approval required: yes
- Approver role: consumer owner / authorized reviewer
- Evidence expectations: Explicit confirmation recorded in a consumer-owned artifact when durable decisions change.
- Completion criteria: Required checklist items addressed; approval obtained when required.
```

### 7.4 What a Workflow must not do

- Grant silent execution authority
- Replace consumer ADRs
- Embed full checklist item text (reference by `id` / link instead)
- Claim an implemented runner or CLI executor

---

## 8. Checklist conventions

### 8.1 Required metadata table

| Field | Description |
|-------|-------------|
| `id` | Stable checklist identifier (`kebab-case`) |
| `title` | Human-readable name |
| `status` | `draft` \| `active` \| `deprecated` |
| `version` | SemVer-style document version |
| `scope` | `core` \| `module` \| `pack` \| `consumer-local` |
| `summary` | Short discovery text |
| `owner_role` | Intended role (for example `reviewer`, `releaser`) |

### 8.2 Body sections

A Checklist definition **should** include:

1. **Purpose**  
2. **When to use / when not to use** (short)  
3. **Items** — required and optional (see §8.3)  
4. **Evidence expectations** — what “done” looks like for items that need proof  
5. **Completion interpretation** — how to judge the checklist complete  
6. **Approval** — if a human sign-off is expected after the checklist  

### 8.3 Required vs optional items

Mark every item explicitly:

| Marker | Meaning |
|--------|---------|
| `(required)` | Must be satisfied (or explicitly waived, with recorded rationale, only by an owner/role the Consumer has authorized under its applicable policy or process) before the referencing stage/workflow may be treated as complete. A waiver must not override L0 constraints, L2 Consumer ADR decisions, or applicable L3 Consumer local policy provisions |
| `(optional)` | Recommended; omission alone does not block completion |

**Illustrative item list (example only — not a shipped checklist):**

```markdown
## Items

- (required) Diff reviewed for unintended scope
- (required) Tests relevant to the change were considered
- (optional) Performance impact noted
- (optional) Follow-up issues filed
```

### 8.4 Definition versus instance

| Artifact | Owner | Phase 4 MVP |
|----------|-------|-------------|
| **Checklist definition** | AIOS Core / Module / Pack source | **In scope** (conventions + later content) |
| **Checklist instance** (filled run) | Consumer repository / process | **Out of scope** — no mandatory instance schema |

Do not introduce a checklist execution-instance format in this document.

### 8.5 What a Checklist must not do

- Own architecture or product decisions (those remain ADRs / L2)
- Store consumer-filled answers inside AIOS Core definitions
- Imply automated enforcement solely by existing in `checklists/`

---

## 9. Workflow → Checklist references

| Rule | Convention |
|------|------------|
| Prefer | Stable checklist `id` |
| Also provide | Relative Markdown link to the canonical definition when the file exists |
| Avoid | Copying checklist item bodies into the workflow |
| Reuse | The same checklist may be referenced by multiple workflows or stages |

**Illustrative reference forms:**

```markdown
- Checklist id: `release`
- Definition: [`../checklists/release_checklist.md`](../checklists/release_checklist.md)
```

If a referenced checklist file is not yet populated, say so honestly (placeholder / draft). Do not claim validation that was not performed.

---

## 10. Versioning

- Bump `version` in the metadata table when the definition’s guidance changes meaningfully.
- Prefer SemVer-style intent: MAJOR for breaking guidance changes; MINOR for additive stages/items; PATCH for clarifications.
- Do not equate document `version` with AIOS Framework `VERSION`, Module package versions, or consumer `AIOS_VERSION.md` sync markers.
- No formal state machine or release automation is required for these documents.

---

## 11. Relationship to methodologies

Core methodologies under `methodology/` (for example RDIV) remain **methodology guidance** (L6 by default).

Workflows may **link** to methodologies. They must not duplicate or replace them.

---

## 12. Future work (explicitly out of this document’s authority)

Phase 4 content work established Core Feature Development and Release Workflow definitions under `workflows/`, plus initial Core Review and Release Checklist definitions under `checklists/`. Those packages are **not** created by this conventions document; they follow it. This document’s lifecycle status remains **Draft** until Product Owner approval of the conventions themselves.

Not established by this conventions document:

- Additional Core / Module / Pack Workflow or Checklist packages beyond the initial Phase 4 set
- Checklist instance schemas
- Workflow / checklist CLI commands (`list`, `show`, `validate`, `execute`)
- Automatic stage transitions or branching engines
- Module package population
- Workflow or checklist execution engines

---

## Document maintenance

Changes to lifecycle states, Markdown-only format rules, governance mapping, or execution boundaries require Product Owner awareness and an update to this file. Keep Framework Contract §6 concept meanings synchronized by **reference**, not by redefinition.

End of Workflow & Checklist Conventions v1.0.0.
