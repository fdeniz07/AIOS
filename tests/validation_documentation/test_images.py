"""Markdown and HTML image validation."""

from __future__ import annotations

from pathlib import Path

from .conftest import codes, run_doc, write_md


def test_markdown_image_valid(framework: Path):
    assets = framework / "docs" / "pic.png"
    assets.parent.mkdir(parents=True, exist_ok=True)
    assets.write_bytes(b"\x89PNG\r\n\x1a\n")
    write_md(framework, "docs/a.md", "![pic](pic.png)\n")
    result = run_doc(framework)
    assert "DOC-006" not in codes(result)


def test_markdown_image_missing_doc006(framework: Path):
    write_md(framework, "docs/a.md", "![pic](gone.png)\n")
    result = run_doc(framework)
    assert "DOC-006" in codes(result)
    assert result.exit_code() == 1


def test_html_image_missing_doc006(framework: Path):
    write_md(framework, "docs/a.md", '<img src="gone.png">\n')
    result = run_doc(framework)
    assert "DOC-006" in codes(result)


def test_html_image_valid(framework: Path):
    img = framework / "docs" / "ok.png"
    img.parent.mkdir(parents=True, exist_ok=True)
    img.write_bytes(b"x")
    write_md(framework, "docs/a.md", '<img src="ok.png" alt="x">\n')
    result = run_doc(framework)
    assert "DOC-006" not in codes(result)


def test_external_image_skipped(framework: Path):
    write_md(framework, "docs/a.md", "![x](https://example.com/x.png)\n")
    result = run_doc(framework)
    assert codes(result) == []
