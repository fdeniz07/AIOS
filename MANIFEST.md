# AIOS Manifest

Version: 1.1.0

Status: Active

Last Updated: 2026-11-02

---

## Product Mission

AIOS (**Artificial Intelligence Operating System**) is an open-source **AI Software Engineering Framework**.

It turns AI coding assistants into repository-aware engineering partners by placing durable context — rules, methodologies, workflows, prompts and structure — into the repository itself.

> **AIOS provides the framework, not the content.**

Consumer repositories own their domain knowledge, product roadmaps, ADRs, backlogs and curricula.

---

## Product Scope

### In scope

- Generic agent operating guidance (`AGENTS.md`)
- Governance rules intended for reuse across projects
- Engineering methodologies (RDIV, Architecture First, and related)
- Reusable discovery / review prompts
- Templates and checklists (as they mature)
- Optional packs for specialized domains
- Lightweight tooling such as `aiosctl sync`
- Documentation that explains how to adopt AIOS

### Out of scope (for AIOS Core)

- Consumer-project roadmaps, sprint backlogs and product ADRs
- Domain curricula and lesson content
- Claiming unimplemented automation as shipped engines
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
7. **Adaptive to project context** — ceremony scales with repository reality
8. **Framework ≠ content** — Core stays reusable; packs and consumers carry domain material

---

## Existing Capabilities

### Available now

| Capability | Location |
|------------|----------|
| Generic agent operating manual | `AGENTS.md` |
| Product contract / navigation | `MANIFEST.md`, `PROJECT_STRUCTURE.md`, `README.md` |
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

### Planned

See `ROADMAP.md` for phased evolution (CLI, workflows, skills, knowledge, modules, validation, integrations).

---

## Planned Engineering Domains

Reusable engineering knowledge is intentional product scope. Planned module / skill domains include:

- Architecture Engineering
- Development Engineering
- Testing & Quality Engineering
- Security Engineering
- DevOps & Cloud Engineering
- Data Engineering
- Documentation & Governance

These domains should land as reusable skills, workflows and knowledge — not as consumer-specific project content.

---

## Optional Packs

| Pack | Status | Purpose |
|------|--------|---------|
| `packs/education/` | Partial | Education-oriented agent guidance and (later) related rules/prompts |

Education-specific rules under `rules/` remain in place for **consumer sync compatibility** and are not migrated in Phase 0.

---

## Consumer-Project Boundaries

| Belongs in AIOS | Belongs in the consumer repository |
|-----------------|------------------------------------|
| Generic AGENTS / rules / methodologies | Product roadmap and backlog |
| Reusable prompts and skills | Project ADRs and decision logs |
| Sync tooling and adoption docs | Domain code and curricula |
| Optional packs | Environment secrets and deployment config |

### Sync contract (compatibility-critical)

`aiosctl sync` currently copies `rules/*.md` into `<project>/.agents/` and writes `AIOS_VERSION.md`.

- Source glob and destination path are part of the compatibility surface
- `aiosctl.yaml` may list helper project hints but is **not read by the CLI today**
- Sync is selected with `--project`
- Orphan destination files are not deleted automatically

Do not break this contract without a versioned migration plan for consumers.

---

## Entry Points and Navigation

| Start here | Why |
|------------|-----|
| `README.md` | Overview, status, quick start |
| `AGENTS.md` | How AI agents must operate |
| `MANIFEST.md` | This product contract |
| `PROJECT_STRUCTURE.md` | Actual tree and directory status |
| `ROADMAP.md` | Framework evolution phases |
| `methodology/README.md` | Method index |
| `CONTRIBUTING.md` | How to contribute |
| `SECURITY.md` | Vulnerability reporting |
| `packs/education/AGENTS.education.md` | Preserved education operating manual |

---

## Versioning Note

Framework documentation versions (for example AGENTS / Manifest `1.1.0`) describe document maturity.

Git tags such as `v1.0.0` record repository releases and may lag or lead individual document versions. Prefer `ROADMAP.md` and this manifest over badge text when judging capability status.
