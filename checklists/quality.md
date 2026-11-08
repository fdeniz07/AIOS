# Quality Checklist

| Field | Value |
|-------|-------|
| `id` | `quality` |
| `title` | Quality Checklist |
| `status` | `draft` |
| `version` | `0.1.0` |
| `scope` | `core` |
| `summary` | Optional documentation and process hygiene aid for AIOS Core maintainers. |
| `owner_role` | `core-maintainer` |

This document is a Core Checklist **definition**. It follows [`../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md`](../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md).

**Authority:** Optional Core aid. Default guidance level is **L6**. It is a verification aid, not an approval authority and not a mandatory Consumer gate. It does not replace Consumer ADRs (**L2**), explicitly adopted Consumer local policies (**L3**), or non-overridable **L0** constraints. AI recommends; humans decide. Filled execution records remain Consumer-owned.

**Optional use:** Not every change requires this checklist. Mark items **N/A** when they do not apply. Completing every item is not required for every change.

---

## 1. Purpose

Provide a narrowly scoped documentation and process hygiene aid for AIOS Core maintainers.

---

## 2. When to use

- When reviewing Core documentation or process artifacts for clarity, consistency, and maintainability.
- As a complementary hygiene pass after content edits, when helpful.

## 3. When not to use

- As a substitute for engineering change review — use [`review.md`](review.md).
- As a substitute for release readiness — use [`release_checklist.md`](release_checklist.md).
- As a substitute for contribution acceptance checks — use [`../docs/CONTRIBUTION_CHECKLISTS.md`](../docs/CONTRIBUTION_CHECKLISTS.md).
- As education / vocabulary finish QA — use root [`../QUALITY_CONTROL.md`](../QUALITY_CONTROL.md) or Pack materials.
- As notebook creation verification — use [`notebook_creation.md`](notebook_creation.md).
- As a replacement for automated validation — run `python -m validation` (and related tests) separately when applicable.
- As authority to commit, push, publish, deploy, or enforce Consumer policy.

---

## 4. Items

Mark each item as done or **N/A**.

### A. Document and Content Quality

- [ ] Purpose is clear (or **N/A**)
- [ ] Scope is explicit (or **N/A**)
- [ ] Intended audience is clear (or **N/A**)
- [ ] Statements are consistent with the current repository state (or **N/A**)
- [ ] Assumptions are distinguished from verified facts (or **N/A**)
- [ ] Examples are understandable and appropriately contextualized (or **N/A**)

### B. Documentation Consistency

- [ ] Relevant authoritative documents are referenced (or **N/A**)
- [ ] Terminology and naming are consistent (or **N/A**)
- [ ] Relative links and file references are valid (or **N/A**)
- [ ] Outdated or contradictory statements are avoided (or **N/A**)
- [ ] Ownership and responsibility boundaries are clear (or **N/A**)

### C. Technical and Structural Hygiene

- [ ] Referenced paths and artifacts are present (or **N/A**)
- [ ] Examples and instructions are internally consistent (or **N/A**)
- [ ] Limitations and prerequisites are documented where relevant (or **N/A**)
- [ ] Unnecessary duplication and conflicting guidance are avoided (or **N/A**)

### D. Maintenance Readiness

- [ ] Content is maintainable (or **N/A**)
- [ ] Update triggers or dependencies are clear where relevant (or **N/A**)
- [ ] Document is consistent with the current repository structure (or **N/A**)
- [ ] Unresolved issues are identified rather than silently assumed away (or **N/A**)

---

## 5. Responsibility boundaries

| Artifact | Responsibility (not replaced by this checklist) |
|----------|--------------------------------------------------|
| [`review.md`](review.md) | Engineering change review |
| [`release_checklist.md`](release_checklist.md) | Release readiness |
| [`../docs/CONTRIBUTION_CHECKLISTS.md`](../docs/CONTRIBUTION_CHECKLISTS.md) | Contribution acceptance quality |
| [`../QUALITY_CONTROL.md`](../QUALITY_CONTROL.md) | Education / vocabulary-oriented quality control |
| [`notebook_creation.md`](notebook_creation.md) | Notebook creation |
| `python -m validation` | Automated read-only repository validation |

---

## 6. Final Review Notes

| Field | Value |
|-------|-------|
| Reviewer | <!-- name or role --> |
| Review date | <!-- YYYY-MM-DD --> |
| Findings | <!-- brief notes; use N/A if none --> |
| Follow-up references | <!-- issues, PRs, or docs; optional --> |

---

## 7. Related references

- Workflow / Checklist conventions: [`../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md`](../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md)
- Framework Contract: [`../docs/FRAMEWORK_CONTRACT.md`](../docs/FRAMEWORK_CONTRACT.md)
- Agent operating manual: [`../AGENTS.md`](../AGENTS.md)
