# AIOS Integration — OpenAI Codex

Status: Documentation guide (Phase 9)

## 1. Purpose and Scope

Help a Consumer project use AIOS documentation with **OpenAI Codex** project guidance via `AGENTS.md`.

In scope:

- Mapping AIOS artifacts to Codex `AGENTS.md` discovery
- Manual Consumer-side setup
- Distinguishing Codex-native instruction discovery from AIOS governance

Out of scope:

- Changing Codex product behavior
- Inventing Codex configuration keys beyond documented options
- Automatic adoption/installation by AIOS
- New AIOS governance layers

---

## 2. Platform Overview

According to OpenAI’s Codex documentation for `AGENTS.md` (ChatGPT Learn — Custom instructions with AGENTS.md):

Codex reads `AGENTS.md` guidance before doing work and builds an instruction chain once per run (in the TUI, typically once per launched session).

Discovery order (as documented):

1. **Global scope** — under Codex home (default `~/.codex`, overridable with `CODEX_HOME`):
   - Prefer `AGENTS.override.md` if present and non-empty
   - Otherwise `AGENTS.md`
   - Only one non-empty global file is used at this level
2. **Project scope** — from project root (typically Git root) down to the current working directory:
   - In each directory: `AGENTS.override.md`, then `AGENTS.md`, then any configured `project_doc_fallback_filenames`
   - At most one file per directory
3. **Merge order** — concatenate root → leaf; files closer to the working directory override earlier guidance because they appear later

Additional documented behaviors:

- Empty files are skipped.
- Combined size stops at `project_doc_max_bytes` (default **32 KiB**).
- Fallback filenames and size limits can be configured in Codex config (for example `~/.codex/config.toml`).
- Nested overrides should be placed close to specialized work.

OpenAI’s broader customization docs also treat `AGENTS.md` as persistent project guidance that travels with the repository.

---

## 3. AIOS Artifact Mapping

| AIOS artifact | Typical Codex placement (Consumer-owned) | Distinction |
|---------------|------------------------------------------|-------------|
| Framework Contract | Linked from Consumer root `AGENTS.md` | AIOS remains the contract authority |
| AIOS framework `AGENTS.md` | Referenced by Consumer guidance; do not blindly overwrite Consumer product policy with framework prose | Framework manual vs Consumer operating file |
| Core methodologies / workflows / skills | Linked when relevant; keep root `AGENTS.md` concise because of size limits | L6 recommendations unless adopted |
| Optional `.agents/` sync output | May be referenced after `aiosctl sync` | Sync is AIOS-derived; Codex reads `AGENTS.md` / overrides natively |
| Module guidance | Nested or linked only after evaluation; disclose lifecycle status | Not installed/adopted by Codex discovery |

Note: AIOS also uses a root file named `AGENTS.md` inside the AIOS framework repository. In a Consumer repository, `AGENTS.md` is **Consumer-owned** Codex/project guidance unless the Consumer explicitly chooses to vendor framework text.

---

## 4. Recommended Project Structure

Illustrative Consumer layout:

```text
consumer-repo/
├── AGENTS.md                      # Primary Codex project guidance
├── services/
│   └── payments/
│       └── AGENTS.override.md     # Optional nested override
├── docs/adr/                      # Consumer ADRs (L2)
├── .agents/                       # Optional: aiosctl sync destination
└── ...
```

Global personal defaults (outside the repo) may live under `~/.codex/AGENTS.md` as documented by OpenAI. Keep team-shared rules in the repository.

---

## 5. Manual Setup

1. Decide Core adoption posture (see [`../../examples/01-core-adoption/README.md`](../../examples/01-core-adoption/README.md)).
2. Create Consumer root `AGENTS.md` with concise repository expectations.
3. Link AIOS Framework Contract and Consumer ADR locations.
4. Add nested `AGENTS.md` or `AGENTS.override.md` only where directory-specific rules are required.
5. Keep the combined instruction size within Codex’s documented byte budget, or raise `project_doc_max_bytes` deliberately in Codex config.
6. Optionally sync AIOS rules into `.agents/`.
7. Verify loaded sources with Codex (OpenAI documents prompts such as summarizing current instructions).

Illustrative Consumer root `AGENTS.md`:

```markdown
# AGENTS.md

## Repository expectations

- Product ADRs in docs/adr/ are authoritative for durable architecture decisions.
- AIOS Framework Contract is the reference for AIOS boundaries and L0–L7 precedence.
- Prefer minimal, reversible changes.
- Do not adopt AIOS Modules automatically.
- When recommending a Module, disclose status/maturity from module.yaml and README.
```

Optional Codex config knobs (documented by OpenAI; Consumer-controlled):

```toml
# ~/.codex/config.toml (illustrative)
project_doc_fallback_filenames = ["TEAM_GUIDE.md"]
project_doc_max_bytes = 65536
```

Only use fallback filenames when the Consumer intentionally relies on alternate instruction file names. AIOS does not require them.

---

## 6. Practical Usage Example

Scenario: Codex runs from a Consumer service directory.

1. Codex loads global guidance (if any), then repository root `AGENTS.md`, then any nested override down to CWD.
2. The developer asks Codex to implement a change in that service.
3. Codex follows merged guidance, with nested overrides taking effect later in the chain.
4. AIOS Module text, if referenced, remains advisory until Consumer adoption is recorded.
5. No AIOS installer or resolver runs as part of Codex instruction discovery.

---

## 7. Limitations

- Combined guidance is subject to `project_doc_max_bytes` truncation.
- Empty instruction files are ignored.
- An `AGENTS.override.md` replaces the regular `AGENTS.md` in the same directory for discovery.
- Codex customization layers (memories, skills, MCP, subagents) are separate from AIOS Modules/Packs; do not equate them.
- AIOS validation does not verify Codex profile configuration.

---

## 8. Governance Boundaries

- L0–L7 remain unchanged.
- Consumer ADRs/local policies remain durable product authority.
- Codex `AGENTS.md` files are Consumer-controlled configuration (plus optional personal global files).
- AIOS must not treat Codex discovery as Module installation or automatic adoption.
- Draft Modules remain non-stable, non-installed, and non-adopted by default.

---

## 9. Official References

- Custom instructions with AGENTS.md: https://learn.chatgpt.com/docs/agent-configuration/agents-md
- Codex customization overview: https://learn.chatgpt.com/docs/customization/overview
- Codex prompting guide (AGENTS.md discovery notes): https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
- Open `AGENTS.md` format site: https://agents.md/

AIOS references:

- [`FRAMEWORK_CONTRACT.md`](../FRAMEWORK_CONTRACT.md)
- [`../../AGENTS.md`](../../AGENTS.md)
- [`README.md`](README.md)
