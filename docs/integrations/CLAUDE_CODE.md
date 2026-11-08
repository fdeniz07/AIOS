# AIOS Integration — Claude Code

Status: Documentation guide (Phase 9)

## 1. Purpose and Scope

Help a Consumer project use AIOS documentation with **Claude Code** project memory / instruction files.

In scope:

- Mapping AIOS artifacts to `CLAUDE.md`, optional `AGENTS.md`, and related Claude Code instruction locations
- Manual Consumer-side setup
- Distinguishing Claude Code-native memory from AIOS governance

Out of scope:

- Changing Claude Code product behavior
- Implementing Claude Code plugins or hooks for AIOS
- Automatic Consumer modification by AIOS
- New AIOS governance layers

---

## 2. Platform Overview

According to Anthropic’s Claude Code documentation (“How Claude remembers your project”):

| Mechanism | Native location | Notes |
|-----------|-----------------|--------|
| Project instructions | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team-shared project instructions; commonly committed |
| Local project preferences | `./CLAUDE.local.md` | Personal project preferences; typically gitignored |
| User instructions | `~/.claude/CLAUDE.md` | Personal preferences across projects |
| Managed policy | OS-specific managed path (IT/DevOps) | Organization-wide instructions |
| `AGENTS.md` | Repository `AGENTS.md` / `.claude/AGENTS.md` | Native discovery from Claude Code **v2.1.277+**; default loading is **not** automatic when project `CLAUDE.md` / `CLAUDE.local.md` is present (see below) |
| Topic-scoped rules | `.claude/rules/` | Path/topic-scoped instruction files under the Claude directory model |
| Auto memory | Claude-managed notes | Separate from human-authored `CLAUDE.md`; Claude writes learnings from corrections |

Claude Code treats these files as context, not as an enforced configuration runtime. Anthropic documents that hard blocks should use mechanisms such as PreToolUse hooks when an action must be denied regardless of model judgment.

Project `CLAUDE.md` / `.claude/CLAUDE.md` is the primary Consumer-shared instruction surface for Claude Code.

### `CLAUDE.md` and `AGENTS.md` discovery

Official Claude Code memory documentation distinguishes native `AGENTS.md` support from opt-in combined loading. Do **not** assume both files are always loaded together.

**Version requirement:** Reading `AGENTS.md` directly requires Claude Code **v2.1.277 or later**.

**Default behavior** (`Project instructions` = `claude-md-or-agents-md`):

| Project instruction files present | What Claude Code loads by default |
|-----------------------------------|-----------------------------------|
| `AGENTS.md`, and no `CLAUDE.md` / `.claude/CLAUDE.md` / `CLAUDE.local.md` in the working directory or above it | Native `AGENTS.md` discovery |
| `AGENTS.md` **and** a `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` in that directory chain | `CLAUDE.md` files only — `AGENTS.md` is **not** automatically loaded |
| A `CLAUDE.md` that imports `AGENTS.md` (for example `@AGENTS.md`) | `CLAUDE.md`, with `AGENTS.md` included through the import |

Notes from the same official docs:

- User `~/.claude/CLAUDE.md`, organization managed `CLAUDE.md`, and `.claude/rules/` files do **not** by themselves block native `AGENTS.md` discovery.
- Adding `CLAUDE.local.md` in a project that relies on `AGENTS.md` stops default native `AGENTS.md` loading unless combined loading is enabled or the file is imported.

**Opt-in combined loading** is a separate feature from native `AGENTS.md` discovery. Combined loading uses Project instructions mode `claude-md-and-agents-md` (via `/config`, or via user/managed `pluginConfigs`). That mode loads `CLAUDE.md` and `AGENTS.md` together; an `AGENTS.md` already imported or symlinked from `CLAUDE.md` is not loaded a second time. Claude Code documents that this plugin option is read from user/managed settings (not from project/local settings files).

**Built-in plugin identifier compatibility** (official memory docs):

| Claude Code version | Plugin ID for `pluginConfigs` | Behavior documented by Anthropic |
|---------------------|-------------------------------|----------------------------------|
| **v2.1.277+** | Native `AGENTS.md` discovery available | Distinct from combined-loading settings |
| **Before v2.1.285** | `agents-md@builtin` | Current ID `cc-plugin-agents-md@builtin` is **ignored** |
| **Current docs example** | `cc-plugin-agents-md@builtin` | Documented identifier for the built-in AGENTS.md plugin |
| **v2.1.285 and later** | Either ID | Reads an entry under `cc-plugin-agents-md@builtin` **or** `agents-md@builtin` |

Current-documentation example (`v2.1.285+` preferred key):

```json
{
  "pluginConfigs": {
    "cc-plugin-agents-md@builtin": {
      "options": { "instructionFiles": "claude-md-and-agents-md" }
    }
  }
}
```

If a settings file must also be read by Claude Code **before v2.1.285**, use the older identifier instead (or in addition, when sharing one file across mixed versions):

```json
{
  "pluginConfigs": {
    "agents-md@builtin": {
      "options": { "instructionFiles": "claude-md-and-agents-md" }
    }
  }
}
```

Do not treat native discovery (default `claude-md-or-agents-md` when no project `CLAUDE.md` is present) as the same feature as combined `CLAUDE.md` + `AGENTS.md` loading (`claude-md-and-agents-md`).

**Import alternative:** a `CLAUDE.md` may explicitly include shared guidance with `@AGENTS.md`. This remains useful when a project keeps both files, when Project instructions is set to `claude-md`, or when a session cannot load `AGENTS.md` directly.

Without a relevant `CLAUDE.md` / `.claude/CLAUDE.md` / `CLAUDE.local.md` in the applicable directory chain, native `AGENTS.md` discovery applies under the default setting.

---

## 3. AIOS Artifact Mapping

| AIOS artifact | Typical Claude Code placement (Consumer-owned) | Distinction |
|---------------|--------------------------------------------------|-------------|
| Framework Contract | Linked from Consumer `CLAUDE.md` / `AGENTS.md` | AIOS contract remains authoritative for AIOS meaning |
| AIOS `AGENTS.md` | Referenced from Consumer `CLAUDE.md` and/or Consumer `AGENTS.md` according to the discovery rules above | Consumer file is local operating policy text; AIOS file is framework manual |
| Core rules / methodologies / workflows | Linked when relevant; optionally mirrored as concise bullets in `CLAUDE.md` | Keep Claude instruction files concise |
| Optional synced `.agents/` | May be referenced after `aiosctl sync` | Sync is AIOS-derived; Claude instruction files are Claude-native |
| Module guidance | Linked only after evaluation; disclose draft/experimental status | Recommendation only until Consumer adopts to L3 |

Auto memory is a Claude Code feature. It is not an AIOS Module adoption mechanism and must not silently become a substitute for Consumer ADRs.

---

## 4. Recommended Project Structure

Illustrative Consumer layout:

```text
consumer-repo/
├── CLAUDE.md                 # Shared Claude Code project instructions
├── AGENTS.md                 # Optional cross-tool guidance; native load depends on CLAUDE.md presence / settings
├── CLAUDE.local.md           # Optional personal preferences (gitignore); counts as CLAUDE.md for default AGENTS.md discovery
├── docs/adr/                 # Consumer ADRs (L2)
├── .agents/                  # Optional: aiosctl sync destination
├── .claude/
│   ├── CLAUDE.md             # Alternative project instructions location
│   └── rules/                # Optional topic-scoped rules
└── ...
```

Prefer one clear project instruction entry point for the team (`CLAUDE.md` or `.claude/CLAUDE.md`) and avoid duplicated conflicting rule sets.

---

## 5. Manual Setup

1. Decide Core adoption posture (see [`../../examples/01-core-adoption/README.md`](../../examples/01-core-adoption/README.md)).
2. Create `CLAUDE.md` (or `.claude/CLAUDE.md`) with concise build/test commands, architecture pointers, and review expectations.
3. Add explicit references to AIOS Framework Contract / Consumer ADRs.
4. Add `CLAUDE.local.md` only for personal machine-specific preferences; keep it out of git if it contains local-only data.
5. Optionally maintain `AGENTS.md` for cross-tool guidance. Remember the default: if `CLAUDE.md` or `CLAUDE.local.md` exists in the applicable directory chain, Claude Code does **not** automatically load `AGENTS.md` unless you enable `claude-md-and-agents-md` or import it (for example `@AGENTS.md`).
6. Optionally sync AIOS `rules/*.md` into `.agents/`.
7. Use `/init` only as a Claude Code convenience to draft `CLAUDE.md`; review the result before treating it as Consumer policy.

Illustrative `CLAUDE.md` excerpt (with explicit `AGENTS.md` import):

```markdown
@AGENTS.md

# Project instructions

- Architecture decisions live in docs/adr/ (authoritative for product choices).
- AIOS Framework Contract is the framework reference for engineering process boundaries.
- Prefer minimal, reversible changes.
- Do not adopt AIOS Modules automatically.
- If recommending a Module, disclose metadata status (draft/active/deprecated) and maturity.
```

---

## 6. Practical Usage Example

Scenario: a developer starts Claude Code in a Consumer repository.

1. Claude Code loads project instruction files according to the discovery rules above (default: `CLAUDE.md` wins over automatic `AGENTS.md` when both would otherwise compete).
2. The developer requests a change.
3. Claude Code follows Consumer instructions, respects ADR pointers, and may consult linked AIOS docs.
4. If Module guidance appears relevant, Claude Code can recommend it with status disclosure.
5. Durable adoption is recorded only by the Consumer owner in a Consumer ADR (**L2**) or local policy (**L3**).

Claude Code context loading is not AIOS automatic adoption.

---

## 7. Limitations

- Instruction files are context, not hard enforcement; use Claude Code hooks/policy controls when denial must be guaranteed.
- Default Project instructions do not load `CLAUDE.md` and `AGENTS.md` together; combined loading is opt-in (`claude-md-and-agents-md`).
- Native `AGENTS.md` discovery requires Claude Code v2.1.277+; some sessions may still need an `@AGENTS.md` import from `CLAUDE.md`.
- Combined-loading settings keys differ by version: use `agents-md@builtin` before v2.1.285; current docs use `cc-plugin-agents-md@builtin`; v2.1.285+ accepts either ID.
- Auto memory is separate from authored project instructions and can drift from formal ADRs if unchecked.
- Large instruction files reduce consistency; Anthropic recommends concise instructions.
- AIOS does not manage `~/.claude` user settings or managed enterprise policy files.

---

## 8. Governance Boundaries

- L0–L7 remain unchanged.
- Consumer ADRs (L2) and local policies (L3) remain durable authority for product decisions.
- Claude Code configuration remains Consumer-controlled.
- AIOS must not treat Claude auto memory as Module adoption or ADR replacement.
- Draft Modules remain non-stable, non-installed, non-adopted by default.

---

## 9. Official References

- How Claude remembers your project (includes `AGENTS.md` discovery, Project instructions modes, and `@AGENTS.md` imports): https://code.claude.com/docs/en/memory
- Explore the `.claude` directory: https://code.claude.com/docs/en/claude-directory
- Claude Code best practices: https://www.anthropic.com/research/claude-code-best-practices
- Glossary (`CLAUDE.md`): https://code.claude.com/docs/en/glossary

AIOS references:

- [`FRAMEWORK_CONTRACT.md`](../FRAMEWORK_CONTRACT.md)
- [`../../AGENTS.md`](../../AGENTS.md)
- [`README.md`](README.md)
