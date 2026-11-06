# Phase 8.2 — Framework Structure Validation Design

**Status:** Canonical Phase 8.2 design (documentation)

**Authority:** Consolidated canonical design based on the PO-approved Phase 8.2 decisions and subsequent explicit PO clarifications. The original detailed proposal was not available as a persistent source artifact; rule and acceptance details are formalized in this document for implementation.

**Depends on:** Phase 8.1.2 Shared Validation Foundation (`validation/`, [`VALIDATION_FOUNDATION.md`](VALIDATION_FOUNDATION.md))

**Implementation note:** This document is design-only. Validator code is out of scope for the design-documentation phase.

**Terminology:** Prefer the terms *Framework root*, *candidate*, *required path*, *optional path*, *reserved path*, *finding*, *execution failure*, *link entry*, and *resolved target* consistently below.

---

## 1. Purpose, scope and non-goals

### Purpose

Define a **read-only Framework Structure Validator** that checks whether a Framework root satisfies the AIOS framework layout contract: required files and directories exist with the correct path types, using the shared Phase 8.1.2 Finding model, orchestrator and reporter.

### Scope

- Structural existence and path-type checks only
- Root discovery (explicit `--root` or upward search)
- Deterministic findings and Phase 8.1.2 exit-code semantics
- Symbolic-link **target-type** semantics for required paths and markers (see §7)
- Fixture-based automated tests (implementation phase)
- Default CLI registration of this validator under `python -m validation`

### Non-goals

- Module Contract Validation (Phase 8.3)
- Documentation integrity / link validation (Phase 8.4)
- CI wiring (Phase 8.5)
- Final audit (Phase 8.6)
- Content inspection of files (beyond path type / existence)
- YAML / metadata validation
- Automatic repair, install, adoption, file creation or deletion
- Changes to `aiosctl sync`, `doctor`, or `version`
- Changes to Framework Contract, Roadmap, `AGENTS.md`, or other governance documents as part of this design phase
- Treating reserved/planned paths as required
- Treating `.agents/` as required
- Separate finding codes for Optional, Reserved or Unknown path classifications
- Recursive link following or directory-content inspection beyond contract paths

---

## 2. Required root files and directories

### Required root files

These paths must exist and must resolve to **regular files** (see §7 for symbolic-link target-type semantics):

| Path |
|------|
| `README.md` |
| `AGENTS.md` |
| `MANIFEST.md` |
| `PROJECT_STRUCTURE.md` |
| `ROADMAP.md` |
| `VERSION` |
| `docs/FRAMEWORK_CONTRACT.md` |
| `scripts/aiosctl.py` |

### Required directories

These paths must exist and must resolve to **directories** (see §7):

| Path |
|------|
| `docs/` |
| `rules/` |
| `methodology/` |
| `scripts/` |
| `tests/` |

---

## 3. Path classifications

### Conditional

| Path | Policy |
|------|--------|
| `.github/` | Missing: **no finding**. Existing directory (or link whose resolved target is a directory): **no finding**. Existing non-directory (wrong resolved type): **STR-007**. Uninspectable filesystem error: **STR-006** (see §9). |

### Optional

Absence produces **no findings**. Presence produces **no findings**, including when the present entry has a different type. No separate STR codes apply:

- `modules/`
- `packs/`
- `prompts/`
- `skills/`
- `workflows/`
- `checklists/`
- `templates/`
- `assets/`
- `lab/`

### Reserved / planned

| Path | Policy |
|------|--------|
| `examples/` | Absence **and** wrong type are **ignored** (no findings) |
| `generators/` | Absence **and** wrong type are **ignored** (no findings) |
| `knowledge/` | Absence **and** wrong type are **ignored** (no findings) |

### Non-required / ignored

| Path | Policy |
|------|--------|
| `.agents/` | Not required; **ignored** by this validator |

### Unknown root entries

Any other top-level name under the Framework root is **tolerated** and produces **no findings**.

---

## 4. STR-001 through STR-009 rule catalog

PO-approved meanings (do not restore any former STR-007–STR-009 interpretations):

| Rule | Severity | Meaning |
|------|----------|---------|
| STR-001 | ERROR | Missing required root file |
| STR-002 | ERROR | Missing required directory |
| STR-003 | ERROR | Required file path has the wrong type |
| STR-004 | ERROR | Required directory path has the wrong type |
| STR-005 | ERROR | Framework root not found during upward discovery |
| STR-006 | ERROR | Required inspection or discovery operation is uninspectable |
| STR-007 | ERROR | `.github/` exists but is not a directory |
| STR-008 | ERROR | Explicit `--root` is missing or is not a directory |
| STR-009 | ERROR | Explicit root directory does not satisfy the minimum-two-marker candidate rule |

`category` is always `framework-structure`.  
`code` and `rule` both use the STR id (for example `STR-001`) so duplicate identity `(rule, path)` remains stable.

| Code | Severity | Trigger | Message (canonical) | Suggestion (canonical) |
|------|----------|---------|---------------------|------------------------|
| **STR-001** | ERROR | A required root file path is missing | `Required framework file is missing: <path>` | `Create the required file at the Framework root (or restore it from AIOS Core).` |
| **STR-002** | ERROR | A required directory path is missing | `Required framework directory is missing: <path>` | `Create the required directory at the Framework root (or restore it from AIOS Core).` |
| **STR-003** | ERROR | A required file path exists but its resolved target is not a regular file (including wrong-type link target or broken link) | `Required path must be a file: <path>` | `Replace or relocate the non-file entry so <path> resolves to a regular file.` |
| **STR-004** | ERROR | A required directory path exists but its resolved target is not a directory (including wrong-type link target or broken link) | `Required path must be a directory: <path>` | `Replace or relocate the non-directory entry so <path> resolves to a directory.` |
| **STR-005** | ERROR | Upward discovery finds no Framework root candidate | `AIOS Framework root was not found.` | `Run from inside an AIOS framework repository, or pass --root to an explicit Framework root.` |
| **STR-006** | ERROR | Required path, discovery marker, explicit root, or conditional path inspection is uninspectable due to a filesystem error | `Framework path or discovery marker could not be inspected: <path> (<error class>)` | `Resolve the filesystem error preventing inspection of <path>, then re-run validation.` |
| **STR-007** | ERROR | `.github/` exists but does not resolve to a directory | `Conditional path .github must be a directory when present.` | `Ensure .github is a directory, or remove the non-directory entry.` |
| **STR-008** | ERROR | Explicit `--root` is missing or is not a directory | `Explicit validation root is missing or not a directory: <path>` | `Pass --root with an existing directory path.` |
| **STR-009** | ERROR | Explicit `--root` directory exists and fewer than two valid file markers are **conclusively** established (no unresolved marker inspection error) | `Explicit validation root is not an AIOS framework candidate (fewer than two root markers).` | `Point --root at a directory containing at least two of: VERSION, MANIFEST.md, PROJECT_STRUCTURE.md, docs/FRAMEWORK_CONTRACT.md.` |

Optional, Reserved and Unknown classifications do **not** receive separate finding codes.

STR-006 applies to required paths, root discovery markers, explicit root inspection and conditional path inspection.

---

## 5. Finding field mapping (Phase 8.1.2)

| Finding field | Phase 8.2 usage |
|---------------|-----------------|
| `code` | `STR-00N` |
| `severity` | `Severity.ERROR` for STR-001–STR-009 |
| `category` | `framework-structure` |
| `message` | Human-readable description including path when applicable; for STR-006 include the filesystem error class when available |
| `path` | Repository-relative path using `/` separators when applicable; may be `None` for STR-005 when no Framework root path applies |
| `rule` | Same STR id as `code` |
| `suggestion` | Optional remediation text as in the catalog |

Aggregation, duplicate suppression `(rule, path)`, deterministic ordering, and serialization remain exactly as defined in Phase 8.1.2. No parallel Finding type is introduced.

---

## 6. Root discovery

### Inputs

- **Explicit root:** optional CLI `--root <path>`
- **Starting location:** when `--root` is omitted, search upward from the process starting location (implementation default: current working directory)

### Explicit root

1. If the path is missing or is not a directory → **STR-008** (exit code **1**). Stop further structure checks that require a Framework root.
2. If the path cannot be inspected due to a filesystem error → **STR-006** and set execution failure (exit code **2**) when candidate determination cannot complete reliably.
3. Perform candidate determination per §8.
4. If fewer than two valid markers are **conclusively** established and there is **no** unresolved marker inspection error → **STR-009** (exit code **1**).
5. If marker inspection is incomplete and could affect the result → **STR-006** + execution failure (exit code **2**). Do **not** emit STR-009 in that case.
6. If the directory is a valid candidate (≥ two valid file markers) → use it as the Framework root and run normal structure validation.

### Upward discovery

1. Walk from the starting location **upward** toward the filesystem root.
2. At each directory, evaluate markers using §8.
3. Select the **nearest** ancestor that **conclusively** satisfies the minimum-two-marker rule as the Framework root.
4. If a nearer ancestor is **conclusively not** a candidate, continue to its parent.
5. If inspection of a nearer ancestor is **incomplete** and could affect whether it is a candidate:
   - **Stop** upward discovery.
   - Do **not** silently skip that ancestor and select a higher candidate.
   - Return **STR-006** and exit code **2**.
6. If every ancestor is conclusively not a candidate → **STR-005** with exit code **1** (completed validation result; not exit 2).

### After a Framework root is accepted

Evaluate required and conditional path rules relative to that root. Optional, reserved, unknown, and `.agents/` policies apply as classified in §3.

---

## 7. Symbolic link policy (PO-approved target-type semantics)

Distinguish the **link entry** (the path being examined) from its **resolved target**.

| Situation | Behavior |
|-----------|----------|
| Link entry whose target exists and resolves to a **regular file** | Accepted where a regular file is expected |
| Link entry whose target exists and resolves to a **directory** | Accepted where a directory is expected |
| Link entry whose target resolves to the **wrong type** | Corresponding type mismatch finding (**STR-003**, **STR-004**, or **STR-007** as applicable) |
| **Broken** symbolic link | Treated as an existing path that does **not** satisfy the expected file/directory type → **STR-003** or **STR-004** (or **STR-007** for `.github/` when applicable); does **not** count as a valid root marker |
| Link target cannot be inspected due to a filesystem error | **STR-006** when reliable inspection is prevented (and execution failure / exit 2 when completion is unreliable) |

Additional constraints:

- The validator must **not** follow links recursively or inspect directory contents beyond the paths required by the contract.
- The validator remains **read-only**.

---

## 8. Four root markers and candidate determination

The four approved markers are:

| Marker path |
|-------------|
| `VERSION` |
| `MANIFEST.md` |
| `PROJECT_STRUCTURE.md` |
| `docs/FRAMEWORK_CONTRACT.md` |

### Marker counting rules

A marker **counts** only if its path **resolves to a regular file**.

- A missing marker does **not** count.
- A marker resolving to a directory does **not** count.
- A broken symbolic link does **not** count.
- A marker inspection filesystem error must **not** be silently treated as missing; apply **STR-006** / execution-failure rules in §6 and §9.

### Early success

Once **two** valid file markers have been positively established for a directory:

1. Candidate determination **succeeds immediately**.
2. **No further marker checks** are required for that candidate.
3. Remaining (unchecked) markers **must not be inspected**.
4. A hypothetical filesystem error on an unchecked marker is **irrelevant** and **must not** produce **STR-006**, because that marker is never inspected after early success.
5. Discovery proceeds using the accepted candidate according to the nearest-ancestor policy (explicit root uses that candidate; upward discovery may stop at this nearest qualifying ancestor).

### Incomplete candidate determination

If fewer than two valid markers have been established and an inspection error occurs on another marker that could affect the result:

- Emit **STR-006**.
- Set `execution_error` when candidate determination cannot complete reliably.
- Return exit code **2**.
- Do **not** classify the directory as a non-candidate merely because the unreadable marker was treated as missing.
- Do **not** emit **STR-009** while an unresolved inspection error remains.

### Candidate rule

A directory is an AIOS Framework root **candidate** if and only if it has **at least two** valid file markers **conclusively** established.

Full required-file and required-directory type enforcement for the complete required set runs only **after** a Framework root is selected.

---

## 9. Uninspectable paths and filesystem error semantics (STR-006)

Use controlled filesystem exception handling. Do **not** silently convert permission or I/O errors into missing-path findings (STR-001 / STR-002) or into conclusive non-candidate results.

### Situation matrix

| Situation | Finding | Exit code |
|-----------|---------|-----------|
| Required path is missing | STR-001 or STR-002 | 1 |
| Required path exists with wrong type (including wrong-type or broken link) | STR-003 or STR-004 | 1 |
| Required path cannot be inspected | STR-006 | 2 if validation cannot complete reliably |
| Explicit root is missing | STR-008 | 1 |
| Explicit root is not a directory | STR-008 | 1 |
| Explicit root cannot be inspected due to filesystem error | STR-006 | 2 |
| `.github/` exists with wrong type | STR-007 | 1 |
| `.github/` cannot be inspected due to filesystem error | STR-006 | 2 when reliable completion is prevented |
| Upward discovery finds no conclusive candidate | STR-005 | 1 |
| Upward discovery cannot inspect a marker needed for reliable candidate determination | STR-006 | 2 |
| Unresolved nearer ancestor could affect candidacy | STR-006 | 2 (do not select a higher candidate) |
| Explicit root has fewer than two valid markers conclusively, with no unresolved inspection error | STR-009 | 1 |

### STR-006 Finding requirements

- Severity: **ERROR**
- Category: `framework-structure`
- Code and rule: `STR-006`
- Include the relevant repository-relative `path` where available
- Include the filesystem error class in the message when available
- Canonical message: `Framework path or discovery marker could not be inspected: <path> (<error class>)`
- Canonical suggestion: `Resolve the filesystem error preventing inspection of <path>, then re-run validation.`
- Set the shared validation **execution-error** state whenever validation cannot complete reliably

### Exit-code precedence

Preserve Phase 8.1.2 precedence: if `execution_error` is set, exit code is **2**, even when ERROR findings (including STR-006) are also present.

STR-005 remains a **completed** ERROR finding with exit code **1**. It is not an execution failure.

The validator remains **read-only**: it must not create, delete, chmod, or repair paths to recover from STR-006.

---

## 10. `.github/` conditional behavior

| Observation | Result |
|-------------|--------|
| Missing `.github/` | No finding |
| Existing directory (or link resolving to a directory) | No finding |
| Existing non-directory (wrong resolved type, including broken link when treated as wrong type) | **STR-007** (exit 1) |
| Uninspectable due to filesystem error | **STR-006** per §9 (exit 2 when reliable completion is prevented) |

---

## 11. CLI behavior

Independent of `python scripts/aiosctl.py`.

### Default

```powershell
python -m validation
```

- Runs **Framework Structure Validation by default** (this Phase 8.2 validator is registered on the shared orchestrator).
- Uses upward root discovery from the current working directory when `--root` is omitted.
- Must not claim Module Contract, documentation-integrity, or other future validators were executed unless they are separately registered in later phases.

### Explicit root

```powershell
python -m validation --root <path>
```

- Uses `<path>` as the explicit root candidate subject to STR-008 / STR-009 / STR-006 and then the structure contract when valid.

### Banner / reporting

- Use Phase 8.1.2 `format_report`.
- Announce that Framework Structure Validation ran.
- Do not imply comprehensive AIOS validation beyond registered validators.

No additional CLI flags are introduced by this design.

---

## 12. Exit code semantics

Inherited unchanged from Phase 8.1.2:

| Exit code | Meaning |
|-----------|---------|
| `0` | No ERROR findings and no execution failure |
| `1` | At least one ERROR finding (including completed STR-005, STR-008, STR-009, and ordinary STR-001–STR-004 / STR-007 results) |
| `2` | Execution or configuration failure (including unreliable STR-006 completion) |

WARNING/INFO are not used by STR-001–STR-009 in this design. Future validators may emit them without changing this contract.

---

## 13. FS-01 through FS-12 acceptance criteria

Exactly twelve primary acceptance criteria:

| ID | Criterion |
|----|-----------|
| **FS-01** | A valid minimal framework fixture produces no ERROR findings and exit code 0. |
| **FS-02** | Missing required files produce STR-001 and exit code 1. |
| **FS-03** | Missing required directories produce STR-002 and exit code 1. |
| **FS-04** | Required path type mismatches produce STR-003 or STR-004 and exit code 1. |
| **FS-05** | A valid explicit root is selected and validated. |
| **FS-06** | Upward discovery selects the nearest qualifying ancestor. |
| **FS-07** | Root not found produces STR-005 and exit code 1. |
| **FS-08** | Uninspectable paths produce STR-006; unreliable completion produces exit code 2. |
| **FS-09** | Missing optional/reserved paths produce no findings; optional paths also produce no findings when present with a different type; reserved wrong types remain ignored. |
| **FS-10** | Unknown root entries produce no findings. |
| **FS-11** | Findings are deterministic. |
| **FS-12** | Validation is read-only. |

### Supplementary test expectations

These behaviors must be covered explicitly in the implementation-phase fixture suite (they do not expand the twelve primary FS ids):

- `.github/` absent, directory, non-directory, and uninspectable cases
- Explicit root missing, non-directory, and fewer-than-two-markers cases
- Explicit-root marker inspection failure
- Upward-discovery marker inspection failure
- `.agents/` ignored
- Marker path existing as a directory does **not** count as a valid marker
- Valid file-target symbolic link
- Valid directory-target symbolic link
- Wrong-type symbolic link target
- Broken symbolic link
- Symbolic link target inspection error
- Early success after two valid markers: marker inspection **stops** after the second valid marker; remaining markers are not inspected
- Marker inspection error before two valid markers (incomplete determination → STR-006 / exit 2)
- Unresolved nearer ancestor prevents selecting a higher candidate

### FS-08 testability note

FS-08 must include at least one deterministic, testable filesystem-error scenario where supported by the test platform. Where permission-based tests are unreliable (for example, privileged execution), use an injected filesystem abstraction or controlled monkeypatch to simulate the error.

Do **not** claim a permission test passed unless it was actually executed in the implementation phase. This documentation-only task does not execute those tests.

---

## 14. Fixture-based testing expectations

- Tests live under an isolated suite (for example `tests/validation_structure/` or equivalent) using **temporary fixtures only**.
- Tests must **not** mutate the real AIOS repository tree to create failure cases.
- Cover FS-01–FS-12 and the supplementary expectations in §13.
- Assert Finding fields (`code`/`rule`, `severity`, `path`, `category`) and exit codes.
- Assert CLI default and `--root` behaviors via subprocess or in-process `main()` as appropriate.
- Existing `tests/cli/` (`sync` / `doctor` / `version`) must remain green; `aiosctl` must not be modified for this phase.

---

## 15. Read-only guarantees

The Framework Structure Validator:

- Performs only read / stat / list operations on contract paths
- Does **not** create, rewrite, delete, move, or repair files or directories
- Does **not** install Modules, adopt guidance, or modify Consumer repositories
- Does **not** change permissions to “fix” STR-006
- Does **not** recursively walk through symbolic links or inspect unrelated directory contents

---

## 16. Architecture and extension approach

```text
validation/
├── models.py / orchestrator.py / reporter.py   # Phase 8.1.2 shared foundation
├── framework_structure.py                      # Phase 8.2 validator (implementation phase)
└── __main__.py                                 # registers Framework Structure Validator by default
```

- Implement a pure function (or thin callable) returning `Sequence[Finding]`.
- Register it on `Orchestrator` under a stable name (for example `framework-structure`).
- Reuse `aggregate_findings`, `format_report`, and `ValidationResult.exit_code()`.
- Preserve Phase 8.1.2 duplicate suppression `(rule, path)` and deterministic finding ordering.
- Later phases add additional callables; they must not fork the Finding model.

---

## 17. Scope exclusions and dependencies

### Dependencies

- Phase 8.1.2 Shared Validation Foundation (accepted, on `main`)
- Python 3.10+

### Exclusions (remain out of Phase 8.2 implementation)

- Module discovery and `module.yaml` validation (8.3)
- Markdown / documentation integrity (8.4)
- CI job integration (8.5)
- Final audit (8.6)
- `aiosctl validate` command (not required by this design; structure runs via `python -m validation`)
- Content-level checks inside required files
- Enforcement of optional or reserved path presence
- Additional CLI flags beyond `--root`
- New governance decisions beyond this canonical design

---

## Document control

| Item | Value |
|------|--------|
| Document id | `FRAMEWORK_STRUCTURE_VALIDATION_DESIGN` |
| Phase | 8.2 |
| Kind | **Canonical design** |
| Companion runtime doc (implementation phase) | `docs/FRAMEWORK_STRUCTURE_VALIDATION.md` (not created by this design-documentation task) |
