"""Orchestrator integration for Module Contract execution failures."""

from __future__ import annotations

import os
from pathlib import Path

from validation.models import EXIT_EXECUTION_FAILURE, Severity
from validation.module_contract import ModuleFileSystem, make_module_contract_runner
from validation.orchestrator import Orchestrator

from .conftest import complete_draft, write_module


def test_mod021_through_runner_and_orchestrator_exit_2(framework: Path):
    write_module(framework, "sample-module", complete_draft())
    target = framework / "modules" / "sample-module" / "module.yaml"

    class BoomFS(ModuleFileSystem):
        def lstat(self, path: Path) -> os.stat_result:
            if path == target:
                raise PermissionError("denied")
            return super().lstat(path)

    orchestrator = Orchestrator()
    orchestrator.register(
        "module-contract",
        make_module_contract_runner(explicit_root=framework, fs=BoomFS()),
    )
    result = orchestrator.run()

    assert result.execution_error is not None
    assert result.exit_code() == EXIT_EXECUTION_FAILURE
    assert result.exit_code() == 2
    mod021 = [f for f in result.findings if f.code == "MOD-021"]
    assert len(mod021) == 1
    assert mod021[0].severity is Severity.ERROR
    assert mod021[0].category == "module-contract"
