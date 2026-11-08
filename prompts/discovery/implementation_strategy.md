# Implementation Strategy

## Purpose

Develop a practical implementation strategy from an approved task and discovered repository context. Organize work into a safe sequence that minimizes risk and preserves maintainability—without implementing changes.

---

## When to Use

After completing (preferred):

1. Repository Analysis
2. Risk Assessment

Run before any implementation work begins.

## When Not to Use

- When analysis and risk context are missing for a non-trivial change.
- As a substitute for the Core Feature Development Workflow or RDIV methodology.
- To authorize commit, push, publication, deployment, or other approval-gated operations.

---

## Required Context

- Repository Analysis complete (or equivalent).
- Risk Assessment complete (or explicit owner waiver for a trivial change).
- Task or change request is defined and, for large work, approved to plan.
- No implementation started for this strategy.

---

## Prompt

Define an implementation strategy for the stated task using repository evidence, analysis, and risk findings.

Produce a plan only. Do not modify files. Do not generate production code. Do not redesign the repository unless redesign is the approved task. Do not authorize commit, push, publish, deploy, or release.

Include:

1. **Scope and non-goals**
2. **Relevant existing components and patterns** to reuse
3. **Proposed implementation sequence** (phases)
4. **Files or areas likely to be affected**
5. **Dependencies and prerequisites**
6. **Validation approach** (tests, reviews, `python -m validation` or project equivalents when relevant)
7. **Risks and rollback considerations**
8. **Open questions and required approvals**

For each phase, provide:

- Phase name
- Goal
- Why this phase comes now
- Expected deliverables
- Dependencies
- Exit criteria

Align with existing methodology and workflows when present. Do not replace [`methodology/`](../../methodology/) guidance or Core workflows under [`workflows/`](../../workflows/). Preserve Framework Contract boundaries and human approval gates in [`AGENTS.md`](../../AGENTS.md).

---

## Expected Output

- Scope / Non-goals
- Reuse targets (existing components and patterns)
- Phased implementation plan (as above)
- Likely affected areas
- Validation plan
- Rollback / risk notes
- Open questions and approval gates

---

## Constraints

- Do not implement, commit, push, publish, or deploy.
- Do not silently expand scope beyond the approved task.
- Do not redefine L0–L7 or Consumer ownership.
- Do not claim an automated orchestrator or execution engine.
- AI recommends; humans decide.

## Related References

- Discovery order: [`README.md`](README.md)
- Framework Contract: [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md)
- Agent operating manual: [`AGENTS.md`](../../AGENTS.md)
- Feature Development Workflow: [`workflows/feature_development.md`](../../workflows/feature_development.md)
- RDIV methodology: [`methodology/rdiv.md`](../../methodology/rdiv.md)
