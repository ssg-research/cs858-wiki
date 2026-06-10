#!/usr/bin/env python3
"""
Extract text from a PDF file, or render pages to PNG for direct visual reading.

Usage:
    uv run python3 scripts/read-pdf.py <path> [--pages START-END] [--layout] [--render OUT_DIR]

Examples:
    uv run python3 scripts/read-pdf.py raw/pdfs/paper.pdf
    uv run python3 scripts/read-pdf.py raw/pdfs/paper.pdf --pages 1-4
    uv run python3 scripts/read-pdf.py raw/pdfs/paper.pdf --pages 3 --layout
    uv run python3 scripts/read-pdf.py raw/pdfs/paper.pdf --pages 8 --render /tmp/pages

Modes:
    default        Plain text (pdfplumber extract_text). Fast, but tables collapse.
    --layout       Layout-preserving text. Keeps cell positions roughly aligned —
                   use when reading tables. Slower than default.
    --render DIR   Rasterize each requested page to a PNG in DIR at 200 DPI. Use
                   this when a table has merged cells, rotated text, or borderless
                   layout that defeats text extraction. The PNG can then be read
                   directly as an image.
"""

from __future__ import annotations

import argparse
import os
import sys

import pdfplumber


def parse_page_range(spec: str, total: int) -> range:
    """Parse a page range like '1-4' or '3' into a zero-based range."""
    if "-" in spec:
        parts = spec.split("-", 1)
        start = max(int(parts[0]) - 1, 0)
        end = min(int(parts[1]), total)
        return range(start, end)
    page = int(spec) - 1
    if page < 0 or page >= total:
        print(f"Page {spec} out of range (1-{total})", file=sys.stderr)
        sys.exit(1)
    return range(page, page + 1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract text from a PDF.")
    parser.add_argument("path", help="Path to the PDF file")
    parser.add_argument(
        "--pages",
        default=None,
        help="Page range to extract, e.g. '1-4' or '3' (1-indexed). Default: all.",
    )
    parser.add_argument(
        "--layout",
        action="store_true",
        help="Use layout-preserving text extraction (better for tables).",
    )
    parser.add_argument(
        "--render",
        default=None,
        metavar="OUT_DIR",
        help="Rasterize requested pages to PNG in OUT_DIR (200 DPI). Skips text output.",
    )
    args = parser.parse_args()

    with pdfplumber.open(args.path) as pdf:
        total = len(pdf.pages)
        pages = parse_page_range(args.pages, total) if args.pages else range(total)

        if args.render:
            os.makedirs(args.render, exist_ok=True)
            for i in pages:
                out_path = os.path.join(args.render, f"p{i + 1:03d}.png")
                pdf.pages[i].to_image(resolution=200).save(out_path)
                print(out_path)
            return

        for i in pages:
            page = pdf.pages[i]
            print(f"--- Page {i + 1}/{total} ---")
            text = (
                page.extract_text(layout=True) if args.layout else page.extract_text()
            )
            if text:
                print(text)
            else:
                print("[no extractable text]")
            print()


if __name__ == "__main__":
    main()
