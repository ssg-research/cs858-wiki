#!/usr/bin/env python3
"""
Read a paper PDF: extract text, search it, inspect structure, or render
pages to PNG for direct visual reading.

Usage:
    uv run python3 scripts/read-pdf.py <path> [--pages SPEC] [mode flags]

Recommended workflow for compiling a paper (cheapest first):
    1. --info                    page count, metadata, outline/TOC. Run this
                                 FIRST to learn where sections live instead of
                                 dumping the whole PDF.
    2. --search "Table 3"        find which pages mention a term (case-
                                 insensitive). Use to locate tables, sections,
                                 or hyperparameters before extracting.
    3. --pages 4-7               plain-text extraction of just those pages.
    4. --pages 5 --layout        layout-preserving text. Keeps table cells
                                 roughly column-aligned. Use for tables.
    5. --pages 5 --tables        structured table extraction (TSV). Use when
                                 --layout is still ambiguous.
    6. --pages 5 --render DIR    rasterize to PNG (200 DPI) and read the
                                 image directly. Last resort for merged
                                 cells, rotated text, or borderless tables
                                 that defeat text extraction.

Page SPEC is 1-indexed and accepts commas and ranges: '3', '1-4', '1-4,7,9-12'.

Examples:
    uv run python3 scripts/read-pdf.py raw/pdfs/paper.pdf --info
    uv run python3 scripts/read-pdf.py raw/pdfs/paper.pdf --search "ablation"
    uv run python3 scripts/read-pdf.py raw/pdfs/paper.pdf --pages 1-4
    uv run python3 scripts/read-pdf.py raw/pdfs/paper.pdf --pages 3 --layout
    uv run python3 scripts/read-pdf.py raw/pdfs/paper.pdf --pages 6 --tables
    uv run python3 scripts/read-pdf.py raw/pdfs/paper.pdf --pages 8 --render /tmp/pages
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import TYPE_CHECKING, Any, cast

import pdfplumber
from pdfminer.pdfdocument import PDFNoOutlines
from pdfminer.pdfparser import PDFSyntaxError
from pdfplumber.utils.exceptions import PdfminerException

if TYPE_CHECKING:
    from pdfplumber.pdf import PDF


def parse_page_spec(spec: str, total: int) -> list[int]:
    """Parse '1-4,7,9-12' (1-indexed) into a sorted list of 0-based pages."""
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, _, end_s = part.partition("-")
            try:
                start, end = int(start_s), int(end_s)
            except ValueError:
                sys.exit(f"ERROR: bad page range '{part}' (expected e.g. '2-5')")
            if start > end:
                sys.exit(f"ERROR: page range '{part}' is backwards")
            if start < 1 or start > total:
                sys.exit(f"ERROR: page {start} out of range (PDF has {total} pages)")
            pages.update(range(start - 1, min(end, total)))
        else:
            try:
                page = int(part)
            except ValueError:
                sys.exit(f"ERROR: bad page number '{part}'")
            if page < 1 or page > total:
                sys.exit(f"ERROR: page {page} out of range (PDF has {total} pages)")
            pages.add(page - 1)
    if not pages:
        sys.exit(f"ERROR: page spec '{spec}' selects no pages")
    return sorted(pages)


def show_info(pdf: PDF) -> None:
    """Print page count, document metadata, and the outline (TOC) if present."""
    print(f"Pages: {len(pdf.pages)}")
    # pdfplumber's metadata dict is untyped; getattr keeps pyright quiet
    # without an inline ignore.
    metadata = cast("dict[str, Any]", getattr(pdf, "metadata", None) or {})
    for key in ("Title", "Author", "Subject", "CreationDate", "Producer"):
        value = metadata.get(key)
        if value:
            print(f"{key}: {value}")
    print()
    try:
        outlines = list(pdf.doc.get_outlines())
    except PDFNoOutlines:
        print("Outline: (none embedded)")
        return
    print("Outline:")
    for level, title, *_ in outlines:
        indent = "  " * (int(level) - 1)
        print(f"{indent}- {title}")


def search_pdf(pdf: PDF, needle: str, pages: list[int]) -> None:
    """Print page numbers and matching lines for a case-insensitive needle."""
    needle_lower = needle.lower()
    hits = 0
    for i in pages:
        text = pdf.pages[i].extract_text() or ""
        for line in text.splitlines():
            if needle_lower in line.lower():
                print(f"p{i + 1}: {line.strip()}")
                hits += 1
    if hits == 0:
        print(f"No matches for '{needle}'.")
    else:
        print(f"\n{hits} matching line(s).", file=sys.stderr)


def show_tables(pdf: PDF, pages: list[int]) -> None:
    """Print extracted tables as TSV, one block per table."""
    found = 0
    for i in pages:
        tables = pdf.pages[i].extract_tables()
        for t_idx, table in enumerate(tables, 1):
            found += 1
            print(f"--- Page {i + 1}, table {t_idx} ---")
            for row in table:
                print("\t".join("" if cell is None else str(cell) for cell in row))
            print()
    if found == 0:
        print(
            "[no tables detected by extract_tables — try --layout, "
            "or --render and read the PNG]"
        )


def render_pages(pdf: PDF, pages: list[int], out_dir: str, dpi: int) -> None:
    os.makedirs(out_dir, exist_ok=True)
    for i in pages:
        out_path = os.path.join(out_dir, f"p{i + 1:03d}.png")
        pdf.pages[i].to_image(resolution=dpi).save(out_path)
        print(out_path)


def extract_text(pdf: PDF, pages: list[int], layout: bool) -> None:
    total = len(pdf.pages)
    for i in pages:
        page = pdf.pages[i]
        print(f"--- Page {i + 1}/{total} ---")
        text = page.extract_text(layout=True) if layout else page.extract_text()
        if text:
            print(text)
        else:
            print("[no extractable text — likely scanned; try --render]")
        print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read a PDF: text, search, info, tables, or PNG render."
    )
    parser.add_argument("path", help="Path to the PDF file")
    parser.add_argument(
        "--pages",
        default=None,
        help="Pages to operate on, 1-indexed: '3', '1-4', '1-4,7'. Default: all.",
    )
    parser.add_argument(
        "--info",
        action="store_true",
        help="Print page count, metadata, and outline/TOC, then exit.",
    )
    parser.add_argument(
        "--search",
        default=None,
        metavar="TEXT",
        help="Print pages and lines containing TEXT (case-insensitive).",
    )
    parser.add_argument(
        "--layout",
        action="store_true",
        help="Layout-preserving text extraction (better for tables).",
    )
    parser.add_argument(
        "--tables",
        action="store_true",
        help="Extract tables as TSV instead of running text.",
    )
    parser.add_argument(
        "--render",
        default=None,
        metavar="OUT_DIR",
        help="Rasterize requested pages to PNG in OUT_DIR. Skips text output.",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=200,
        help="Resolution for --render (default: 200).",
    )
    args = parser.parse_args()

    if not os.path.exists(args.path):
        sys.exit(f"ERROR: file not found: {args.path}")

    try:
        pdf_ctx = pdfplumber.open(args.path)
    except (PDFSyntaxError, PdfminerException) as exc:
        sys.exit(f"ERROR: not a readable PDF: {exc}")

    with pdf_ctx as pdf:
        total = len(pdf.pages)
        pages = parse_page_spec(args.pages, total) if args.pages else list(range(total))

        if args.info:
            show_info(pdf)
        elif args.search:
            search_pdf(pdf, args.search, pages)
        elif args.render:
            render_pages(pdf, pages, args.render, args.dpi)
        elif args.tables:
            show_tables(pdf, pages)
        else:
            if not args.pages and total > 25:
                print(
                    f"[note: dumping all {total} pages; consider --info first, "
                    f"then --pages to target sections]",
                    file=sys.stderr,
                )
            extract_text(pdf, pages, args.layout)


if __name__ == "__main__":
    main()
