# README Improvement

## Purpose

Propose focused improvements to an existing README based on repository evidence. Preserve correct content, fix concrete usability or accuracy problems, and separate recommendations from confirmed facts—without modifying files unless separately authorized.

---

## When to Use

- After a README Review (preferred) or when specific README problems are known.
- When onboarding docs need a minimal, structured improvement.
- Before a documentation-focused PR.

## When Not to Use

- To perform a wholesale rewrite of unrelated sections.
- To invent unsupported product or maturity claims.
- To modify files without an explicit user request authorizing implementation.

---

## Required Context

- Current README content.
- Repository evidence (and prior README Review findings when available).
- Owner priorities for the improvement (optional).

---

## Prompt

Propose a focused README improvement for this repository.

Review the current README and repository evidence. Identify concrete usability or accuracy problems. Preserve correct existing information, useful navigation, and valid links. Do not introduce unsupported product claims.

Deliver:

1. Problem summary (what hurts readers today)
2. Minimal improvement plan (ordered, scoped)
3. Proposed revised sections or patches (text the owner can apply)
4. Unsupported claims to remove or rephrase
5. Links/navigation to preserve or fix
6. Facts vs recommendations vs assumptions

Do not modify files unless the user separately requests and authorizes implementation. Prefer linking to authoritative docs ([`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md), [`CONTRIBUTING.md`](../../CONTRIBUTING.md), [`SECURITY.md`](../../SECURITY.md), [`MANIFEST.md`](../../MANIFEST.md)) instead of duplicating them.

---

## Expected Output

- Problem summary
- Minimal improvement plan
- Proposed README text (section-level)
- Claims to remove or qualify
- Link/navigation notes
- Validation suggestions (manual review checklist)
- Open questions for the owner

---

## Constraints

- Do not rewrite unrelated sections.
- Do not invent features, statuses, or guarantees.
- Do not commit, push, or publish.
- Do not redefine governance or L0–L7.
- AI recommends; humans decide.

## Related References

- Related review prompt: [`../review/readme_review.md`](../review/readme_review.md)
- Contributing: [`CONTRIBUTING.md`](../../CONTRIBUTING.md)
- Framework Contract: [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md)
