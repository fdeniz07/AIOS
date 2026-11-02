# PROJECT_RULES.md

# AIOS Project Rules

## Purpose

This document provides **reusable AIOS Core project guidance** for repositories that adopt the AIOS framework.

It is an AIOS-managed guidance file. When synchronized into a consumer repository (typically as `.agents/PROJECT_RULES.md`), it remains an **AIOS-derived artifact**, not a consumer-owned ADR or product decision.

All AI assistants, contributors, and developers should apply these rules in an AIOS adoption context, **subject to the instruction precedence** defined in `docs/FRAMEWORK_CONTRACT.md` §7 and operationalized in root `AGENTS.md` §2.

---

## Authority and Precedence

This file is **not** the highest authority in a consumer repository.

It operates within the **AIOS Core** context (L4 — AIOS Core binding defaults) and is subordinate to:

1. **L0** — Non-overridable constraints (safety, legal, security, privacy, licensing, compliance)
2. **L1** — Explicit user instructions for the current task (within L0; durable consumer decisions are not silently amended)
3. **L2** — Consumer-approved ADRs and product decisions
4. **L3** — Consumer local policies and project instructions

Consumer-owned instructions and decisions are **not** subordinate to generic AIOS Core defaults in this file.

If this file conflicts with an applicable consumer ADR or local policy, respect the consumer decision, disclose the conflict when relevant, and do not silently overwrite consumer-owned artifacts.

Canonical hierarchy: `docs/FRAMEWORK_CONTRACT.md` §7 and root `AGENTS.md` §2.

Do not invent a competing hierarchy inside this file.

### Binding versus recommendation

| Kind | In this file |
|------|----------------|
| Binding Core defaults | General, documentation, code, Git and collaboration rules below — when no higher-level instruction applies |
| Adaptive recommendations | Module/Pack suggestions and optional tooling advice — recommendations unless the consumer explicitly adopts them as local policy (then L3) |

---

## Sync Compatibility Note

This file is part of the `rules/*.md` sync source used by `aiosctl sync` (`rules/*.md` → consumer `.agents/`).

- Path and filename `rules/PROJECT_RULES.md` are part of the sync compatibility surface.
- Future syncs may copy revised source content into a consumer `.agents/` directory.
- Existing **frozen** legacy consumer copies (for example historical GitHub-DevOps-Learning-Path `.agents/` artifacts) remain unchanged until someone **manually** updates or re-syncs them.
- No mandatory re-sync is required for legacy synced consumers.

---

# General Principles

* Keep the project clean and maintainable.
* Prefer simplicity over unnecessary complexity.
* Avoid duplicate documentation.
* Follow a modular architecture **when appropriate to the project**; do not impose heavy patterns by default.
* Keep the repository scalable.
* Document important decisions.
* Never break existing functionality without a valid reason.

---

# Documentation Rules

* All documentation must be written in **English** unless a consumer local policy (L3) or approved product decision (L2) explicitly requires another language for that repository.
* Use Markdown (`.md`) for documentation.
* Keep documents concise and easy to read.
* Avoid duplicated information across multiple files.
* Update documentation whenever the project structure changes.

---

# Code Rules

* Write clean, readable, and maintainable code.
* Follow language-specific best practices.
* Prefer descriptive naming.
* Keep functions and classes focused on a single responsibility.
* Remove dead code whenever possible.

---

# Git Rules

* Use meaningful commit messages.
* Keep commits small and focused.
* Do not commit generated files unless required.
* Never commit secrets, passwords, or API keys.

---

# AI Collaboration Rules

When working with AI assistants (ChatGPT, Codex, Copilot, Cursor, Claude, etc.):

* Analyze before modifying.
* Explain architectural decisions.
* Prefer incremental changes.
* Avoid unnecessary file creation.
* Reuse existing structures whenever possible.
* Respect the existing project architecture and consumer-owned decisions.
* Recommend relevant AIOS Modules or Packs adaptively; do not impose them.

---

# Project Structure

Projects should follow a consistent and modular structure.

The exact folder layout may differ depending on the project type, but organization and readability must always be maintained.

AIOS must not force a single architecture style onto every consumer repository.

---

# Related Rule Files

Other active markdown files may exist under `rules/` and may be synchronized alongside this file.

Do not assume files exist unless they are present in the repository. The following names are **not** currently present in AIOS Core and must not be treated as required:

* STYLE_GUIDE.md
* GIT_RULES.md
* CODING_STANDARDS.md
* AI_RULES.md

Within the `rules/` set, resolve conflicts using root `AGENTS.md` §2 and the Framework Contract — not by treating this file as universally supreme.

---

# Final Principle

Every improvement should make the project easier to understand, easier to maintain, and easier to extend — without overriding consumer ownership or non-overridable constraints.

---

## Architecture First

Before implementing new features:

1. Analyze the current architecture.
2. Identify the best integration point.
3. Minimize unnecessary changes.
4. Preserve consistency across the repository.
5. Prefer consumer-approved architecture decisions when they exist.
