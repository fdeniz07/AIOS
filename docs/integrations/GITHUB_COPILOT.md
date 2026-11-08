# AIOS Integration — GitHub Copilot

Status: Documentation guide (Phase 9)

## 1. Purpose and Scope

Help a Consumer project use AIOS documentation with **GitHub Copilot** custom instructions.

In scope:

- Mapping AIOS artifacts to Copilot repository instruction files
- Manual Consumer-side setup
- Clear separation between Copilot-native features and AIOS conventions

Out of scope:

- Changing Copilot product behavior
- Claiming uniform support across every Copilot client/feature
- Automatic instruction generation by AIOS
- New AIOS governance layers

---

## 2. Platform Overview

GitHub documents several custom-instruction **types**. Support is **surface-specific**. Do not assume that a type available on one Copilot surface is available on another.

### Instruction types (platform catalog)

| Type | Native file / location | Notes |
|------|------------------------|--------|
| Personal instructions | GitHub.com personal settings, or client-local personal files where documented | Apply to the signed-in user |
| Repository-wide instructions | `.github/copilot-instructions.md` | Repository-scoped guidance |
| Path-specific instructions | `.github/instructions/**/*.instructions.md` | Frontmatter `applyTo` glob; not supported on every surface |
| Agent instructions | `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md` | Not supported on every surface |
| Organization instructions | Organization Copilot settings | Business/Enterprise; surface-limited as documented by GitHub |

### Support matrix by surface

Authoritative matrix: [Support for different types of custom instructions](https://docs.github.com/en/copilot/reference/custom-instructions-support).

Selected GitHub.com rows from that matrix:

| Copilot surface | Supported instruction types |
|-----------------|-----------------------------|
| **GitHub.com Copilot Chat** | Personal instructions; repository-wide instructions (`.github/copilot-instructions.md`); organization instructions |
| **GitHub.com Copilot cloud agent** | Repository-wide; path-specific; agent instructions (`AGENTS.md` / `CLAUDE.md` / `GEMINI.md`); organization instructions |
| **GitHub.com Copilot code review** | Repository-wide; path-specific; agent instructions (including `REVIEW.md` where documented); organization instructions |

Important: **GitHub.com Copilot Chat does not support path-specific instructions or agent instructions** according to the official support matrix. Those types may still exist for Cloud Agent, code review, IDE clients, or Copilot CLI — verify each surface separately.

Other environments (VS Code, Visual Studio, JetBrains, Eclipse, Xcode, Copilot CLI) have their own supported subsets in the same matrix. Always re-check the matrix for the Consumer’s client before relying on a file type.

### Precedence versus support (keep separate)

These are different questions:

| Question | What answers it | What it does **not** answer |
|----------|-----------------|-----------------------------|
| **Availability** — which instruction types a surface can load | Official [support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support) | Ordering among loaded instructions |
| **Precedence / ordering** — how loaded instructions are ranked when multiple apply | Custom-instructions [concept page](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions) (surface-dependent notes) | Whether an instruction type is supported on that surface |

**GitHub.com Copilot Chat availability** remains grounded only in the support matrix:

- Personal instructions
- Repository-wide instructions (`.github/copilot-instructions.md`)
- Organization instructions

Path-specific instructions and agent instructions (`AGENTS.md` / `CLAUDE.md` / `GEMINI.md`) are **not** listed as supported for GitHub.com Copilot Chat in that matrix. Their presence in repository files, or their appearance in a general precedence description, does **not** make them supported on that Chat surface.

**Official-source ambiguity on Chat precedence:** the concept page’s “Precedence of custom instructions” section for Copilot Chat on GitHub.com describes an order that includes path-specific instructions and agent instructions under “Repository custom instructions,” while the support matrix does **not** list those types for GitHub.com Copilot Chat. AIOS does **not** invent a reconciled definitive precedence order for GitHub.com Copilot Chat to paper over that inconsistency.

Practical guidance for Consumers:

1. Treat the **support matrix** as authoritative for which instruction types GitHub.com Copilot Chat can use.
2. Treat the concept page’s precedence text as GitHub’s general ordering note for that surface, but **do not** infer Chat support for path-specific or agent instructions from it.
3. For Cloud Agent, code review, IDE clients, and Copilot CLI, use the matrix row for that surface; do not reuse the GitHub.com Chat availability list.
4. Prefer non-conflicting instruction sets; GitHub also notes that many other clients combine applicable files without a single general precedence order.

Platform instruction loading does **not** redefine AIOS L0–L7 precedence.

---

## 3. AIOS Artifact Mapping

| AIOS artifact | Typical Copilot placement (Consumer-owned) | Distinction |
|---------------|---------------------------------------------|-------------|
| Framework Contract / Core operating guidance | Summarized or linked from `.github/copilot-instructions.md` and/or Consumer `AGENTS.md` | Copilot loads native instruction files; AIOS remains the governance source |
| AIOS Core `rules/*.md` | Optional sync into `.agents/`; optionally reflected in Copilot instructions | `.agents/` sync is AIOS-derived; `.github/copilot-instructions.md` is Copilot-native |
| Workflows / Skills / Methodologies | Linked from repository instructions when broadly relevant | Keep instructions short; prefer pointers over pasting large docs |
| Module guidance | Mention only after explicit Consumer evaluation; disclose lifecycle status | Not auto-adopted |

Do not confuse:

- Copilot **agent instruction files** (`AGENTS.md`, etc.)
- Copilot **custom agent definition files** under `.github/agents/` (specialized agent configs — a different GitHub feature)

---

## 4. Recommended Project Structure

Illustrative Consumer layout:

```text
consumer-repo/
├── AGENTS.md                              # Optional agent instructions (feature support varies)
├── docs/adr/                              # Consumer ADRs (L2)
├── .agents/                               # Optional: aiosctl sync destination
├── .github/
│   ├── copilot-instructions.md            # Repository-wide Copilot instructions
│   └── instructions/
│       └── backend.instructions.md        # Optional path-specific instructions
└── ...
```

---

## 5. Manual Setup

1. Decide Core adoption posture (see [`../../examples/01-core-adoption/README.md`](../../examples/01-core-adoption/README.md)).
2. Create `.github/copilot-instructions.md` with short, broadly applicable Consumer guidance.
3. Point to AIOS documents the Consumer actually maintains as references (clone, submodule, docs mirror, or URL — Consumer choice).
4. Add path-specific `.github/instructions/*.instructions.md` files only when needed, with `applyTo` frontmatter as documented by GitHub.
5. Optionally maintain `AGENTS.md` for agent surfaces that support it; verify feature support for your client.
6. Optionally sync AIOS rules into `.agents/` with `aiosctl sync`.
7. Review GitHub’s support matrix for your IDE / GitHub.com / code review / cloud agent surfaces.

Example repository-wide file (illustrative):

```markdown
# Project guidance for Copilot

- Product architecture decisions live in docs/adr/ and outrank generic defaults.
- Treat AIOS Framework Contract and AGENTS.md as framework references when linked by this repository.
- Prefer minimal, reversible changes.
- Do not adopt AIOS Modules automatically. Recommend Module guidance only with explicit status disclosure.
- Do not invent secrets, credentials, or unstated architectural facts.
```

Example path-specific frontmatter (GitHub-documented form):

```markdown
---
applyTo: "services/**/*.ts"
---

- Follow the service boundary conventions in docs/adr/.
- Prefer existing patterns in this directory over new abstractions.
```

---

## 6. Practical Usage Example

Scenario: Copilot Chat in a Consumer repository.

1. `.github/copilot-instructions.md` states Consumer ADR authority and AIOS reference posture.
2. A developer asks Copilot to implement a change.
3. Copilot receives applicable repository instructions for that surface/client.
4. Copilot follows Consumer conventions and may consult linked AIOS guidance.
5. Module recommendations, if any, remain advisory until recorded as Consumer policy.

GitHub notes that due to non-deterministic AI behavior, Copilot may not follow custom instructions identically every time. Treat instructions as guidance, not a hard enforcement engine.

---

## 7. Limitations

- Instruction type support differs by Copilot feature and client; use the official support matrix, not assumptions from another surface.
- On GitHub.com Copilot Chat, path-specific and agent instruction files are unsupported even if present in the repository.
- GitHub’s Chat precedence description and Chat support matrix are not fully consistent; AIOS does not invent a definitive Chat precedence order to reconcile them.
- Custom instructions do not guarantee policy compliance; keep CI and review gates.
- Organization instructions are not supported in all local client sessions.
- For pull-request review, GitHub documents that Copilot reads instructions from the **head** branch.

---

## 8. Governance Boundaries

- L0–L7 remain unchanged. Copilot instruction loading does not redefine AIOS precedence.
- Consumer-approved ADRs / product decisions remain **L2**; Consumer local policies remain **L3**.
- Copilot instruction files are Consumer-owned configuration.
- AIOS sync does not own Copilot configuration and does not adopt Modules.
- Draft Module packages must not be described as active/installed/adopted.

---

## 9. Official References

- Support matrix (which surfaces support which instruction types): https://docs.github.com/en/copilot/reference/custom-instructions-support
- Custom instructions concept (including precedence notes): https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions
- Adding repository custom instructions: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
- Customize Copilot overview: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-copilot-overview
- Copilot customization cheat sheet: https://docs.github.com/en/copilot/reference/customization-cheat-sheet

AIOS references:

- [`FRAMEWORK_CONTRACT.md`](../FRAMEWORK_CONTRACT.md)
- [`../../AGENTS.md`](../../AGENTS.md)
- [`README.md`](README.md)
