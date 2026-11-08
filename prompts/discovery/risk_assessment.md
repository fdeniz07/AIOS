# Risk Assessment

## Purpose

Identify relevant risks before implementation or significant repository changes. Classify risks by impact and likelihood, cite evidence and uncertainty, and recommend mitigations—without accepting risk on behalf of the owner.

---

## When to Use

- After Repository Analysis (preferred).
- Before planning implementations or making architectural decisions.
- Before large refactors, migrations, or Consumer adoption changes.

## When Not to Use

- Before enough repository context exists to ground the assessment.
- As a substitute for security vulnerability disclosure processes.
- To approve, reject, or accept residual risk for the Consumer or repository owner.

---

## Required Context

- Repository Analysis completed, or equivalent current understanding of structure and purpose.
- Intended change or upcoming work described when known.
- No implementation started for the assessed change (unless reassessing mid-work).

---

## Prompt

Perform a risk assessment for this repository and the intended upcoming work (if provided).

Base findings on repository evidence and the prior analysis. Separate **observed risks**, **hypotheses**, and **mitigation recommendations**. Do not modify files. Do not implement fixes. Do not invent owner risk-acceptance decisions.

Evaluate at least these categories when relevant:

1. Architectural and dependency risks
2. Compatibility and migration risks
3. Security and privacy implications
4. Data integrity risks
5. Testing and validation gaps
6. Operational and deployment risks
7. Documentation and governance inconsistencies
8. Consumer-specific risks (ownership, sync, local policy) when AIOS Consumer adoption is in scope

For each risk, state:

- Description
- Evidence and uncertainty
- Impact (Critical / High / Medium / Low)
- Likelihood (High / Medium / Low)
- Possible consequences
- Recommended mitigation
- Whether resolution should precede further development

If AIOS applies, respect Core / Module / Pack / Consumer boundaries and Consumer ownership of ADR and risk acceptance per [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) and [`AGENTS.md`](../../AGENTS.md).

---

## Expected Output

- Critical Risks
- High Risks
- Medium Risks
- Low Risks
- Cross-cutting themes / systemic issues
- Open questions requiring owner input
- Recommended pre-development mitigations (non-binding)

---

## Constraints

- Do not modify files or generate implementation patches in this pass.
- Do not accept risk for the Consumer or repository owner.
- Do not redefine L0–L7 or governance authority.
- Do not claim a risk engine or automated compliance certification.
- AI recommends; humans decide.

## Related References

- Discovery order: [`README.md`](README.md)
- Framework Contract: [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md)
- Agent operating manual: [`AGENTS.md`](../../AGENTS.md)
- Security reporting (vulnerabilities): [`SECURITY.md`](../../SECURITY.md)
