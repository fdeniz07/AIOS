"""Metadata field validation, precedence R8, and D8 draft leniency."""

from __future__ import annotations

from pathlib import Path

from validation.models import Severity

from .conftest import complete_draft, codes, run_mod, write_module


def _finding_map(result):
    return {(f.code, f.path): f for f in result.findings}


def test_complete_draft_clean(framework: Path):
    write_module(framework, "sample-module", complete_draft())
    result = run_mod(framework)
    assert result.findings == ()
    assert result.exit_code() == 0


def test_missing_module_yaml_mod001_no_field_validation(framework: Path):
    write_module(framework, "sample-module", None, write_yaml=False)
    result = run_mod(framework)
    assert "MOD-001" in codes(result)
    assert "MOD-004" not in codes(result)
    assert "MOD-002" not in codes(result)
    assert "MOD-012" not in codes(result)


def test_module_yaml_directory_mod001(framework: Path):
    pkg = framework / "modules" / "sample-module"
    pkg.mkdir(parents=True)
    (pkg / "module.yaml").mkdir()
    (pkg / "README.md").write_text("# x\n", encoding="utf-8")
    result = run_mod(framework)
    assert "MOD-001" in codes(result)
    assert "MOD-003" not in codes(result)
    assert "MOD-004" not in codes(result)


def test_unparseable_yaml_mod003_no_fields(framework: Path):
    pkg = framework / "modules" / "sample-module"
    pkg.mkdir(parents=True)
    (pkg / "module.yaml").write_text(": not: valid: [[\n", encoding="utf-8")
    (pkg / "README.md").write_text("# x\n", encoding="utf-8")
    result = run_mod(framework)
    assert "MOD-003" in codes(result)
    assert "MOD-004" not in codes(result)
    assert "MOD-002" not in codes(result)


def test_root_not_mapping_mod003(framework: Path):
    pkg = framework / "modules" / "sample-module"
    pkg.mkdir(parents=True)
    (pkg / "module.yaml").write_text("- just\n- a\n- list\n", encoding="utf-8")
    (pkg / "README.md").write_text("# x\n", encoding="utf-8")
    result = run_mod(framework)
    assert "MOD-003" in codes(result)


def test_draft_missing_required_fields_are_warnings(framework: Path):
    write_module(
        framework,
        "sample-module",
        {"status": "draft"},
    )
    result = run_mod(framework)
    mod004 = [f for f in result.findings if f.code == "MOD-004"]
    fields = {f.message for f in mod004}
    assert any("id" in m for m in fields)
    assert any("version" in m for m in fields)
    assert any("title" in m for m in fields)
    assert any("summary" in m for m in fields)
    assert all(f.severity is Severity.WARNING for f in mod004)
    assert result.exit_code() == 0


def test_active_missing_required_fields_are_errors(framework: Path):
    write_module(framework, "sample-module", {"status": "active"})
    result = run_mod(framework)
    mod004 = [f for f in result.findings if f.code == "MOD-004"]
    assert mod004
    assert all(f.severity is Severity.ERROR for f in mod004)
    assert result.exit_code() == 1


def test_unknown_status_missing_fields_are_errors(framework: Path):
    write_module(framework, "sample-module", {"status": "experimental-oops"})
    result = run_mod(framework)
    assert any(f.code == "MOD-008" for f in result.findings)
    mod004 = [f for f in result.findings if f.code == "MOD-004"]
    # status present but invalid → no MOD-004 for status; id/version/title/summary Error
    assert mod004
    assert all(f.severity is Severity.ERROR for f in mod004)
    assert "MOD-002" not in codes(result)


def test_missing_status_is_error_and_unknown(framework: Path):
    data = complete_draft()
    del data["status"]
    write_module(framework, "sample-module", data, readme=None)
    result = run_mod(framework)
    status_findings = [
        f for f in result.findings if f.code == "MOD-004" and "status" in f.message
    ]
    assert status_findings
    assert status_findings[0].severity is Severity.ERROR
    assert "MOD-002" not in codes(result)


def test_wrong_type_status_int_mod005_unknown_lifecycle(framework: Path):
    write_module(
        framework,
        "sample-module",
        {
            "status": 1,
            "id": "sample-module",
            "version": "1.0.0",
            "title": "T",
            "summary": "S",
            "applies_when": ["a"],
            "avoid_when": ["b"],
        },
        readme=None,
    )
    result = run_mod(framework)
    assert any(
        f.code == "MOD-005" and "status" in f.message for f in result.findings
    )
    assert "MOD-002" not in codes(result)
    assert "MOD-012" not in codes(result)


def test_wrong_type_status_list_mod005_unknown_lifecycle(framework: Path):
    write_module(
        framework,
        "sample-module",
        {
            "status": [],
            "id": "sample-module",
            "version": "1.0.0",
            "title": "T",
            "summary": "S",
            "applies_when": ["a"],
            "avoid_when": ["b"],
        },
        readme=None,
    )
    result = run_mod(framework)
    assert any(
        f.code == "MOD-005" and "status" in f.message for f in result.findings
    )
    assert "MOD-002" not in codes(result)
    assert "MOD-012" not in codes(result)


def test_draft_invalid_semver_still_error(framework: Path):
    write_module(
        framework,
        "sample-module",
        complete_draft(version="not-a-version"),
    )
    result = run_mod(framework)
    assert any(f.code == "MOD-007" and f.severity is Severity.ERROR for f in result.findings)


def test_invalid_maturity_mod009(framework: Path):
    write_module(
        framework,
        "sample-module",
        complete_draft(maturity="production"),
    )
    result = run_mod(framework)
    assert "MOD-009" in codes(result)


def test_invalid_id_format_mod006(framework: Path):
    write_module(framework, "sample-module", complete_draft(id="Bad_ID"))
    result = run_mod(framework)
    assert "MOD-006" in codes(result)


def test_dependencies_mod010_not_mod013(framework: Path):
    data = complete_draft()
    data["dependencies"] = []
    write_module(framework, "sample-module", data)
    result = run_mod(framework)
    assert "MOD-010" in codes(result)
    assert "MOD-013" not in codes(result)


def test_unknown_field_mod013(framework: Path):
    data = complete_draft()
    data["owner_team"] = "platform"
    write_module(framework, "sample-module", data)
    result = run_mod(framework)
    assert "MOD-013" in codes(result)


def test_missing_applies_when_avoid_when_mod014(framework: Path):
    data = complete_draft()
    del data["applies_when"]
    del data["avoid_when"]
    write_module(framework, "sample-module", data)
    result = run_mod(framework)
    mod014 = [f for f in result.findings if f.code == "MOD-014"]
    assert len(mod014) == 2


def test_wrong_type_list_mod005(framework: Path):
    write_module(
        framework,
        "sample-module",
        complete_draft(tags="not-a-list"),
    )
    result = run_mod(framework)
    assert any(
        f.code == "MOD-005" and "tags" in f.message for f in result.findings
    )


def test_non_kebab_tags_mod023(framework: Path):
    write_module(
        framework,
        "sample-module",
        complete_draft(tags=["ok-tag", "BadTag"]),
    )
    result = run_mod(framework)
    assert "MOD-023" in codes(result)


def test_dir_name_mismatch_mod017(framework: Path):
    write_module(
        framework,
        "sample-module",
        complete_draft(id="other-id"),
    )
    result = run_mod(framework)
    assert "MOD-017" in codes(result)


def test_r8_precedence_missing_beats_format(framework: Path):
    """Empty id → MOD-004 only, not MOD-006."""
    write_module(
        framework,
        "sample-module",
        complete_draft(id=""),
    )
    result = run_mod(framework)
    id_related = [
        f
        for f in result.findings
        if f.code in {"MOD-004", "MOD-005", "MOD-006"} and "id" in f.message.lower()
    ]
    assert len(id_related) == 1
    assert id_related[0].code == "MOD-004"


def test_deprecation_when_not_deprecated_mod011(framework: Path):
    data = complete_draft(status="active")
    data["deprecation"] = {"reason": "x"}
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Active\n",
    )
    result = run_mod(framework)
    assert "MOD-011" in codes(result)


def test_deprecated_without_deprecation_object_no_finding(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nMove on.\n",
    )
    result = run_mod(framework)
    assert "MOD-011" not in codes(result)
    assert "MOD-016" not in codes(result)


def test_deprecated_maturity_present_mod015(framework: Path):
    data = complete_draft(status="deprecated", maturity="stable")
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nMove on.\n",
    )
    result = run_mod(framework)
    assert "MOD-015" in codes(result)


def test_deprecation_missing_reason_mod016(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    data["deprecation"] = {"successor": "other-module"}
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nMove on.\n",
    )
    result = run_mod(framework)
    assert "MOD-016" in codes(result)


def test_invalid_successor_mod022(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    data["deprecation"] = {"reason": "done", "successor": "Not_Kebab"}
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nMove on.\n",
    )
    result = run_mod(framework)
    assert "MOD-022" in codes(result)


def test_invalid_sunset_mod025(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    data["deprecation"] = {"reason": "done", "sunset": "31-12-2027"}
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nMove on.\n",
    )
    result = run_mod(framework)
    assert "MOD-025" in codes(result)


def test_sunset_impossible_calendar_date_mod025(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    data["deprecation"] = {"reason": "done", "sunset": "2026-02-31"}
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nMove on.\n",
    )
    result = run_mod(framework)
    assert "MOD-025" in codes(result)


def test_sunset_april_31_mod025(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    data["deprecation"] = {"reason": "done", "sunset": "2025-04-31"}
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nMove on.\n",
    )
    result = run_mod(framework)
    assert "MOD-025" in codes(result)


def test_sunset_year_zero_mod025(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    data["deprecation"] = {"reason": "done", "sunset": "0000-01-01"}
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nMove on.\n",
    )
    result = run_mod(framework)
    assert "MOD-025" in codes(result)


def test_sunset_valid_leap_day_ok(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    data["deprecation"] = {"reason": "done", "sunset": "2024-02-29"}
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nMove on.\n",
    )
    result = run_mod(framework)
    assert "MOD-025" not in codes(result)


def test_sunset_invalid_leap_day_mod025(framework: Path):
    data = complete_draft(status="deprecated")
    data.pop("maturity", None)
    data["deprecation"] = {"reason": "done", "sunset": "2025-02-29"}
    write_module(
        framework,
        "sample-module",
        data,
        readme="# Deprecated\n\n## Migration\n\nMove on.\n",
    )
    result = run_mod(framework)
    assert "MOD-025" in codes(result)


def test_empty_applies_when_items_allowed(framework: Path):
    write_module(
        framework,
        "sample-module",
        complete_draft(applies_when=["", "ok"]),
    )
    result = run_mod(framework)
    assert "MOD-005" not in codes(result)
