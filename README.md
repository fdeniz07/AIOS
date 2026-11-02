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

Product contract: [`MANIFEST.md`](MANIFEST.md)

---

## Repository Structure

```text
AIOS/
├── AGENTS.md              # Generic operating manual for AI agents
├── MANIFEST.md            # Product scope and navigation
├── PROJECT_STRUCTURE.md   # Actual tree + status labels
├── ROADMAP.md             # Framework evolution phases
├── rules/                 # Syncable governance rules (aiosctl source)
├── methodology/           # RDIV, Architecture First, …
├── prompts/               # Reusable prompts (discovery active; others partial)
├── packs/education/       # Optional education pack (preserved AGENTS)
├── templates/             # Placeholders for reusable templates
├── checklists/            # Partial quality checklists
├── scripts/aiosctl.py     # Rule sync CLI
├── assets/                # Branding and diagrams
├── lab/aios-demo-api/     # Demo app for CI smoke tests
├── knowledge/             # Planned
├── skills/                # Planned
├── workflows/             # Planned
├── tests/                 # Planned (framework tests)
└── examples/              # Planned adoption examples
```

Empty directories are **planned or reserved**, not shipped engines.

---

# Capability Status

### Available now

- Generic `AGENTS.md` operating manual
- Governance rules under `rules/`
- Engineering methodologies under `methodology/`
- Discovery prompt skeletons under `prompts/discovery/`
- Generic architecture review prompt
- `aiosctl sync` for copying `rules/*.md` → consumer `.agents/`
- OSS docs: license, contributing, security, code of conduct
- Optional preserved education manual: `packs/education/AGENTS.education.md`

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

See [`ROADMAP.md`](ROADMAP.md) for phased direction.

---

# Core Components

| Component | Purpose | Status |
|-----------|---------|--------|
| **AGENTS.md** | How AI agents must operate | Available |
| **MANIFEST.md** | Product contract and navigation | Available |
| **PROJECT_STRUCTURE.md** | Real layout + status | Available |
| **rules/** | Syncable governance | Available |
| **methodology/** | RDIV and related methods | Available |
| **prompts/** | Reusable prompt assets | Partial |
| **packs/** | Optional domain packs | Partial |
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

Decision priorities and gates are defined in `AGENTS.md` and `rules/DECISION_RULES.md`.

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
- Adaptive to Project Context
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

- `AGENTS.md`
- `MANIFEST.md`
- `PROJECT_STRUCTURE.md`
- `rules/`
- `methodology/`

Optional:

- `prompts/discovery/`
- `packs/education/` when building education-oriented repositories

## 3. Open your consumer repository in your coding assistant

## 4. Initialize the assistant

```text
Read AGENTS.md and MANIFEST.md.
Follow AIOS operating rules.
Understand the repository before making changes.
Respect approval gates.
Wait for confirmation when standards conflict.
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
5. Adaptive Project Intelligence
6. Engineering modules
7. Validation and automation
8. Ecosystem and integrations

Phases are directional, not dated commitments.

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
