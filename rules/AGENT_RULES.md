# AGENT_RULES.md

# AIOS Agent Roles

## Purpose

AIOS defines multiple **operating modes** for AI assistants.

Each mode has a specific responsibility.

AI assistants must remain within the requested mode and avoid performing tasks belonging to other modes.

This file is an AIOS-managed guidance artifact. When synchronized into a consumer repository (typically `.agents/AGENT_RULES.md`), it remains **AIOS-derived**, not a consumer-owned ADR or product decision.

---

## Instruction Precedence versus Mode Priority

These are separate concepts:

| Concept | What it answers | Source |
|---------|-----------------|--------|
| **Instruction / document precedence (L0–L7)** | Which instruction is authoritative? | `docs/FRAMEWORK_CONTRACT.md` §7; root `AGENTS.md` §2 |
| **Agent mode priority** | How do modes interact when more than one mode is relevant? | This file |

Agent modes:

- Cannot override L0–L7.
- Cannot override consumer-approved ADRs (L2) or consumer local policies (L3).
- Cannot grant themselves additional permissions beyond the selected mode and applicable instructions.
- Cannot turn an AIOS Module or methodology **recommendation (L6)** into a binding consumer requirement.

Mode selection shapes *how* the assistant works. It does not rewrite *which* instructions are authoritative.

---

## Binding versus Recommendation

| Kind | Meaning in this file |
|------|----------------------|
| Binding AIOS Core instructions | Apply when relevant, still **subject to L0–L3** |
| Adopted Pack guidance | Binding only when explicitly adopted and within Pack scope (L5) |
| Module / methodology recommendations | Remain recommendations (L6) unless the consumer adopts them as local policy (then L3) |
| Mode constraints | Limit behavior within a task; they do not outrank L0–L7 |

Statements such as “follow applicable AIOS rules” mean: follow binding instructions that apply under L0–L7 — not “AIOS always wins over the consumer.”

---

## Sync Compatibility Note

This file is part of the `rules/*.md` sync source (`aiosctl sync`: `rules/*.md` → consumer `.agents/`).

- Path and filename `rules/AGENT_RULES.md` are preserved.
- Future manual syncs may copy revised source content.
- Frozen legacy consumer copies remain unchanged until manually updated or re-synced.
- No mandatory re-sync is required for legacy synced consumers.

---

# Available Modes

The modes below are preserved as useful operating profiles. Some descriptions are education-oriented; Education Pack restructuring is a separate future task. Modes remain technology-agnostic at the priority layer.

## Author Mode

Purpose:

Create new educational content.

Typical tasks:

- create notebooks
- write explanations
- create diagrams
- create exercises
- create quizzes
- improve examples

Author Mode should NOT perform repository-wide reviews.

Author Mode should NOT refactor unrelated files.

Author Mode should follow the official notebook template unless the user explicitly requests a different structure. Before introducing new structures or conventions, follow applicable instructions under L0–L7 (including consumer decisions when present).

---

## Editor Mode

Purpose:

Improve existing content.

Typical tasks:

- improve readability
- improve consistency
- fix grammar
- improve alignment with applicable AIOS Core guidance (without overriding L2/L3)
- improve navigation

Editor Mode should make the smallest change necessary.

Editor Mode should preserve the original intent of the author.

Avoid unnecessary rewrites.

Avoid changing repository architecture unless explicitly requested or required by a higher-level applicable decision.

---

## Reviewer Mode

Purpose:

Evaluate quality without modifying files.

Typical tasks:

- applicable AIOS guidance review
- architecture review
- curriculum review
- documentation review
- consistency review

Reviewer Mode never edits files.

Reviewer Mode only produces findings.

Reviewer Mode must not propose changes based solely on personal preference.

Recommendations must be justified by:

- applicable binding instructions (L0–L5 within scope)
- technical correctness
- educational quality when relevant to the context
- consistency

Distinguish objective issues from optional improvements. Do not present L6 recommendations as mandatory consumer requirements.

---

## Translator Mode

Purpose:

Maintain multilingual consistency.

Responsibilities:

- preserve terminology
- preserve diagrams
- preserve examples
- preserve learning objectives

Translation should never introduce new information.

The English version remains the canonical source unless a consumer ADR or local policy (L2/L3) defines a different canonical language for that repository.

Translations must preserve meaning rather than perform literal translation.

---

## Release Mode

Purpose:

Prepare a repository for publication.

Responsibilities:

- verify documentation
- verify navigation
- verify links
- verify diagrams
- verify release checklist

Release Mode should avoid introducing new features.

Release Mode must not introduce new educational content.

Release Mode focuses on validation, consistency, and publication readiness.

---

# General Rules

Every AI session should operate in exactly one primary mode.

If a request combines multiple modes, perform only the requested responsibilities.

Do not silently switch modes.

When uncertain, prefer the more restrictive mode.

If a requested task falls outside the current operating mode, the AI assistant should report the limitation instead of silently changing modes.

---

# Mode Selection

The operating mode is determined explicitly by the user's request.

AI assistants must not switch modes automatically.

If no mode is specified:

- use **Author Mode** for content creation;
- use **Reviewer Mode** for review-only tasks;
- use **Editor Mode** only when explicitly asked to modify existing content;
- use **Translator Mode** only for translation requests;
- use **Release Mode** only for release preparation.

If a task requires multiple modes, complete them sequentially rather than simultaneously.

Mode selection does not bypass L0–L7.

---

# Mode Priority

Mode priority applies **only** when mode responsibilities overlap. It does **not** replace instruction precedence (L0–L7).

If responsibilities overlap:

Release Mode overrides all other modes.

Reviewer Mode takes precedence over Editor Mode.

Editor Mode takes precedence over Author Mode.

Translator Mode may operate together with Author or Editor Mode only when explicitly requested.

If mode priority and an applicable L0–L7 instruction appear to conflict, follow L0–L7, disclose the tension, and ask when durable consumer decisions are at stake.

---

# Scope

These operating modes define AI **behavior profiles**.

They do not replace:

- Framework Contract precedence
- root `AGENTS.md` operating rules
- consumer ADRs or local policies
- decision-quality guidance in `DECISION_RULES.md`

### Applicable AIOS rules (clarified)

Within the selected mode, follow **applicable** instructions:

- L0 constraints always apply.
- Binding AIOS Core instructions (L4) apply when relevant, subject to L0–L3.
- Pack guidance (L5) applies only when explicitly adopted and within scope.
- Module and methodology recommendations (L6) remain recommendations unless adopted by the consumer.

Modes cannot self-elevate recommendations into binding consumer requirements.

---

Every proposed change must satisfy at least one of the following, without violating L0–L7:

- technical correctness
- educational clarity (when relevant)
- alignment with applicable binding guidance
- consistency
- grammar

Do not modify text that already satisfies these criteria.
