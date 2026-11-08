"""Inline, reference-style, directory, encoded, and external link checks."""

from __future__ import annotations

from pathlib import Path

from .conftest import codes, run_doc, write_md


def test_inline_link_missing_doc001(framework: Path):
    write_md(framework, "docs/a.md", "See [missing](nope.md).\n")
    result = run_doc(framework)
    assert "DOC-001" in codes(result)
    assert result.exit_code() == 1


def test_reference_style_link_missing_doc001(framework: Path):
    write_md(
        framework,
        "docs/a.md",
        "See [label][ref].\n\n[ref]: missing-target.md\n",
    )
    result = run_doc(framework)
    assert "DOC-001" in codes(result)


def test_reference_style_link_valid(framework: Path):
    write_md(framework, "docs/a.md", "See [label][ref].\n\n[ref]: b.md\n")
    write_md(framework, "docs/b.md", "# B\n")
    result = run_doc(framework)
    assert "DOC-001" not in codes(result)
    assert result.exit_code() == 0


def test_parent_directory_link(framework: Path):
    write_md(framework, "docs/sub/a.md", "[up](../b.md)\n")
    write_md(framework, "docs/b.md", "# B\n")
    result = run_doc(framework)
    assert codes(result) == []


def test_directory_link_valid(framework: Path):
    (framework / "docs" / "guide").mkdir(parents=True)
    write_md(framework, "docs/a.md", "[guide](guide/)\n")
    result = run_doc(framework)
    assert "DOC-001" not in codes(result)
    assert "DOC-002" not in codes(result)


def test_incompatible_target_type_doc002(framework: Path):
    # Image pointing at a directory → incompatible type.
    (framework / "docs" / "assets").mkdir(parents=True)
    write_md(framework, "docs/a.md", "![x](assets)\n")
    result = run_doc(framework)
    assert "DOC-002" in codes(result)


def test_url_encoded_path(framework: Path):
    write_md(framework, "docs/my file.md", "# Encoded\n")
    write_md(framework, "docs/a.md", "[x](my%20file.md)\n")
    result = run_doc(framework)
    assert "DOC-001" not in codes(result)


def test_external_urls_skipped(framework: Path):
    write_md(
        framework,
        "docs/a.md",
        "\n".join(
            [
                "[h](https://example.com/missing)",
                "[m](mailto:dev@example.com)",
                "[t](tel:+123456789)",
                "[http](http://example.com)",
            ]
        )
        + "\n",
    )
    result = run_doc(framework)
    assert codes(result) == []
    assert result.exit_code() == 0


def test_code_fence_exclusion(framework: Path):
    write_md(
        framework,
        "docs/a.md",
        "```\n[not-real](missing.md)\n```\n\nReal text.\n",
    )
    result = run_doc(framework)
    assert "DOC-001" not in codes(result)


def test_path_traversal_doc003(framework: Path):
    write_md(framework, "docs/a.md", "[x](../../outside.md)\n")
    result = run_doc(framework)
    assert "DOC-003" in codes(result)
    assert result.exit_code() == 1
