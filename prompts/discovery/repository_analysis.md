# Repository Analysis

## Purpose

Help an AI assistant understand an existing repository before meaningful engineering work. Produce an evidence-based picture of purpose, structure, stack, architecture, conventions, tooling, and documentation—without modifying the repository.

---

## When to Use

- At the start of work on an unfamiliar repository.
- Before architectural decisions, implementation planning, or significant documentation changes.
- When prior analysis is missing, outdated, or incomplete.

## When Not to Use

- When the user already supplied a current, accepted repository analysis and asked for a later discovery step.
- As a substitute for architecture review, risk assessment, or implementation strategy.
- To authorize or perform repository modifications.

---

## Required Context

- Repository content is available for inspection (local checkout, attached tree, or equivalent).
- Task or goal is known at least at a high level (optional but helpful).
- AIOS guidance may apply when the repository uses AIOS; do not assume AIOS is present without evidence.

---

## Prompt

Analyze this repository before any architectural or implementation decisions.

Work from repository evidence. Separate **observed facts**, **assumptions**, and **recommendations**. Do not modify files. Do not implement changes. Do not invent undocumented capabilities.

Examine and report on:

1. **Purpose and scope** — What the repository is for; primary audience; in-scope vs out-of-scope signals from README, manifests, or equivalent docs.
2. **Directory structure and entry points** — Important roots, packages, apps, docs, and how a new contributor would navigate.
3. **Technology stack and dependencies** — Languages, frameworks, package manifests, lockfiles, and notable tooling.
4. **Architecture and boundaries** — Major components, layers, ownership boundaries, and how they relate (including Core / Module / Pack / Consumer style boundaries if AIOS evidence exists).
5. **Engineering conventions** — Coding, docs, contribution, branching, or review norms visible in-repo.
6. **Tests, validation, CI/CD, and tooling** — What exists, what it covers, and what is missing or unclear.
7. **Documentation and governance** — Authoritative docs, roadmaps, contracts, agent/operating manuals, and how status is described.
8. **Unknowns and gaps** — Missing evidence, contradictions, and questions that must be answered before development.

If AIOS artifacts are present, treat [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) and [`AGENTS.md`](../../AGENTS.md) as governance references; do not redefine L0–L7 or ownership rules.

---

## Expected Output

- Repository Summary
- Current Architecture (evidence-based)
- Strengths
- Weaknesses / gaps
- Observed Facts vs Assumptions vs Recommendations
- Missing Information
- Questions Before Development

---

## Constraints

- Do not modify files or claim automatic repository changes.
- Do not grant commit, push, publish, deploy, or release authority.
- Do not replace Skills, Workflows, or Methodology documents.
- Prefer linking to authoritative docs over duplicating them.
- AI recommends; humans decide.

## Related References

- Discovery order: [`README.md`](README.md)
- Framework Contract: [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md)
- Agent operating manual: [`AGENTS.md`](../../AGENTS.md)
- Related Skill (when present): [`skills/repository_analysis.md`](../../skills/repository_analysis.md)
