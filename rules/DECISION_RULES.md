# DECISION_RULES.md

# AIOS Editorial Decision Rules

## Purpose

This document defines **decision-quality and decision-making guidance** for AI assistants when multiple valid solutions exist.

It helps choose among alternatives through predictable, minimal and maintainable changes.

It does **not** define instruction/document authority. Authority and precedence follow:

- `docs/FRAMEWORK_CONTRACT.md` §7
- Root `AGENTS.md` §2 (L0–L7)

This file is an AIOS-managed guidance artifact. When synchronized into a consumer repository (typically `.agents/DECISION_RULES.md`), it remains **AIOS-derived**, not a consumer-owned ADR or product decision.

---

## Instruction Precedence versus Decision Quality

These are separate concepts:

| Concept | What it answers | Source |
|---------|-----------------|--------|
| **Instruction / document precedence (L0–L7)** | Which instruction is authoritative? | Framework Contract §7; `AGENTS.md` §2 |
| **Decision-quality criteria** | Which valid option is better once authority is settled? | This file |

Decision-quality criteria **do not** change instruction authority or precedence.

In particular:

- They do not place “AIOS compliance” above consumer-approved ADRs (L2) or consumer local policies (L3).
- They do not override L0 non-overridable constraints (safety, legal, security, privacy, licensing, compliance).
- Module and methodology suggestions remain **recommendations (L6)** unless the consumer explicitly adopts them as local policy (then L3).

---

## Respecting Consumer Decisions

Existing consumer ADRs and product decisions must be respected (L2).

If a proposed decision conflicts with an existing consumer ADR or durable product decision:

1. Disclose the conflict.
2. Explain the trade-offs.
3. Ask the authorized consumer decision owner.
4. Do not silently replace the ADR or rewrite the durable decision.

Consumer-owned decisions are not subordinate to generic AIOS Core defaults in this file.

---

## Sync Compatibility Note

This file is part of the `rules/*.md` sync source (`aiosctl sync`: `rules/*.md` → consumer `.agents/`).

- Path and filename `rules/DECISION_RULES.md` are preserved for compatibility.
- Future manual syncs may copy revised source content.
- Frozen legacy consumer copies remain unchanged until manually updated or re-synced.
- No mandatory re-sync is required for legacy synced consumers.

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

- required by an applicable consumer decision or local policy (L2/L3)
- required by binding AIOS Core defaults that do not conflict with L0–L3
- explicitly requested by the user (L1), within L0

Preserve the existing repository structure.

---

## Do Not Invent Standards

Never invent ad-hoc standards when applicable official standards already exist.

Do not create without justification:

- new terminology
- new lifecycle states
- new document types
- new folder conventions
- new naming conventions

Prefer:

1. Consumer-approved standards and ADRs (L2/L3)
2. Adopted AIOS Core / Pack standards within their scope (L4/L5)
3. Explicit user direction (L1), within L0

---

## Prefer Consistency

When two valid solutions exist **and** higher-level instructions do not decide, prefer the one that is more consistent with the existing repository.

Consistency is more important than personal preference.

---

## Preserve Educational Content

Educational material should never be removed simply because it is incomplete.

Possible actions:

- improve
- relocate
- mark for future integration

Do not delete educational content without explicit justification.

When working outside an education-oriented Pack or consumer, treat this as domain-sensitive guidance — not a reason to override product ADRs.

---

## Preserve User Intent

Explicit user instructions for the current task (L1) take precedence over stylistic preferences, within L0.

They do not silently amend durable consumer ADRs or local policies (L2/L3). Disclose conflicts and obtain authorization before durable changes.

Do not reinterpret the requested scope.

If unsure, modify less rather than more.

---

## Template vs Implementation

If an implementation differs from a template:

- determine which artifact is authoritative under L0–L7;
- do not assume the template is always authoritative;
- preserve stable published content unless a higher-level decision or explicit request establishes a new standard.

---

## Backward Compatibility

Avoid changes that break:

- links
- references
- repository navigation
- chapter numbering (where used)

Preserve compatibility whenever practical.

---

## Documentation First

When architecture changes:

Update applicable documentation such as:

- README
- ROADMAP (consumer or framework, as appropriate)
- Architecture documentation
- Consumer ADRs when the change is a durable product decision (consumer-owned)

Keep documentation synchronized with implementation without claiming ownership of consumer ADRs.

---

## Prefer Explicitness

Never rely on assumptions.

If uncertainty exists:

- preserve the existing implementation;
- avoid speculative modifications;
- report uncertainty rather than inventing a solution.

---

# Decision-Quality Priority

When multiple decisions remain possible **after** applying L0–L7 instruction precedence, use this quality order:

1. Correctness (and satisfaction of applicable L0 constraints)
2. Fit to explicit user instructions for the current task (L1)
3. Fit to consumer ADRs / product decisions and local policies (L2/L3)
4. Fit to applicable AIOS Core defaults (L4) — “AIOS compliance” in this sense only
5. Educational quality (when the work is educational / Pack-adopted context)
6. Repository consistency
7. Maintainability
8. Readability
9. Visual improvements
10. Cosmetic improvements

Never sacrifice a higher **quality** priority for a lower one.

This list ranks alternatives. It does **not** rewrite document precedence.

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

Unless explicitly requested (and still within L0), AI assistants must NOT:

- rename repositories
- rename chapters
- delete educational material
- remove diagrams
- change learning objectives
- invent terminology
- introduce new lifecycle labels
- reorganize the curriculum
- perform large-scale refactoring
- silently replace consumer ADRs or durable product decisions

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

- correctness and applicable L0 constraints
- respect for consumer decisions (L2/L3)
- applicable AIOS Core guidance (L4), without treating it as supreme over the consumer
- educational quality when relevant to the adopted context
- consistency

Avoid recommending changes based solely on personal preference.

Recommendations (including Module suggestions) must not be presented as mandatory overrides of binding consumer instructions.

---

# Final Principle

The best AIOS-assisted modification is the smallest change that clearly improves the repository while respecting non-overridable constraints, consumer ownership, applicable AIOS Core defaults and the author’s intent.
