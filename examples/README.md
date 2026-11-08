# AIOS Adoption Examples

Status: Documentation examples (Phase 9)

These examples explain how a **Consumer** project can adopt AIOS guidance.

They are **documentation only**. They are not runnable applications, installers, discovery engines, or automatic decision systems.

---

## What these examples are

| Example | Path | Focus |
|---------|------|--------|
| Core Adoption | [`01-core-adoption/`](01-core-adoption/README.md) | Using AIOS Core documentation and governance in a Consumer project |
| Module-Guided Adoption | [`02-module-guided-adoption/`](02-module-guided-adoption/README.md) | Evaluating and optionally adopting Module guidance under Consumer control |

Both examples preserve the approved architectural layers:

- **Core** — common engineering foundation
- **Module** — reusable engineering capability (optional; L6 by default)
- **Pack** — optional domain / use-case extension (L5 when explicitly adopted)
- **Consumer** — product ownership, ADRs, local policy, and implementation

Instruction precedence remains Framework Contract §7 / [`AGENTS.md`](../AGENTS.md) §2 (**L0–L7**). These examples do not invent a competing hierarchy.

---

## What these examples are not

- Not a runtime or Adaptive Guidance Engine
- Not Module discovery, resolver, or installer behavior
- Not automatic adoption or automatic configuration modification
- Not Consumer product templates with filled ADRs or backlogs
- Not proof that validation success equals architectural correctness

---

## How to use

1. Read [`docs/FRAMEWORK_CONTRACT.md`](../docs/FRAMEWORK_CONTRACT.md).
2. Read the Core Adoption example first.
3. Read the Module-Guided Adoption example only when Module guidance is relevant.
4. Record durable Consumer decisions in Consumer-owned artifacts (ADRs / local policy).

AIOS recommends. The Consumer owner decides.

---

## Related references

| Document | Role |
|----------|------|
| [`docs/FRAMEWORK_CONTRACT.md`](../docs/FRAMEWORK_CONTRACT.md) | Authoritative architectural and governance contract |
| [`AGENTS.md`](../AGENTS.md) | Agent operating manual (operationalizes L0–L7) |
| [`docs/integrations/README.md`](../docs/integrations/README.md) | Coding-assistant integration guides |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | Contribution process |
| [`ROADMAP.md`](../ROADMAP.md) | Phase 9 intent and framework evolution |

Historical empty folders under `examples/` (for example `DevOps`, `German`, `Python`) remain reserved placeholders and are not active adoption examples.
