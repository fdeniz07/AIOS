# AGENT_RULES.md

# AIOS Agent Roles

## Purpose

AIOS defines multiple operating modes for AI assistants.

Each mode has a specific responsibility.

AI assistants must remain within the requested mode and avoid performing tasks belonging to other modes.

---

# Available Modes

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

Author Mode should follow the official notebook template unless the user explicitly requests a different structure. Author Mode should follow all applicable AIOS rules before introducing new structures or conventions.

---

## Editor Mode

Purpose:

Improve existing content.

Typical tasks:

- improve readability
- improve consistency
- fix grammar
- improve AIOS compliance
- improve navigation

Editor Mode should make the smallest change necessary.

Editor Mode should preserve the original intent of the author.

Avoid unnecessary rewrites.

Avoid changing repository architecture unless explicitly requested.

---

## Reviewer Mode

Purpose:

Evaluate quality without modifying files.

Typical tasks:

- AIOS compliance review
- architecture review
- curriculum review
- documentation review
- consistency review

Reviewer Mode never edits files.

Reviewer Mode only produces findings.

Reviewer Mode must not propose changes based solely on personal preference.

Recommendations must be justified by:

- AIOS rules
- technical correctness
- educational quality
- consistency

Reviewer Mode should distinguish between objective issues and optional improvements.

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

The English version remains the canonical source.

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

---

# Mode Priority

If responsibilities overlap:

Release Mode overrides all other modes.

Reviewer Mode takes precedence over Editor Mode.

Editor Mode takes precedence over Author Mode.

Translator Mode may operate together with Author or Editor Mode only when explicitly requested.

---

# Scope

These operating modes define AI behaviour.

They do not replace AIOS project rules.

All applicable AIOS rules remain mandatory regardless of the selected operating mode.

---

Every proposed change must satisfy at least one of the following:

- technical correctness
- educational clarity
- AIOS compliance
- consistency
- grammar

Do not modify text that already satisfies these criteria.

---