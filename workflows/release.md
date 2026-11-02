# Release Workflow

| Field | Value |
|-------|-------|
| `id` | `release` |
| `title` | Release Workflow |
| `status` | `draft` |
| `version` | `0.1.0` |
| `scope` | `core` |
| `summary` | Stack-agnostic guidance from release scope through validation, approval, optional publication, and post-release verification, without execution authority. |

This document is a Core Workflow **definition**. It follows [`../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md`](../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md).

**Authority:** Core Workflow guidance is **L6** by default. It does not grant execution authority, replace Consumer ADRs (**L2**), override explicitly adopted Consumer local policies (**L3**), or weaken non-overridable **L0** constraints. Instruction precedence remains Framework Contract §7 / [`../AGENTS.md`](../AGENTS.md) §2. AI recommends; humans decide. Durable release and product decisions belong to the Consumer (or the AIOS Product Owner for AIOS Core itself).

Human approval gates in [`../AGENTS.md`](../AGENTS.md) §8 remain authoritative. This Workflow introduces no new global approval policies or governance levels. **Release approval** (Stage 7) is distinct from **operational authorization** to perform a specific tag, push, publish, or deploy action (Stage 8). Required prior approvals must be obtained **before** the relevant operation. Final review or post-release verification does **not** retroactively authorize an operation performed without required prior approval.

**Boundary with Feature Development:** [`feature_development.md`](feature_development.md) covers analysis through implementation, validation, review, and handover. This Release Workflow starts when a release scope or release candidate is **independently** identified. Feature Development completion does **not** authorize a release. This Workflow does **not** repeat feature implementation planning or coding. Defects found during release validation may be handed back to Feature Development through an explicit handoff. Release completion does **not** imply deployment unless the Consumer release process includes it.

**RDIV relationship:** [`../methodology/rdiv.md`](../methodology/rdiv.md) remains the authoritative methodology. This Workflow orchestrates release-oriented application of RDIV — it does not redefine or duplicate it. Link only.

**Version surfaces (existing contracts only):**

| Surface | Role |
|---------|------|
| Root `VERSION` | Authoritative AIOS **Framework** version source for tooling such as `aiosctl version` |
| Git tags / GitHub Releases | Distinct **publication** records when used — not automatically synchronized with `VERSION` |
| Document `version` fields | Document-local; not Framework version |
| Module / Pack versions | Separate surfaces when packages exist; do not invent Module package release here |
| Consumer `AIOS_VERSION.md` | Sync/integration marker — **not** a Framework release version |

When root `VERSION` and the latest Git tag differ: **identify and report** the discrepancy; state that the relationship requires **owner assessment**. Do not assume it is automatically an error. Do not automatically reconcile or modify either value. Do not introduce a new SemVer policy, mandatory tag naming convention, version-bump algorithm, or mandatory changelog format.

---

## 1. Purpose

Provide a reusable, stack-agnostic sequence for moving from an identified release scope through readiness assessment, validation, human release decision, optional publication, and post-release verification — without assuming CI, a package registry, a deployment platform, or a public release process.

Definitions live here as Core guidance. Filled run records and Consumer-local adaptations remain Consumer-owned.

---

## 2. Prerequisites

Before starting:

- A release scope or release candidate has been **independently identified** (not inferred solely from Feature Development completion).
- Relevant Feature Development (or equivalent) work for in-scope changes is complete enough to assess, or gaps are explicitly accepted as release blockers/risks by the authorized owner.
- Contributors treat this Workflow as **L6 recommendation** unless the Consumer (or AIOS Core owner process) has explicitly adopted it as local policy (**L3**).
- No assumption that a workflow engine, automatic tagger, publisher, or deployer exists.
- Applicable ADRs, local policies, and Framework Contract compatibility expectations can be discovered.

Adjust ceremony to release class: documentation-only or no-publication internal closes may use conditional light/skip paths below; sync-breaking or public Framework releases must not skip assessment merely because the change set looks small.

---

## 3. Stages

### 1. Release Scope and Target Identification

- **Classification:** Required
- **Intent:** State what is being released (or closed without publication), for whom, and what is explicitly out of scope — including whether publication/deployment is in scope at all.
- **Inputs:** Owner release intent; candidate change set or version target; known constraints; optional Feature Development handover notes.
- **Outputs:** Release scope statement; out-of-scope list; publication intent (publish / no-publish); initial risk notes.
- **Checklist references:** _(none in this version)_
- **Approval required:** no for drafting scope; **yes** if the scope itself would create or change a durable product/release decision without an existing owner decision
- **Approver role:** Consumer owner / AIOS Product Owner (for Core) when durable release decisions are created or changed
- **Evidence expectations:** Scope and publication intent are explicit enough that later stages can skip or deepen correctly.
- **Completion criteria:** Target and exclusions are written; Feature Development is not treated as silent release authorization; no-publication path is allowed when intended.

### 2. Version and Compatibility Assessment

- **Classification:** Required for Framework/Core or sync-affecting releases. **Light / skip with rationale** only when the close is explicitly non-versioned (no Framework version change and no versioned distribution) and owner-accepted.
- **Intent:** Assess version and compatibility using **existing** repository contracts — Framework vs Module/Pack vs Consumer Integration distinctions ([`../docs/FRAMEWORK_CONTRACT.md`](../docs/FRAMEWORK_CONTRACT.md) §10); identify sync-breaking or consumer-impact risks; report `VERSION` vs tag discrepancies without auto-fixing them.
- **Inputs:** Release scope; root `VERSION` (authoritative Framework version source); known tags/releases if inspected; Contract compatibility expectations; Module surfaces only if they actually exist.
- **Outputs:** Version/compatibility assessment notes; discrepancy report if `VERSION` and latest tag differ (owner assessment required — not assumed automatic error); sync-breaking impact flags when relevant.
- **Checklist references:** _(none in this version)_
- **Approval required:** no for assessment; **yes** before adopting a durable versioning/compatibility decision that supersedes an existing owner decision or breaks public/sync contracts ([`../AGENTS.md`](../AGENTS.md) §8 where applicable)
- **Approver role:** Consumer owner / AIOS Product Owner when durable version or compatibility decisions require approval
- **Evidence expectations:** Assessment cites existing sources (`VERSION`, Contract, observed tags if checked); does not invent SemVer/tag policy; does not invent Module package release.
- **Completion criteria:** Compatibility posture for this release is stated; discrepancies disclosed; no automatic VERSION/tag reconciliation performed by agents under this Workflow’s authority (it has none).

### 3. Changelog and Release Notes

- **Classification:** **Conditional** — required when the repository’s practice uses changelog/release notes for this release class, or when a public release needs human-readable notes. **Skip with rationale** when no such practice exists and no public notes are required.
- **Intent:** Prepare or update human-readable release communication without mandating a specific changelog format (`CHANGELOG.md` may exist; format is not a Core-enforced schema).
- **Inputs:** Scope; change summary; existing changelog/notes practice if any.
- **Outputs:** Draft notes or changelog updates appropriate to practice; or explicit skip rationale.
- **Checklist references:** _(none in this version)_
- **Approval required:** no for drafts; **yes** if notes would assert durable product claims the owner has not accepted
- **Approver role:** Consumer owner / AIOS Product Owner when durable claims require acceptance
- **Evidence expectations:** Content matches actual changes; no false validation or publication claims.
- **Completion criteria:** Notes prepared per applicable practice, or skip justified; no mandatory format invented.

### 4. Documentation and Artifact Readiness

- **Classification:** Required (depth scales with release class)
- **Intent:** Confirm documentation and release artifacts needed for the stated scope are ready or gaps are disclosed (readiness ≠ inventing missing distribution machinery).
- **Inputs:** Scope; version/compatibility notes; docs and artifacts in repository relevant to the release.
- **Outputs:** Readiness notes; gap list; owner-visible blockers if any.
- **Checklist references:** _(none in this version)_
- **Approval required:** no
- **Approver role:** n/a
- **Evidence expectations:** Gaps are explicit; Consumer-specific packaging is not pretended to be Core-universal.
- **Completion criteria:** Readiness for the stated scope is assessed; blockers named before approval/publication.

### 5. Quality and Release Validation

- **Classification:** Required for meaningful versioned or published releases. **Light** for documentation-only or explicitly no-publication closes (verify docs accuracy as appropriate).
- **Intent:** Run or cite **available** validation relevant to the release (tests, CI results, `aiosctl doctor`, `aiosctl version` readouts, manual checks). Do **not** claim current CI is a complete Core release suite. Report what was actually run and what was not.
- **Inputs:** Scope; readiness notes; existing CI/test/`doctor` capabilities when present.
- **Outputs:** Validation record (ran / not ran / results); residual quality risks.
- **Checklist references:** _(none in this version)_
- **Approval required:** no
- **Approver role:** n/a
- **Evidence expectations:** Honest status only; no claim that unrun checks passed; tooling remains stack-agnostic (use what the repo has).
- **Completion criteria:** Validation status is truthful relative to scope; critical gaps disclosed before Release Approval.

### 6. Security and Dependency Review

- **Classification:** **Conditional** — deepen when dependency changes, secret exposure risk, supply-chain surface, or other security-relevant change surface exists. **Light / skip with rationale** for minor documentation-only releases without those risks.
- **Intent:** Review security and dependency impacts appropriate to the change surface without mandating a full security program for every release.
- **Inputs:** Scope; dependency/lockfile or secret-touching diffs when present; known Consumer security policy if any.
- **Outputs:** Security/dependency notes; findings or explicit low-risk rationale.
- **Checklist references:** _(none in this version)_
- **Approval required:** **yes** if proceeding would knowingly accept a disclosed high-impact security risk against owner policy; otherwise no for routine review notes
- **Approver role:** Consumer owner / authorized security decision-maker when acceptance of material risk is required
- **Evidence expectations:** Depth matches risk; secrets are never committed ([`../AGENTS.md`](../AGENTS.md) §9).
- **Completion criteria:** Risk-appropriate review done or skip justified; material risks disclosed.

### 7. Release Approval

Use checklist `release` at this stage to assess applicable **pre-publication readiness** and the human release decision. Completing Stage 7 does **not** mark the entire Release Checklist complete. Publication-related authorization must still be obtained before each applicable Stage 8 operation. Checklist completion for the release run is addressed at Stage 9 after applicable closure items.

- **Classification:** **Required** before versioned publication, public release, or sync-breaking migration release. **Light / Consumer-policy path** for explicit no-publication internal closes that do not assert a Framework release.
- **Intent:** Obtain the human **release decision** (go / no-go / defer) distinct from performing Git/tag/publish/deploy operations. Preserve Consumer (or AIOS Core owner) ownership and existing AGENTS gates. Do not claim AGENTS enumerates every publication verb (for example Git tagging) if it does not; map irreversible, public-contract, and durable-decision impacts to existing gates.
- **Inputs:** Scope; version/compatibility assessment; notes; readiness; validation; security notes.
- **Outputs:** Explicit release decision; conditions or deferrals; record of required prior approvals still outstanding before any Stage 8 operation.
- **Checklist references:** Checklist id: `release` — Definition: [`Release Checklist`](../checklists/release_checklist.md) (Stage 7: pre-publication readiness and release decision items only — not full checklist completion)
- **Approval required:** **yes** for go-to-publish / Framework release decisions and AGENTS §8-impacting outcomes; per owner policy for no-publish close
- **Approver role:** Consumer owner / AIOS Product Owner / authorized releaser role (role-based)
- **Evidence expectations:** Decision is explicit; outstanding operational authorizations for Stage 8 are listed, not assumed.
- **Completion criteria:** Human release decision recorded for the release class; Stage 8 not treated as already authorized unless separately granted; applicable pre-publication Release Checklist items assessed for this stage without claiming full checklist completion.

### 8. Tagging and Publication

- **Classification:** **Conditional** — only when publication (tag, GitHub Release, package publish, and/or Consumer-defined deploy) is **in scope** and **authorized**. **Skip** on no-publish paths.
- **Intent:** Perform or coordinate authorized publication steps **only** under applicable prior human/Consumer-owner authorization. This Workflow **grants no** operational authority to commit, tag, push, publish, or deploy.
- **Inputs:** Stage 7 go decision; explicit operational authorization for the specific actions; prepared notes/artifacts.
- **Outputs:** Publication record (what was published where) or explicit skip; pointers to tags/releases if created by authorized humans/tooling under their process.
- **Checklist references:** _(none in this version)_
- **Approval required:** **yes** — applicable prior authorization for each operational action before it is performed (not after)
- **Approver role:** Consumer owner / AIOS Product Owner / authorized releaser for the specific publication channel
- **Evidence expectations:** Actions match authorization; no agent-assumed tag/push/publish; deployment only if Consumer process includes it and authorization exists.
- **Completion criteria:** Authorized publication completed as scoped, or stage skipped with rationale; no retroactive authorization pattern used.

### 9. Post-Release Verification and Handover

Use the same checklist `release` to complete applicable **post-release verification** or **no-publication closure** items. The Release Checklist is considered complete for the release run only when all applicable items across the run have been satisfied or validly waived (Stage 7 readiness/decision work plus Stage 9 closure work). This Workflow and checklist grant no commit, tag, push, publish, or deploy authority.

- **Classification:** Required (short). After publication, verify at a depth appropriate to the release. On no-publication paths, record that the process **closed without publication**.
- **Intent:** Confirm observable post-conditions, hand over residual risks, and close the Workflow run. Reference existing Consumer rollback/incident procedures **when present**; if none exist, disclose relevant risks and ownership. This Core Workflow does **not** create a rollback runbook, rollback stage mandate, or rollback automation/authority.
- **Inputs:** Publication record or no-publish close; validation notes; owner contacts/process links if any.
- **Outputs:** Verification notes; handover summary; residual risks; optional pointer to Consumer incident/rollback process if it exists.
- **Checklist references:** Checklist id: `release` — Definition: [`Release Checklist`](../checklists/release_checklist.md) (Stage 9: post-release verification or no-publication closure items; full checklist completion only when all applicable run items are satisfied or validly waived)
- **Approval required:** no unless Consumer local policy requires formal close-out sign-off
- **Approver role:** Consumer owner when their policy requires close-out approval
- **Evidence expectations:** Claims match reality; no invented rollback system; no false deploy implications.
- **Completion criteria:** Process closed with verification or explicit no-publish closure; residuals and ownership stated; applicable Release Checklist closure items completed so that, together with Stage 7 assessments, all applicable checklist items for the run are satisfied or validly waived.

---

## 4. Completion criteria

The Release Workflow may be treated as complete when:

1. Stages required for the release class were completed (or explicitly and justifiably light-pathed / skipped under the classifications above).
2. Version/compatibility posture and any `VERSION`/tag discrepancies were assessed and disclosed without unauthorized mutation.
3. Validation and readiness status is truthful for the stated scope.
4. Required human release decisions and any required prior operational authorizations were obtained **before** corresponding operations.
5. Publication occurred only if in scope and authorized — or the run closed explicitly without publication.
6. Post-release verification or no-publish closure handover exists at an appropriate depth.
7. L0 was respected; L2 ADRs and applicable L3 policies were respected or conflicts were disclosed and resolved by authorized owners.
8. Feature Development responsibilities were not duplicated; defects were handed back when appropriate.

Completeness of this Core **definition** does not imply an automated release, green CI suite claim, deployment, or rollback capability.

---

## 5. Related methodologies

Link only — do not duplicate:

- [`../methodology/rdiv.md`](../methodology/rdiv.md) — authoritative RDIV methodology
- [`../methodology/architecture_first.md`](../methodology/architecture_first.md) — understand impact before releasing structural change
- [`../methodology/ai_collaboration.md`](../methodology/ai_collaboration.md) — AI assists; human decides
- [`../methodology/model_agnostic.md`](../methodology/model_agnostic.md) — governance independent of a single model vendor

Related Workflow (boundary, not a substitute):

- [`feature_development.md`](feature_development.md) — implementation through handover; does not authorize release

Operational gates and precedence: [`../AGENTS.md`](../AGENTS.md).
Versioning terminology and compatibility: [`../docs/FRAMEWORK_CONTRACT.md`](../docs/FRAMEWORK_CONTRACT.md) §10.
Authoring rules: [`../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md`](../docs/WORKFLOW_CHECKLIST_CONVENTIONS.md).

---

## 6. Non-goals

This Workflow does **not**:

- Implement or require a workflow execution engine
- Provide automatic stage transitions or branching
- Use YAML frontmatter or a runtime parser
- Perform or authorize automatic version bumps
- Automatically reconcile `VERSION` and Git tags
- Mandate a SemVer policy or Git tag naming convention
- Authorize automatic Git commit, tag, push, publication, or deployment
- Define a checklist instance schema
- Authorize automatic Consumer repository modification
- Authorize automatic Module or Pack adoption
- Mandate a deployment pipeline
- Create a mandatory rollback system or rollback automation
- Replace Consumer ADRs, product decisions, or existing methodologies
- Duplicate Feature Development responsibilities (implementation planning or coding)
- Treat Consumer `AIOS_VERSION.md` as a Framework release version
- Invent Module package release while Module packages do not exist
- Claim that current CI is a complete Core release test suite
- Claim that [`../AGENTS.md`](../AGENTS.md) explicitly lists every publication verb (for example Git tagging) if it does not
- Elevate Core Release guidance above L6 unless explicitly adopted as local policy

---

End of Release Workflow `release` v0.1.0 (`draft`).
