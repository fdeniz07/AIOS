# Vision Alignment

## Purpose

Evaluate whether a proposed change is consistent with the repository's documented purpose and direction. Distinguish documented commitments from recommendations and assumptions—without creating product decisions or roadmap commitments.

---

## When to Use

- After Repository Analysis, Risk Assessment, and Implementation Strategy (preferred discovery order).
- Before reviewing documentation in depth or implementing changes.
- When a proposal may expand scope, duplicate capability, or drift from stated mission.

## When Not to Use

- To approve architecture, accept ADRs, or set roadmap priorities.
- As a substitute for Architecture Review or Framework Contract interpretation.
- To invent or revise product vision without owner input.

---

## Required Context

- Repository has been analyzed enough to identify purpose docs and direction signals.
- A proposed change, feature, or direction is stated.
- Relevant docs available when they exist (README, roadmap, contract, manifest).

---

## Prompt

Evaluate vision alignment for the proposed change against this repository's documented purpose and direction.

Use repository evidence. Separate **documented commitments**, **recommendations**, and **assumptions**. Do not modify files. Do not create roadmap commitments, product decisions, or architecture approvals.

Assess consistency with:

1. Repository mission and product scope
2. Framework Contract / governance docs when present ([`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) for AIOS)
3. Existing roadmap direction ([`ROADMAP.md`](../../ROADMAP.md) or Consumer roadmap—do not treat AIOS Core roadmap as automatically editable)
4. Core / Module / Pack / Consumer boundaries (when AIOS applies)
5. Reuse and stack-agnostic principles
6. Potential duplication or scope drift

State clearly:

- What the repository claims to be
- Who it serves
- Whether the proposal fits, partially fits, or conflicts
- Evidence for the judgment
- Risks of misalignment
- Questions the owner should resolve before proceeding

---

## Expected Output

- Primary Purpose (documented)
- Target Audience
- Repository Differentiators
- Documented Direction / Roadmap Signals
- Alignment Verdict (Fit / Partial / Conflict) with evidence
- Scope-drift or duplication concerns
- Critical Artifacts that define vision
- Open questions for the owner

---

## Constraints

- Do not create commitments, dates, priorities, or approvals.
- Do not silently change roadmap or product scope.
- Do not redefine L0–L7 or ownership boundaries.
- Consumer / repository owner decisions remain owner-owned.
- AI recommends; humans decide.

## Related References

- Discovery order: [`README.md`](README.md)
- Framework Contract: [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md)
- Product navigation: [`MANIFEST.md`](../../MANIFEST.md), [`README.md`](../../README.md)
- Roadmap: [`ROADMAP.md`](../../ROADMAP.md)
