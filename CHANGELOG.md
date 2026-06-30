# Changelog

## v1.0.1

### Fixed

Improved user override behavior.

Repository rule conflicts
must now be detected and reported
before implementation.

Explicit confirmation is required
before violating repository standards.

## v1.0.0 RC1

### Improved

- Added Approval Gates.
- AI now detects repository rule conflicts before silently violating project standards.
- AI provides recommendations when user requests conflict with repository conventions.

## 2026-06-30

### Validation

Confirmed that Approval Gates work correctly.

The AI now:

- analyzes the repository,
- checks the roadmap,
- verifies project rules,
- detects approval-required actions,
- waits for explicit confirmation before creating new notebooks.
