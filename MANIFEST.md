# AIOS Manifest

Version: 1.2.0

Status: Active

Last Updated: 2026-11-02

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
| **Module** | Reusable engineering capability (planned packages; adaptive recommendations as approved design) |
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
- Lightweight tooling such as `aiosctl sync`
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
| Rule synchronization CLI | `scripts/aiosctl.py` (`sync`) |
| OSS baseline docs | `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md` |
| Optional education operating manual (preserved) | `packs/education/AGENTS.education.md` |

### Partially available

| Capability | Notes |
|------------|-------|
| Prompt library beyond discovery | Many files are empty placeholders |
| Templates / checklists | Directories exist; several files empty |
| CI | Repository report + demo API tests; not a full framework validator |
| Visual / branding assets | Present under `assets/` |
| Optional packs | Education pack partial; migration of education `rules/` still gated |

### Planned

See `ROADMAP.md` for phased evolution (CLI, workflows, skills, knowledge, populated modules, validation, integrations).

Adaptive module **selection as automated tooling** is not implemented. Adaptive **recommendation** is an approved design principle.

---

## Planned Engineering Domains

Intended Module domains (packages not populated yet):

- Architecture Engineering
- Development Engineering
- Testing & Quality Engineering
- Security Engineering
- DevOps & Cloud Engineering
- Data Engineering
- Documentation & Governance

These should land as reusable Module assets — not as consumer-specific project content.

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
- Sync is selected with `--project`
- Orphan destination files are not deleted automatically

Do not break this contract without a versioned migration plan for consumers.

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

Document versions (for example Manifest `1.2.0`) describe document maturity and may differ from git tags. Prefer `ROADMAP.md`, this manifest and the Framework Contract over badge text when judging capability status.
