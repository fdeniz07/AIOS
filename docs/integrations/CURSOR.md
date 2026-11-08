# AIOS Integration — Cursor

Status: Documentation guide (Phase 9)

## 1. Purpose and Scope

Help a Consumer project use AIOS Core (and optionally Module) documentation with **Cursor** Agent instructions.

In scope:

- Mapping AIOS artifacts to Cursor Rules and `AGENTS.md`
- Manual Consumer-side setup
- Governance boundaries that remain Consumer-owned

Out of scope:

- Changing Cursor product behavior
- Automatic rule installation by AIOS
- Windsurf or other platforms
- New AIOS governance layers

---

## 2. Platform Overview

According to Cursor’s official Rules documentation, Cursor provides persistent instructions for Agent through:

| Mechanism | Native location / form | Notes |
|-----------|------------------------|--------|
| Project Rules | `.cursor/rules/*.mdc` | Version-controlled; frontmatter controls when a rule applies |
| User Rules | Cursor Customize → Rules (account / environment) | Global to the user’s Cursor environment |
| Team Rules | Cursor dashboard (Team / Enterprise) | Organization-managed; can be enforced |
| `AGENTS.md` | Repository root and nested directories | Plain markdown alternative to Project Rules |

Project Rules use `.mdc` files with frontmatter fields such as `description`, `globs`, and `alwaysApply`. Cursor documents that a plain `.md` file in `.cursor/rules` is ignored by the rules system because it lacks that frontmatter. Prefer `AGENTS.md` when you want plain markdown without rule metadata.

Cursor documents nested `AGENTS.md` support: subdirectory files apply when working with files in that directory or its children, with more specific instructions taking precedence.

Cursor also documents that Rules do **not** impact Cursor Tab or other non-Agent AI features.

---

## 3. AIOS Artifact Mapping

| AIOS artifact | Typical Cursor placement (Consumer-owned) | Distinction |
|---------------|---------------------------------------------|-------------|
| Framework Contract | Linked from Consumer `AGENTS.md` or a Project Rule; not copied as Cursor config | AIOS governance source |
| AIOS `AGENTS.md` (framework manual) | Referenced by Consumer instructions; Consumer may keep a shorter Consumer `AGENTS.md` | Do not silently replace Consumer ADRs |
| Core `rules/*.md` | Optional: sync to Consumer `.agents/` via `aiosctl sync`; optionally summarize into Project Rules / Consumer `AGENTS.md` | Sync destination `.agents/` is AIOS-derived; Cursor Project Rules are native Cursor config |
| Methodologies / Workflows / Skills | Linked from Consumer instructions when relevant | Remain L6 recommendations unless Consumer adopts them as L3 policy |
| Module README / Module Skills | Linked only after explicit evaluation; disclose `draft` status | Never auto-adopt |

Native Cursor functionality decides **how** instructions are loaded into Agent context. AIOS decides **what** framework guidance means under L0–L7.

---

## 4. Recommended Project Structure

Illustrative Consumer layout (Consumer chooses what to create):

```text
consumer-repo/
├── AGENTS.md                 # Consumer-owned agent instructions (Cursor-native)
├── docs/
│   └── adr/                  # Consumer ADRs (L2)
├── .agents/                  # Optional: aiosctl sync destination (AIOS-derived)
├── .cursor/
│   └── rules/
│       └── aios-core.mdc     # Optional: Cursor Project Rule pointing to AIOS guidance
└── ...
```

Keep durable product decisions in Consumer ADRs / local policy, not only inside Cursor rule text.

---

## 5. Manual Setup

1. Decide Core adoption posture (see [`../../examples/01-core-adoption/README.md`](../../examples/01-core-adoption/README.md)).
2. Create or update Consumer `AGENTS.md` with project norms and explicit pointers to AIOS documents you want agents to consult.
3. Optionally create `.cursor/rules/*.mdc` when you need Cursor-native activation control (`alwaysApply`, `globs`, or description-based inclusion).
4. Optionally run `aiosctl sync` if you want AIOS `rules/*.md` copied into `.agents/`.
5. Do **not** treat synced `.agents/` files as Consumer ADRs.
6. Commit Consumer-owned instruction files so the team shares them.

Example Project Rule frontmatter pattern documented by Cursor:

```markdown
---
description: AIOS Core operating defaults for this repository
alwaysApply: false
---

When working in this repository:

- Treat docs/FRAMEWORK_CONTRACT.md (AIOS reference) and this repo's ADRs as authority inputs.
- Follow this repository's AGENTS.md and approved ADRs over generic recommendations.
- Do not adopt Modules automatically; recommend only with disclosure of Module status.
```

Paths inside the rule body should point to locations that exist in the Consumer repository or to an explicit AIOS checkout/reference the Consumer maintains.

---

## 6. Practical Usage Example

Scenario: a Consumer uses Cursor Agent for a feature change.

1. Consumer `AGENTS.md` states that architecture decisions live in `docs/adr/` and that AIOS Core is reference guidance.
2. Developer asks Cursor Agent to implement a change.
3. Agent reads Consumer `AGENTS.md` / applicable Project Rules.
4. Agent consults linked AIOS Core docs when relevant.
5. If Module guidance seems useful, Agent recommends it as L6 advice and discloses draft/experimental status when applicable.
6. Durable adoption still requires an explicit Consumer decision recorded in an ADR or local policy.

No AIOS runtime executes. Cursor loads instructions through its own Rules / `AGENTS.md` mechanisms.

---

## 7. Limitations

- Cursor Rules apply to Agent context as documented by Cursor; they are not a substitute for CI, linters, or legal/security controls.
- Rules do not affect Cursor Tab (per Cursor docs).
- Plain `.md` files under `.cursor/rules` are ignored by Cursor’s rules system.
- AIOS validation success does not prove Cursor setup quality or Consumer adoption quality.
- Team Rules require Cursor Team/Enterprise capabilities as documented by Cursor.

---

## 8. Governance Boundaries

- L0–L7 remain unchanged.
- Consumer ADRs (L2) and local policies (L3) outrank generic AIOS defaults.
- Cursor configuration is Consumer-controlled.
- AIOS must not silently overwrite Consumer decisions through Cursor rules.
- Module recommendations remain optional; draft Modules are not stable/installed/adopted by presence alone.

---

## 9. Official References

- Cursor Rules: https://cursor.com/docs/rules
- Cursor Help — Rules: https://cursor.com/help/customization/rules
- Cursor Learn — Customizing agents: https://cursor.com/learn/customizing-agents

AIOS references:

- [`FRAMEWORK_CONTRACT.md`](../FRAMEWORK_CONTRACT.md)
- [`../../AGENTS.md`](../../AGENTS.md)
- [`README.md`](README.md)
