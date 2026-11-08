# Example 01 — Core Adoption

Status: Documentation example only

This example explains how a **Consumer** project uses AIOS **Core** documentation and governance.

It does **not** implement a Consumer application, sync automation beyond the existing `aiosctl sync` contract, or any automatic decision system.

---

## 1. Purpose

Show a documentation-only adoption path where:

- AIOS Core provides reusable operating and governance guidance
- the Consumer retains ownership of product decisions
- agents follow documented precedence instead of improvising a hierarchy
- guidance remains distinct from automatic execution

---

## 2. Core documents in a Consumer context

A Consumer typically starts with these AIOS Core entry points:

| AIOS artifact | Consumer use |
|---------------|--------------|
| [`docs/FRAMEWORK_CONTRACT.md`](../../docs/FRAMEWORK_CONTRACT.md) | Authoritative boundaries, ownership, consumption models, and L0–L7 precedence |
| [`AGENTS.md`](../../AGENTS.md) | Day-to-day agent operating manual that **operationalizes** the Contract |
| [`methodology/`](../../methodology/) | Engineering methods (typically **L6** recommendations unless explicitly adopted) |
| [`rules/`](../../rules/) | Syncable Core governance markdown (source for optional `aiosctl sync`) |
| [`workflows/`](../../workflows/), [`checklists/`](../../checklists/), [`skills/`](../../skills/) | Optional Core process artifacts (recommendations by default) |

The Consumer may:

1. **Reference-only** — read AIOS docs without copying managed files
2. **Synced** — copy `rules/*.md` into Consumer `.agents/` via `aiosctl sync`
3. **Hybrid** — combine reference-only guidance with synced rule copies

Sync writes only to designated generated paths. Sync does **not** transfer ownership of Consumer ADRs or product decisions.

---

## 3. Framework Contract and AGENTS.md

These two documents are complementary, not competing authorities:

| Document | Role |
|----------|------|
| Framework Contract | Architectural meta-document: boundaries, ownership, consumption, L0–L7 |
| `AGENTS.md` | Operating manual for agents: how to behave under that contract |

Practical rule:

- Use the Contract to decide **what belongs where** and **which instruction wins**.
- Use `AGENTS.md` to decide **how an agent should work day to day**.
- If they appear inconsistent, **do not invent a new hierarchy**. Report the conflict and request clarification.

Canonical precedence: Framework Contract §7, operationalized in `AGENTS.md` §2.

```text
L0 Non-overridable constraints
L1 Explicit user instructions (current task)
L2 Consumer-approved ADRs / product decisions
L3 Consumer local policies
L4 AIOS Core binding operating / governance defaults
L5 Explicitly adopted Pack guidance
L6 Module / methodology recommendations
L7 External knowledge (reference only)
```

Higher applicable levels take precedence over lower ones.

---

## 4. Consumer-owned decisions and responsibilities

The Consumer remains the owner of:

- Product requirements and decisions
- Approved ADRs and architecture choices
- Implementation and runtime systems
- Local engineering policies
- Roadmaps and project-specific artifacts
- Whether to sync `.agents/` and whether to keep syncing

AIOS provides the **framework**, not Consumer content.

Consumer responsibilities in this example:

1. Decide the consumption model (reference-only, synced, or hybrid).
2. Keep durable decisions in Consumer-owned artifacts.
3. Disclose conflicts between a current task request and durable ADRs/policies.
4. Approve durable changes explicitly; do not allow silent overwrite.
5. Treat Core methodologies and process artifacts as recommendations until explicitly adopted into local policy.

---

## 5. Role of Consumer ADRs

Consumer ADRs sit at **L2**.

They outrank generic AIOS defaults (**L4**) and recommendations (**L6**).

Typical ADR topics for Core adoption:

- Whether AIOS is adopted at all
- Reference-only vs synced vs hybrid posture
- Which Core workflows/checklists/skills are treated as binding local policy (**L3**) after explicit adoption
- What remains recommendation-only

Example Consumer ADR posture (illustrative wording only):

> We adopt AIOS Core as reference guidance. Synced `.agents/` files are treated as AIOS-derived operating defaults (L4 source material). Product architecture decisions remain in our ADRs (L2). RDIV and Architecture First remain recommendations (L6) unless a later ADR adopts them as local policy (L3).

This example does **not** create or store a real Consumer ADR inside AIOS.

---

## 6. Guidance versus automatic execution

| AIOS provides | AIOS does not provide in this example |
|---------------|----------------------------------------|
| Documentation and operating defaults | Automatic product decisions |
| Recommended workflows and methods | Autonomous repository restructuring |
| Optional rule sync into `.agents/` | Automatic ADR creation or ADR overwrite |
| Precedence vocabulary (L0–L7) | A runtime that “applies” Core without humans |

Agents may **recommend** following Core guidance. Durable Consumer changes still require applicable human / Consumer-owner approval under existing gates (`AGENTS.md` §8).

Validation success (when used later) checks structural or documentation integrity. It is **not** proof of architectural correctness, content quality, or successful Consumer adoption.

---

## 7. Minimal adoption sequence (manual)

1. Read Framework Contract §3–§9 and `AGENTS.md` §2.
2. Choose a consumption model.
3. Optionally run `aiosctl sync` only if synced rules are desired.
4. Point coding assistants at Consumer-owned instructions that reference AIOS Core (see [`docs/integrations/`](../../docs/integrations/README.md)).
5. Record durable decisions in Consumer ADRs / local policy.
6. Keep Modules and Packs out of scope until explicitly needed.

No automatic adoption occurs at any step.

---

## 8. Boundaries preserved by this example

- Core remains usable without Modules or Packs.
- Consumer ownership is unchanged.
- L0–L7 precedence is unchanged.
- `aiosctl sync` remains the existing rules-copy contract only.
- This example is documentation, not an executable demonstration.
