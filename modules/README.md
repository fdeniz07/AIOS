# AIOS Engineering Module Catalog

This directory holds optional **Engineering Module** packages.

Modules provide reusable, stack-agnostic engineering capability guidance. They are **recommendations by default (L6)**. They are not installed, adopted, or enabled by presence in this catalog. A consumer may explicitly adopt Module guidance into its own local policy (**L3**).

Authoritative contracts:

- Architecture and boundaries: [`../docs/FRAMEWORK_CONTRACT.md`](../docs/FRAMEWORK_CONTRACT.md) §5
- Precedence (L0–L7): [`../docs/FRAMEWORK_CONTRACT.md`](../docs/FRAMEWORK_CONTRACT.md) §7 / [`../AGENTS.md`](../AGENTS.md) §2
- Metadata: [`../docs/MODULE_METADATA.md`](../docs/MODULE_METADATA.md)
- Lifecycle: [`../docs/MODULE_LIFECYCLE.md`](../docs/MODULE_LIFECYCLE.md)
- Validation expectations: [`../docs/MODULE_VALIDATION.md`](../docs/MODULE_VALIDATION.md)

This index lists **only packages that exist** in this repository. It does not duplicate `module.yaml` fields. It is not a registry, resolver, installer, or discovery engine.

## Modules present

| id | Title | Status | Summary | Package |
|----|-------|--------|---------|---------|
| `architecture-engineering` | Architecture Engineering | `draft` | Guidance for understanding, reviewing, and supporting durable software architecture decisions without imposing a product architecture on consumers. | [`architecture-engineering/`](architecture-engineering/) |
| `development-engineering` | Development Engineering | `draft` | Optional stack-agnostic guidance for disciplined implementation within an already agreed scope, without replacing Core workflows or imposing coding standards. | [`development-engineering/`](development-engineering/) |
| `testing-quality-engineering` | Testing & Quality Engineering | `draft` | Optional stack-agnostic guidance for risk-proportionate testing and validation evidence, without replacing Core workflows or mandating test tools. | [`testing-quality-engineering/`](testing-quality-engineering/) |

## Notes

- Framework Governance remains Core-owned; it is not a Module responsibility.
- Capability-specific Skills may live inside Module packages when present (for example a draft Skill under `architecture-engineering`). Cross-cutting Core resources remain under root directories such as `methodology/`, `skills/`, and `workflows/`. This index does not list or resolve individual Skills.
- Planned or undesigned catalog domains are **not** listed here until a package exists.
