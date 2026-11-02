# Release Checklist

| Field | Value |
|-------|-------|
| `id` | `release` |
| `title` | Release Checklist |
| `status` | `draft` |
| `version` | `0.1.0` |
| `scope` | `core` |
| `summary` | Verification list for release readiness, human release decision, optional publication authorization, and closure — without execution authority. |
| `owner_role` | `releaser` |

This document is a Core Checklist **definition**. It follows [`../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md`](../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md).

**Authority:** Core checklist guidance is **L6** by default. It is a verification aid, not an approval authority and not an operational authorization. It does not replace Consumer ADRs (**L2**), explicitly adopted Consumer local policies (**L3**), or non-overridable **L0** constraints. AI recommends; humans decide. Filled execution records remain Consumer-owned.

Supports [`../workflows/release.md`](../workflows/release.md) (`id`: `release` workflow). Does not reproduce all workflow stages. Does not grant commit, tag, push, publish, or deploy authority.

**Boundaries:** Release approval (human go/no-go/defer) is distinct from operational authorization for each publication action. Completing the Review Checklist (`id`: `review`) does not satisfy this checklist or Release Workflow Stage 7. Do not invent SemVer rules, mandatory tag naming, version-bump algorithms, mandatory changelog formats, Module package release processes, deployment mandates, or Core rollback systems. Do not automatically reconcile root `VERSION` and Git tags.

---

## 1. Purpose

Provide a reusable verification list for release readiness, the human release decision, optional publication authorization checks, and closure — without execution authority.

---

## 2. When to use

- When following [`../workflows/release.md`](../workflows/release.md) for a versioned, published, or explicitly closed release process.
- Before treating a release decision or no-publication closure as verified against Core release readiness expectations.

---

## 3. When not to use

- As a substitute for Feature Development review — use Review Checklist `id`: `review` / [`review.md`](review.md).
- As authority to commit, tag, push, publish, or deploy.
- To store filled Consumer release run records inside AIOS Core.
- To redefine version policy, tag conventions, or Consumer ADRs.

---

## 4. Items

- (required) Release scope and publish / no-publish intent are explicit.
- (required) Feature Development completion is not treated as release authorization.
- (required) Framework, Module/Pack, and Consumer version surfaces are distinguished (not conflated); Consumer `AIOS_VERSION.md` is not treated as a Framework release version.
- (required) When a versioned assessment inspects both root `VERSION` and Git tags (or equivalent publication tags) and they differ, the discrepancy is disclosed for owner assessment; values are not automatically reconciled. This item does not require tags to exist.
- (required) Sync-breaking and Consumer-impact risks are disclosed when relevant to the release scope.
- (optional) Changelog or release notes are prepared according to existing repository practice, or a skip rationale is recorded. **Becomes required** when the repository’s existing practice uses changelog/notes for this release class, or when a public release requires human-readable notes.
- (required) Documentation and artifact readiness for the stated scope are assessed; gaps are disclosed.
- (required) Validation record states what was run and what was not run; current CI is not claimed as a complete Core release suite; unrun checks are not represented as passed.
- (optional) Security and dependency review is performed, or a justified low-risk skip is recorded. **Becomes required** when dependency changes, secret-exposure risk, supply-chain surface, or other security-relevant change surface exists.
- (required) Human release decision (go / no-go / defer) is recorded for applicable release classes (versioned publication, public release, or sync-breaking migration release; per owner policy for no-publish closes).
- (required) When publication or another operational action is in scope, required operational authorization is obtained **before** each applicable action (tag, push, publish, deploy, or equivalent). If publication is out of scope, record that no such operation is authorized or performed under this run.
- (required) Post-release verification is recorded after publication, or an explicit no-publication closure is recorded.
- (required) Existing Consumer rollback or incident procedure is referenced when it exists; otherwise relevant risks and ownership are disclosed. This item does not create a Core rollback mandate.

**Waivers:** A `(required)` item may be explicitly waived only by an owner/role the Consumer has authorized under its applicable policy or process, with recorded rationale. A waiver must not override L0 constraints, L2 Consumer ADR decisions, or applicable L3 Consumer local policy provisions ([`../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md`](../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md) §8.3).

---

## 5. Evidence expectations

- Scope and publication intent are written clearly enough to judge later items.
- Version/compatibility notes cite existing sources (`VERSION`, Contract distinctions, observed tags when inspected).
- Validation and security/skip rationales match reality.
- Release decision and any operational authorizations are explicit and timed **before** corresponding operations.
- Closure or post-release verification notes match whether publication occurred.

---

## 6. Completion interpretation

Treat this checklist as complete for a given release run when every applicable `(required)` item is satisfied or validly waived, conditional “becomes required” items are handled under their stated triggers, and used `(optional)` items are addressed or consciously omitted. Completion verifies readiness/decision/closure under this definition — it does not perform or authorize publication or deployment.

---

## 7. Approval

Human release decision and any operational authorizations follow [`../AGENTS.md`](../AGENTS.md) §8, [`../workflows/release.md`](../workflows/release.md), and applicable Consumer (or AIOS Core owner) policy. This checklist does not create a new approval authority or governance level. Approver role is typically `releaser` / Consumer owner / AIOS Product Owner for Core (role-based). Release approval and operational authorization remain distinct.

---

End of Release Checklist `release` v0.1.0 (`draft`).
