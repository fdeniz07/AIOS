# Documentation Generator

## Purpose

Generate accurate, maintainable engineering documentation from supplied requirements and verified repository context. Produce documentation content only—do not claim to create files or modify repositories automatically.

---

## When to Use

- When the audience, document purpose, and available evidence are known.
- To draft technical overviews, architecture explanations, API/component docs, setup guides, engineering process docs, or developer reference material.
- After discovery/review when documentation gaps are confirmed.

## When Not to Use

- To invent undocumented features or mark speculative content as shipped.
- To replace Framework Contract, ADRs, or other authoritative sources by copying them wholesale.
- To automatically write files into the repository without separate authorization.

---

## Required Context

- Intended audience and document purpose.
- Document type requested.
- Repository evidence and/or explicit source materials.
- Existing terminology, architecture, and style to follow.
- Known gaps the draft must label as assumptions.

---

## Prompt

Generate engineering documentation for the requested type and audience.

Establish purpose and audience first. Use repository evidence where available. Label assumptions and missing information explicitly. Follow existing terminology and architecture. Link to authoritative sources instead of duplicating them. Avoid unsupported implementation or feature claims. Preserve Consumer ownership of Consumer-specific decisions and documentation.

Supported document types (as requested):

- Technical overviews
- Architecture explanations
- API and component documentation
- Setup and usage guides
- Engineering process documentation
- Developer-facing reference material

Process:

1. Confirm audience, purpose, and document type
2. List evidence sources used and gaps
3. Draft structured Markdown content
4. Mark assumptions and TODOs clearly
5. Provide a short validation checklist for the owner (links, commands, claims to verify)

For AIOS-related docs, treat [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md), [`AGENTS.md`](../../AGENTS.md), [`MANIFEST.md`](../../MANIFEST.md), and [`PROJECT_STRUCTURE.md`](../../PROJECT_STRUCTURE.md) as authoritative for architecture and status language. Do not redefine L0–L7 or Core / Module / Pack / Consumer boundaries.

Output documentation content only. Do not claim file creation, automatic commits, or repository modification.

---

## Expected Output

- Document metadata (audience, purpose, type, evidence used)
- Draft Markdown body
- Assumptions / missing information
- Suggested links to authoritative sources
- Owner validation checklist
- Open questions

---

## Constraints

- Do not create or modify repository files automatically.
- Do not invent features, runtimes, resolvers, installers, or adoption mechanisms.
- Do not grant commit, push, publish, or deploy authority.
- Do not replace Skills, Workflows, or Methodology with this prompt.
- AI recommends; humans decide.

## Related References

- Framework Contract: [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md)
- Project structure: [`PROJECT_STRUCTURE.md`](../../PROJECT_STRUCTURE.md)
- Agent operating manual: [`AGENTS.md`](../../AGENTS.md)
- Contribution guidance: [`CONTRIBUTING.md`](../../CONTRIBUTING.md)
