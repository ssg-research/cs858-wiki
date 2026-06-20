#!/usr/bin/env python3
"""One-time generator for the reading-list tables in ``wiki/README.md``.

Reads ``docs/CS858-F26-papers-stripped.xlsx`` (sheet ``UpdatedList``) and prints
the Part 1 / Part 2 sections as HTML tables.

The spreadsheet groups papers under a shared theme with vertically merged cells.
A Markdown table cannot express a vertical merge, so each theme is rendered with
an HTML ``rowspan`` cell, the one construct that survives GitHub, GitHub Pages,
and the common static-site generators. The full-width "Part" banners become
Markdown headings instead of table rows.

Per-paper layout:

* the primary paper links to its reading companion when one exists (see
  ``READY``), otherwise to the shared ``under-construction.md`` placeholder and
  carries a dagger marker;
* essential readings keep the hyperlinks already stored in the spreadsheet
  (arXiv, USENIX, IEEE, ACM, and similar).

Papers are renumbered sequentially in reading-list order, so the numbering stays
monotonic while the spreadsheet's theme order is preserved.

Run from the repo root::

    uv run python3 scripts/build-paper-table.py > /tmp/reading-list.md

The output is spliced into ``wiki/README.md`` by hand so the surrounding prose
stays under editorial control.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import cast

from openpyxl import load_workbook

XLSX = Path("docs/CS858-F26-papers-stripped.xlsx")
SHEET = "UpdatedList"

# Papers whose reading companion already exists, keyed by reading-list number.
READY: dict[int, str] = {
    1: "madry-2018-pgd",
    5: "carlini-2022-lira",
    7: "abadi-2016-dp-sgd",
}

NUMBER_COL = 1  # A: Paper #
TITLE_COL = 2  # B: primary paper
THEME_COL = 3  # C: theme (vertically merged across its papers)
TOPIC_COL = 4  # D: topic (Part 1) or Software/Hardware (Part 2)
ESSENTIAL_COL = 5  # E: essential readings

UC_PAGE = "under-construction.md"
UC_MARK = ' <sup title="Reading companion under construction">&dagger;</sup>'

HEADERS = ("#", "Theme", "Topic", "Primary Reading", "Essential Readings")


@dataclass(frozen=True)
class XlsxCell:
    text: str
    href: str | None


@dataclass(frozen=True)
class Reading:
    title: str
    href: str | None


@dataclass
class Paper:
    number: int
    title: str
    topic: str
    theme: str
    essential: list[Reading] = field(default_factory=list)


@dataclass
class Part:
    title: str
    papers: list[Paper] = field(default_factory=list)


def read_sheet(
    path: Path, sheet: str
) -> tuple[dict[tuple[int, int], XlsxCell], int, int]:
    """Return every non-empty cell as a ``{(row, col): XlsxCell}`` map.

    All openpyxl access is confined here; values cross the boundary as plain
    strings via :func:`cast`, so the rest of the module stays statically typed.
    """
    workbook = load_workbook(path)
    worksheet = workbook[sheet]
    max_row = worksheet.max_row
    max_col = worksheet.max_column
    cells: dict[tuple[int, int], XlsxCell] = {}
    for row in range(1, max_row + 1):
        for col in range(1, max_col + 1):
            cell = worksheet.cell(row=row, column=col)
            value = cast("object | None", cell.value)
            link = cell.hyperlink
            href = link.target if link is not None else None
            text = "" if value is None else " ".join(str(value).split())
            if text or href:
                cells[(row, col)] = XlsxCell(text=text, href=href)
    return cells, max_row, max_col


def cell_text(cells: dict[tuple[int, int], XlsxCell], row: int, col: int) -> str:
    cell = cells.get((row, col))
    return cell.text if cell else ""


def readings(
    cells: dict[tuple[int, int], XlsxCell], rows: range, cols: range
) -> list[Reading]:
    out: list[Reading] = []
    for row in rows:
        for col in cols:
            cell = cells.get((row, col))
            if cell and cell.text:
                out.append(Reading(title=cell.text, href=cell.href))
    return out


def parse(cells: dict[tuple[int, int], XlsxCell], max_row: int) -> list[Part]:
    """Turn the cell map into Part -> Paper structure using cell values alone."""
    part_rows = [
        r
        for r in range(2, max_row + 1)
        if cell_text(cells, r, NUMBER_COL).startswith("Part")
    ]
    paper_rows = [
        r for r in range(2, max_row + 1) if cell_text(cells, r, NUMBER_COL).isdigit()
    ]
    boundaries = sorted(part_rows + paper_rows + [max_row + 1])

    parts: list[Part] = []
    current_part: Part | None = None
    current_theme = ""
    for row in range(2, max_row + 1):
        head = cell_text(cells, row, NUMBER_COL)
        theme = cell_text(cells, row, THEME_COL)
        if theme:
            current_theme = theme
        if head.startswith("Part"):
            current_part = Part(title=head)
            parts.append(current_part)
            continue
        if not head.isdigit():
            continue
        if current_part is None:
            msg = f"paper row {row} appears before any Part header"
            raise ValueError(msg)
        end = min(b for b in boundaries if b > row) - 1
        block = range(row, end + 1)
        current_part.papers.append(
            Paper(
                number=int(head),
                title=cell_text(cells, row, TITLE_COL),
                topic=cell_text(cells, row, TOPIC_COL),
                theme=current_theme,
                essential=readings(
                    cells, block, range(ESSENTIAL_COL, ESSENTIAL_COL + 1)
                ),
            )
        )
    position = 1
    for part in parts:
        for paper in part.papers:
            paper.number = position
            position += 1
    return parts


def esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def link(title: str, href: str | None) -> str:
    safe = esc(title)
    if not href:
        return safe
    return f'<a href="{href.replace("&", "&amp;")}">{safe}</a>'


def reading_cell(items: list[Reading]) -> str:
    if not items:
        return ""
    bullets = "".join(f"<li>{link(r.title, r.href)}</li>" for r in items)
    return f"<ul>{bullets}</ul>"


def paper_cell(paper: Paper) -> str:
    slug = READY.get(paper.number)
    if slug:
        return f'<a href="papers/{slug}.md">{esc(paper.title)}</a>'
    return f'<a href="{UC_PAGE}">{esc(paper.title)}</a>{UC_MARK}'


def part_heading(title: str) -> str:
    """Render 'Part 1 Risks ...' as 'Part 1: Risks ...'."""
    words = title.split(" ", 2)
    if len(words) == 3 and words[0] == "Part":
        return f"Part {words[1]}: {words[2]}"
    return title


def render_table(part: Part) -> str:
    lines = ["<table>", "  <thead>", "    <tr>"]
    lines += [f"      <th>{h}</th>" for h in HEADERS]
    lines += ["    </tr>", "  </thead>", "  <tbody>"]

    papers = part.papers
    for idx, paper in enumerate(papers):
        lines.append("    <tr>")
        lines.append(f"      <td>{paper.number}</td>")
        if idx == 0 or papers[idx - 1].theme != paper.theme:
            span = 1
            while idx + span < len(papers) and papers[idx + span].theme == paper.theme:
                span += 1
            lines.append(f'      <td rowspan="{span}">{esc(paper.theme)}</td>')
        lines.append(f"      <td>{esc(paper.topic)}</td>")
        lines.append(f"      <td>{paper_cell(paper)}</td>")
        lines.append(f"      <td>{reading_cell(paper.essential)}</td>")
        lines.append("    </tr>")

    lines += ["  </tbody>", "</table>"]
    return "\n".join(lines)


def main() -> None:
    cells, max_row, _ = read_sheet(XLSX, SHEET)
    parts = parse(cells, max_row)
    blocks: list[str] = []
    for part in parts:
        blocks.append(f"### {part_heading(part.title)}")
        blocks.append(render_table(part))
    blocks.append(
        "<sup>&dagger;</sup> Reading companion under construction; the link opens"
        " a placeholder page."
    )
    print("\n\n".join(blocks))


if __name__ == "__main__":
    main()
