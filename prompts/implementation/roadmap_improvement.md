# Roadmap Improvement

## Purpose

Help a repository owner improve an existing roadmap without taking ownership of product decisions. Clarify status, milestones, dependencies, and acceptance criteria while preserving owner-defined priorities and sequencing.

---

## When to Use

- After a Roadmap Review (preferred) or when status language is known to be outdated.
- When milestones need clearer deliverables or dependencies.
- Before an owner-directed roadmap documentation PR.

## When Not to Use

- To invent product commitments, dates, priorities, or approvals.
- To silently change scope or phase status.
- To automatically modify AIOS Core [`ROADMAP.md`](../../ROADMAP.md) or any Consumer roadmap.

---

## Required Context

- Current roadmap document and owner goals for the improvement.
- Repository evidence for completed vs planned work.
- Prior Roadmap Review findings when available.

---

## Prompt

Propose roadmap improvements for owner review.

Analyze the current roadmap and relevant repository evidence. Identify outdated or ambiguous status statements. Improve milestone and deliverable clarity. Identify missing dependencies and acceptance criteria. Distinguish **proposals** from **accepted commitments**.

Critical rules:

- Roadmap ownership remains with the repository owner / Consumer.
- Never invent product commitments, dates, priorities, or approvals.
- Never silently change scope or phase status.
- Do not automatically modify AIOS Core `ROADMAP.md`.
- Return proposed changes for owner review only.

Structure the response as:

1. Findings driving the improvement
2. Proposed status clarifications (with evidence)
3. Proposed milestone / deliverable wording
4. Missing dependencies or acceptance criteria (suggestions)
5. Explicit list of items that require owner decision
6. Text the owner can accept, edit, or reject

Align suggestions with architecture and governance when relevant ([`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md)). Do not redefine L0–L7 or Core / Module / Pack / Consumer boundaries.

---

## Expected Output

- Findings summary
- Proposed clarifications (non-binding)
- Suggested milestone/deliverable text
- Dependency and acceptance-criteria gaps
- Owner decision list
- Assumptions and open questions

---

## Constraints

- Do not take product ownership or set priorities.
- Do not commit, push, or publish roadmap changes.
- Do not claim automatic roadmap generation or approval.
- AI recommends; humans decide.

## Related References

- Related review prompt: [`../review/roadmap_review.md`](../review/roadmap_review.md)
- Framework Contract: [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md)
- AIOS roadmap (reference / target only if owner specifies): [`ROADMAP.md`](../../ROADMAP.md)
