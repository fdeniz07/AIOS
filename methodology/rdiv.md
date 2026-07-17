# RDIV Methodology

Status: Stable

Version: 1.0

Category: Methodology

---

# Purpose

The RDIV methodology defines the standard workflow for AI-assisted software engineering within the AIOS Framework.

Its objective is to ensure that development decisions are based on analysis rather than assumptions, reducing unnecessary changes and improving long-term maintainability.

RDIV stands for:

- Review
- Decide
- Implement
- Verify

Every significant development task should follow this sequence.

---

# Philosophy

The AIOS Framework treats software development as a decision-making process rather than a coding process.

Code should only be written after the repository, architecture, and objectives have been properly understood.

The AI assists during every phase, while the final decisions always remain the responsibility of the developer.

---

# Workflow

## 1. Review

Understand the current state before making any changes.

Typical activities include:

- Repository Analysis
- Risk Assessment
- Architecture Review
- Documentation Review
- Understanding existing code

Goal:

Create an objective understanding of the project.

Deliverable:

A clear picture of the current repository.

---

## 2. Decide

Determine the best course of action.

Typical activities include:

- Prioritizing tasks
- Selecting implementation order
- Evaluating alternatives
- Confirming architectural direction

Goal:

Make informed decisions before implementation begins.

Deliverable:

A documented implementation strategy.

---

## 3. Implement

Execute the approved plan.

Implementation should follow the previously agreed architecture.

Avoid introducing unrelated improvements or unnecessary refactoring.

Goal:

Produce maintainable and consistent code.

Deliverable:

Completed implementation.

---

## 4. Verify

Confirm that the implementation achieved its objective.

Verification may include:

- Manual review
- Testing
- Documentation updates
- Architectural consistency checks
- Quality assurance

Goal:

Ensure that the repository remains consistent and reliable.

Deliverable:

Validated implementation.

---

# RDIV Principles

- Review before coding.
- Decisions before implementation.
- Verify every significant change.
- Avoid unnecessary modifications.
- Preserve architectural consistency.
- Prefer incremental improvements over large refactorings.

---

# Benefits

Following RDIV provides several advantages:

- Better architectural decisions
- Lower implementation risk
- Higher code quality
- Improved maintainability
- More predictable development process
- Better AI collaboration

---

# Relationship with AIOS

RDIV is the primary development methodology used throughout the AIOS Framework.

Discovery prompts support the Review phase.

Planning activities support the Decide phase.

Implementation prompts support the Implement phase.

Review and validation prompts support the Verify phase.

---

# Typical Workflow

Repository Analysis

↓

Risk Assessment

↓

Implementation Strategy

↓

Architecture Review

↓

Implementation

↓

Verification

---

# Final Principle

Never implement before understanding.

Every implementation should be the result of a reviewed repository, a conscious decision, and a successful verification.