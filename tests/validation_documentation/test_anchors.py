"""Anchor / heading slug validation."""

from __future__ import annotations

from pathlib import Path

from validation.documentation_integrity import github_heading_slug, unique_slug

from .conftest import codes, run_doc, write_md


def test_github_slug_basic_and_punctuation():
    assert github_heading_slug("Hello World") == "hello-world"
    assert github_heading_slug("Hello, World!") == "hello-world"
    assert github_heading_slug("  Trimmed  ") == "trimmed"


def test_github_slug_unicode_german_turkish():
    assert github_heading_slug("Über Äpfel") == "über-äpfel"
    assert github_heading_slug("Türkçe Başlık") == "türkçe-başlık"
    assert github_heading_slug("Straße öffnen") == "straße-öffnen"
    # Capital Turkish İ lowercases to i + combining dot (U+0307) in Python;
    # document that behavior rather than inventing a locale-specific mapping.
    slug = github_heading_slug("ĞÜŞİÖÇ ığüşiöç")
    assert slug.startswith("ğüş")
    assert "ığüşiöç" in slug
    assert github_heading_slug("çağdaş çözüm") == "çağdaş-çözüm"


def test_duplicate_heading_slugs():
    seen: dict[str, int] = {}
    assert unique_slug(github_heading_slug("Same"), seen) == "same"
    assert unique_slug(github_heading_slug("Same"), seen) == "same-1"
    assert unique_slug(github_heading_slug("Same"), seen) == "same-2"


def test_valid_anchor(framework: Path):
    write_md(
        framework,
        "docs/a.md",
        "# Hello World\n\nSee [section](#hello-world).\n",
    )
    result = run_doc(framework)
    assert "DOC-004" not in codes(result)


def test_invalid_anchor_doc004(framework: Path):
    write_md(framework, "docs/a.md", "# Title\n\n[bad](#missing-anchor).\n")
    result = run_doc(framework)
    assert "DOC-004" in codes(result)


def test_duplicate_heading_anchors(framework: Path):
    write_md(
        framework,
        "docs/a.md",
        "# Dup\n\n# Dup\n\n[first](#dup)\n[second](#dup-1)\n[bad](#dup-2)\n",
    )
    result = run_doc(framework)
    assert "DOC-004" in codes(result)
    messages = " ".join(f.message for f in result.findings if f.code == "DOC-004")
    assert "#dup-2" in messages or "dup-2" in messages


def test_explicit_html_anchors(framework: Path):
    write_md(
        framework,
        "docs/a.md",
        '<a id="custom-id"></a>\n<a name="named-anchor"></a>\n\n'
        "[a](#custom-id)\n[b](#named-anchor)\n",
    )
    result = run_doc(framework)
    assert "DOC-004" not in codes(result)


def test_unicode_heading_anchor_link(framework: Path):
    write_md(
        framework,
        "docs/a.md",
        "# Türkçe Başlık\n\n[go](#türkçe-başlık)\n",
    )
    result = run_doc(framework)
    assert "DOC-004" not in codes(result)


def test_empty_fragment_ok(framework: Path):
    write_md(framework, "docs/a.md", "[top](#)\n")
    result = run_doc(framework)
    assert "DOC-004" not in codes(result)


def test_cross_file_anchor(framework: Path):
    write_md(framework, "docs/b.md", "# Target Section\n")
    write_md(framework, "docs/a.md", "[x](b.md#target-section)\n[y](b.md#missing)\n")
    result = run_doc(framework)
    assert any(
        f.code == "DOC-004" and "missing" in (f.message + (f.path or ""))
        for f in result.findings
    )
    assert not any(
        f.code == "DOC-004" and "target-section" in f.message for f in result.findings
    )
