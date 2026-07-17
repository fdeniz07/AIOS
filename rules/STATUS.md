# STATUS_RULES.md

# AIOS Content Lifecycle Standard

## Purpose

This document defines the official lifecycle states used by AIOS-managed repositories.

The goal is to provide a consistent vocabulary for educational content, documentation, templates, and project artifacts.

All AI-generated and human-authored content must use these status definitions consistently.

---

# Lifecycle Overview

```text
Idea
   ↓
Draft
   ↓
In Review
   ↓
Published
   ↓
Updated
   ↓
Published

        or

Published
   ↓
Deprecated
   ↓
Legacy
```

---

# Status Definitions

## Idea

Content has been proposed but does not yet exist.

Characteristics:

- planning only
- no implementation
- may change completely

Examples:

- roadmap entries
- backlog items
- feature proposals

---

## Draft

The content has been written but is not yet considered complete.

Characteristics:

- first implementation
- educational review pending
- visuals may be incomplete
- examples may change

Suitable for:

- notebooks
- documentation
- templates

---

## In Review

The content is currently under technical or editorial review.

Review may include:

- technical validation
- educational quality
- grammar
- consistency
- AIOS compliance
- visual review

---

## Published

The content is officially part of the project.

Requirements:

- reviewed
- AIOS compliant
- navigation complete
- visual standards satisfied
- learning objectives verified

Published content should remain stable.

---

## Updated

Published content that receives improvements while remaining part of the curriculum.

Examples:

- improved examples
- better diagrams
- typo fixes
- additional exercises

Updating does NOT restart the lifecycle.

---

## Reference Material

Reference material supports learning but is not part of the primary curriculum.

Examples:

- migration guides
- historical notes
- advanced reading
- comparison documents
- supplementary examples

Reference material should never replace a canonical chapter.

---

## Pending Curriculum Integration

Content is valid but has not yet been assigned to its final position within the learning path.

Typical situations:

- notebooks written before roadmap redesign
- translated material awaiting synchronization
- content developed ahead of schedule

This status indicates future integration, not retirement.

---

## Deprecated

The content should no longer be used for new work.

Reasons:

- replaced by newer content
- obsolete technology
- outdated workflow

Deprecated content may remain temporarily for compatibility.

---

## Legacy

Legacy content is preserved only for historical purposes.

Legacy content:

- is no longer maintained
- is not part of the active curriculum
- has been replaced
- exists only for historical reference

Legacy should be used sparingly.

Do NOT use Legacy for content that will later become part of the curriculum.

Use **Pending Curriculum Integration** instead.

---

# Status Selection Guide

| Situation | Status |
|-----------|--------|
| Planned but not written | Idea |
| First version | Draft |
| Being reviewed | In Review |
| Official content | Published |
| Improved published content | Updated |
| Supplementary material | Reference Material |
| Waiting for roadmap placement | Pending Curriculum Integration |
| Scheduled for replacement | Deprecated |
| Historical archive | Legacy |

---

# General Rules

- Every primary educational artifact should declare its status.
- Status must reflect the actual lifecycle stage.
- Status should not be used as a progress indicator.
- Do not invent custom status labels.
- Use the official AIOS terminology consistently.

---

# AI Guidelines

AI assistants must:

- preserve existing status labels unless instructed otherwise;
- recommend status changes only when justified;
- never mark active curriculum content as Legacy;
- distinguish between educational maturity and curriculum placement.

---

# Examples

✅ Correct

Chapter under development

Status: Draft

---

Supplementary migration guide

Status: Reference Material

---

Notebook waiting for roadmap assignment

Status: Pending Curriculum Integration

---

Retired documentation kept for history

Status: Legacy

---

Obsolete guide replaced by a newer version

Status: Deprecated