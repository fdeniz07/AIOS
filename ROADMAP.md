# AIOS Roadmap

Status: Active

Last Updated: 2026-11-02

This is the **AIOS framework** product roadmap.

It describes proposed evolutionary phases, not fixed delivery dates and not guaranteed release version numbers.

Consumer-project roadmaps, ADRs and backlogs belong in those repositories — not here.

Authoritative governance and precedence: [`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md) §7 (operationalized in [`AGENTS.md`](AGENTS.md) §2).

---

## Guiding Constraints

- Remain an open-source AI Software Engineering Framework
- Stay reusable across projects and technology stacks
- Support beginners through senior engineers and teams
- Prefer incremental change over rewrites
- Avoid unnecessary complexity
- Preserve useful Git history and consumer sync compatibility
- Provide the framework, not the domain content
- Do not present planned capabilities (module runtime, discovery engine, automated apply of recommendations, etc.) as already implemented

---

## Phase 0 — Foundation and Identity

**Intent:** Align AIOS identity and documentation with reality.

**Completed:**

- Generic `AGENTS.md`
- Honest README capability status
- Complete `MANIFEST.md` and `PROJECT_STRUCTURE.md` (Phase 0 baseline)
- Framework `ROADMAP.md`
- Minimal OSS docs (`CONTRIBUTING`, `SECURITY`, `CODE_OF_CONDUCT`)
- Preserve education operating manual under `packs/education/`
- Keep `rules/` sync contract unchanged for consumers

**Status:** Completed

---

## Phase 1 — Framework Contract and Governance Alignment

**Intent:** Make adoption unambiguous and align Core documentation with the approved contract.

**Status:** Completed

### Closure note

- Formally approved by the Product Owner.
- Final validation: Phase 1.7 – **PASS**.
- Governance Foundation acceptance criteria satisfied.

### Completed Phase 1 objectives

- Framework Contract created and approved (`docs/FRAMEWORK_CONTRACT.md`)
- L0–L7 governance / precedence model established (Contract §7)
- Root `AGENTS.md` aligned to operationalize L0–L7
- L4/L6 methodology authority clarified (Core methodologies remain L6 recommendations by default; explicit consumer adoption → L3)
- Relevant Core governance documents aligned (`rules/PROJECT_RULES.md`, `rules/DECISION_RULES.md`, `rules/AGENT_RULES.md`)
- `README.md` and `MANIFEST.md` aligned with the Contract
- Education Pack README created (`packs/education/README.md`) as domain-agnostic Education & Learning Engineering overview
- Framework Contract precedence correction (L0–L7 explicit; outdated AGENTS “tension” removed)
- Repository documentation refresh of `PROJECT_STRUCTURE.md`, `ROADMAP.md` and `CONTRIBUTING.md`
- Governance consistency and regression validation (Phase 1.5.x)

### Phase 1 exit summary

The **governance foundation is complete**: authoritative Framework Contract, operational L0–L7 model, Core document alignment, Education Pack entry-point documentation, and sync-compatible Core rules surface.

Items listed below remain **Product Owner–approved deferrals** as **future work**. They are **not** Phase 1 blockers and do not reopen Phase 1.

### Explicitly deferred beyond Phase 1 (Product Owner decisions)

1. **Education-rule migration**
   - Keep education-specific rules in their current `rules/` locations.
   - Preserve the existing flat `rules/*.md` → consumer `.agents/` sync contract.
   - Do not migrate, rename, remove, or reorganize these rules as part of Phase 1.
   - Handle migration as a separately scoped future task with compatibility analysis and explicit approval.

2. **Skills / workflows contribution standards**
   - Defer detailed contribution paths and standards to future capability / module development phases (see Phases 3, 4, 6, 8).
   - Do not imply that skills/workflows execution infrastructure already exists.

3. **Release documentation hygiene**
   - Defer the Phase 1 `CHANGELOG.md` update to a separate release-hygiene task.
   - Not a Phase 1 exit blocker.

4. **Implementation status labeling**
   - Remains ongoing documentation hygiene as placeholders fill in.
   - Not a Phase 1 exit blocker.

### Outside Phase 1 scope (future capabilities)

These remain later-phase direction only — **not implemented** and not Phase 1 incomplete work:

- Adaptive Module selection engines, populated module packages, automated recommendation apply
- CLI growth beyond `aiosctl sync` (Phase 2)
- Populated `workflows/`, `skills/`, `knowledge/` and related tooling (Phases 3–6)
- Broader validation/automation and ecosystem samples (Phases 7–8)

---

## Phase 2 — CLI Improvements

**Intent:** Grow `aiosctl` beyond rule sync — carefully.

Current: `aiosctl sync` copies `rules/*.md` → `<project>/.agents/`

Proposed commands (planned, not implemented):

- `validate`
- `doctor`
- `init`
- `version`

Also planned: decide whether `aiosctl.yaml` should become a real config surface.

**Compatibility rule:** do not break existing sync paths without a versioned migration.

---

## Phase 3 — Workflow and Checklist System

**Intent:** Provide a small set of stack-agnostic workflows and usable checklists.

- Populate `workflows/` with canonical engineering flows
- Complete release / review checklists
- Keep ceremony adaptive to project size

---

## Phase 4 — Skills and Knowledge

**Intent:** Add reusable engineering knowledge without shipping consumer content.

- Skill schema and examples under `skills/`
- Shared reference material under `knowledge/`
- Domains such as architecture, testing, security, DevOps, data, documentation

---

## Phase 5 — Adaptive Project Intelligence

**Intent:** Help agents detect repository context and adapt process depth.

- Project-type signals (library, service, monorepo, docs-only, etc.)
- Guidance for choosing workflows and skills
- Still documentation/convention-first unless/until tooling is proven
- No autonomous module discovery or selection engine is assumed by this phase’s intent alone

---

## Phase 6 — Engineering Modules

**Intent:** Package reusable engineering capabilities as optional modules/packs.

Examples of intended domains:

- Architecture Engineering
- Development Engineering
- Testing & Quality Engineering
- Security Engineering
- DevOps & Cloud Engineering
- Data Engineering
- Documentation & Governance

Education materials remain optional packs, not Core identity.

Module recommendations remain non-binding (**L6**) until a consumer explicitly adopts them as local policy (**L3**).

---

## Phase 7 — Validation and Automation

**Intent:** Verify framework integrity.

- Populate `tests/` for structure and contract checks
- Strengthen CI beyond demo API smoke tests
- Validate docs references and required entry points

---

## Phase 8 — Ecosystem and Integrations

**Intent:** Improve adoption across coding agents and host projects.

- Adoption examples under `examples/` (pointers or minimal samples)
- Integration notes for major coding assistants
- Community contribution of skills and workflows

---

## Explicit Non-Goals for This Roadmap

- Hosting a single company's product backlog inside AIOS Core
- Replacing general-purpose coding assistants
- Building a large runtime “AI OS kernel” before the documentation contract is solid
- Breaking `aiosctl sync` consumers for cosmetic folder moves
- Claiming planned Modules or adaptive tooling as shipped Core features

---

## How to Use This Document

Contributors and agents should treat later phases as **direction**, not unfinished work to invent in one pass.

Prefer completing earlier phases with small, reviewable changes.

Changes that affect architecture, governance, compatibility or consumer ownership must respect [`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md) and applicable approval gates.
