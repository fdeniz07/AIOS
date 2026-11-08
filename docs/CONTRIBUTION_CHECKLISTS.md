# AIOS Contribution Checklists

Status: Active documentation aid (Phase 9)

| Field | Value |
|-------|-------|
| `id` | `contribution-checklists` |
| `title` | AIOS Contribution Checklists |
| `status` | `active` |
| `version` | `1.0.0` |
| `scope` | `core` |
| `summary` | Artifact-specific contribution and review checklists |
| `owner_role` | `core-maintainer` |

These checklists help contributors and reviewers verify artifact-specific quality before maintainer acceptance.

They are subordinate to:

- [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md)
- [`../AGENTS.md`](../AGENTS.md)
- [`SKILL_KNOWLEDGE_CONVENTIONS.md`](SKILL_KNOWLEDGE_CONVENTIONS.md)
- [`WORKFLOW_CHECKLIST_CONVENTIONS.md`](WORKFLOW_CHECKLIST_CONVENTIONS.md)
- [`MODULE_METADATA.md`](MODULE_METADATA.md)
- [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md)
- [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md)
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md)

Item classification follows [`WORKFLOW_CHECKLIST_CONVENTIONS.md`](WORKFLOW_CHECKLIST_CONVENTIONS.md) §8.3:

| Marker | Meaning |
|--------|---------|
| `(required)` | Must be satisfied (or explicitly waived, with recorded rationale, only by an authorized owner/role) before the contribution may be treated as checklist-complete. A waiver must not override L0, L2 Consumer ADR decisions, or applicable L3 local policy. |
| `(optional)` | Recommended; omission alone does not block completion |

These checklists do **not**:

- Introduce new lifecycle status values
- Replace human maintainer acceptance
- Implement validators, auto-fixers, or runtimes
- Become an execution engine, adoption mechanism, or installation mechanism
- Imply Consumer adoption

Preserved artifact / Module lifecycle values remain exactly:

- `draft`
- `active`
- `deprecated`

---

## Shared checks (all artifacts)

- [ ] `(required)` Change fits an intentional roadmap phase or an approved issue.
- [ ] `(required)` Framework Contract boundaries are preserved (Core / Module / Pack / Consumer).
- [ ] `(required)` L0–L7 precedence is unchanged and not redefined.
- [ ] `(required)` Status language is honest (`draft` / `active` / `deprecated` as applicable).
- [ ] `(required)` No claim of automatic adoption, installation, discovery engine, or resolver behavior.
- [ ] `(required)` Consumer-owned decisions remain Consumer-owned.
- [ ] `(required)` Relevant existing validation was considered (`python -m validation` when docs/structure/module contracts are affected).

---

## Skill checklist

Use for Core Skills under `skills/` or Module-local Skills under `modules/<id>/skills/`.

Conventions authority: [`SKILL_KNOWLEDGE_CONVENTIONS.md`](SKILL_KNOWLEDGE_CONVENTIONS.md)

### Purpose and scope

- [ ] `(required)` Purpose states a focused reusable capability outcome.
- [ ] `(required)` Scope is stack-agnostic unless a documented, justified limitation exists.
- [ ] `(required)` Placement is correct (Core only if genuinely cross-cutting; otherwise Module-local when a Module package exists).
- [ ] `(required)` Skill does not own multi-role orchestration (that belongs to Workflows).

### Actionable instructions

- [ ] `(required)` Procedure steps are ordered and actionable (**how**).
- [ ] `(required)` Inputs and outputs are identified.
- [ ] `(required)` When-to-use / when-not-to-use guidance is present.
- [ ] `(required)` Related references are links only (no pasted full Workflow/Knowledge bodies).

### Clear limitations

- [ ] `(required)` Constraints, failure modes, and stop conditions are documented.
- [ ] `(required)` Human approval / decision boundaries are explicit.
- [ ] `(required)` Skill text does not authorize automatic Consumer repository modification, Module adoption, commits, or secret handling beyond L0-safe guidance.

### Compliance with Skill conventions

- [ ] `(required)` Pure Markdown with metadata table (no YAML frontmatter requirement).
- [ ] `(required)` Stable lowercase kebab-case `id`.
- [ ] `(required)` Lifecycle is one of `draft` / `active` / `deprecated`.
- [ ] `(required)` Default authority remains L6 unless a Consumer explicitly adopts it as local policy (L3).
- [ ] `(required)` Does not claim a Skill runner or execution engine.

---

## Workflow checklist

Use for Core Workflows under `workflows/` or Module-local Workflows when present.

Conventions authority: [`WORKFLOW_CHECKLIST_CONVENTIONS.md`](WORKFLOW_CHECKLIST_CONVENTIONS.md)

### Defined steps

- [ ] `(required)` Stages / steps are explicitly defined.
- [ ] `(optional)` Gates, handoffs, and decision points are clear where needed.
- [ ] `(required)` Workflow remains a multi-step process definition (not a single atomic Skill).

### Inputs and outputs

- [ ] `(required)` Expected inputs / preconditions are identified.
- [ ] `(required)` Expected outputs / artifacts / handoff results are identified.
- [ ] `(required)` Checklist references (if any) use ids/links rather than embedding full checklist bodies incorrectly.

### Process consistency

- [ ] `(required)` Placement is correct (Core only if cross-cutting; capability-specific flows prefer Module-local placement).
- [ ] `(optional)` Process depth / ceremony remains proportionate; no mandatory heavyweight path for every project.
- [ ] `(required)` Does not silently override Consumer ADRs, local policies, or L0 constraints.

### Compliance with Workflow conventions

- [ ] `(required)` Pure Markdown with required metadata table fields per conventions.
- [ ] `(required)` Lifecycle is one of `draft` / `active` / `deprecated`.
- [ ] `(required)` Definition-versus-instance boundary is preserved (no Consumer filled run records stored as Core definitions).
- [ ] `(required)` No workflow execution engine is implied or required.
- [ ] `(required)` Default authority remains L6 until explicit Consumer adoption → L3.

---

## Knowledge checklist

Use for Core Knowledge under `knowledge/` or Module-local Knowledge when present.

Conventions authority: [`SKILL_KNOWLEDGE_CONVENTIONS.md`](SKILL_KNOWLEDGE_CONVENTIONS.md)

### Information accuracy

- [ ] `(required)` Statements are accurate for the claimed scope.
- [ ] `(required)` Uncertain or evolving claims are disclosed.
- [ ] `(required)` No invented APIs, files, product decisions, or “implemented engines”.

### Sources where applicable

- [ ] `(required)` External or normative sources are cited when claims depend on them.
- [ ] `(required)` Source links are used as L7 reference material, not as new governance authority.
- [ ] `(required)` Consumer-specific private content is not introduced into Core/Module Knowledge.

### Distinction from executable instructions

- [ ] `(required)` Knowledge explains **what** / **why**, not a disguised step-by-step Skill or Workflow.
- [ ] `(required)` Actionable procedures are linked to Skills/Workflows instead of being embedded as executable runs.
- [ ] `(required)` No Knowledge retrieval / RAG engine is implied.

### Compliance with Knowledge conventions

- [ ] `(required)` Pure Markdown with metadata table (no YAML frontmatter requirement).
- [ ] `(required)` Stable lowercase kebab-case `id`.
- [ ] `(required)` Lifecycle is one of `draft` / `active` / `deprecated`.
- [ ] `(required)` Placement follows Core vs Module rules.
- [ ] `(required)` Default authority remains L6 (or L5 when Pack-contextualized and explicitly adopted).

---

## Module checklist

Use for packages under `modules/<id>/`.

Authorities: [`MODULE_METADATA.md`](MODULE_METADATA.md), [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md), [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md), Framework Contract §5.

### Metadata completeness

- [ ] `(required)` `module.yaml` includes required fields: `id`, `version`, `title`, `summary`, `status`.
- [ ] `(required)` `id` is lowercase English kebab-case and Pack-independent.
- [ ] `(required)` `version` is SemVer.
- [ ] `(required)` `status` is exactly one of `draft` / `active` / `deprecated`.
- [ ] `(required)` Optional fields (`maturity`, `applies_when`, `avoid_when`, `tags`, `provides`, `requires_core`, `deprecation`) are valid when present.
- [ ] `(required)` No forbidden metadata v1 dependency fields (for example `dependencies`).
- [ ] `(required)` Metadata does not claim Consumer adoption, installation, or sync state.

### Lifecycle compliance

- [ ] `(required)` Draft Modules disclose incompleteness and are not generally recommended for durable new adoption.
- [ ] `(required)` Active Modules provide a usable `README.md` entry point and required metadata.
- [ ] `(required)` Deprecated Modules include README heading exactly `## Migration`.
- [ ] `(required)` No additional lifecycle states are invented.
- [ ] `(required)` Active/draft status is never equated with adopted/installed.

### Module Contract compatibility

- [ ] `(required)` Module has a clear responsibility and scope.
- [ ] `(required)` Guidance remains L6 by default; explicit Consumer adoption → Consumer-owned L3 within scope.
- [ ] `(required)` Module does not redefine Core governance or L0–L7.
- [ ] `(required)` Module does not depend on a specific Pack.
- [ ] `(required)` No resolver, installer, registry engine, or auto-adoption behavior is introduced.

### Correct Core / Module / Pack / Consumer boundaries

- [ ] `(required)` Capability-specific Skills/Knowledge/Workflows are Module-local when packaged here.
- [ ] `(required)` Core identity documents are not forked into the Module.
- [ ] `(required)` Consumer ADRs, product architecture, and local policies remain Consumer-owned.
- [ ] `(required)` Pack composition references (if any) are documentation-only and not Module dependencies.
- [ ] `(required)` Catalog index updates (if needed) remain a thin index, not a discovery/resolver runtime.

---

## Reviewer note

Checklist completion supports human review. It does not replace maintainer acceptance and does not prove architectural correctness by itself.
