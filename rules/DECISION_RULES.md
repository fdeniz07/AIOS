# DECISION_RULES.md

# AIOS Editorial Decision Rules

## Purpose

This document defines the decision-making principles that AI assistants must follow when modifying AIOS-managed repositories.

Unlike style or formatting rules, these guidelines determine **how decisions are made** when multiple valid solutions exist.

AI assistants must prefer predictable, minimal, and maintainable changes over unnecessary refactoring.

---

# Core Principles

## Preserve Before Replace

Always preserve existing work whenever possible.

Prefer improving existing content over replacing it completely.

Do not rewrite documents unless explicitly requested.

---

## Minimal Changes

Modify only what is necessary.

Avoid unrelated improvements.

Avoid cosmetic refactoring unless specifically requested.

Every modification should have a clear purpose.

---

## Respect Existing Architecture

Do not reorganize folders or rename files unless:

- required by the roadmap
- required by AIOS rules
- explicitly requested

Preserve the existing repository structure.

---

## Do Not Invent Standards

Never create:

- new terminology
- new lifecycle states
- new document types
- new folder conventions
- new naming conventions

Use only officially defined AIOS standards.

---

## Prefer Consistency

When two valid solutions exist, prefer the one that is more consistent with the existing repository.

Consistency is more important than personal preference.

---

## Preserve Educational Content

Educational material should never be removed simply because it is incomplete.

Possible actions:

- improve
- relocate
- mark for future integration

Do not delete educational content without explicit justification.

---

## Preserve User Intent

User instructions always take precedence over stylistic preferences.

Do not reinterpret the requested scope.

If unsure, modify less rather than more.

---

## Template vs Implementation

If an implementation differs from a template:

- determine which reflects the current AIOS standard;
- do not assume the template is always authoritative;
- preserve stable published content unless the template has explicitly become the new standard.

---

## Backward Compatibility

Avoid changes that break:

- links
- references
- repository navigation
- chapter numbering

Preserve compatibility whenever practical.

---

## Documentation First

When architecture changes:

Update:

- README
- ROADMAP
- Architecture documentation

Keep documentation synchronized with implementation.

---

## Prefer Explicitness

Never rely on assumptions.

If uncertainty exists:

- preserve the existing implementation;
- avoid speculative modifications;
- report uncertainty rather than inventing a solution.

---

# Decision Priority

When multiple decisions are possible, use this order:

1. Correctness
2. User instructions
3. AIOS compliance
4. Educational quality
5. Repository consistency
6. Maintainability
7. Readability
8. Visual improvements
9. Cosmetic improvements

Never sacrifice a higher priority to improve a lower one.

---

# Allowed Modifications

AI assistants may:

- improve explanations
- fix incorrect information
- improve consistency
- update links
- improve diagrams
- improve formatting
- reorganize sections when explicitly justified

---

# Disallowed Modifications

Unless explicitly requested, AI assistants must NOT:

- rename repositories
- rename chapters
- delete educational material
- remove diagrams
- change learning objectives
- invent terminology
- introduce new lifecycle labels
- reorganize the curriculum
- perform large-scale refactoring

---

# Uncertainty Policy

If confidence is low:

Prefer preserving the current implementation.

Do not guess.

Do not invent.

Report uncertainty instead.

---

# Review Policy

Repository reviews should focus on:

- correctness
- AIOS compliance
- educational quality
- consistency

Avoid recommending changes based solely on personal preference.

---

# Final Principle

The best AIOS modification is the smallest change that clearly improves the repository while fully respecting AIOS standards and the author's intent.