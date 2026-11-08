# Phase 8.3 — Module Contract Validation Design

**Status:** Accepted Phase 8.3 design (D1–D12); subsequently implemented

**Authority:** Design document. Derived from approved Module contracts, the Phase 8.3 Discovery & Contract Mapping report (observations), Phase 8.1.2 Shared Validation Foundation, Phase 8.2 Framework Structure Validation architecture, and explicit PO decisions recorded in §15.

**Depends on:**

- [`MODULE_METADATA.md`](MODULE_METADATA.md) (metadata v1 field model)
- [`MODULE_VALIDATION.md`](MODULE_VALIDATION.md) (validation strategy expectations)
- [`MODULE_LIFECYCLE.md`](MODULE_LIFECYCLE.md) (lifecycle governance)
- [`FRAMEWORK_CONTRACT.md`](FRAMEWORK_CONTRACT.md) §5 / §7
- [`VALIDATION_FOUNDATION.md`](VALIDATION_FOUNDATION.md)
- [`FRAMEWORK_STRUCTURE_VALIDATION_DESIGN.md`](FRAMEWORK_STRUCTURE_VALIDATION_DESIGN.md)

**Implementation note (historical):** This document defined the accepted design rules prior to implementation. The Module Contract Validator was subsequently implemented. Documentation Integrity Validation and CI wiring were added in later Phase 8 work; Pack validation remains out of scope. The D1–D12 decisions below are unchanged.

**Terminology:** Prefer *Module package*, *Module candidate*, *module.yaml*, *catalog index*, *finding*, *execution failure*, *documented requirement*, *observation*, *design proposal*, and *PO-accepted* consistently.

**Legend used throughout:**

| Label | Meaning |
|-------|---------|
| **Documented** | Explicit rule in an approved Module/Framework document |
| **Observation** | Seen in the repository (Phase 8.3 discovery); not automatically normative |
| **PO-accepted** | Product Owner decision recorded in §15 |
| **Technical behavior** | Implementation technique (filesystem / parse split) that is not itself a Module Contract sentence |

---

## 1. Purpose, scope and non-goals

### Purpose

Define a **read-only Module Contract Validator** that checks Engineering Module packages under `modules/` against the approved Module metadata, lifecycle, and validation-strategy contracts, using the shared Phase 8.1.2 Finding model, orchestrator and reporter.

### In scope (design)

- Discovery of Module package candidates under `modules/` (strategy below)
- Structural presence checks for package entry points under documented and PO-accepted rules
- `module.yaml` parse and metadata-field validation per metadata v1
- Lifecycle-aware checks where already documented (`draft` / `active` / `deprecated`), without inferring lifecycle when metadata is absent or `status` is missing/invalid
- Deterministic findings, finding precedence (R8), and Phase 8.1.2 exit-code semantics
- Framework-root symlink containment (**PO-accepted D12**)
- Fixture-based test strategy for the future implementation phase
- Default CLI registration under `python -m validation` (**PO-accepted D10**)

### Explicit non-goals

- Implementing the validator, schemas, tests, or CI (implementation phase)
- Changing `MODULE_METADATA.md`, `MODULE_VALIDATION.md`, `MODULE_LIFECYCLE.md`, Framework Contract, MANIFEST, PROJECT_STRUCTURE, ROADMAP, or AGENTS.md
- Changing L0–L7 or Core / Module / Pack / Consumer authority
- Module installation, adoption, sync, resolution, or runtime execution
- Pack validation, Skill runner validation as a separate product, or documentation-link integrity (Phase 8.4)
- Making Framework-root `modules/` mandatory (Phase 8.2 keeps it **optional**)
- Catalog index synchronization against filesystem (**PO-accepted D9: out of scope for MVP**)
- Verifying that a `deprecation.successor` Module exists or resolving Module relationships
- Rejecting empty string items in `applies_when` / `avoid_when` solely for emptiness (**R10**)
- Correcting stale Framework Contract / MANIFEST wording about unpopulated Modules (separate documentation task)

---

## 2. Relationship to existing validation

### Shared foundation (Phase 8.1.2)

Reuse without forking:

- `Finding`, `Severity` (`ERROR` / `WARNING` / `INFO`), `ValidationResult`
- `aggregate_findings` with duplicate identity `(rule, path)`
- `Orchestrator` / `ValidatorSpec` / `ValidatorAbortError` for unreliable completion (exit 2)
- `format_report` and exit codes `0` / `1` / `2`

**Design:** Category string `module-contract` for Module findings.  
**Design:** Finding `code` and `rule` both use a stable `MOD-xxx` id (see §9).

### Framework Structure Validation (Phase 8.2)

| Concern | Phase 8.2 | Phase 8.3 (this design) |
|---------|-----------|-------------------------|
| Root `modules/` path | Optional; absence / wrong type → **no** structure finding | Does **not** make `modules/` required at Framework root |
| When `modules/` missing | Structure OK | Module validator discovers **zero** packages → no Module findings |
| When `modules/` wrong type | Structure ignores (optional) | Module validator emits **Error** (**PO-accepted D1**) |
| Symlink / FS errors | `STR-*` / PathKind model | Technical reference for inspection technique; Module codes are separate (`MOD-*`); containment is Module-specific (**D12**) |

Structure validation and Module validation are **independent registered validators**. Passing one does not imply the other.

---

## 3. Scope and responsibilities (A)

### What Module Contract Validation checks

1. Module package discovery under `modules/` (per §4).
2. Per-candidate `module.yaml` and `README.md` **filesystem and containment** inspections (§4 / §8) — **lifecycle-independent** (including missing/wrong-type/broken entry points, D12 out-of-root, and MOD-021 unreliable inspection). Status-dependent README **presence severity** (`MOD-002`) and deprecated Migration validation (`MOD-012`) apply **only** when Module `status` is known and valid (§6); they are not implied by every structural entry-point check.
3. `module.yaml` YAML parseability and metadata v1 field rules with deterministic finding precedence (§5, R8), when a usable parseable mapping exists.
4. Documented lifecycle constraints when `status` is known and valid (status/maturity enums; deprecated `## Migration`; `deprecation` object consistency) (§6). When status is **unknown**, do **not** apply `MOD-002` or `MOD-012`, and do **not** infer lifecycle.
5. Documented bans (`dependencies` key → Error; not also MOD-013) (§5, R8).
6. Unknown top-level metadata fields → Warning (**Documented:** `MODULE_METADATA.md` §7; `MODULE_VALIDATION.md` §4).
7. Directory name versus metadata `id` mismatch → Warning (**PO-accepted D3**), only when `id` is successfully read.
8. Out-of-root symlink rejection for `modules/`, candidates, `module.yaml`, and `README.md` (**PO-accepted D12**) — **lifecycle-independent**; always apply containment inspection for in-scope paths, including when status is unknown.

### What it does not check

- Consumer adoption / installation state
- Whether Module guidance is “architecturally correct”
- Pack composition or Pack manifests
- Content quality of README narrative (except documented mechanical headings such as `## Migration` when deprecated and README is readable)
- Skill *behavior*, Skill filename conventions, or `provides` ↔ Skill id hard matching
- `modules/README.md` catalog synchronization (**D9 out of scope**)
- Successor Module existence for `deprecation.successor`
- Empty-element rejection inside applicability lists (**R10**)
- Cross-repo sync / `aiosctl` behavior
- Framework Contract stale prose consistency (documentation task)
- Recursive inspection of unrelated Framework paths
- Reading external targets of out-of-root symlinks (**D12**)

### Discovery root

Module discovery is limited to the Framework root’s `modules/` directory (existing catalog location: `modules/README.md`, Phase 7 packaging).

**Documented (Framework Structure):** `modules/` is optional at Framework root (`FRAMEWORK_STRUCTURE_VALIDATION_DESIGN.md` §3).

**Behavior when `modules/` is absent:** treat as “no Module packages present”; emit no Module contract findings for packages; this validator contributes no ERROR solely due to absence of `modules/`.

---

## 4. Module discovery (B)

### Established vs design policy

| Topic | Status |
|-------|--------|
| Catalog lives under `modules/` | **Observation** + Phase 7 / `modules/README.md`; Framework Contract §5.2 illustrative layout |
| Every Module package is an immediate child directory of `modules/` | **Observation** (six packages); discovery **design** for MVP |
| Nested packages under `modules/foo/bar/` | **Not documented** as Modules — **not** discovered in MVP |
| Non-directory children under `modules/` | **PO-accepted D2** |
| Symlinked package directories | **PO-accepted D12** containment + in-root type acceptance |

### Discovery algorithm

1. Resolve Framework root (reuse Phase 8.2 root selection when running via default CLI; explicit `--root` remains Framework-root oriented). Use the **canonical Framework root** path for containment checks.
2. Inspect `modules` relative to that root using the filesystem model in §8.
3. If `modules` is **MISSING** → zero candidates; stop (no Module package findings).
4. If `modules` is **FILE** / **OTHER** / broken link → **Error** (**PO-accepted D1**; `MOD-019`).
5. If `modules` is a symlink resolving **outside** the Framework root → **Error** (`MOD-024`); do **not** inspect the external target (**D12**).
6. If `modules` inspection is unreliable (permission/I/O/resolution failure) → **MOD-021** + `execution_error` (exit 2). Do **not** use MOD-003 or MOD-024.
7. If `modules` is **DIRECTORY** (or in-root symlink→directory):
   - List **immediate** child names only (no recursive descent into nested trees).
   - Ignore the catalog index file `README.md` (not a Module package; not a D2 Warning).
   - Each immediate child that resolves to an **in-root directory** (or in-root symlink→directory) is a **Module candidate**.
   - Immediate child that is a file / wrong type / broken link (other than ignored `README.md`) → **Warning** (**PO-accepted D2**; `MOD-018`).
   - Immediate child symlink out-of-root → **Error** (`MOD-024`); not a candidate; do not read external target.
8. Do **not** treat `modules/README.md` itself as a Module package.
9. Do **not** validate catalog index rows against the filesystem (**D9 out of scope**).

### Candidate `module.yaml` entry-point handling — no lifecycle inference

A Module candidate is identified by filesystem discovery **before** metadata is read.

Inspect the candidate’s `module.yaml` path (§8). Classification:

| Filesystem observation | Finding | Lifecycle effect |
|------------------------|---------|------------------|
| **MISSING** | Warning `MOD-001` (**D4**) | Status **unknown** |
| **Wrong type** (directory / OTHER / not a regular file) | Warning `MOD-001` | Status **unknown** |
| **Broken symlink** | Warning `MOD-001` (same as missing/wrong-type entry point) | Status **unknown** |
| **Out-of-root symlink** (successfully resolved) | Error `MOD-024` (**D12**); **do not** read the external target | Status **unknown**; no metadata parse |
| **Unreliable inspection** (permission/I/O/resolution failure) | Error `MOD-021` + `execution_error` (exit 2) | Do **not** emit MOD-001 or MOD-003 |
| Regular file (or in-root symlink→file) | Proceed to YAML parse (§5.1) | Status from metadata when parse succeeds |

When `MOD-001` applies (missing or wrong-type / broken entry point), or when metadata is otherwise unusable for lifecycle:

- Status is **unknown**. The validator **must not** infer `draft`, `active`, or `deprecated` from the directory name, README text, catalog index, or any other artifact.
- Do **not** apply status-dependent README presence severity (`MOD-002`).
- Do **not** apply deprecated Migration validation (`MOD-012`).
- Stop metadata-field validation for that candidate when there is no usable parseable mapping.
- Directory-versus-`id` comparison (**D3**) **cannot** run without a readable `id`.
- **D12 still applies:** still inspect candidate `README.md` for symlink containment when that path is in scope. Successfully resolved out-of-root README → `MOD-024` (never read external target). Unreliable README inspection/resolution → `MOD-021` + exit 2. In-root acceptance and broken-symlink→wrong-type mapping remain as in §8, but wrong-type/missing/broken README do **not** produce `MOD-002` while status is unknown.

If `module.yaml` is a readable in-root regular file (or accepted in-root file symlink) but cannot be parsed as a mapping, see §5.1 / MOD-003 (parse/mapping only — not FS I/O). After MOD-003, status remains unknown; the same README lifecycle skip and D12-preserving rules apply.

---

## 5. Metadata validation matrix (C)

Sources: `MODULE_METADATA.md` §§3–7; `MODULE_VALIDATION.md` §§3–5; `MODULE_LIFECYCLE.md` §§1–5; PO decisions §15; precedence R8.

### 5.1 Presence and parse

| Check | Basis | Severity | Notes |
|-------|-------|----------|-------|
| `module.yaml` **missing** | **PO-accepted D4** | Warning (`MOD-001`) | Status unknown; no lifecycle inference |
| `module.yaml` **wrong type** or **broken symlink** | Entry-point FS policy (§4 / §8) | Warning (`MOD-001`) | Same as missing for lifecycle; not MOD-021 |
| `module.yaml` out-of-root symlink (resolved) | **PO-accepted D12** | Error (`MOD-024`) | Do not read external target; not MOD-001 |
| `module.yaml` FS inspection unreliable | **Technical behavior** / **R11** | Error + execution_error (`MOD-021`) | Not MOD-001 / MOD-003 / MOD-024 |
| YAML **parse** failure or root not a mapping | Mechanical metadata validation | Error (`MOD-003`) | Only after successful in-root file read; content/syntax/shape only |

### 5.2 Field validation precedence (R8)

For a **single field defect**, emit **exactly one** primary finding, in this order:

1. **Missing or empty** required field → `MOD-004` (severity: **D8** Warning only when `status` is explicitly and validly `draft`; otherwise **Error**, including when status is unknown — see §5.3 / §6).
2. Else **wrong field type** → `MOD-005`.
3. Else present, non-empty value with **invalid field-specific format** → field code:
   - `id` → `MOD-006`
   - `version` / `requires_core` → `MOD-007`
   - `status` → `MOD-008`
   - `maturity` → `MOD-009`

Metadata field validation (including `MOD-004`) runs **only** when `module.yaml` is a usable in-root regular file (or accepted in-root file symlink) that parses to a mapping. If `module.yaml` is missing, wrong-type, broken, out-of-root, unreadable (`MOD-021`), or unparseable (`MOD-003`), do **not** perform metadata field validation.

**Special cases:**

- `dependencies` key present → `MOD-010` **only**; do **not** also emit `MOD-013` for that key.
- Other unknown top-level keys → `MOD-013`.
- Non-kebab `tags` entries (correct list type) → `MOD-023` (not MOD-005).
- Invalid `deprecation.successor` format → `MOD-022`.
- Invalid `deprecation.sunset` format → `MOD-025`.

### 5.3 Field matrix

| Field | Req/Opt | Type | Constraints | Validation behavior | Severity | Source |
|-------|---------|------|-------------|---------------------|----------|--------|
| `status` | Required when metadata present | enum | Exactly `draft` \| `active` \| `deprecated` | Missing/empty → **Error** `MOD-004`; invalid enum → **Error** `MOD-008`; **never infer draft** | Error | Metadata §4; **PO-accepted D8 exception** |
| `id` | Required when metadata present | string | Lowercase English kebab-case; non-empty | Missing/empty → MOD-004; bad format → MOD-006 | Missing/empty → **Warning only** when `status` is explicitly and validly `draft` (**D8**); otherwise **Error** (including unknown status). Bad format → Error | Metadata §3.1, §7; D8 |
| `version` | Required when metadata present | string | SemVer | Missing/empty → MOD-004; bad SemVer → MOD-007 | Missing/empty → Warning only for valid `draft` (**D8**); otherwise Error (including unknown status). Bad SemVer → Error | Metadata §3.1; D8 |
| `title` | Required when metadata present | string | Non-empty | Missing/empty → MOD-004 | Missing/empty → Warning only for valid `draft` (**D8**); otherwise Error (including unknown status) | Metadata §3.1; D8 |
| `summary` | Required when metadata present | string | Non-empty | Missing/empty → MOD-004 | Missing/empty → Warning only for valid `draft` (**D8**); otherwise Error (including unknown status) | Metadata §3.1; D8 |
| `maturity` | Optional | enum | `experimental` \| `stable` when present | If present → enum (MOD-009 if invalid) | Error if present but invalid | Metadata §4; Validation §4 |
| `maturity` when `status: deprecated` | Optional omit preferred | — | “Should normally be omitted” | If present → Warning | Warning (`MOD-015`) | Metadata §4; Lifecycle §3; Validation §5 |
| `applies_when` | Optional | list of strings | Short hints | Missing → Warning; present → must be list of strings; **empty string elements allowed in MVP** | Warning if missing; Error if wrong type; **no** empty-element rule (**R10**) | Validation §3, §4; R10 |
| `avoid_when` | Optional | list of strings | Short hints | Same as `applies_when` | Same | Validation §3, §4; R10 |
| `tags` | Optional | list of strings | Lowercase kebab-case recommended | Wrong type → MOD-005; non-kebab item → MOD-023 | Error / Warning | Metadata §3.2, §7; **D5** |
| `provides` | Optional | list of strings | Coarse labels | If present → list of strings | Error if wrong type | Metadata §3.2 |
| `requires_core` | Optional | string | SemVer minimum | If present → SemVer (MOD-007) | Error if invalid format | Metadata §6; Validation §4 |
| `requires_core` vs Framework `VERSION` | Not required | — | Informational | **Out of scope** for MVP | — | Discovery; Metadata §6 |
| `deprecation` | Conditional object | object | Only when `status: deprecated` | See §5.4 | Error if present when not deprecated / wrong type | Metadata §5; Validation §4; **R9** |
| `deprecation.reason` | Recommended when deprecated | string | Short rationale | Missing when object present → Warning | Warning (`MOD-016`) | Metadata §5; R9 |
| `deprecation.successor` | Optional | string | Module `id` format if present | Invalid format → Warning; no existence check | Warning (`MOD-022`) | Metadata §5; **D6** |
| `deprecation.sunset` | Optional | string | ISO `YYYY-MM-DD` if present | Invalid format → Error | Error (`MOD-025`) — **PO-accepted R10** (severity not explicit in source docs) | Metadata §5 shape; R10 |
| `dependencies` | **Forbidden** in v1 | — | Must not appear | Key present → MOD-010 only | Error | Metadata §3.3; Validation §4; R8 |
| Unknown top-level fields | Tolerated initially | — | Warn | MOD-013 per unknown key (except `dependencies`) | Warning | Metadata §7; Validation §4 |

### 5.4 Deprecation object — exact requirements (R9)

From `MODULE_METADATA.md` §5, `MODULE_LIFECYCLE.md` §5, `MODULE_VALIDATION.md` §4, and **R9**:

| Rule | Behavior |
|------|----------|
| `deprecation` only when `status: deprecated` | Object present when `draft`/`active` → Error (`MOD-011`) |
| **`status: deprecated` and `deprecation` object missing** | **No finding** for object absence alone (**R9**) |
| `reason` | Recommended; if object exists and `reason` missing → Warning (`MOD-016`); not Error |
| `successor` | Optional; invalid format → Warning (`MOD-022`); **no** existence check; **no** dependency resolution |
| `sunset` | Optional; invalid format → Error (`MOD-025`, **PO-accepted R10**) |
| README `## Migration` | See §6 / R7 — only when README exists and is readable |

**Do not invent:** mandatory `deprecation` object, mandatory `reason`, mandatory `successor`, or successor existence.

### 5.5 Type checking notes

- Lists must be YAML sequences; scalars where lists expected → Error (`MOD-005`).
- Enum comparisons are exact string match (case-sensitive).
- Do not invent additional status/maturity values (`MODULE_LIFECYCLE.md` §1).
- Empty string items in `applies_when` / `avoid_when` are **not** rejected in MVP (**R10**).

---

## 6. Lifecycle-aware validation (D)

### Status values (**Documented**)

| Status | Documented expectations relevant to validation |
|--------|------------------------------------------------|
| `draft` | May be incomplete; incompleteness not Error by default (`MODULE_LIFECYCLE.md` §1.1; `MODULE_VALIDATION.md` §3), refined by **D8** for metadata fields |
| `active` | Requires usable entry: `module.yaml`, `README.md`, five required metadata fields valid (`MODULE_VALIDATION.md` §3) |
| `deprecated` | Require README section with **exact** heading `## Migration` when README is present/readable (Error); maturity normally omitted (Warning if present); `deprecation` object optional to omit (**R9**) |

### Maturity values (**Documented**)

| Maturity | Notes |
|----------|-------|
| `experimental` | Optional; independent of status |
| `stable` | Optional; does not guarantee SLA/compatibility (`MODULE_LIFECYCLE.md` §3.3) |

### Missing metadata / missing status ⇒ unknown status (no lifecycle inference)

Status is **unknown** when any of the following hold:

- `module.yaml` missing, wrong type, or broken symlink (`MOD-001`) — **no metadata field validation**
- `module.yaml` out-of-root symlink (`MOD-024`; no parse) — **no metadata field validation**
- `module.yaml` unreliable inspection (`MOD-021`; exit 2) — **no metadata field validation**
- `module.yaml` unparseable / not a mapping (`MOD-003`) — **no metadata field validation**
- Parseable metadata mapping with **missing, empty, or invalid `status`** (`MOD-004` / `MOD-008` per R8) — field validation **does** run on that mapping

When status is unknown:

- **Do not** infer `draft`, `active`, or `deprecated`.
- **Do not** apply status-dependent README presence findings (`MOD-002`).
- **Do not** apply deprecated Migration validation (`MOD-012`).
- **Do not** apply D8 lenient Warnings (draft leniency requires an explicit valid `status: draft`).
- For a **parseable** mapping with missing/empty/invalid `status`: missing/empty `id`, `version`, `title`, and `summary` → **`MOD-004` Error** (not Warning).
- **Do** continue lifecycle-independent FS rules for in-scope `README.md`: out-of-root → `MOD-024`; unreliable inspection → `MOD-021` + exit 2 (**D12** / **R11**).

### D8 — Lenient draft required fields (**PO-accepted**)

Applies **only** when `status` is explicitly present and equals `draft`:

| Condition | Severity |
|-----------|----------|
| Missing/empty `id`, `version`, `title`, or `summary` | **Warning** (`MOD-004`) |
| Invalid field types | **Error** (`MOD-005`) |
| Invalid SemVer (`version` / `requires_core` when present) | **Error** (`MOD-007`) |
| Invalid enum values (`status` already valid as draft; `maturity` if present) | **Error** (`MOD-008`/`MOD-009`) |
| Forbidden `dependencies` | **Error** (`MOD-010`) |
| Missing/empty `status` | **Error** (`MOD-004`) — not Warning; status becomes unknown; no draft inference |
| Invalid `status` enum | **Error** (`MOD-008`) — not Warning; status unknown; no draft inference |

For **`active`** and **`deprecated`**, documented required-field **Errors** remain in force for missing/empty `id`, `version`, `title`, `summary`, and `status`.

When status is **unknown** but the YAML mapping is parseable, missing/empty `id` / `version` / `title` / `summary` are **`MOD-004` Error** (same as active/deprecated required-field Errors for those fields). Draft leniency does **not** apply.

### README presence, wrong type, and deprecated Migration (R7)

Classify `README.md` with the same FS model as §8. Do **not** treat permission/I/O failures as “absent”.

**Lifecycle-independent FS rules (always, including unknown status):**

| Case | Findings |
|------|----------|
| README FS inspection unreliable (permission/I/O/resolution failure) | `MOD-021` + `execution_error` (exit 2) — **not** MOD-002 / MOD-012 / MOD-024 |
| README out-of-root symlink (successfully resolved) | `MOD-024` Error; **do not** read the external target — **not** MOD-002 / MOD-012 |

**Status-dependent README rules (only when `status` is known and valid):**

| Case | Findings |
|------|----------|
| `status: active`, README **missing** or **wrong type** or **broken symlink** | `MOD-002` Error only |
| `status: draft`, README **missing** or **wrong type** or **broken symlink** | `MOD-002` Warning only (**D7**) |
| `status: deprecated`, README **missing** or **wrong type** or **broken symlink** | `MOD-002` Error **only** — **do not** emit `MOD-012` (**R7**) |
| `status: deprecated`, README exists, is an in-root regular file (or accepted in-root file symlink), and is **readable**, but exact `## Migration` heading absent | `MOD-012` Error **only** — not MOD-002 |

**When status is unknown** (missing/wrong-type/broken `module.yaml`, or parseable metadata with missing/empty/invalid `status`):

- Do **not** emit `MOD-002` for missing, wrong-type, or broken README.
- Do **not** emit `MOD-012`.
- Do **not** infer draft/active/deprecated.
- Still apply the lifecycle-independent README rows above (`MOD-024` / `MOD-021`).

### Empirical caveat

**Observation:** All six existing Modules are `status: draft` and `maturity: experimental` with `version: 0.1.0`. Paths for `active` and `deprecated` are documented but not empirically exercised in-repo. Implementation tests must use fixtures.

---

## 7. Cross-artifact consistency (E)

| Check | Classification | Behavior |
|-------|----------------|----------|
| Directory name vs `id` | **PO-accepted D3** | Warning (`MOD-017`) when both known and differ |
| `module.yaml` missing / wrong type / broken symlink | **PO-accepted D4** + §4/§8 | Warning `MOD-001` (unknown status) |
| `README.md` missing / wrong type / broken symlink | **Documented** / **D7** / **R7** / §8 | `MOD-002` only when status known; never when status unknown; no MOD-012 for these cases |
| `README.md` out-of-root / unreliable FS | **D12** / **R11** | `MOD-024` / `MOD-021` even when status unknown |
| `provides` vs Skill ids | **Out of scope** | — |
| Skill id vs filename | **Out of scope** | — |
| Related Modules links | **Out of scope** for MVP Errors | — |
| Catalog sync | **Out of scope (D9)** | — |
| `requires_core` vs `VERSION` | **Out of scope** | — |

---

## 8. Filesystem semantics (F)

### Technical reference

Phase 8.2 `FileSystem.inspect` (`lstat`/`stat`, `FileNotFoundError`→MISSING, `NotADirectoryError`→OTHER, other `OSError`→ERROR, symlink target-type, broken→OTHER) is the preferred inspection technique. Module findings use `MOD-*`, not `STR-*`.

### Module path classification

| Inspection result | Meaning |
|-------------------|---------|
| MISSING | Absent path — entry-point presence rules |
| FILE | Regular file (or accepted in-root symlink→file) where a file is expected |
| DIRECTORY | Directory (or accepted in-root symlink→directory) where a directory is expected |
| OTHER | Wrong type (including broken symlink; `NotADirectoryError`) — entry-point wrong-type rules; **not** execution failure |
| ERROR | Permission/I/O — `MOD-021` + exit 2 when required inspection cannot complete |

### Entry-point rules for `module.yaml` and `README.md`

| Observation | `module.yaml` | `README.md` |
|-------------|---------------|-------------|
| MISSING | `MOD-001` Warning | If status **known**: `MOD-002` (severity by status; §6). If status **unknown**: **no** `MOD-002` |
| Wrong type (not a regular file) | `MOD-001` Warning | If status **known**: `MOD-002`. If status **unknown**: **no** `MOD-002` |
| Broken symlink | `MOD-001` Warning (same as missing/wrong-type) | If status **known**: `MOD-002` (same as missing/wrong-type). If status **unknown**: **no** `MOD-002` |
| Unreliable inspection (permission/I/O/resolution failure) | `MOD-021` + exit 2 | `MOD-021` + exit 2 (**always**, including unknown status) |
| Successfully resolved out-of-root symlink | `MOD-024` Error; never read external target | `MOD-024` Error; never read external target (**always**, including unknown status) |
| In-root symlink→file of expected type | Accept; then parse / content checks | Accept; Migration check **only** if `status: deprecated` is known |

`MOD-012` applies **only** when `status: deprecated` is known and `README.md` is an existing, in-root, readable regular file (or accepted in-root file symlink) and the exact `## Migration` heading is absent. It is never used when status is unknown, nor for missing, wrong-type, broken, out-of-root, or unreliable README inspection.

**D12 is independent of lifecycle:** candidate `README.md` containment inspection remains in scope even when status is unknown.

### Symlinks — in-root acceptance and D12 containment

**PO-accepted D12** applies to:

- `modules/`
- Module candidate directories
- `module.yaml`
- `README.md`

| Situation | Finding |
|-----------|---------|
| Symlink resolves **successfully** to a target **outside** the canonical Framework root | `MOD-024` Error; **do not** inspect or read the external target |
| In-root symlink with expected target type (file or directory as required) | Accept |
| Broken symlink on discovery children / `modules/` | Wrong-type behavior (`MOD-019` / `MOD-018` as applicable) — **not** MOD-024 |
| Broken symlink on `module.yaml` | `MOD-001` — **not** MOD-024 / MOD-021 |
| Broken symlink on `README.md` | `MOD-002` **only if status known**; if status unknown → no MOD-002 — **not** MOD-024 / MOD-021 |
| Permission, I/O, symlink-loop, or other resolution failures preventing reliable inspection | `MOD-021` + `execution_error` (exit **2**) — **not** MOD-001 / MOD-002 / MOD-012 / MOD-024 (**R11**); applies even when status unknown |

No recursive walk beyond contract paths. No write/chmod/repair. External targets of out-of-root symlinks must **never** be read.

### Distinction: parse vs filesystem vs containment (R11)

| Failure class | Code | Exit |
|---------------|------|------|
| YAML syntax/parse/mapping shape | `MOD-003` | 1 if Error findings |
| Successfully resolved out-of-root symlink (incl. README when status unknown) | `MOD-024` | 1 |
| Broken / wrong-type / missing `module.yaml` | `MOD-001` | 0 (Warning) |
| Broken / wrong-type / missing `README.md` with **known** status | `MOD-002` | 1 if Error severity; 0 if Warning |
| Broken / wrong-type / missing `README.md` with **unknown** status | *(no MOD-002 / MOD-012)* | — |
| Unreliable FS inspection / resolution (permission, I/O, loops, …) | `MOD-021` | **2** + `execution_error` |
| Deprecated (**known**) readable README missing `## Migration` | `MOD-012` | 1 |
| Ordinary contract violations | relevant `MOD-*` | 1 if any ERROR |

---

## 9. Finding code register (G)

**Namespace:** `MOD-xxx`  
**Category:** `module-contract`  
**Status:** Design-accepted code set for implementation after PO design acceptance.

| Code | Meaning | Severity | Trigger | Basis |
|------|---------|----------|---------|-------|
| MOD-001 | `module.yaml` missing, wrong type, or broken symlink | WARNING | No usable metadata entry point; status unknown | **D4** + §4/§8 |
| MOD-002 | `README.md` missing, wrong type, or broken symlink | ERROR or WARNING | Only when status **known**: active/deprecated → Error; draft → Warning (**D7**); **not** when status unknown; **not** for FS I/O failure; **not** combined with MOD-012 (**R7**) | Doc + D7 + R7 + §8 |
| MOD-003 | YAML parse or root-not-mapping failure | ERROR | Parser/shape after successful in-root file read | Mechanical metadata; **not** FS I/O |
| MOD-004 | Required field missing or empty | ERROR or WARNING | `status` missing/empty always Error; `id`/`version`/`title`/`summary` missing/empty → Warning **only** for explicit valid `draft` (**D8**); otherwise Error including unknown status on parseable mappings; no field validation if yaml missing/wrong-type/broken/unreadable/unparseable | Doc + D8 |
| MOD-005 | Metadata field has invalid type | ERROR | Wrong YAML type | Doc + R8 |
| MOD-006 | Invalid `id` format | ERROR | Non-empty id failing kebab-case | Doc + R8 |
| MOD-007 | Invalid SemVer | ERROR | Non-empty `version` / `requires_core` failing SemVer | Doc + R8 |
| MOD-008 | Invalid `status` enum | ERROR | Non-empty status not in enum; no draft inference | Doc + D8 + R8 |
| MOD-009 | Invalid `maturity` enum | ERROR | Present but invalid | Doc + R8 |
| MOD-010 | `dependencies` key present | ERROR | Forbidden key; **not** also MOD-013 | Doc + R8 |
| MOD-011 | `deprecation` inconsistent with status / not an object | ERROR | Object when not deprecated, or wrong type | Doc |
| MOD-012 | Deprecated README lacks exact `## Migration` | ERROR | Only when `status: deprecated` is **known**; existing in-root readable README; heading absent (**R7**); never when status unknown; never for missing/wrong-type/broken/out-of-root/unreliable README | Doc + R7 |
| MOD-013 | Unknown metadata field | WARNING | Extra top-level key (not `dependencies`) | Doc + R8 |
| MOD-014 | Missing `applies_when` or `avoid_when` | WARNING | Optional lists absent | Doc |
| MOD-015 | Maturity present on deprecated Module | WARNING | Prefer omit | Doc |
| MOD-016 | Deprecated `deprecation.reason` missing | WARNING | Object present without reason (**R9**) | Doc + R9 |
| MOD-017 | Directory name does not match `id` | WARNING | Both known and differ | **D3** |
| MOD-018 | Unexpected non-directory under `modules/` | WARNING | Child not dir (except ignored `README.md`) | **D2** |
| MOD-019 | `modules` exists but is not a directory | ERROR | Wrong resolved type / broken | **D1** |
| MOD-020 | *(reserved / unused in MVP)* | — | Catalog sync | **D9 out of scope** |
| MOD-021 | Filesystem inspection / resolution unreliable | ERROR + execution_error | Permission/I/O/loop/unreliable resolve | Technical FS + **R11** |
| MOD-022 | Invalid `deprecation.successor` id format | WARNING | Present but invalid format; no existence check | **D6** |
| MOD-023 | Non-kebab-case `tags` entry | WARNING | Tag string pattern | **D5** |
| MOD-024 | Symlink resolves outside Framework root | ERROR | Successful out-of-root resolve on in-scope paths (`modules/`, candidates, `module.yaml`, `README.md`); lifecycle-independent; do not read target | **D12** |
| MOD-025 | Invalid `deprecation.sunset` format | ERROR | Present but not ISO `YYYY-MM-DD` | **PO-accepted R10** |

Do **not** reuse `STR-*`.  
Do **not** fold FS permission failures into MOD-001, MOD-002, MOD-003, or MOD-012.  
Do **not** fold successful out-of-root resolves into MOD-021.  
Do **not** describe unreliable inspection as “unreadable-as-absent”.

---

## 10. CLI and integration (H)

1. Add a Module Contract validator callable (future `validation/module_contract.py` or equivalent).
2. Register on the shared `Orchestrator` as `module-contract`.
3. **Default `python -m validation` registers and runs Module Contract Validation** with Framework Structure Validation (**PO-accepted D10**).
4. Banner must accurately list registered validators; must not claim documentation integrity or Pack validation.
5. Preserve `--root` as Framework-root selector (Phase 8.2); Module discovery is relative to that root’s `modules/`.
6. **No additional CLI flags in MVP** (**PO-accepted D11**).
7. **Must not** modify `scripts/aiosctl.py`, `sync`, `doctor`, or `version`.

### Exit codes

Unchanged from Phase 8.1.2: ERROR→1; execution_error→2; WARNING/INFO alone→0.

---

## 11. Test strategy (I)

Do not create tests in this design phase. Future tests classify as follows. **No unresolved D8/D12 test dependency remains.**

### 1. Documented contract tests

- Active required fields missing/empty → Error
- Invalid status/maturity enums → Error
- Invalid SemVer → Error
- `dependencies` present → MOD-010 only (not MOD-013)
- Unknown fields → MOD-013
- Missing `applies_when` / `avoid_when` → Warning
- Active missing or wrong-type README → MOD-002 Error
- Deprecated existing readable README without `## Migration` → MOD-012 only (no MOD-002)
- `deprecation` present when not deprecated → MOD-011
- Deprecated maturity present → MOD-015
- Object present without `reason` → MOD-016
- Missing `deprecation` object when deprecated → **no** finding (**R9**)

### 2. Accepted technical behavior tests

- Deterministic aggregation `(rule, path)`
- Read-only snapshot
- README or `module.yaml` permission/I/O/resolution failure → MOD-021 + exit 2 (**not** MOD-001/MOD-002/MOD-012), including when status unknown
- `NotADirectoryError` / wrong-type `module.yaml` → MOD-001 (not execution failure)
- Wrong-type/missing/broken README with **known** status → MOD-002; with **unknown** status → no MOD-002
- YAML parse failure → MOD-003 without execution_error; status unknown afterward → no MOD-002/MOD-012
- Successful FS read + bad YAML → MOD-003, not MOD-021
- Field finding precedence R8 (single code per field defect)
- In-root symlink acceptance for expected types
- Out-of-root README symlink even when status unknown → MOD-024; external target not read (**D12**)
- Out-of-root symlink on `module.yaml` / `modules/` / candidate → MOD-024
- Broken `module.yaml` symlink → MOD-001 Warning
- Broken `README.md` symlink with known status → MOD-002; with unknown status → no MOD-002; never MOD-012
- MOD-025 invalid sunset format

### 3. PO-decision-dependent tests (all decisions accepted)

| Area | Decision |
|------|----------|
| Missing or wrong-type `module.yaml` → Warning; no status inference; no MOD-002/MOD-012 | D4 + §6/§8 |
| Parseable yaml with missing/empty/invalid status → status Error; missing/empty id/version/title/summary → MOD-004 Error; no draft inference; no MOD-002/MOD-012 | D8 + §6 |
| Missing/wrong-type/broken/unreadable/unparseable yaml → no metadata field validation | §5 / §6 |
| Draft missing or wrong-type README → Warning | D7 |
| Deprecated missing or wrong-type README → MOD-002 only (no MOD-012) | R7 |
| Deprecated readable README without Migration → MOD-012 only | R7 |
| Dir name ≠ `id` → Warning | D3 |
| Non-directory child under `modules/` → Warning | D2 |
| `modules` wrong type → Error | D1 |
| Non-kebab tags → MOD-023 | D5 |
| Invalid successor format → MOD-022; no existence check | D6 |
| D8 lenient: draft missing/empty id/version/title/summary → Warning | D8 |
| D8: draft invalid types/SemVer/enums/`dependencies` → Error | D8 |
| Active/deprecated missing required fields → Error | D8 boundary |
| Default CLI registers `module-contract` | D10 |
| No extra flags | D11 |
| Out-of-root README rejection MOD-024 even when status unknown; never read external target | D12 |
| Catalog sync | D9 — **no MVP tests** |

### Explicitly deferred

- Real privileged permission flakiness (use injection)
- Pack validation, Consumer adoption, installer behavior
- `provides` ↔ Skill id matching, Skill filename rules
- Empty-element rejection in applicability lists

---

## 12. Risks, compatibility, open items (J)

### Risks

| Risk | Mitigation |
|------|------------|
| Over-validating draft packages | D4/D7 file Warnings; D8 lenient for missing/empty id/version/title/summary **only** when status is explicitly valid `draft` |
| Inferring draft from missing/invalid status | Explicitly forbidden (D8); unknown-status missing id/version/title/summary → MOD-004 Error |
| Applying field validation without usable parseable yaml | Forbidden — skip fields if missing/wrong-type/broken/unreadable/unparseable |
| Duplicate MOD-002/MOD-012 | R7: missing/wrong-type/broken → MOD-002 only (known status); readable Migration miss → MOD-012 only |
| Applying MOD-002/MOD-012 when status unknown | Forbidden — skip lifecycle README findings; keep lifecycle-independent FS/containment |
| Implying all structural entry-point checks need known status | Forbidden — §3 item 2: FS/containment independent; MOD-002/MOD-012 status-dependent |
| Treating FS I/O failure as absent README/yaml | Forbidden — use MOD-021; never “unreadable-as-absent” |
| Duplicate field findings | R8 precedence |
| Out-of-root reads | D12 + MOD-024 even when status unknown; never read external target |
| Confusing MOD-001/002/003/012/021/024 | §6 unknown-status rules + §8 entry-point table + R11 |
| Stale Framework Contract / MANIFEST | Documentation conflict only |
| Coupling to sync | Forbidden |

### Documentation conflicts (critical)

| Location | Issue |
|----------|-------|
| `docs/FRAMEWORK_CONTRACT.md` §5.2 / §14 | Stale “Modules / module.yaml not implemented” vs Phase 7 packages |
| `MANIFEST.md` | Stale “packages not populated yet” wording |

**Action:** Separate documentation alignment task. Validator follows Module Metadata / Validation / Lifecycle + this design.

### Remaining source-document notes (non-blocking)

- `deprecation.sunset` Error severity is **PO-accepted R10**, not an explicit “Error” word in Metadata §5 (format is documented; severity is PO decision).
- Empty string items in `applies_when` / `avoid_when` remain undocumented; MVP explicitly does **not** add a rejection rule (**R10**).

### Explicit exclusions

Resolver, installer, adopter, sync integration, Pack validation, Skill-filename enforcement, `provides`↔Skill hard match, Framework `VERSION` hard match for `requires_core`, catalog sync (D9), authority-model changes, CI wiring (Phase 8.5), documentation integrity (Phase 8.4).

---

## 13. Authority preservation

Unchanged and out of validator mutation scope:

- Module guidance **L6** by default
- Explicit Consumer adoption → **L3**
- Explicit Pack adoption → **L5**
- Consumer ADRs → **L2**
- Metadata never implies adoption/installation (`MODULE_METADATA.md` §2, §8; Validation §7)

---

## 14. Acceptance criteria for this final design revision

This revision is complete when:

1. D8 Lenient-with-status-clarification and D12 out-of-root rejection are recorded as **PO-accepted**.
2. R7–R11 corrections are reflected in lifecycle, metadata, filesystem, findings, and tests.
3. Finding register covers **MOD-001–MOD-025** consistently (MOD-020 reserved unused).
4. No blocking unresolved PO decisions remain for MVP.
5. Only this design document was modified; no implementation, tests, commit, or push occurred.

Implementation may start only after **explicit Product Owner design acceptance**.

---

## 15. PO decision register

| ID | Decision | Status |
|----|----------|--------|
| D1 | `modules/` exists but is not a directory → **Error** | **Accepted** |
| D2 | Unexpected non-directory under `modules/` (except `README.md`) → **Warning** | **Accepted** |
| D3 | Directory name ≠ metadata `id` → **Warning** | **Accepted** |
| D4 | Candidate without `module.yaml` → **Warning**; **no lifecycle inference** | **Accepted** |
| D5 | Non-kebab-case `tags` → **Warning** (`MOD-023`) | **Accepted** |
| D6 | Invalid `deprecation.successor` format → **Warning**; no existence check | **Accepted** |
| D7 | Draft without `README.md` → **Warning** | **Accepted** |
| D8 | Lenient draft missing/empty `id`/`version`/`title`/`summary` → Warning **only** when `status` is explicitly valid `draft`; invalid types/SemVer/enums/`dependencies` → Error; missing/empty/invalid `status` → Error and unknown status; unknown-status missing/empty `id`/`version`/`title`/`summary` on parseable mappings → MOD-004 Error; **no draft inference**; no field validation without usable parseable yaml | **Accepted** |
| D9 | Catalog index synchronization | **Accepted: out of scope for MVP** |
| D10 | Register Module Contract Validation in default `python -m validation` | **Accepted** |
| D11 | No additional CLI flags in MVP | **Accepted** |
| D12 | Out-of-root symlink → **MOD-024 Error**; do not read external target; resolution failures → MOD-021 exit 2 | **Accepted** |
| R7 | Deprecated README: MOD-002 vs MOD-012 non-duplication | **Accepted** |
| R8 | Field finding precedence | **Accepted** |
| R9 | Missing `deprecation` object alone → no finding | **Accepted** |
| R10 | MOD-025 sunset Error; no empty-list-item rule in MVP | **Accepted** |
| R11 | Path resolution: out-of-root vs broken vs unreliable | **Accepted** |

---

## Document control

| Item | Value |
|------|--------|
| Document id | `MODULE_CONTRACT_VALIDATION_DESIGN` |
| Phase | 8.3 |
| Kind | **Design proposal (final PO correction revision)** |
| Companion implementation doc | Deferred until design acceptance |
| Finding namespace | `MOD-001` … `MOD-025` (MOD-020 reserved) |
| Baseline at initial authoring | `d81e4475c269282eec9249044480b70d5d155eb9` on `main` |
