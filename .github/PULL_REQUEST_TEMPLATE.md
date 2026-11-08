# Pull Request

Thank you for contributing to AIOS.

Completing this template helps review. It does **not** replace human review or maintainer acceptance.

Authoritative references:

- [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- [`docs/FRAMEWORK_CONTRACT.md`](../docs/FRAMEWORK_CONTRACT.md)
- [`docs/CONTRIBUTION_CHECKLISTS.md`](../docs/CONTRIBUTION_CHECKLISTS.md)

---

## Summary

<!-- What does this PR change? -->

-

## Motivation

<!-- Why is the change needed? Link related issues when applicable. -->

-

## Scope / changed areas

<!-- List the main paths or topics touched. Prefer small, focused PRs. -->

-

## Framework Contract compatibility

<!-- Confirm the change respects Core / Module / Pack / Consumer boundaries and does not redefine L0–L7. -->

-

## Consumer impact

<!-- Any effect on synced `.agents/` content, Consumer ownership, or adoption guidance? Write "None" if not applicable. -->

-

## Validation performed

<!-- Example: `python -m validation`, relevant pytest suites, manual doc review. Validation success alone does not prove architectural correctness or content quality. -->

-

## Contribution checklist

- [ ] Change is focused and within the intended scope
- [ ] Existing architecture and governance boundaries are preserved
- [ ] L0–L7 precedence is not redefined
- [ ] Status language accurately reflects implementation maturity (`draft` / `active` / `deprecated` as applicable)
- [ ] Consumer ownership and `aiosctl sync` compatibility are preserved where relevant
- [ ] Relevant validation has been considered and results are reported above
- [ ] Relevant sections of [`docs/CONTRIBUTION_CHECKLISTS.md`](../docs/CONTRIBUTION_CHECKLISTS.md) were reviewed when applicable
- [ ] No secrets, credentials, tokens, or personal data are included
