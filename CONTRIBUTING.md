# Contributing to AIOS

Thank you for your interest in improving AIOS.

AIOS is an open-source **AI Software Engineering Framework**.

Contributions should strengthen the **reusable framework**, not add unrelated consumer-project content.

---

## Governance references

Before proposing architectural or policy changes, treat these as complementary authorities:

| Document | Role |
|----------|------|
| [`docs/FRAMEWORK_CONTRACT.md`](docs/FRAMEWORK_CONTRACT.md) | **Authoritative architectural and governance contract** — boundaries, ownership, consumption models, sync compatibility, L0–L7 precedence |
| [`AGENTS.md`](AGENTS.md) | **Operationalizes** the framework’s instruction and governance model for AI agents (especially §2) |
| [`MANIFEST.md`](MANIFEST.md) / [`PROJECT_STRUCTURE.md`](PROJECT_STRUCTURE.md) / [`README.md`](README.md) | Product navigation and honest capability status |
| [`ROADMAP.md`](ROADMAP.md) | Framework evolution phases |
| [`docs/CONTRIBUTION_CHECKLISTS.md`](docs/CONTRIBUTION_CHECKLISTS.md) | Artifact-specific contribution checklists (Skill, Workflow, Knowledge, Module) |

The canonical **L0–L7** precedence model must remain consistent across relevant documentation. Full definition: Framework Contract §7; agent detail: `AGENTS.md` §2. Do not invent a competing hierarchy in PRs.

Changes that affect **architecture, governance, compatibility, or consumer ownership** must respect the Framework Contract and applicable approval gates (open an issue for large changes; do not silently amend consumer-facing contracts).

---

## Before You Start

1. Read `docs/FRAMEWORK_CONTRACT.md`, `README.md`, `MANIFEST.md`, `AGENTS.md` and `PROJECT_STRUCTURE.md`
2. Check `ROADMAP.md` so new work fits an intentional phase
3. Open an issue before large architectural changes
4. Prefer small, focused pull requests
5. Use [`docs/CONTRIBUTION_CHECKLISTS.md`](docs/CONTRIBUTION_CHECKLISTS.md) for Skill, Workflow, Knowledge, or Module contributions

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

## Contribution process

All substantive contributions follow this process. It does **not** introduce a new artifact lifecycle or a new acceptance authority. Existing Draft / Active / Deprecated lifecycle values and maintainer acceptance remain unchanged.

```text
Proposal
  → Contract Review
  → Contribution
  → Validation
  → Human Review
  → Maintainer Acceptance
  → Merge
```

| Stage | Purpose |
|-------|---------|
| **Proposal** | Describe the change and why it belongs in AIOS. Open an issue for architectural, governance, compatibility, or large-scope work. |
| **Contract Review** | Check fit against Framework Contract boundaries, L0–L7, ownership rules, and roadmap phase intent. Stop or redesign if the proposal conflicts with approved contracts. |
| **Contribution** | Implement the smallest change that solves the proposal. Follow existing conventions and artifact checklists. |
| **Validation** | Run relevant existing checks (for example `python -m validation`, demo tests when Python code changes). Validation success is not proof of architectural correctness or content quality. |
| **Human Review** | Peer / maintainer review of intent, contract fit, honesty of status language, and Consumer impact. |
| **Maintainer Acceptance** | A maintainer accepts that the contribution may merge. Acceptance does not create a new lifecycle state and does not auto-adopt guidance for Consumers. |
| **Merge** | Land the change on the target branch after acceptance. |

### Contributor responsibilities

- Read the governance references before proposing structural or policy changes.
- Keep Core reusable and stack-agnostic.
- Prefer Module-local placement for capability-specific Skills/Knowledge/Workflows when Module packages exist.
- Preserve the `aiosctl sync` contract unless proposing an explicitly versioned migration.
- Use honest status language (`draft` / `active` / `deprecated`; do not mark planned work as implemented).
- Do not invent platform features, validators, resolvers, installers, or automatic adoption behavior.
- Complete the relevant sections of [`docs/CONTRIBUTION_CHECKLISTS.md`](docs/CONTRIBUTION_CHECKLISTS.md).

### Maintainer responsibilities

- Review proposals against the Framework Contract and roadmap intent.
- Protect Consumer ownership and sync compatibility.
- Require disclosure when Modules/Skills/Workflows remain `draft`.
- Accept or reject contributions; acceptance remains a human maintainer decision.
- Ensure merged work does not silently change L0–L7 or architectural boundaries.

---

## Development Notes

- The Git repository root is the directory that contains `AGENTS.md` and `.git`
- Do not break the `aiosctl sync` contract (`rules/*.md` → consumer `.agents/`) without a versioned migration proposal
- `aiosctl.yaml` is not read by the CLI yet; do not assume it drives sync
- Keep changes minimal and reversible
- Follow existing naming and Markdown conventions
- Do not mark planned work (Modules, discovery engines, new CLI commands, etc.) as implemented

---

## Suggested Workflow

1. Fork and create a branch
2. Make the smallest change that solves the issue
3. Update docs when behavior or structure changes; keep L0–L7 wording aligned with the Contract when you touch precedence-related text
4. Run relevant local checks (for example `python -m validation`, and demo tests under `lab/aios-demo-api` when Python code changes)
5. Open a pull request using the repository template

---

## Pull Request Expectations

- Clear description of **why** the change exists
- Notes on consumer compatibility impact, if any
- No unrelated refactors
- Honest status language (do not mark planned work as implemented)
- Architecture / governance / ownership changes cite the Framework Contract and stay within approved decisions
- Artifact contributions include checklist confirmation from [`docs/CONTRIBUTION_CHECKLISTS.md`](docs/CONTRIBUTION_CHECKLISTS.md)

---

## Code of Conduct

Participation is governed by `CODE_OF_CONDUCT.md`.

---

## Questions

Use GitHub Issues for discussion.

For security-sensitive reports, see `SECURITY.md`.
