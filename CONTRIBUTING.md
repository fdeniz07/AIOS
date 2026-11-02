# Contributing to AIOS

Thank you for your interest in improving AIOS.

AIOS is an open-source **AI Software Engineering Framework**.

Contributions should strengthen the **reusable framework**, not add unrelated consumer-project content.

---

## Before You Start

1. Read `README.md`, `MANIFEST.md`, `AGENTS.md` and `PROJECT_STRUCTURE.md`
2. Check `ROADMAP.md` so new work fits an intentional phase
3. Open an issue before large architectural changes
4. Prefer small, focused pull requests

---

## What We Welcome

- Clarifying documentation
- Stack-agnostic methodologies and workflows
- Reusable prompts, templates and checklists
- Skills / knowledge contributions aligned with engineering domains
- Tests and validation that protect the framework contract
- Bug fixes in `aiosctl` that preserve consumer sync compatibility

---

## What Usually Does Not Belong in Core

- A single product's backlog, sprint board or private ADR set
- Full courses, vocabulary databases or lesson notebooks
- Secrets, credentials or environment-specific paths
- Broad rewrites without an issue and migration plan

Education-oriented material belongs in optional packs (see `packs/education/`) or in consumer repositories.

---

## Development Notes

- The Git repository root is the directory that contains `AGENTS.md` and `.git`
- Do not break the `aiosctl sync` contract (`rules/*.md` → consumer `.agents/`) without a versioned migration proposal
- `aiosctl.yaml` is not read by the CLI yet; do not assume it drives sync
- Keep changes minimal and reversible
- Follow existing naming and Markdown conventions

---

## Suggested Workflow

1. Fork and create a branch
2. Make the smallest change that solves the issue
3. Update docs when behavior or structure changes
4. Run relevant local checks (for example demo tests under `lab/aios-demo-api` when Python code changes)
5. Open a pull request using the repository template

---

## Pull Request Expectations

- Clear description of **why** the change exists
- Notes on consumer compatibility impact, if any
- No unrelated refactors
- Honest status language (do not mark planned work as implemented)

---

## Code of Conduct

Participation is governed by `CODE_OF_CONDUCT.md`.

---

## Questions

Use GitHub Issues for discussion.

For security-sensitive reports, see `SECURITY.md`.
