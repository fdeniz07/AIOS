# Security Policy

## Supported Versions

Security fixes are accepted against the default branch of this repository (`main`).

Because AIOS is primarily a documentation and governance framework with a small Python helper CLI, please indicate the commit hash or release tag when reporting an issue.

---

## What to Report

Please report vulnerabilities that affect:

- `scripts/aiosctl.py` or future CLI commands
- CI configuration that could leak secrets
- Instructions that would cause adopters to commit credentials or disable essential safeguards
- Any path traversal, unsafe file write, or unexpected overwrite behavior in tooling

Please **do not** file public issues for active vulnerability reports when private disclosure is safer.

---

## What Is Out of Scope

- Security posture of third-party coding assistants or LLM providers
- Vulnerabilities only present in unrelated consumer repositories
- Theoretical issues in empty placeholder directories with no executable code

---

## How to Report

Use GitHub's private vulnerability reporting for this repository if enabled:

**Repository → Security → Advisories / Report a vulnerability**

If private reporting is unavailable, open a minimal GitHub Issue titled `Security report request` **without** exploitable detail and ask maintainers for a secure channel.

Do not include secrets, tokens or personal data in public issues.

---

## Maintainer Response

Maintainers will try to acknowledge valid reports and work on a fix or guidance update.

Response times are best-effort for this volunteer-maintained project.

---

## Safe Adoption Guidance

When using AIOS in your own repositories:

- Never commit API keys, passwords or private certificates
- Review AI-generated changes before merging
- Treat `aiosctl sync` as a file-copy helper; inspect `.agents/` outputs
- Keep consumer secrets out of synced rule files
