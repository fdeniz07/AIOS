# README Review

## Purpose

Review a repository README for accuracy, clarity, usability, and consistency with repository evidence and authoritative documentation. Return findings with severity and recommended corrections—without editing the README.

---

## When to Use

- Before publishing or updating a README.
- When onboarding friction or inaccurate claims are suspected.
- After significant product or documentation changes.

## When Not to Use

- To rewrite the README in place without a separate authorized implementation request.
- As a substitute for full repository analysis or architecture review.
- To invent features that are not evidenced in the repository.

---

## Required Context

- Current README content (path usually `README.md`).
- Access to repository evidence for verifying claims.
- Related authoritative docs when present (manifest, contract, contributing, security).

---

## Prompt

Review this repository's README against repository evidence.

Do not edit files. Do not assume documented functionality exists without evidence. Separate **confirmed issues**, **suspected issues**, and **suggestions**.

Check:

1. Project purpose and audience clarity
2. Installation and usage claims vs actual implementation
3. Feature and capability claims vs evidence
4. Documentation navigation and link validity
5. Examples and commands (accuracy and completeness)
6. Project status and maturity statements
7. Contribution and security references
8. Consistency with authoritative docs (for AIOS: [`MANIFEST.md`](../../MANIFEST.md), [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md), [`CONTRIBUTING.md`](../../CONTRIBUTING.md), [`SECURITY.md`](../../SECURITY.md))

For each finding include:

- Severity (Blocker / Major / Minor / Nit)
- Evidence (path, quote, or missing artifact)
- Affected README section
- Recommended correction

Preserve correct existing content in your recommendations. Prefer linking to authoritative sources over duplicating them in the README.

---

## Expected Output

- Overall README assessment
- Findings table or list (severity, evidence, section, recommendation)
- Unsupported claims
- Broken or weak navigation/links
- Suggested minimal correction priorities
- Questions for the owner

---

## Constraints

- Do not edit the README automatically.
- Do not invent product claims or maturity upgrades.
- Do not redefine governance or L0–L7.
- AI recommends; humans decide.

## Related References

- Framework Contract: [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md)
- Contributing: [`CONTRIBUTING.md`](../../CONTRIBUTING.md)
- Security: [`SECURITY.md`](../../SECURITY.md)
