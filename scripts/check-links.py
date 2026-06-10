#!/usr/bin/env python3
"""
Validate that every relative Markdown link in the wiki resolves to a file.

The CS858 wiki uses plain relative Markdown links between pages, e.g.
    [Differential privacy](../concepts/differential-privacy.md)
so a link is broken if its target path does not exist relative to the file
it appears in. This is the core structural lint and needs no graph manifest.

Absolute URLs (http, https, mailto) and pure in-page anchors (#section) are
skipped. Anchors on a file link (foo.md#bar) are validated only at the file
level (does foo.md exist), not the heading level.

Exit code 0 if all links resolve; exit code 1 if any are broken.
Run from repo root:
    uv run python3 scripts/check-links.py
"""

from __future__ import annotations

import glob
import os
import re
import sys

# [text](target) — capture the target. Skip image links handled below.
_LINK = re.compile(r"(!?)\[[^\]]*\]\(([^)\s]+?)(?:\s+\"[^\"]*\")?\)")


def is_external(target: str) -> bool:
    return "://" in target or target.startswith(("mailto:", "tel:"))


def strip_code(content: str) -> str:
    """Blank out fenced code blocks and inline code spans.

    Docs and index pages contain example link syntax inside code (schema
    snippets, format hints like `[slug](slug.md)`). Those are illustrations,
    not real links, so they must not be validated.
    """
    out_lines: list[str] = []
    in_fence = False
    for line in content.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            out_lines.append("")
            continue
        out_lines.append("" if in_fence else line)
    text = "\n".join(out_lines)
    # Inline code spans (single or multi backtick runs).
    return re.sub(r"`+[^`]*`+", "", text)


def find_broken(md_path: str) -> list[tuple[str, str]]:
    """Return (target, reason) for each unresolved relative link in a file."""
    with open(md_path) as fh:
        content = strip_code(fh.read())
    base_dir = os.path.dirname(md_path)
    broken: list[tuple[str, str]] = []
    for is_image, target in _LINK.findall(content):
        if is_external(target) or target.startswith("#"):
            continue
        path_part = target.split("#", 1)[0]
        if not path_part:
            continue  # pure anchor
        resolved = os.path.normpath(os.path.join(base_dir, path_part))
        if not os.path.exists(resolved):
            kind = "image" if is_image else "link"
            broken.append((target, f"{kind} target not found: {resolved}"))
    return broken


def main() -> int:
    md_files = sorted(glob.glob("wiki/**/*.md", recursive=True))
    md_files += sorted(glob.glob("docs/**/*.md", recursive=True))

    total_broken = 0
    for md_path in md_files:
        broken = find_broken(md_path)
        if broken:
            print(f"{md_path}:")
            for target, reason in broken:
                print(f"  [{target}] — {reason}")
            total_broken += len(broken)

    if total_broken == 0:
        print(f"All Markdown links resolve ({len(md_files)} files checked).")
        return 0
    print(f"\n{total_broken} broken link(s) found.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
