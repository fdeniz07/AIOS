# Review Checklist

| Field | Value |
|-------|-------|
| `id` | `review` |
| `title` | Review Checklist |
| `status` | `draft` |
| `version` | `0.1.0` |
| `scope` | `core` |
| `summary` | Verification list for human review of engineering changes before treating a change as reviewed. |
| `owner_role` | `reviewer` |

This document is a Core Checklist **definition**. It follows [`../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md`](../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md).

**Authority:** Core checklist guidance is **L6** by default. It is a verification aid, not an approval authority. It does not replace Consumer ADRs (**L2**), explicitly adopted Consumer local policies (**L3**), or non-overridable **L0** constraints. AI recommends; humans decide. Filled execution records remain Consumer-owned.

Primary workflow consumer: Feature Development Stage 8 in [`../workflows/feature_development.md`](../workflows/feature_development.md). This checklist may also be reused outside Feature Development for stack-agnostic human review of engineering changes.

**Boundary:** Completing this checklist does **not** constitute Release Approval, replace Release Workflow Stage 7 in [`../workflows/release.md`](../workflows/release.md), replace Consumer decisions or ADRs, or grant operational authorization (commit, tag, push, publish, deploy).

---

## 1. Purpose

Provide a reusable verification list for human review of engineering changes before treating a change as reviewed.

---

## 2. When to use

- Before treating a Feature Development Stage 8 review as complete.
- For other engineering change reviews where a Core verification aid is useful.
- When confirming that prior AGENTS approval gates were respected for operations already performed.

---

## 3. When not to use

- As a substitute for Release Approval or the Release Checklist (`id`: `release`).
- As authority to perform Git, publication, or deployment operations.
- As a place to store filled Consumer execution records inside AIOS Core.
- To redefine architecture or product decisions (those remain Consumer ADRs / L2).

---

## 4. Items

- (required) Actual diff reviewed against the intended scope; unintended scope called out.
- (required) Tests and validation relevant to the change were considered; unrun checks are not represented as passed.
- (required) Applicable prior approvals required by [`../AGENTS.md`](../AGENTS.md) §8 were obtained before related operations; final review is not treated as retroactive authorization.
- (required) Conflicts with Consumer ADRs (**L2**) and applicable local policies (**L3**) were identified and disclosed.
- (required) Non-overridable **L0** constraints were respected.
- (required) No secrets, credentials, or similar sensitive material were introduced.
- (required) Out-of-scope changes were avoided or explicitly authorized by an applicable owner.
- (optional) Documentation was updated when the change warranted it.
- (optional) Remaining risks and follow-up work were recorded where relevant.
- (optional) Performance and operability impact were considered when relevant to the change.

**Waivers:** A `(required)` item may be explicitly waived only by an owner/role the Consumer has authorized under its applicable policy or process, with recorded rationale. A waiver must not override L0 constraints, L2 Consumer ADR decisions, or applicable L3 Consumer local policy provisions ([`../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md`](../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md) §8.3).

---

## 5. Evidence expectations

- Scope fit is supported by the reviewed diff (or an equivalent change description).
- Validation status matches what was actually run.
- Required disclosures (ADR/policy conflicts, residual risks) are visible to the authorized reviewer.
- Waiver rationale, when used, is recorded in a Consumer-owned artifact.

---

## 6. Completion interpretation

Treat this checklist as complete for a given change when every `(required)` item is satisfied or validly waived, and any used `(optional)` items are either addressed or consciously omitted. Completion means the change may be treated as **reviewed** under this definition — not released, published, or deployed.

---

## 7. Approval

Human sign-off after this checklist, when required, follows [`../AGENTS.md`](../AGENTS.md) §8 and applicable Consumer policy. The checklist itself does not create a new approval authority or governance level. Approver role is typically `reviewer` / Consumer owner (role-based).

---

End of Review Checklist `review` v0.1.0 (`draft`).
