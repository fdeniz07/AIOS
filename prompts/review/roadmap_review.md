# Roadmap Review

## Purpose

Review a roadmap document for consistency, clarity, traceability, and realistic status reporting. Preserve the distinction between completed, planned, deferred, and proposed work—without creating commitments or changing priorities.

---

## When to Use

- Before roadmap updates or release planning reviews.
- When status language may be outdated relative to repository evidence.
- When sequencing, dependencies, or acceptance criteria need scrutiny.

## When Not to Use

- To set priorities, dates, or product commitments for the owner.
- To automatically modify AIOS Core [`ROADMAP.md`](../../ROADMAP.md) or a Consumer roadmap.
- As architecture approval or Framework Contract amendment.

---

## Required Context

- Roadmap document under review (path specified by the user).
- Repository evidence for completed vs planned work.
- Related contract/manifest docs when assessing alignment.

---

## Prompt

Review the specified roadmap against repository evidence.

Do not edit files. Do not create commitments, change priorities, or approve roadmap changes. Consumer / repository roadmap ownership remains with the owner. Do not treat AIOS Core `ROADMAP.md` as an automatically editable target.

Check:

1. Phase and milestone descriptions (clarity and scope)
2. Status accuracy against repository evidence
3. Completed versus planned versus deferred versus proposed work
4. Dependencies and sequencing
5. Acceptance criteria and deliverables
6. Duplicated or contradictory items
7. Architecture and governance alignment (for AIOS: [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md))

For each finding include severity, evidence, affected roadmap section, and recommended clarification. Clearly label what is documented commitment vs recommendation.

---

## Expected Output

- Overall roadmap assessment
- Status accuracy findings
- Sequencing / dependency issues
- Ambiguous or contradictory items
- Alignment notes (architecture / governance)
- Recommended clarifications for owner review
- Open questions

---

## Constraints

- Do not invent dates, priorities, or approvals.
- Do not silently change phase status or scope.
- Do not redefine L0–L7 or ownership boundaries.
- AI recommends; humans decide.

## Related References

- Framework Contract: [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md)
- AIOS roadmap (reference only unless that is the review target): [`ROADMAP.md`](../../ROADMAP.md)
- Manifest: [`MANIFEST.md`](../../MANIFEST.md)
