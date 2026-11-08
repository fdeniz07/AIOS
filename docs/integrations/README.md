# AIOS Coding Assistant Integrations

Status: Documentation guides (Phase 9)

These guides explain how a **Consumer** project can use AIOS documentation with major coding assistants.

They map AIOS artifacts onto **native platform instruction mechanisms**. They do not replace those platforms, invent platform features, or change AIOS governance.

Windsurf is explicitly outside the approved Phase 9 scope.

---

## Guides

| Platform | Guide |
|----------|--------|
| Cursor | [`CURSOR.md`](CURSOR.md) |
| GitHub Copilot | [`GITHUB_COPILOT.md`](GITHUB_COPILOT.md) |
| Claude Code | [`CLAUDE_CODE.md`](CLAUDE_CODE.md) |
| OpenAI Codex | [`OPENAI_CODEX.md`](OPENAI_CODEX.md) |

Each guide is independently understandable and follows the same structure:

1. Purpose and Scope
2. Platform Overview
3. AIOS Artifact Mapping
4. Recommended Project Structure
5. Manual Setup
6. Practical Usage Example
7. Limitations
8. Governance Boundaries
9. Official References

---

## Shared principles

- AIOS is repository-centered guidance, not a coding-assistant runtime.
- Platform configuration remains under **Consumer control**.
- Native platform features and AIOS conventions are distinct.
- Instruction precedence remains Framework Contract §7 / [`AGENTS.md`](../../AGENTS.md) §2 (**L0–L7**).
- These guides do not introduce new AIOS governance or precedence rules.
- Optional `aiosctl sync` still copies only `rules/*.md` → Consumer `.agents/` and does not install Modules or rewrite Consumer ADRs.

---

## Related AIOS references

| Document | Role |
|----------|------|
| [`FRAMEWORK_CONTRACT.md`](../FRAMEWORK_CONTRACT.md) | Authoritative architectural and governance contract |
| [`../../AGENTS.md`](../../AGENTS.md) | Agent operating manual |
| [`../../examples/README.md`](../../examples/README.md) | Adoption examples |
| [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md) | Contribution process |
