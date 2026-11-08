# AIOS Manifest

Version: 1.2.1

Status: Active

Last Updated: 2026-11-08

---

## Product Mission

AIOS (**Artificial Intelligence Operating System**) is an open-source **AI Software Engineering Framework**.

It turns AI coding assistants into repository-aware engineering partners by placing durable context — rules, methodologies, workflows, prompts and structure — into the repository itself.

> **AIOS provides the framework, not the content.**

Slogan: *Engineer the workspace, not the prompt.*

Consumer repositories own their domain knowledge, product roadmaps, ADRs, backlogs and curricula.

---

## Framework Contract and AGENTS.md

| Document | Role |
|----------|------|
| [`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md) | **Authoritative architectural meta-document** — boundaries, ownership, consumption, sync compatibility, precedence |
| [`AGENTS.md`](AGENTS.md) | **Operating manual** that operationalizes the contract for AI agents |

These are not competing hierarchy levels. If they appear inconsistent, report the issue; do not invent a new hierarchy.

Canonical instruction precedence (**L0–L7**): Framework Contract §7; operational detail in `AGENTS.md` §2.

---

## Architectural Boundaries

| Layer | Meaning |
|-------|---------|
| **Core** | Common engineering foundation and cross-domain principles |
| **Module** | Reusable engineering capability (six draft / experimental packages present; adoption is explicit) |
| **Pack** | Optional domain- or use-case-specific extension (for example Education) |
| **Consumer** | Product repository — owns ADRs, backlog, implementation and local policy |

Relationship rules:

- A Pack may use one or more Modules.
- A Module must not be tied to one Pack unless explicitly justified.
- Core remains usable without Packs or Modules.
- Modules are **recommendations** unless the consumer adopts them as local policy.

### Binding versus recommendation

| Kind | Authority |
|------|-----------|
| Binding AIOS Core guidance | L4 — subject to L0–L3 |
| Adopted Pack guidance | L5 — only when explicitly adopted and in scope |
| Module / methodology recommendations | L6 — recommendations by default |
| Consumer ADRs / product decisions | L2 — override generic AIOS defaults |
| Consumer local policies | L3 — consumer-owned |

Non-overridable safety, legal, security, privacy, licensing and compliance constraints remain **L0**.

---

## Product Scope

### In scope

- Framework Contract and generic agent operating guidance
- Governance rules intended for reuse across projects
- Engineering methodologies (RDIV, Architecture First, and related)
- Reusable discovery / review prompts
- Templates and checklists (as they mature)
- Optional packs for specialized domains
- Lightweight tooling via `scripts/aiosctl.py` (`sync`, `version`, `doctor`)
- Documentation that explains how to adopt AIOS

### Out of scope (for AIOS Core)

- Consumer-project roadmaps, sprint backlogs and product ADRs
- Domain curricula and lesson content as Core identity
- Claiming unimplemented automation as shipped engines
- Autonomous module-selection or decision engines
- Lock-in to a single LLM, IDE or language stack

---

## Target Audience

- Beginners learning professional repository practice
- Intermediate developers improving AI-assisted delivery
- Senior engineers and architects enforcing consistency
- Technical teams standardizing AI collaboration

---

## Core Principles

1. **Repository-driven engineering** — engineer the workspace, not only the prompt
2. **Architecture First** — understand structure before changing it
3. **RDIV** — Review → Decide → Implement → Verify
4. **Model-agnostic governance** — rules outlive any single model
5. **Human-in-the-loop** — conflicts disclosed; approvals respected
6. **Minimal change** — preserve useful work; avoid rewrites
7. **Adaptive to project context** — recommend proportionally; do not impose
8. **Consumer authority** — approved consumer ADRs/product decisions prevail over generic AIOS defaults (within L0)
9. **Framework ≠ content** — Core stays reusable; packs and consumers carry domain material

---

## Consumption Models

| Model | Meaning |
|-------|---------|
| **Reference-only** | Reference AIOS without copying AIOS-managed files |
| **Synced** | Copy AIOS-managed artifacts under the sync contract |
| **Hybrid** | Combination of the two — not a separate runtime |

See Framework Contract §8–§9.

---

## Existing Capabilities

### Available now

| Capability | Location |
|------------|----------|
| Framework Contract | `docs/FRAMEWORK_CONTRACT.md` |
| Agent operating manual (L0–L7) | `AGENTS.md` |
| Product / structure navigation | `MANIFEST.md`, `PROJECT_STRUCTURE.md`, `README.md` |
| Governance rule set (syncable) | `rules/` |
| Engineering methodologies | `methodology/` |
| Discovery prompt pack (partial bodies) | `prompts/discovery/` |
| Architecture review prompt | `prompts/review/architecture_review.md` |
| `aiosctl` CLI | `scripts/aiosctl.py` — implemented commands: `sync`, `version`, `doctor` |
| CLI regression tests | `tests/cli/` (covers `sync`, `version`, `doctor`) |
| Independent validation CLI | `python -m validation` (separate from `aiosctl`; Framework Structure, Module Contract, Documentation Integrity) |
| Validation pytest suites | `tests/validation_foundation/`, `tests/validation_structure/`, `tests/validation_module_contract/`, `tests/validation_documentation/` |
| OSS baseline docs | `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md` |
| Optional education operating manual (preserved) | `packs/education/AGENTS.education.md` |

### Partially available

| Capability | Notes |
|------------|-------|
| Prompt library beyond discovery | Many files are empty placeholders |
| Templates / checklists | Directories exist; several files empty |
| Visual / branding assets | Present under `assets/` |
| Optional packs | Education pack partial; migration of education `rules/` still gated |

### Tooling distinction (`aiosctl` versus `python -m validation`)

| Entry point | Role today |
|-------------|------------|
| `scripts/aiosctl.py` | Consumer-facing CLI. Implemented: `sync`, `version`, `doctor`. **Not** implemented: `validate`, `init`. |
| `python -m validation` | Independent read-only repository validation entry point (Validation Foundation). Not an `aiosctl` subcommand. |
| `aiosctl.yaml` | May list helper project hints; **not consumed by the CLI today**. |

`aiosctl sync` remains the compatibility-critical sync contract (see below). Prefer `python -m validation` for framework validators; do not treat it as `aiosctl validate`.

### Planned

See `ROADMAP.md` for phased evolution. Remaining `aiosctl` commands **`validate`** and **`init`** are not implemented.

Adaptive module **selection as automated tooling** is not implemented. Adaptive **recommendation** is an approved design principle.

---

## Engineering Modules (current catalog)

Six Engineering Module packages exist under `modules/` as documentation/content packages. Metadata (`module.yaml`) currently records **`status: draft`** and **`maturity: experimental`** for each.

| Module | Package id |
|--------|------------|
| Architecture Engineering | `architecture-engineering` |
| Development Engineering | `development-engineering` |
| Testing & Quality Engineering | `testing-quality-engineering` |
| Security Engineering | `security-engineering` |
| DevOps & Cloud Engineering | `devops-cloud-engineering` |
| Data Engineering | `data-engineering` |

Important boundaries:

- Packages **exist** and can be inspected in the repository.
- They are **not** stable, installed, or automatically adopted.
- They are **not** mandatory for Consumer repositories.
- Module guidance remains **L6** by default; durable use requires explicit Consumer adoption into local policy (**L3** within scope).
- Catalog presence is not a discovery engine, resolver, installer, or runtime.

**Documentation Engineering** (sometimes phrased as Documentation & Governance) is **explicitly deferred** and is **not** part of this six-package catalog. Framework Governance remains Core-owned.

---

## Optional Packs

| Pack | Status | Purpose |
|------|--------|---------|
| `packs/education/` | Partial | Education-oriented agent guidance and (later) related rules/prompts |

Education-specific rules under `rules/` remain for **sync compatibility** until an approved migration. Pack guidance is binding only when adopted (L5).

---

## Consumer-Project Boundaries

| Belongs in AIOS | Belongs in the consumer repository |
|-----------------|------------------------------------|
| Framework Contract, generic AGENTS, Core rules, methodologies | Product roadmap and backlog |
| Reusable prompts, planned skills/modules | Project ADRs and decision logs |
| Sync tooling and adoption docs | Domain code and curricula |
| Optional packs (source) | Environment secrets and deployment config; whether to adopt a Pack |

AIOS must not silently overwrite consumer-owned decisions or artifacts.

### Sync contract (compatibility-critical)

`aiosctl sync` currently copies `rules/*.md` into `<project>/.agents/` and writes `AIOS_VERSION.md`.

- Source glob and destination path are part of the compatibility surface
- Synced files are AIOS-derived; they are not consumer ADRs
- `aiosctl.yaml` may list helper project hints but is **not read by the CLI today**
- Sync is selected with explicit `--project`
- Orphan destination files are not deleted automatically

Do not break this contract without a versioned migration plan for consumers.

### CI (current)

GitHub Actions (`.github/workflows/ci.yml`) currently runs:

| Job | What it executes |
|-----|------------------|
| `repository-analysis` / `report-verification` | Repository report artifact |
| `application-test` | Demo API tests under `lab/aios-demo-api/` |
| `framework-validation-tests` | `pytest` over `tests/cli` and the validation test suites (`tests/validation_*`) |
| `framework-validation-cli` | `python -m validation` (independent of `aiosctl`) |

These jobs do not implement `aiosctl validate` or `aiosctl init`.

---

## Entry Points and Navigation

| Start here | Why |
|------------|-----|
| `README.md` | Overview, status, quick start |
| `docs/FRAMEWORK_CONTRACT.md` | Authoritative framework contract and precedence |
| `AGENTS.md` | How AI agents must operate (L0–L7) |
| `MANIFEST.md` | This product manifest |
| `PROJECT_STRUCTURE.md` | Actual tree and directory status |
| `ROADMAP.md` | Framework evolution phases |
| `methodology/README.md` | Method index |
| `CONTRIBUTING.md` | How to contribute |
| `SECURITY.md` | Vulnerability reporting |
| `packs/education/AGENTS.education.md` | Preserved education operating manual |

---

## Versioning Note

Distinguish conceptually:

- **AIOS Framework Version** — distribution / Core contract surface (git tags + doc versions today)
- **Module / Pack Version** — proposed for future populated packages
- **Consumer Integration Version** — partial today via sync `AIOS_VERSION.md` (timestamp + source path)

Document versions (for example Manifest `1.2.1`) describe document maturity and may differ from git tags. Prefer `ROADMAP.md`, this manifest and the Framework Contract over badge text when judging capability status.
