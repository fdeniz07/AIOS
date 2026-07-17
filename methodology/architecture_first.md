# Architecture First

Status: Stable

Version: 1.0

Category: Methodology

---

# Purpose

The Architecture First methodology ensures that architectural understanding always precedes implementation.

Within the AIOS Framework, no significant implementation should begin before the repository structure, architecture, and project objectives have been analyzed.

This approach minimizes technical debt, reduces unnecessary refactoring, and promotes long-term maintainability.

---

# Philosophy

Good software is built through understanding, not assumptions.

Every repository already contains decisions, patterns, and architectural intentions.

Before introducing new code, these existing decisions should be understood and respected.

Architecture is the foundation upon which all implementation decisions are made.

---

# Core Principles

## Understand Before Changing

Never modify code before understanding:

- Repository structure
- Project goals
- Existing architecture
- Design decisions
- Documentation

---

## Preserve Existing Architecture

New implementations should integrate with the current architecture whenever possible.

Avoid unnecessary redesigns.

Only recommend architectural changes when there is clear technical justification.

---

## Minimize Unnecessary Changes

Every modification increases maintenance cost.

Prefer:

- Small improvements
- Incremental development
- Focused implementations

Avoid:

- Large refactorings without necessity
- Architectural rewrites
- Changes unrelated to the current objective

---

## Architecture Drives Implementation

Implementation should follow architecture.

Architecture should never be changed simply to make implementation easier.

---

# Recommended Workflow

Step 1

Repository Analysis

↓

Step 2

Risk Assessment

↓

Step 3

Architecture Review

↓

Step 4

Implementation Strategy

↓

Step 5

Implementation

↓

Step 6

Verification

---

# AI Responsibilities

The AI should:

- Analyze the repository.
- Identify architectural patterns.
- Detect inconsistencies.
- Highlight risks.
- Recommend improvements only when justified.

The AI should not:

- Rewrite architecture unnecessarily.
- Ignore existing project conventions.
- Introduce unrelated changes.
- Assume missing information.

---

# Developer Responsibilities

The developer is responsible for:

- Making architectural decisions.
- Approving implementation plans.
- Reviewing AI suggestions.
- Ensuring business requirements are respected.

The AI assists.

The developer decides.

---

# Benefits

Applying the Architecture First methodology results in:

- Lower technical debt
- Better consistency
- Easier maintenance
- Predictable development
- Reduced implementation risk
- Improved collaboration between AI and developer

---

# Relationship with RDIV

Architecture First primarily supports the Review and Decide phases of the RDIV methodology.

A proper architectural understanding enables better implementation decisions and more reliable verification.

---

# Final Principle

Architecture is not an obstacle to development.

It is the guide that makes sustainable development possible.