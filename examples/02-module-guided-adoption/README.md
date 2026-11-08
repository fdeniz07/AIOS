# Example 02 — Module-Guided Adoption

Status: Documentation example only

This example explains how a **Consumer** may evaluate and optionally adopt AIOS **Module** guidance.

It does **not** install Modules, resolve dependencies, discover Modules at runtime, or automatically adopt Module recommendations.

---

## 1. Purpose

Show a documentation-only path where:

- Core remains the foundation
- Modules remain optional reusable engineering capabilities
- Module guidance stays **L6** until the Consumer explicitly adopts it
- Draft Modules are never treated as stable, active, installed, or automatically adopted

---

## 2. Core and Module relationship

Approved composition model:

```text
Core          → common foundation
Modules       → reusable engineering capabilities (optional)
Packs         → optional domain / use-case extensions (may compose Modules)
Consumer      → product ownership, ADRs, local policy, implementation
```

Rules preserved by this example:

- Core must remain usable without any Module.
- A Module must not depend on a specific Pack.
- A Pack may reference Modules; that is composition, not a Module dependency graph.
- Module presence in the AIOS repository does **not** activate the Module for every Consumer.

Authoritative architecture: [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) §5.

---

## 3. Module metadata and lifecycle

When a Module package exists, identity and lifecycle signals live in:

| Artifact | Role |
|----------|------|
| `modules/<id>/module.yaml` | Machine-readable identity and lifecycle fields |
| `modules/<id>/README.md` | Human/agent entry point, scope, adoption notes |

Metadata field model: [`docs/MODULE_METADATA.md`](../../docs/MODULE_METADATA.md)

Lifecycle governance: [`docs/MODULE_LIFECYCLE.md`](../../docs/MODULE_LIFECYCLE.md)

Exactly three lifecycle **status** values exist:

| Status | Meaning for Consumers |
|--------|------------------------|
| `draft` | Work in progress; **not generally recommended** for new durable adoption; disclose incompleteness |
| `active` | Maintained and available for **evaluation**; still **not** adopted or installed by metadata alone |
| `deprecated` | Not recommended for new adoption; README must include `## Migration` |

Optional **maturity** (`experimental` / `stable`) is independent of status. Maturity never means automatic adoption.

Current Engineering Module packages in this repository remain **`draft` / `experimental`**. This example must not present them as stable, active, installed, or mandatory.

---

## 4. Module-local Skills and Knowledge

Default placement:

- Capability-specific Skills and Knowledge belong **inside** the Module package when Modules exist.
- Root `skills/` and `knowledge/` remain reserved for genuinely cross-cutting Core resources.

Conventions: [`docs/SKILL_KNOWLEDGE_CONVENTIONS.md`](../../docs/SKILL_KNOWLEDGE_CONVENTIONS.md)

In this repository today (illustrative inventory, not an adoption claim):

| Module | Local capability notes |
|--------|------------------------|
| `architecture-engineering` | Module-local Skill `architecture-boundary-review` (`draft`) |
| `development-engineering` | Module-local Skill `implementation-change-hygiene` (`draft`) |
| `testing-quality-engineering` | Skeleton-only; no Module-local Skills yet |
| `security-engineering` | Skeleton-only; no Module-local Skills yet |
| `devops-cloud-engineering` | Skeleton-only; no Module-local Skills yet |
| `data-engineering` | Skeleton-only; no Module-local Skills yet |

Module Skills/Knowledge are **L6** recommendations by default. They do not replace Core workflows, Core checklists, or Consumer ADRs.

---

## 5. Consumer-controlled adoption decisions

Module guidance does **not** bind a Consumer until explicitly adopted.

Recommended manual sequence:

1. Confirm Core adoption posture first (see [`../01-core-adoption/`](../01-core-adoption/README.md)).
2. Inspect Module `README.md` and `module.yaml`.
3. Check `status` and `maturity`. If `draft`, treat as incomplete evaluation material only.
4. Decide whether the Module is relevant (`applies_when` / `avoid_when` and README narrative).
5. If useful, **recommend** Module guidance for a task (**L6**).
6. If the Consumer wants durable binding guidance, record the adoption decision in a Consumer ADR (**L2**) or local policy (**L3**). Explicitly adopted Module guidance becomes Consumer-owned local policy at **L3** within the approved scope.
7. Keep unadopted Module text as recommendation only.

Allowed:

- Analyze and recommend Modules
- Explain trade-offs and when **not** to use a Module
- Wait for Consumer-owner approval before durable adoption
- Record adoption only after an explicit Consumer decision

Not allowed in this example (and not implemented by AIOS Phase 9):

- Automatic Module discovery registry behavior beyond the thin catalog index
- Resolver or installer behavior
- Silent overwrite of Consumer ADRs/policies
- Autonomous Consumer repository restructuring
- Treating catalog presence as adoption

---

## 6. Draft, Active, and adopted — keep them distinct

| State | Who sets it | Means adopted? | Means installed? |
|-------|-------------|----------------|------------------|
| Module `status: draft` | AIOS Module metadata | No | No |
| Module `status: active` | AIOS Module metadata | No | No |
| Module `status: deprecated` | AIOS Module metadata | No | No |
| Consumer adopted Module guidance | Consumer ADR / local policy | **Yes** (Consumer-owned L3 within scope) | Still not an AIOS installer claim |

Critical distinctions:

- **Active ≠ adopted**
- **Draft ≠ installed**
- **Catalog entry ≠ mandatory**
- **Recommendation ≠ local policy**

Draft Modules must never be presented as stable, active, installed, or automatically adopted.

---

## 7. Precedence during Module-guided work

Unchanged L0–L7 model:

1. L0 constraints still win.
2. Current explicit user instructions (L1) govern the task within L0, without silently amending durable Consumer decisions.
3. Consumer ADRs (L2) and local policies (L3) outrank generic AIOS defaults and Module recommendations.
4. Unadopted Module guidance remains **L6**.
5. Explicitly adopted Pack guidance remains **L5** within adopted scope only.
6. External articles and examples remain **L7** reference only.

This example does not introduce new governance levels or change Framework Contract §7.

---

## 8. Practical documentation walkthrough

Illustrative Consumer conversation (not executable):

1. Agent reads Consumer repository and Core docs.
2. Agent notices architecture-boundary risk and recommends evaluating `architecture-engineering`.
3. Agent discloses that the Module and its Skill are currently `draft` / `experimental`.
4. Consumer owner decides either:
   - use the Skill text as temporary advice for this task only, or
   - record the adoption decision in a Consumer ADR (**L2**) or local policy (**L3**); explicitly adopted Module guidance then applies as Consumer-owned local policy at **L3** within the approved scope.
5. No installer runs. No Module package is “activated” by AIOS.

---

## 9. Boundaries preserved by this example

- Core / Module / Pack / Consumer boundaries remain intact.
- Framework Governance remains Core-owned.
- Consumer-approved architecture and product decisions remain **L2**; Consumer local engineering policies remain **L3**.
- Thin catalog index (`modules/README.md`) is not a registry, resolver, or installer.
- This example is documentation only.
