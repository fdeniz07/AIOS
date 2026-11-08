"""Orchestrator integration for Documentation Integrity."""

from __future__ import annotations

import os
from pathlib import Path

from validation.documentation_integrity import (
    DocFileSystem,
    make_documentation_integrity_runner,
)
from validation.models import EXIT_EXECUTION_FAILURE, Severity
from validation.orchestrator import Orchestrator

from .conftest import write_md


def test_doc005_through_runner_and_orchestrator_exit_2(framework: Path):
    write_md(framework, "docs/a.md", "# Ok\n")
    target = framework / "docs" / "a.md"

    class BoomFS(DocFileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == target:
                raise PermissionError("denied")
            return super().lstat(path)

    orchestrator = Orchestrator()
    orchestrator.register(
        "documentation-integrity",
        make_documentation_integrity_runner(explicit_root=framework, fs=BoomFS()),
    )
    result = orchestrator.run()

    assert result.execution_error is not None
    assert result.exit_code() == EXIT_EXECUTION_FAILURE
    assert result.exit_code() == 2
    doc005 = [f for f in result.findings if f.code == "DOC-005"]
    assert len(doc005) == 1
    assert doc005[0].severity is Severity.ERROR
    assert doc005[0].category == "documentation-integrity"


def test_default_orchestrator_runs_three_validators(tmp_path: Path):
    from tests.validation_structure.conftest import write_minimal_framework
    from validation.__main__ import build_default_orchestrator

    root = write_minimal_framework(tmp_path / "fw")
    write_md(root, "docs/ok.md", "# Ok\n")
    orch = build_default_orchestrator(explicit_root=root)
    assert orch.validator_names == (
        "documentation-integrity",
        "framework-structure",
        "module-contract",
    )
    result = orch.run()
    assert result.execution_error is None
    assert result.exit_code() == 0
