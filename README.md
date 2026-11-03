<p align="center">
  <img src="assets/images/banner.png" alt="AIOS Banner">
</p>

<p align="center">

![Version](https://img.shields.io/badge/version-v1.0.0-blue?style=for-the-badge)
![License](https://img.shields.io/github/license/fdeniz07/AIOS?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/fdeniz07/AIOS?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/fdeniz07/AIOS?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/fdeniz07/AIOS?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/fdeniz07/AIOS?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)
![AI Ready](https://img.shields.io/badge/AI-Ready-success?style=for-the-badge)

</p>

<p align="center">

**Repository-driven AI Engineering Framework**

*Engineer the workspace, not the prompt.*

</p>

---

# AIOS

AIOS (**Artificial Intelligence Operating System**) is an open-source framework that helps AI coding assistants behave like **repository-aware engineering partners**.

Instead of relying only on chat prompts, AIOS keeps durable engineering context in the repository: operating rules, methodologies, workflows, prompts and structure.

> AIOS provides the **framework**, not the **content**.
>
> Your product knowledge, ADRs, backlogs and curricula stay in your repositories (or in optional packs).

---

## Table of Contents

- Why AIOS
- Philosophy
- Architecture
- Repository Structure
- Governance and Ownership
- How to Consume AIOS
- Capability Status
- Core Components
- AIOS Workflow
- Decision Guidance
- Repository Lifecycle
- Compatible With
- Quick Start
- Tooling Notes (`aiosctl`)
- Validation
- Roadmap
- Contributing
- License
- Vision

---

# Why AIOS?

Modern AI coding assistants are powerful, yet they often:

- ignore repository conventions
- forget previous project decisions
- create inconsistent documentation
- modify unrelated files
- skip quality checks
- duplicate existing implementations

The problem is rarely “not enough prompt text”.

The real gap is **missing persistent project context**.

AIOS moves that context into the repository so humans and agents share the same operating contract.

---

# Philosophy

> AI doesn't become better because of longer prompts.
>
> AI becomes better because of better repositories.

AIOS teaches assistants through engineering structure: rules, methods, reviews and explicit approval gates.

---

# Architecture

<p align="center">
<img src="assets/images/architecture.png" alt="Architecture">
</p>

AIOS sits between your repository and your AI coding assistant as a **governance and method layer**.

Before rushing to code, assistants are expected to:

- understand
- analyze
- plan
- implement
- review
- document

Detailed layout and directory status: [`PROJECT_STRUCTURE.md`](PROJECT_STRUCTURE.md)

Product manifest: [`MANIFEST.md`](MANIFEST.md)

Authoritative framework contract: [`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md)

Agent operating manual (operationalizes the contract): [`AGENTS.md`](AGENTS.md)

### Adaptive Project Intelligence (Phase 6 — completed design)

Phase 6 delivers a **conceptual and documentation foundation** for how agents assess project/task context, scale process depth, recommend guidance, and respect existing governance. It does **not** ship an adaptive runtime, recommendation engine, registry, resolver, scoring system, or automation.

| Document | Role |
|----------|------|
| [`docs/ADAPTIVE_PROJECT_CONTEXT.md`](docs/ADAPTIVE_PROJECT_CONTEXT.md) | Project Context and Task Context models |
| [`docs/PROCESS_DEPTH_MODEL.md`](docs/PROCESS_DEPTH_MODEL.md) | Process Depth (intensity) classification |
| [`docs/ADAPTIVE_GUIDANCE_MODEL.md`](docs/ADAPTIVE_GUIDANCE_MODEL.md) | Guidance types, relevance, and lifecycle |
| [`docs/ADAPTIVE_GOVERNANCE_MODEL.md`](docs/ADAPTIVE_GOVERNANCE_MODEL.md) | Interactions with precedence and human approval |
| [`docs/ADAPTIVE_REFERENCE_SCENARIOS.md`](docs/ADAPTIVE_REFERENCE_SCENARIOS.md) | Integrated illustrative validation scenarios |
| [`docs/ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md`](docs/ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md) | Documentation-level audit record (**PASS WITH FINDINGS**; not runtime verification) |

Phased status: [`ROADMAP.md`](ROADMAP.md) Phase 6.

---

## Repository Structure

```text
AIOS/
├── AGENTS.md                    # Agent operating manual (operationalizes the contract)
├── MANIFEST.md                  # Product scope and navigation
├── PROJECT_STRUCTURE.md         # Actual tree + status labels
├── ROADMAP.md                   # Framework evolution phases
├── docs/FRAMEWORK_CONTRACT.md   # Authoritative architectural contract
├── docs/ADAPTIVE_*.md           # Phase 6 Adaptive Project Intelligence design docs
├── rules/                       # Syncable governance rules (aiosctl source)
├── methodology/                 # RDIV, Architecture First, …
├── prompts/                     # Reusable prompts (discovery active; others partial)
├── packs/education/             # Optional education pack (partial)
├── templates/                   # Placeholders for reusable templates
├── checklists/                  # Partial quality checklists
├── scripts/aiosctl.py           # Rule sync CLI
├── assets/                      # Branding and diagrams
├── lab/aios-demo-api/           # Demo app for CI smoke tests
├── knowledge/                   # Planned
├── skills/                      # Planned
├── workflows/                   # Planned
├── tests/                       # Planned (framework tests)
└── examples/                    # Planned adoption examples
```

Empty directories are **planned or reserved**, not shipped engines.

---

# Governance and Ownership

[`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md) is the **authoritative architectural meta-document** for AIOS boundaries, consumption models, ownership and instruction precedence.

[`AGENTS.md`](AGENTS.md) **operationalizes** that contract for AI coding agents. It is not a competing authority layer.

### Consumer ownership

- Consumer-approved ADRs and product decisions take precedence over generic AIOS defaults.
- Consumer local policies remain consumer-owned.
- AIOS must not silently overwrite consumer decisions or artifacts.
- Applicable safety, legal, security, privacy, licensing and compliance constraints remain non-overridable.

### Instruction precedence (summary)

AIOS uses a canonical **L0–L7** precedence model (non-overridable constraints → user task instructions → consumer ADRs → consumer local policies → AIOS Core → adopted Packs → Module/methodology recommendations → external knowledge).

Full definition: [`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md) §7 and [`AGENTS.md`](AGENTS.md) §2.

### Adaptive module recommendations

AIOS is designed to analyze project context and **recommend** relevant engineering Modules.

- The project owner retains decision authority.
- Modules are recommendations unless explicitly adopted as consumer local policy.
- Phase 6 documents the Adaptive Project Intelligence **design** (context, process depth, guidance, governance, scenarios, documentation audit).
- This repository does **not** ship an autonomous module-selection or adaptive recommendation **engine** today.

---

# How to Consume AIOS

| Model | Meaning |
|-------|---------|
| **Reference-only** | Read AIOS guidance in place; do not copy AIOS-managed files into the consumer |
| **Synced** | Copy AIOS-managed artifacts under the sync contract (`rules/*.md` → `.agents/` today) |
| **Hybrid** | Combination of reference-only and synced — not a separate runtime |

Synced `.agents/` files are AIOS-derived guidance. Sync does not make AIOS the owner of consumer ADRs or product decisions.

Details: [`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md) §8–§9.

---

# Capability Status

### Available now

- Framework Contract: `docs/FRAMEWORK_CONTRACT.md`
- Generic `AGENTS.md` operating manual (L0–L7 operationalized)
- Governance rules under `rules/`
- Engineering methodologies under `methodology/`
- Discovery prompt skeletons under `prompts/discovery/`
- Generic architecture review prompt
- `aiosctl sync` for copying `rules/*.md` → consumer `.agents/`
- OSS docs: license, contributing, security, code of conduct
- Optional preserved education manual: `packs/education/AGENTS.education.md`
- Adaptive Project Intelligence **design documentation** (Phase 6 completed):
  - `docs/ADAPTIVE_PROJECT_CONTEXT.md`
  - `docs/PROCESS_DEPTH_MODEL.md`
  - `docs/ADAPTIVE_GUIDANCE_MODEL.md`
  - `docs/ADAPTIVE_GOVERNANCE_MODEL.md`
  - `docs/ADAPTIVE_REFERENCE_SCENARIOS.md`
  - `docs/ADAPTIVE_PROJECT_INTELLIGENCE_AUDIT.md` (documentation-level audit only)

### Partially available

- Broader prompt library (many placeholder files)
- Templates and checklists (several empty)
- CI repository report + demo API tests
- Optional packs beyond the preserved education AGENTS copy

### Planned

- Workflow library under `workflows/`
- Skills and knowledge libraries
- Richer `aiosctl` commands (`validate`, `doctor`, `init`, `version`)
- Framework contract tests under `tests/`
- Engineering domain modules
- Deeper coding-agent integrations
- Adaptive recommendation **engine** / runtime (separate future approval; not part of Phase 6)

See [`ROADMAP.md`](ROADMAP.md) for phased direction.

---

# Core Components

| Component | Purpose | Status |
|-----------|---------|--------|
| **docs/FRAMEWORK_CONTRACT.md** | Authoritative framework contract | Available |
| **AGENTS.md** | Agent operating manual (operationalizes the contract) | Available |
| **MANIFEST.md** | Product scope and navigation | Available |
| **PROJECT_STRUCTURE.md** | Real layout + status | Available |
| **rules/** | Syncable Core governance guidance | Available |
| **methodology/** | RDIV and related methods | Available |
| **prompts/** | Reusable prompt assets | Partial |
| **packs/** | Optional domain packs (adopted = L5) | Partial |
| **Adaptive Project Intelligence docs** | Context, depth, guidance, governance, scenarios, documentation audit | Available (Phase 6 design; not a runtime) |
| **Modules** | Reusable engineering capabilities | Planned (adaptive recommendations approved as design) |
| **workflows/** | End-to-end flows | Planned |
| **skills/** | Reusable engineering skills | Planned |
| **knowledge/** | Shared reference knowledge | Planned |
| **tests/** | Framework validation | Planned |
| **lab/** | Demo API for CI | Demo only |

---

# AIOS Workflow

<p align="center">
<img src="assets/images/workflow.png" alt="Workflow">
</p>

AIOS recommends **RDIV**:

1. Review
2. Decide
3. Implement
4. Verify

Details: [`methodology/rdiv.md`](methodology/rdiv.md)

This is a **documented method**, not a separate installed runtime engine.

---

# Decision Guidance

<p align="center">
<img src="assets/images/decision-engine.png" alt="Decision guidance">
</p>

Before implementing, agents should evaluate:

- repository rules
- existing implementations
- workflow expectations
- approval gates
- quality standards

If a conflict exists, the agent should stop and request human approval instead of making unsafe assumptions.

- **Instruction precedence (what is authoritative):** [`AGENTS.md`](AGENTS.md) §2 / Framework Contract §7
- **Decision quality (which valid option is better):** [`rules/DECISION_RULES.md`](rules/DECISION_RULES.md)
- **Agent modes (behavior profiles, not document authority):** [`rules/AGENT_RULES.md`](rules/AGENT_RULES.md)

There is no separate automated “decision engine” binary in this repository today.

---

# Repository Lifecycle

<p align="center">
<img src="assets/images/repository-lifecycle.png" alt="Repository Lifecycle">
</p>

1. Read the repository
2. Understand the project
3. Analyze the request
4. Create a plan
5. Implement changes
6. Review the result
7. Improve iteratively
8. Commit safely
9. Continuously evolve the repository

---

# Design Principles

- Repository-Driven Engineering
- Architecture First
- Model-Agnostic AI
- Explicit Governance
- Human-in-the-Loop Decisions
- Adaptive to Project Context (recommend; do not impose)
- Consumer Ownership of ADRs and Product Decisions
- Framework, Not Content

---

# Compatible With

AIOS is **model-agnostic** and is designed to work with modern AI coding assistants, including:

| AI Assistant | Status |
|--------------|--------|
| ChatGPT | Designed for |
| Codex | Designed for |
| Claude Code | Designed for |
| Cursor | Designed for |
| GitHub Copilot | Designed for |
| Windsurf | Designed for |
| Continue.dev | Designed for |
| Roo Code | Designed for |

“Designed for” means governance documents are written to be assistant-neutral.

It does **not** claim automated certification of every tool on every release.

---

# Quick Start

## 1. Clone AIOS

```bash
git clone https://github.com/fdeniz07/AIOS.git
cd AIOS
```

## 2. Adopt the Core framework

At minimum, copy or reference:

- `docs/FRAMEWORK_CONTRACT.md`
- `AGENTS.md`
- `MANIFEST.md`
- `PROJECT_STRUCTURE.md`
- `rules/`
- `methodology/`

Optional:

- `prompts/discovery/`
- `packs/education/` when building education-oriented repositories (Pack guidance applies only when adopted)

## 3. Open your consumer repository in your coding assistant

## 4. Initialize the assistant

```text
Read docs/FRAMEWORK_CONTRACT.md and AGENTS.md.
Respect consumer ADRs and local policies over generic AIOS defaults.
Follow L0–L7 instruction precedence.
Understand the repository before making changes.
Recommend Modules adaptively; do not impose them.
Wait for confirmation when standards or durable decisions conflict.
```

## 5. Sync rules into a consumer project (optional)

From the AIOS repository:

```bash
python scripts/aiosctl.py sync --project /path/to/your/project
```

This copies `rules/*.md` into `<project>/.agents/` and writes `AIOS_VERSION.md`.

---

# Tooling Notes (`aiosctl`)

| Item | Current behavior |
|------|------------------|
| Implemented command | `sync` |
| Source | `rules/*.md` |
| Destination | `<project>/.agents/` |
| Skip logic | Content hash (unless `--force`) |
| Orphan cleanup | Not deleted automatically |
| `aiosctl.yaml` | May list helper project names; **not read by the CLI today** |
| Planned | `validate`, `doctor`, `init`, `version` |

Compatibility with existing consumers depends on keeping the current sync paths and rule filenames stable.

---

# Validation

What exists today:

- Manual / convention-based validation by following `AGENTS.md` and methodologies
- GitHub Actions CI that:
  - writes a simple repository file-count report
  - runs pytest for `lab/aios-demo-api`

What is **not** claimed:

- A full automated AI behavior test framework
- Certified conflict-detection middleware
- Guaranteed enforcement inside third-party IDEs

Consumer learning repositories have been used to exercise AIOS conventions in practice; treat that as adoption experience, not as a formal conformance suite.

---

# Roadmap

High-level direction (details in [`ROADMAP.md`](ROADMAP.md)):

0. Foundation and identity
1. Framework contract
2. CLI improvements
3. Workflow and checklist system
4. Skills and Knowledge
5. Adaptive Project Intelligence — **Completed** (conceptual / documentation foundation; not an adaptive engine)
6. Engineering modules
7. Validation and automation
8. Ecosystem and integrations

Phases are directional, not dated commitments. Completed phases still do not imply unimplemented runtime features.

---

# Contributing

Contributions are welcome — especially reusable workflows, skills, documentation and tests that preserve the framework contract.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) and open an Issue before major architectural changes.

---

# License

Released under the MIT License. See [`LICENSE`](LICENSE).

---

# Vision

AIOS is not another prompt dump.

It is not another AI wrapper.

It is not another coding assistant.

AIOS is an engineering framework that helps AI become a reliable long-term software development partner — across stacks, teams and tools.

---

<p align="center">

### Build better repositories.

# Get better AI.

</p>

---

<p align="center">
Made with ❤️ for the AI Engineering community.
</p>
