# AIOS Project Structure

Version: 1.3.4

Status: Active

Last Updated: 2026-11-05

This document describes the **actual** repository layout and the status of each area.

It must stay consistent with:

- [`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md) — authoritative architectural and governance contract
- [`AGENTS.md`](AGENTS.md) — agent operating manual (L0–L7 operationalization)
- [`MANIFEST.md`](MANIFEST.md) — product navigation

Status legend:

| Status | Meaning |
|--------|---------|
| **active** | Used and meaningful today |
| **partial** | Present with incomplete content |
| **placeholder** | Empty file or reserved name |
| **planned** | Empty directory reserved for future work |
| **demo** | Example / CI smoke target, not Core framework logic |

---

## Architectural layers

| Layer | Meaning | In this repository today |
|-------|---------|--------------------------|
| **Core** | Common engineering foundation | `AGENTS.md`, governance docs, `rules/`, `methodology/`, `scripts/aiosctl.py`, framework docs under `docs/` |
| **Modules** | Reusable engineering capabilities | **Partial** — thin catalog under `modules/`; five draft packages: `architecture-engineering`, `development-engineering`, `testing-quality-engineering`, `security-engineering`, and `devops-cloud-engineering` (each `draft` / `experimental`); Module-local Skills `architecture-boundary-review` and `implementation-change-hygiene` (each `draft`); `testing-quality-engineering`, `security-engineering`, and `devops-cloud-engineering` are skeleton-only (no Module-local Skills yet). Documentation/content only — no Module discovery engine, resolver, installer, or adaptive runtime |
| **Packs** | Optional domain / use-case extensions | `packs/education/` (partial) |
| **Consumer repositories** | Separate projects that adopt AIOS | Outside this repo; own ADRs, roadmaps, policies and implementation |

Relationship (approved, not new policy): Core remains usable without Packs; Packs may use Modules when Modules exist; Module recommendations do not bind a consumer until explicitly adopted (then as consumer-owned **L3** policy).

---

## Instruction precedence (L0–L7)

Canonical model — do not invent a competing hierarchy here.

| Level | Meaning |
|-------|---------|
| **L0** | Non-overridable constraints (safety, legal, security, privacy, licensing, compliance, and other justified non-overridable obligations) |
| **L1** | Explicit user instructions for the current task |
| **L2** | Consumer-approved ADRs and product decisions |
| **L3** | Consumer local policies |
| **L4** | AIOS Core binding defaults |
| **L5** | Explicitly adopted Pack guidance |
| **L6** | Module and methodology recommendations |
| **L7** | External knowledge (reference only) |

- **Authoritative definition:** [`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md) §7
- **Agent operationalization:** [`AGENTS.md`](AGENTS.md) §2

These two documents are complementary (contract vs operating manual), not competing authorities.

---

## Repository Root

```text
AIOS/                          # Git repository root
├── .agents/                   # planned locally; also the sync DESTINATION name in consumers
├── .github/                   # active – community + CI
├── assets/                    # active – branding and diagrams
├── checklists/                # active – initial Core set (review, release); notebook education-specific
├── docs/                      # active – framework documentation
│   ├── FRAMEWORK_CONTRACT.md  # authoritative architectural / governance contract
│   ├── ADAPTIVE_PROJECT_CONTEXT.md
│   ├── PROCESS_DEPTH_MODEL.md
│   ├── ADAPTIVE_GUIDANCE_MODEL.md
│   ├── ADAPTIVE_GOVERNANCE_MODEL.md
│   ├── ADAPTIVE_REFERENCE_SCENARIOS.md
│   ├── ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md
│   ├── WORKFLOW_CHECKLIST_CONVENTIONS.md
│   └── SKILL_KNOWLEDGE_CONVENTIONS.md
├── examples/                  # planned – empty domain folders
├── generators/                # planned – empty
├── knowledge/                 # planned – empty (no Core Knowledge example; remains Planned)
├── lab/                       # demo – sample FastAPI app for CI
├── methodology/               # active
├── modules/                   # partial – Engineering Module catalog (thin index + five draft Modules)
│   ├── README.md              # thin catalog index (not a registry/resolver)
│   ├── architecture-engineering/
│   │   ├── module.yaml        # Module metadata (draft / experimental / 0.1.0)
│   │   ├── README.md          # Module entry (L6 guidance; not adoption)
│   │   └── skills/
│   │       └── architecture_boundary_review.md  # Module Skill draft
│   ├── development-engineering/
│   │   ├── module.yaml        # Module metadata (draft / experimental / 0.1.0)
│   │   ├── README.md          # Module entry (L6 guidance; not adoption)
│   │   └── skills/
│   │       └── implementation_change_hygiene.md  # Module Skill draft
│   ├── testing-quality-engineering/
│   │   ├── module.yaml        # Module metadata (draft / experimental / 0.1.0)
│   │   └── README.md          # Module entry (L6 guidance; not adoption)
│   ├── security-engineering/
│   │   ├── module.yaml        # Module metadata (draft / experimental / 0.1.0)
│   │   └── README.md          # Module entry (L6 guidance; not adoption)
│   └── devops-cloud-engineering/
│       ├── module.yaml        # Module metadata (draft / experimental / 0.1.0)
│       └── README.md          # Module entry (L6 guidance; not adoption)
├── packs/                     # partial – optional packs
│   └── education/
│       ├── README.md          # Education & Learning Engineering Pack overview
│       └── AGENTS.education.md# preserved historical education operating guidance
├── prompts/                   # partial – interaction artifacts (Skills are canonical capabilities when authored)
├── rules/                     # active – aiosctl sync SOURCE (Core + legacy education rules)
├── scripts/                   # active – aiosctl CLI
├── skills/                    # partial – initial Core Skill (repository_analysis.md; artifact lifecycle draft; not a catalog)
├── templates/                 # placeholder – empty template files
├── tests/                     # planned – empty (framework tests not yet present)
├── workflows/                 # active – Phase 4 MVP (feature_development, release)
├── AGENTS.md                  # active – generic operating manual (L0–L7)
├── MANIFEST.md                # active – product contract
├── PROJECT_STRUCTURE.md       # active – this file
├── README.md                  # active
├── ROADMAP.md                 # active – framework roadmap
├── CHANGELOG.md               # active
├── CONTRIBUTING.md            # active
├── SECURITY.md                # active
├── CODE_OF_CONDUCT.md         # active
├── LICENSE                    # active – MIT
├── QUALITY_CHECKLIST.md       # placeholder
├── QUALITY_CONTROL.md         # partial – education-oriented checklist content
└── aiosctl.yaml               # partial – helper config; not read by CLI yet
```

---

## Directory Reference

### `docs/` — **active**

Framework documentation.

| Path | Status | Notes |
|------|--------|-------|
| `docs/FRAMEWORK_CONTRACT.md` | active | Authoritative architectural and governance contract (boundaries, ownership, consumption models, L0–L7 precedence) |
| `docs/ADAPTIVE_PROJECT_CONTEXT.md` | draft | Project Context and Task Context models for Adaptive Project Intelligence (design only; no engine) |
| `docs/PROCESS_DEPTH_MODEL.md` | draft | Complexity Dimensions and Process Depth Classification for Adaptive Project Intelligence (design only; no engine) |
| `docs/ADAPTIVE_GUIDANCE_MODEL.md` | draft | Adaptive Guidance conceptual model for Adaptive Project Intelligence (design specification; no runtime engine or automatic selection). |
| `docs/ADAPTIVE_GOVERNANCE_MODEL.md` | draft | Adaptive Governance conceptual model for Adaptive Project Intelligence (design specification; governance interactions with existing precedence and AGENTS.md §8; no runtime; no new approval policies). |
| `docs/ADAPTIVE_REFERENCE_SCENARIOS.md` | draft | Integrated Adaptive Project Intelligence reference scenarios (illustrative documentation validation references; not policies; not a runtime). |
| `docs/ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md` | draft | Documentation-level Adaptive Project Intelligence final audit specification and recorded Phase 6 documentation audit (**PASS WITH FINDINGS**; consistency and traceability only; not runtime/engine/CI verification). |
| `docs/WORKFLOW_CHECKLIST_CONVENTIONS.md` | draft | Markdown-first Workflow/Checklist authoring conventions |
| `docs/SKILL_KNOWLEDGE_CONVENTIONS.md` | draft | Markdown-first Skill/Knowledge authoring conventions |
| `docs/releases/` | planned | Empty nested folder reserved for future release notes |

Do not treat empty nested folders under `docs/` as implemented documentation products.

### `rules/` — **active**

Governance markdown files. **Sync source** for `aiosctl sync`: every `rules/*.md` is copied to `<consumer>/.agents/`.

Relevant **Core** governance files (non-exhaustive; all `rules/*.md` sync today):

| File | Role |
|------|------|
| `rules/PROJECT_RULES.md` | Project / repository operating rules |
| `rules/DECISION_RULES.md` | Decision process and quality priorities |
| `rules/AGENT_RULES.md` | Agent behavior rules |
| `rules/STATUS.md` | Status / progress conventions |

Also present: education-oriented rules (`BOOK_RULES`, `COURSE_RULES`, `VOCABULARY_RULES`, and related files) retained for **consumer sync compatibility**. They are not permanent Core identity; migration into the Education Pack remains a gated Phase 1 decision.

Do not rename or relocate these files without a migration plan.

### `methodology/` — **active**

Stack-agnostic engineering methods (typically **L6** recommendations unless a consumer adopts them as binding local policy at **L3**):

- RDIV
- Architecture First
- AI Collaboration
- Model-Agnostic AI
- Prompt Lifecycle
- Repository Onboarding

### `prompts/` — **partial**

| Subfolder | Status | Notes |
|-----------|--------|-------|
| `discovery/` | partial / active skeletons | Primary reusable discovery flow |
| `review/` | partial | `architecture_review.md` active; others empty or domain-oriented |
| `implementation/` | placeholder | Mostly empty files |
| `generators/` | placeholder | Empty |
| `translation/` | placeholder | Empty; education-oriented intent |

### `packs/` — **partial**

Optional content packs that are **not** required to use AIOS Core. Pack guidance is binding only when **explicitly adopted** (**L5**).

| Path | Status | Notes |
|------|--------|-------|
| `packs/education/README.md` | active | Optional Education & Learning Engineering Pack overview |
| `packs/education/AGENTS.education.md` | active archive | Preserved historical education-specific operating guidance (byte-preserved from pre–Phase-0 root manual) |

Education rules under `rules/` are **not** fully migrated into the pack yet.

### `scripts/` — **active**

| File | Status | Notes |
|------|--------|-------|
| `aiosctl.py` | active | Implements `sync` only (`validate`, `doctor`, `init`, `version` planned — not implemented) |

### `assets/` — **active**

Logos and architecture / workflow diagrams referenced by `README.md`.

### `templates/` — **placeholder**

Template filenames exist; file bodies are currently empty.

### `lab/aios-demo-api/` — **demo**

Minimal FastAPI application used by CI to prove a simple Python test path.

This is **not** the AIOS framework runtime.

### `workflows/` — **active** (Phase 4 MVP)

Initial Core Workflow definitions: `feature_development.md`, `release.md`.

Directory is active with the Phase 4 Core set. Not a workflow execution engine.

### `checklists/` — **active** (initial Core set)

Active directory with initial Core checklists (`review.md`, `release_checklist.md`). `notebook_creation.md` remains education-specific and separate from Core identity. Directory activity does not change individual checklist artifact lifecycles.

### `knowledge/` — **planned** (empty)

Planned and empty. Reserved for genuinely cross-cutting Core Knowledge when authored under [`docs/SKILL_KNOWLEDGE_CONVENTIONS.md`](docs/SKILL_KNOWLEDGE_CONVENTIONS.md) (conventions remain Draft). No Core Knowledge example exists; Knowledge remains Planned.

### `modules/` — **partial** (Engineering Module Catalog)

Thin catalog of optional Engineering Module packages (Phase 7 foundation).

| Path | Status | Notes |
|------|--------|-------|
| `modules/README.md` | present (thin catalog index) | Lists only packages that exist; not a registry, resolver, or installer; not an artifact lifecycle `active` claim |
| `modules/architecture-engineering/` | partial / draft | Engineering Module; `status: draft`, `maturity: experimental`, `version: 0.1.0` |
| `.../module.yaml` | draft metadata | Metadata v1; informational `requires_core: "1.0.1"` — not runtime enforcement |
| `.../README.md` | draft entry | L6 by default; explicit Consumer adoption → L3; does not own Consumer architecture |
| `.../skills/architecture_boundary_review.md` | draft Module Skill | `id` `architecture-boundary-review`; does not replace Core `repository-analysis` |
| `modules/development-engineering/` | partial / draft | Engineering Module; `status: draft`, `maturity: experimental`, `version: 0.1.0` |
| `.../module.yaml` | draft metadata | Metadata v1; informational `requires_core: "1.0.1"` — not runtime enforcement |
| `.../README.md` | draft entry | L6 by default; explicit Consumer adoption → L3; does not replace Core workflows or own Consumer coding standards |
| `.../skills/implementation_change_hygiene.md` | draft Module Skill | `id` `implementation-change-hygiene`; does not replace Core Feature Development Workflow or Core Review Checklist |
| `modules/testing-quality-engineering/` | partial / draft | Engineering Module; `status: draft`, `maturity: experimental`, `version: 0.1.0`; skeleton-only (no Module-local Skills) |
| `.../module.yaml` | draft metadata | Metadata v1; informational `requires_core: "1.0.1"` — not runtime enforcement |
| `.../README.md` | draft entry | L6 by default; explicit Consumer adoption → L3; enriches Core Feature Development Stage 7; does not replace Core workflows/checklists; Consumer testing policies remain Consumer-owned (**L2**) |
| `modules/security-engineering/` | partial / draft | Engineering Module; `status: draft`, `maturity: experimental`, `version: 0.1.0`; skeleton-only (no Module-local Skills) |
| `.../module.yaml` | draft metadata | Metadata v1; informational `requires_core: "1.0.1"` — not runtime enforcement |
| `.../README.md` | draft entry | L6 by default; explicit Consumer adoption → L3; enriches Core Review/Release security checkpoints; does not replace L0, Core checklists, or `SECURITY.md`; Consumer security policies and risk acceptance remain Consumer-owned (**L2**) |
| `modules/devops-cloud-engineering/` | partial / draft | Engineering Module; `status: draft`, `maturity: experimental`, `version: 0.1.0`; skeleton-only (no Module-local Skills) |
| `.../module.yaml` | draft metadata | Metadata v1; informational `requires_core: "1.0.1"` — not runtime enforcement |
| `.../README.md` | draft entry | L6 by default; explicit Consumer adoption → L3; enriches Core Release/ops practice; IaC inspection ≠ execution; does not replace Core Release or AIOS CI; Consumer infrastructure/deployment/SLO decisions remain Consumer-owned (**L2**) |

Not present: remaining planned Engineering domains (Data, Documentation); Module validation CLI; dependency resolver; auto-adoption; adaptive Module selection engine.

Module guidance does not bind Consumers until explicitly adopted. Framework Governance remains Core-owned.

### `skills/` — **partial** (initial Core Skill; artifact lifecycle `draft`)

Populated with the initial Core Skill definition `repository_analysis.md` (`id` `repository-analysis`). Directory population does **not** mean the Skill lifecycle is `active` or that a complete Skill catalog exists. Artifact lifecycle remains **`draft`** (`version` `0.1.0`). Authoring conventions remain Draft.

- Capability-specific Skills/Knowledge prefer Module-local placement **when Module packages exist** (prefer Module-local paths under existing packages such as `modules/architecture-engineering/`, `modules/development-engineering/`, `modules/testing-quality-engineering/`, `modules/security-engineering/`, or `modules/devops-cloud-engineering/`; do not invent undeclared Module trees).
- Not a Skill runner, Knowledge retrieval/RAG engine, or automated recommendation service.

### `generators/`, `tests/` — **planned**

Reserved empty directories for future generators and framework validation assets.

Module packages may exist under `modules/` separately. These directories are not Module discovery engines or automated recommendation services.

### `examples/` — **planned**

Empty folders (`DevOps`, `German`, `Python`) reserved for future adoption examples.

Not implemented consumer projects.

### `.github/` — **active**

Issue templates, PR template, support note, and CI workflow.

### `.agents/` — **planned** (in this repo)

Empty in the AIOS repository itself.

In **consumer** repositories, `.agents/` is the **destination** of `aiosctl sync`.

---

## Root Files of Note

| File | Status | Purpose |
|------|--------|---------|
| `docs/FRAMEWORK_CONTRACT.md` | active | Authoritative architectural / governance contract |
| `AGENTS.md` | active | Generic agent operating manual; operationalizes L0–L7 |
| `MANIFEST.md` | active | Product scope and navigation |
| `README.md` | active | Landing overview |
| `ROADMAP.md` | active | Framework evolution phases |
| `aiosctl.yaml` | partial | Optional project hints; **CLI does not read this file yet** |
| `QUALITY_CONTROL.md` | partial | Currently education/vocabulary oriented |
| `warning.txt` | local helper | Ignored by `.gitignore`; not part of the published contract |

---

## Framework vs Pack vs Demo vs Consumer

| Layer | What it is | Examples |
|-------|------------|----------|
| **Framework (AIOS Core)** | Reusable governance, methods and tooling entry points | `docs/FRAMEWORK_CONTRACT.md`, `AGENTS.md`, `rules/`, `methodology/`, `scripts/aiosctl.py` |
| **Modules** | Reusable engineering capabilities (partial catalog; five draft Modules present in repository tree — documentation/content only, not a runtime) | `architecture-engineering` (`draft`) + Skill `architecture-boundary-review` (`draft`); `development-engineering` (`draft`) + Skill `implementation-change-hygiene` (`draft`); `testing-quality-engineering` (`draft`, skeleton-only, no Module-local Skill yet); `security-engineering` (`draft`, skeleton-only, no Module-local Skill yet); `devops-cloud-engineering` (`draft`, skeleton-only, no Module-local Skill yet); remaining Engineering domains not packaged |
| **Optional packs** | Domain extensions (L5 when adopted) | `packs/education/` |
| **Demo** | CI / smoke sample | `lab/aios-demo-api/` |
| **Consumer repositories** | Separate projects adopting AIOS | Own ADRs (**L2**), local policies (**L3**); may sync `.agents/` from `rules/` |

AIOS Core must remain usable across stacks. Consumer content stays in consumer repositories.
