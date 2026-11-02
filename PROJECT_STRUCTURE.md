# AIOS Project Structure

Version: 1.1.0

Status: Active

Last Updated: 2026-11-02

This document describes the **actual** repository layout and the status of each area.

Status legend:

| Status | Meaning |
|--------|---------|
| **active** | Used and meaningful today |
| **partial** | Present with incomplete content |
| **placeholder** | Empty file or reserved name |
| **planned** | Empty directory reserved for future work |
| **demo** | Example / CI smoke target, not Core framework logic |

---

## Repository Root

```text
AIOS/                          # Git repository root
├── .agents/                   # planned locally; also the sync DESTINATION name in consumers
├── .github/                   # active – community + CI
├── assets/                    # active – branding and diagrams
├── checklists/                # partial
├── docs/                      # planned / empty nested folders
├── examples/                  # planned – empty domain folders
├── generators/                # planned – empty
├── knowledge/                 # planned – empty
├── lab/                       # demo – sample FastAPI app for CI
├── methodology/               # active
├── packs/                     # partial – optional packs
│   └── education/
├── prompts/                   # partial
├── rules/                     # active – aiosctl sync SOURCE
├── scripts/                   # active – aiosctl CLI
├── skills/                    # planned – empty
├── templates/                 # placeholder – empty template files
├── tests/                     # planned – empty (framework tests not yet present)
├── workflows/                 # planned – empty
├── AGENTS.md                  # active – generic operating manual
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

### `rules/` — **active**

Governance markdown files.

**Sync source** for `aiosctl sync`: every `rules/*.md` is copied to `<consumer>/.agents/`.

Includes both generic engineering rules and education-oriented rules retained for consumer compatibility.

Do not rename or relocate these files without a migration plan.

### `methodology/` — **active**

Stack-agnostic engineering methods:

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
| `review/` | partial | `architecture_review.md` active; others empty |
| `implementation/` | placeholder | Mostly empty files |
| `generators/` | placeholder | Empty |
| `translation/` | placeholder | Empty; education-oriented intent |

### `packs/` — **partial**

Optional content packs that are not required to use AIOS Core.

| Path | Status | Notes |
|------|--------|-------|
| `packs/education/AGENTS.education.md` | active archive | Exact preserved copy of the pre-Phase-0 educational AGENTS manual |

Education rules under `rules/` are **not** migrated here in Phase 0.

### `scripts/` — **active**

| File | Status | Notes |
|------|--------|-------|
| `aiosctl.py` | active | Implements `sync` only (`validate`, `doctor`, `init`, `version` planned) |

### `assets/` — **active**

Logos and architecture / workflow diagrams referenced by `README.md`.

### `checklists/` — **partial**

| File | Status |
|------|--------|
| `notebook_creation.md` | partial – education-oriented |
| `release_checklist.md` | placeholder |
| `review.md` | placeholder |

### `templates/` — **placeholder**

Template filenames exist; file bodies are currently empty.

### `lab/aios-demo-api/` — **demo**

Minimal FastAPI application used by CI to prove a simple Python test path.

This is **not** the AIOS framework runtime.

### `knowledge/`, `skills/`, `workflows/`, `generators/`, `tests/` — **planned**

Reserved empty directories for future reusable engineering assets and validation.

### `examples/` — **planned**

Empty folders (`DevOps`, `German`, `Python`) reserved for future adoption examples.

Not implemented consumer projects.

### `docs/` — **planned**

Reserved documentation area (`docs/releases/` currently empty).

### `.github/` — **active**

Issue templates, PR template, support note, and CI workflow.

### `.agents/` — **planned** (in this repo)

Empty in the AIOS repository itself.

In **consumer** repositories, `.agents/` is the **destination** of `aiosctl sync`.

---

## Root Files of Note

| File | Status | Purpose |
|------|--------|---------|
| `AGENTS.md` | active | Generic agent operating manual |
| `MANIFEST.md` | active | Product scope and navigation |
| `README.md` | active | Landing overview |
| `ROADMAP.md` | active | Framework evolution phases |
| `aiosctl.yaml` | partial | Optional project hints; **CLI does not read this file yet** |
| `QUALITY_CONTROL.md` | partial | Currently education/vocabulary oriented |
| `warning.txt` | local helper | Ignored by `.gitignore`; not part of the published contract |

---

## Framework vs Demo vs Consumer

| Layer | What it is | Examples |
|-------|------------|----------|
| **Framework (AIOS Core)** | Reusable governance and methods | `AGENTS.md`, `rules/`, `methodology/`, `scripts/aiosctl.py` |
| **Optional packs** | Domain extensions | `packs/education/` |
| **Demo** | CI / smoke sample | `lab/aios-demo-api/` |
| **Consumer repositories** | Separate projects adopting AIOS | e.g. learning-path repos using `.agents/` sync |

AIOS Core must remain usable across stacks. Consumer content stays in consumer repositories.
