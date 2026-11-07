"""Supplementary expectations from design §13."""

from __future__ import annotations

from pathlib import Path

import pytest

from validation.framework_structure import (
    ROOT_MARKERS,
    FileSystem,
    PathInspection,
    PathKind,
    evaluate_candidate,
    make_framework_structure_runner,
    validate_framework_structure,
)
from validation.models import Severity
from validation.orchestrator import Orchestrator, ValidatorAbortError

from .conftest import write_minimal_framework


def test_github_absent_ok(minimal_root: Path):
    assert not (minimal_root / ".github").exists()
    result = validate_framework_structure(explicit_root=minimal_root)
    assert result.exit_code() == 0
    assert result.findings == ()


def test_github_directory_ok(minimal_root: Path):
    (minimal_root / ".github").mkdir()
    result = validate_framework_structure(explicit_root=minimal_root)
    assert result.exit_code() == 0
    assert result.findings == ()


def test_github_nondirectory_str007(minimal_root: Path):
    (minimal_root / ".github").write_text("file\n", encoding="utf-8")
    result = validate_framework_structure(explicit_root=minimal_root)
    assert result.exit_code() == 1
    assert len(result.findings) == 1
    f = result.findings[0]
    assert f.code == "STR-007"
    assert f.rule == "STR-007"
    assert f.path == ".github"
    assert f.message == "Conditional path .github must be a directory when present."
    assert f.category == "framework-structure"
    assert f.severity is Severity.ERROR


def test_github_uninspectable_str006(minimal_root: Path):
    class BoomFS(FileSystem):
        def inspect(self, path: Path) -> PathInspection:
            if path.name == ".github":
                return PathInspection(PathKind.ERROR, "OSError")
            return super().inspect(path)

    result = validate_framework_structure(explicit_root=minimal_root, fs=BoomFS())
    assert result.exit_code() == 2
    assert any(f.code == "STR-006" and f.path == ".github" for f in result.findings)


def test_explicit_root_missing_str008(tmp_path: Path):
    missing = tmp_path / "nope"
    result = validate_framework_structure(explicit_root=missing)
    assert result.exit_code() == 1
    f = result.findings[0]
    assert f.code == "STR-008"
    assert "missing or not a directory" in f.message


def test_explicit_root_nondirectory_str008(tmp_path: Path):
    file_root = tmp_path / "file-root"
    file_root.write_text("x\n", encoding="utf-8")
    result = validate_framework_structure(explicit_root=file_root)
    assert result.exit_code() == 1
    assert result.findings[0].code == "STR-008"


def test_explicit_root_fewer_than_two_markers_str009(tmp_path: Path):
    root = tmp_path / "partial"
    root.mkdir()
    (root / "VERSION").write_text("1\n", encoding="utf-8")
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 1
    assert result.execution_error is None
    f = result.findings[0]
    assert f.code == "STR-009"
    assert "fewer than two root markers" in f.message
    assert f.rule == "STR-009"


def test_explicit_root_marker_inspection_failure_no_str009(tmp_path: Path):
    root = tmp_path / "partial"
    root.mkdir()
    (root / "VERSION").write_text("1\n", encoding="utf-8")

    class BoomFS(FileSystem):
        def inspect(self, path: Path) -> PathInspection:
            if path.name == "MANIFEST.md":
                return PathInspection(PathKind.ERROR, "PermissionError")
            return super().inspect(path)

    result = validate_framework_structure(explicit_root=root, fs=BoomFS())
    assert result.exit_code() == 2
    assert any(f.code == "STR-006" for f in result.findings)
    assert not any(f.code == "STR-009" for f in result.findings)


def test_upward_discovery_marker_inspection_failure(tmp_path: Path):
    start = tmp_path / "a" / "b"
    start.mkdir(parents=True)

    class BoomFS(FileSystem):
        def inspect(self, path: Path) -> PathInspection:
            if path.name == "VERSION":
                return PathInspection(PathKind.ERROR, "OSError")
            return super().inspect(path)

    result = validate_framework_structure(start=start, fs=BoomFS())
    assert result.exit_code() == 2
    assert any(f.code == "STR-006" for f in result.findings)
    assert not any(f.code == "STR-005" for f in result.findings)


def test_agents_ignored(minimal_root: Path):
    agents = minimal_root / ".agents"
    agents.mkdir()
    (agents / "x.md").write_text("x\n", encoding="utf-8")
    # Wrong type also ignored.
    result = validate_framework_structure(explicit_root=minimal_root)
    assert result.exit_code() == 0
    assert result.findings == ()


def test_marker_directory_does_not_count(tmp_path: Path):
    root = tmp_path / "root"
    root.mkdir()
    (root / "VERSION").mkdir()  # directory — does not count
    (root / "MANIFEST.md").write_text("m\n", encoding="utf-8")
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 1
    assert result.findings[0].code == "STR-009"


def test_early_success_stops_marker_inspection(tmp_path: Path):
    root = tmp_path / "root"
    root.mkdir()
    (root / "VERSION").write_text("1\n", encoding="utf-8")
    (root / "MANIFEST.md").write_text("m\n", encoding="utf-8")
    inspected: list[str] = []

    class TrackingFS(FileSystem):
        def inspect(self, path: Path) -> PathInspection:
            try:
                rel = path.relative_to(root).as_posix()
            except ValueError:
                rel = path.name
            if rel in ROOT_MARKERS or path.name in {
                "VERSION",
                "MANIFEST.md",
                "PROJECT_STRUCTURE.md",
                "FRAMEWORK_CONTRACT.md",
            }:
                inspected.append(rel)
            return super().inspect(path)

    outcome = evaluate_candidate(root, TrackingFS())
    assert outcome.status.value == "candidate"
    assert inspected == ["VERSION", "MANIFEST.md"]
    assert "PROJECT_STRUCTURE.md" not in inspected
    assert "docs/FRAMEWORK_CONTRACT.md" not in inspected


def test_early_success_unchecked_marker_error_irrelevant(tmp_path: Path):
    root = tmp_path / "root"
    root.mkdir()
    (root / "VERSION").write_text("1\n", encoding="utf-8")
    (root / "MANIFEST.md").write_text("m\n", encoding="utf-8")

    class BoomLaterFS(FileSystem):
        def inspect(self, path: Path) -> PathInspection:
            try:
                rel = path.relative_to(root).as_posix()
            except ValueError:
                rel = ""
            if rel in ("PROJECT_STRUCTURE.md", "docs/FRAMEWORK_CONTRACT.md"):
                return PathInspection(PathKind.ERROR, "PermissionError")
            return super().inspect(path)

    outcome = evaluate_candidate(root, BoomLaterFS())
    assert outcome.status.value == "candidate"
    assert outcome.findings == []
    assert outcome.execution_error is None


def test_marker_error_before_two_valid_incomplete(tmp_path: Path):
    root = tmp_path / "root"
    root.mkdir()
    (root / "VERSION").write_text("1\n", encoding="utf-8")

    class BoomFS(FileSystem):
        def inspect(self, path: Path) -> PathInspection:
            if path.name == "MANIFEST.md":
                return PathInspection(PathKind.ERROR, "PermissionError")
            return super().inspect(path)

    outcome = evaluate_candidate(root, BoomFS())
    assert outcome.status.value == "incomplete"
    assert outcome.execution_error is not None
    assert outcome.findings[0].code == "STR-006"


def test_unresolved_nearer_ancestor_blocks_higher(tmp_path: Path):
    higher = write_minimal_framework(tmp_path / "higher")
    nearer = higher / "nearer"
    nearer.mkdir()
    start = nearer / "work"
    start.mkdir()

    class BoomNearerFS(FileSystem):
        def inspect(self, path: Path) -> PathInspection:
            try:
                # Only boom marker inspection under nearer, not under higher.
                if nearer in path.parents or path.parent == nearer:
                    if path.name in {"VERSION", "MANIFEST.md", "PROJECT_STRUCTURE.md"} or (
                        path.name == "FRAMEWORK_CONTRACT.md"
                    ):
                        return PathInspection(PathKind.ERROR, "OSError")
            except Exception:
                pass
            return super().inspect(path)

    result = validate_framework_structure(start=start, fs=BoomNearerFS())
    assert result.exit_code() == 2
    assert any(f.code == "STR-006" for f in result.findings)
    # Must not silently validate against higher (which would be exit 0).
    assert result.exit_code() != 0


@pytest.mark.skipif(
    not hasattr(Path, "symlink_to"),
    reason="symlink API unavailable",
)
def test_symlink_file_target_accepted(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    real = tmp_path / "real_readme.md"
    real.write_text("linked\n", encoding="utf-8")
    target = root / "README.md"
    target.unlink()
    try:
        target.symlink_to(real)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 0


@pytest.mark.skipif(
    not hasattr(Path, "symlink_to"),
    reason="symlink API unavailable",
)
def test_symlink_directory_target_accepted(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    real = tmp_path / "real_rules"
    real.mkdir()
    target = root / "rules"
    # remove empty dir
    target.rmdir()
    try:
        target.symlink_to(real, target_is_directory=True)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 0


@pytest.mark.skipif(
    not hasattr(Path, "symlink_to"),
    reason="symlink API unavailable",
)
def test_symlink_wrong_type_str003(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    real_dir = tmp_path / "dir_target"
    real_dir.mkdir()
    target = root / "VERSION"
    target.unlink()
    try:
        target.symlink_to(real_dir, target_is_directory=True)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 1
    assert any(f.code == "STR-003" and f.path == "VERSION" for f in result.findings)


@pytest.mark.skipif(
    not hasattr(Path, "symlink_to"),
    reason="symlink API unavailable",
)
def test_broken_symlink_str003_not_marker(tmp_path: Path):
    root = tmp_path / "root"
    root.mkdir()
    missing = tmp_path / "missing-target"
    try:
        (root / "VERSION").symlink_to(missing)
        (root / "MANIFEST.md").symlink_to(missing)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    (root / "PROJECT_STRUCTURE.md").write_text("p\n", encoding="utf-8")
    # Only one valid marker → STR-009
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 1
    assert result.findings[0].code == "STR-009"


@pytest.mark.skipif(
    not hasattr(Path, "symlink_to"),
    reason="symlink API unavailable",
)
def test_broken_symlink_required_file_str003(tmp_path: Path):
    root = write_minimal_framework(tmp_path / "fw")
    missing = tmp_path / "gone"
    target = root / "ROADMAP.md"
    target.unlink()
    try:
        target.symlink_to(missing)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    result = validate_framework_structure(explicit_root=root)
    assert result.exit_code() == 1
    assert any(f.code == "STR-003" and f.path == "ROADMAP.md" for f in result.findings)


def test_injected_inspect_error_on_required_file_str006(minimal_root: Path):
    """BoomFS overrides inspect() — not a real symlink scenario (see M2 suite)."""

    class BoomFS(FileSystem):
        def inspect(self, path: Path) -> PathInspection:
            if path.name == "AGENTS.md":
                return PathInspection(PathKind.ERROR, "OSError")
            return super().inspect(path)

    result = validate_framework_structure(explicit_root=minimal_root, fs=BoomFS())
    assert result.exit_code() == 2
    assert any(f.code == "STR-006" and f.path == "AGENTS.md" for f in result.findings)


def test_runner_raises_validator_abort_on_execution_error(minimal_root: Path):
    class BoomFS(FileSystem):
        def inspect(self, path: Path) -> PathInspection:
            if path.name == "README.md":
                return PathInspection(PathKind.ERROR, "OSError")
            return super().inspect(path)

    runner = make_framework_structure_runner(explicit_root=minimal_root, fs=BoomFS())
    orch = Orchestrator()
    orch.register("framework-structure", runner)
    result = orch.run()
    assert result.exit_code() == 2
    assert any(f.code == "STR-006" for f in result.findings)
    assert result.execution_error is not None


def test_validator_abort_error_preserves_findings():
    finding_codes: list[str] = []

    def boom():
        from validation.models import Finding

        findings = [
            Finding(
                "STR-006",
                Severity.ERROR,
                "framework-structure",
                "Framework path or discovery marker could not be inspected: x (OSError)",
                path="x",
                rule="STR-006",
            )
        ]
        raise ValidatorAbortError("fail", findings)

    orch = Orchestrator()
    orch.register("framework-structure", boom)
    result = orch.run()
    assert result.exit_code() == 2
    assert [f.code for f in result.findings] == ["STR-006"]
    finding_codes.extend(f.code for f in result.findings)
    assert finding_codes == ["STR-006"]
