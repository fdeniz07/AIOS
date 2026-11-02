# AIOS Roadmap

Status: Active

Last Updated: 2026-11-02

This is the **AIOS framework** product roadmap.

It describes proposed evolutionary phases, not fixed delivery dates and not guaranteed release version numbers.

Consumer-project roadmaps, ADRs and backlogs belong in those repositories — not here.

---

## Guiding Constraints

- Remain an open-source AI Software Engineering Framework
- Stay reusable across projects and technology stacks
- Support beginners through senior engineers and teams
- Prefer incremental change over rewrites
- Avoid unnecessary complexity
- Preserve useful Git history and consumer sync compatibility
- Provide the framework, not the domain content

---

## Phase 0 — Foundation and Identity

**Intent:** Align AIOS identity and documentation with reality.

- Generic `AGENTS.md`
- Honest README capability status
- Complete `MANIFEST.md` and `PROJECT_STRUCTURE.md`
- Framework `ROADMAP.md`
- Minimal OSS docs (`CONTRIBUTING`, `SECURITY`, `CODE_OF_CONDUCT`)
- Preserve education operating manual under `packs/education/`
- Keep `rules/` sync contract unchanged for consumers

**Status:** In progress / current documentation phase

---

## Phase 1 — Framework Contract

**Intent:** Make adoption unambiguous.

- Clear Core vs pack vs consumer boundaries
- Documented rule hierarchy without conflicts
- Status labels for placeholders vs active assets
- Contribution paths for skills, workflows and docs
- Decide education-rule migration strategy without breaking `.agents` consumers

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

---

## How to Use This Document

Contributors and agents should treat later phases as **direction**, not unfinished work to invent in one pass.

Prefer completing earlier phases with small, reviewable changes.
