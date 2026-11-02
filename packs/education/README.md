# Education Pack

Status: Partial

Last Updated: 2026-11-02

---

## Pack identity

The **Education Pack** is an optional AIOS **domain extension** for **Education & Learning Engineering**.

Its purpose is to help design, structure, produce, validate and improve **educational experiences** and **learning materials**.

It addresses both:

- educational content and instructional design
- the engineering practices needed to deliver reliable, maintainable learning experiences in a repository

This Pack is **not** limited to any single subject, language, technology stack or content format.

---

## Scope

The Education Pack focuses on **educational methodology** and **learning experience**, not on a particular programming language, natural language or delivery medium.

Illustrative domains (not exhaustive):

- Language learning
- Programming and software education
- Academic education
- Professional and technical training
- Digital education, e-learning and LMS
- Learning materials and instructional content
- Exercises, quizzes, examinations and assessments
- Curriculum design and learning progress

A consumer may apply the Pack to one or more of these domains — or to other educational contexts — when the Pack is **explicitly adopted**.

---

## Relationship to AIOS Core

| Layer | Role |
|-------|------|
| **AIOS Core** | Common engineering and governance foundation |
| **Education Pack** | Optional Education & Learning Engineering extension |

### Precedence (summary)

When this Pack is explicitly adopted, its guidance operates at **L5 (Adopted Pack guidance)** within the canonical instruction model.

- The Pack **cannot override L0–L4**.
- Consumer-approved ADRs and local policies remain authoritative (**L2 / L3**).
- Pack guidance applies only within its **adopted educational scope**.
- Module recommendations remain **recommendations** unless the consumer explicitly adopts them as local policy (**L3**).

Canonical definition:

- [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) §7
- [`AGENTS.md`](../../AGENTS.md) §2

Do not invent a competing hierarchy inside this Pack.

---

## Adoption

The Education Pack must be **explicitly adopted** by a consumer project.

- Presence of this Pack inside the AIOS repository does **not** activate it for every consumer.
- `AGENTS.education.md` must be loaded or applied **only** when the consumer explicitly adopts the Education Pack.
- Adoption authorizes educational guidance within scope; it does **not** authorize autonomous modifications to consumer repositories.
- The project owner retains decision authority over whether and how Pack guidance is applied.

Typical adoption is a consumer-owned decision (documentation, ADR or local policy) that states the Pack is in use for that repository or learning product.

---

## Historical file: `AGENTS.education.md`

Current path: [`AGENTS.education.md`](AGENTS.education.md)

| Fact | Status |
|------|--------|
| What it is | Preserved historical education operating manual |
| Origin | Byte-preserved copy of the former education-focused root AGENTS content (Phase 0) |
| L0–L7 migration | **Not yet migrated** to the current precedence model |
| Universal Core manual? | **No** — must not be treated as the universal AIOS operating manual |
| When to apply | **Only** under explicit Education Pack adoption |
| This task | Content must remain **unchanged** |
| Future revision | Requires a separate approved migration task |

Until migration, treat `AGENTS.education.md` as **historical Pack material** under adoption control — not as a silent replacement for root [`AGENTS.md`](../../AGENTS.md).

Where historical wording conflicts with Core L0–L7 or consumer ADRs, follow Core precedence and consumer ownership; report Pack/Core tension rather than inventing a new hierarchy.

---

## Current implementation status

### Present today

- This README (Pack entry point)
- Preserved historical [`AGENTS.education.md`](AGENTS.education.md)

### Not implemented yet

- Pack metadata / schema (for example `pack.yaml`)
- Migration of education-oriented files that still live under Core `rules/` for sync compatibility
- A filled education notebook/content template set (`templates/notebook_template.md` remains an empty placeholder in Core)
- Autonomous Pack discovery or adoption engine

Do not treat planned Pack capabilities as shipped features.

---

## Future evolution (direction only)

Possible future Pack areas (not current claims of implementation):

- Learning design and instructional methodology
- Curriculum and learning-path design
- Educational content production
- Exercises and assessment
- Learning quality assurance
- Digital learning and LMS integration
- Learning progress and feedback

Any migration of historical AGENTS content or education-related `rules/` into this Pack requires product-owner approval, compatibility analysis and a rollback plan (see Framework Contract migration principles).

---

## Related Core entry points

| Document | Why |
|----------|-----|
| [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) | Pack vs Core boundaries; L5; consumption models |
| [`AGENTS.md`](../../AGENTS.md) | Canonical agent operating manual and L0–L7 |
| [`MANIFEST.md`](../../MANIFEST.md) | Product inventory and Pack status |
| [`README.md`](../../README.md) | Project overview and adoption orientation |

---

End of Education Pack README.
