"""Orchestrator behavior tests."""

from __future__ import annotations

from validation.models import Finding, Severity
from validation.orchestrator import Orchestrator


def _finding(code: str, rule: str = "r", path: str = "p") -> Finding:
    return Finding(
        code=code,
        severity=Severity.INFO,
        category="test",
        message=code,
        rule=rule,
        path=path,
    )


def test_no_validators_returns_empty_ok():
    result = Orchestrator([]).run()
    assert result.findings == ()
    assert result.execution_error is None
    assert result.exit_code() == 0


def test_one_validator():
    orch = Orchestrator()
    orch.register("only", lambda: [_finding("one")])
    result = orch.run()
    assert [f.code for f in result.findings] == ["one"]


def test_multiple_validators_aggregate():
    orch = Orchestrator()
    orch.register("a", lambda: [_finding("from-a", rule="ra")])
    orch.register("b", lambda: [_finding("from-b", rule="rb")])
    result = orch.run()
    assert {f.code for f in result.findings} == {"from-a", "from-b"}


def test_deterministic_execution_order_by_name():
    order: list[str] = []

    def make(name: str):
        def _run():
            order.append(name)
            return []

        return _run

    orch = Orchestrator()
    orch.register("zeta", make("zeta"))
    orch.register("alpha", make("alpha"))
    orch.register("middle", make("middle"))
    orch.run()
    assert order == ["alpha", "middle", "zeta"]


def test_validator_execution_failure_exit_two():
    def boom():
        raise RuntimeError("explode")

    orch = Orchestrator()
    orch.register("ok", lambda: [_finding("kept", rule="keep")])
    orch.register("bad", boom)
    # "bad" runs before "ok" alphabetically — failure before ok collects
    result = orch.run()
    assert result.exit_code() == 2
    assert result.execution_error is not None
    assert "bad" in result.execution_error


def test_validator_failure_preserves_prior_findings():
    def boom():
        raise RuntimeError("explode")

    orch = Orchestrator()
    orch.register("a_first", lambda: [_finding("kept", rule="keep")])
    orch.register("z_fail", boom)
    result = orch.run()
    assert result.exit_code() == 2
    assert [f.code for f in result.findings] == ["kept"]


def test_finding_aggregation_across_validators_dedupes():
    orch = Orchestrator()
    orch.register(
        "a",
        lambda: [
            Finding(
                "soft",
                Severity.INFO,
                "test",
                "info",
                rule="same",
                path="x",
            )
        ],
    )
    orch.register(
        "b",
        lambda: [
            Finding(
                "hard",
                Severity.ERROR,
                "test",
                "error",
                rule="same",
                path="x",
            )
        ],
    )
    result = orch.run()
    assert len(result.findings) == 1
    assert result.findings[0].severity is Severity.ERROR
