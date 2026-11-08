"""Markdown discovery behavior."""

from __future__ import annotations

from pathlib import Path

import pytest

from validation.documentation_integrity import DocFileSystem, _discover_markdown_files

from .conftest import codes, run_doc, write_md


def test_discovers_markdown_outside_docs(framework: Path):
    write_md(framework, "README.md", "# Root\n")
    write_md(framework, "docs/guide.md", "# Guide\n")
    write_md(framework, "modules/x/README.md", "# Module\n")
    write_md(framework, "notes.MARKDOWN", "# Upper\n")
    result = run_doc(framework)
    assert result.exit_code() == 0
    discovered = _discover_markdown_files(framework, DocFileSystem())
    rels = [str(p.relative_to(framework)).replace("\\", "/").lower() for p in discovered]
    assert "readme.md" in rels
    assert "docs/guide.md" in rels
    assert "modules/x/readme.md" in rels
    assert "notes.markdown" in rels


def test_discovery_skips_git_and_is_deterministic(framework: Path):
    write_md(framework, "a.md", "# A\n")
    write_md(framework, "b.md", "# B\n")
    git_dir = framework / ".git"
    git_dir.mkdir()
    write_md(framework, ".git/secret.md", "# Secret\n")
    fs = DocFileSystem()
    first = [str(p) for p in _discover_markdown_files(framework, fs)]
    second = [str(p) for p in _discover_markdown_files(framework, fs)]
    assert first == second
    assert not any(".git" in p.replace("\\", "/") for p in first)


def test_discovery_does_not_recurse_directory_symlink(framework: Path, tmp_path: Path):
    external = tmp_path / "external"
    external.mkdir()
    write_md(external, "hidden.md", "# Hidden\n")
    link = framework / "linked-docs"
    try:
        link.symlink_to(external, target_is_directory=True)
    except OSError as exc:
        pytest.skip(f"symlinks unavailable: {exc}")
    write_md(framework, "visible.md", "# Visible\n")
    discovered = _discover_markdown_files(framework, DocFileSystem())
    names = [p.name.lower() for p in discovered]
    assert "visible.md" in names
    assert "hidden.md" not in names


def test_valid_same_directory_and_nested_links(framework: Path):
    write_md(framework, "docs/a.md", "[b](b.md)\n[nested](sub/c.md)\n")
    write_md(framework, "docs/b.md", "# B\n")
    write_md(framework, "docs/sub/c.md", "# C\n")
    result = run_doc(framework)
    assert codes(result) == []
    assert result.exit_code() == 0
