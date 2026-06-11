#!/usr/bin/env python3
"""
Fetch a paper PDF (and its bibliographic metadata) directly from arXiv.

This removes the manual download-and-rename step. Give it an arXiv abstract
URL, a PDF URL, an ``arxiv:`` string, or a bare arXiv ID, and it:

    1. saves the PDF to ``raw/pdfs/<id>.pdf`` (the path that feeds read-pdf.py), and
    2. prints title / authors / year / primary category from the arXiv API.

The metadata comes from the arXiv API, not the PDF body, so it is the right
source for "never guess author names or years" (see docs/ops/generate-paper-summary.md).

Usage:
    uv run python3 scripts/fetch-arxiv.py <arxiv-url-or-id> [--out-dir DIR] [--force]

Accepted inputs (all resolve to the same paper):
    https://arxiv.org/abs/1706.06083
    https://arxiv.org/abs/1706.06083v2
    https://arxiv.org/pdf/1706.06083.pdf
    arxiv:1706.06083
    1706.06083
    hep-th/9901001          # old-style IDs work too

Security: this fetches only the ID/URL you pass on the command line (a trusted
source). It talks to export.arxiv.org (metadata) and arxiv.org (the PDF) over
HTTPS and nothing else. It never follows a URL found inside a PDF.
"""

from __future__ import annotations

import argparse
import os
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

_API_URL = "https://export.arxiv.org/api/query?id_list="
_PDF_URL = "https://arxiv.org/pdf/"
# arXiv asks API clients to identify themselves with a descriptive User-Agent.
_USER_AGENT = "cs858-wiki-fetch/1.0 (CS858 reading-companion tooling)"
_TIMEOUT = 30

_ATOM = "{http://www.w3.org/2005/Atom}"
_ARXIV = "{http://arxiv.org/schemas/atom}"


@dataclass(frozen=True)
class PaperMeta:
    arxiv_id: str
    title: str
    authors: str
    year: str
    category: str


def normalize_arxiv_id(raw: str) -> str:
    """Reduce a URL, an 'arxiv:' string, or a bare ID to a plain arXiv identifier."""
    ident = raw.strip()
    if not ident:
        sys.exit("ERROR: empty arXiv reference")
    # Drop the scheme so 'arxiv.org/...' and 'https://arxiv.org/...' behave alike.
    if "://" in ident:
        ident = ident.split("://", 1)[1]
    # Pull the ID out of an /abs/ or /pdf/ URL path.
    for marker in ("/abs/", "/pdf/"):
        if marker in ident:
            ident = ident.split(marker, 1)[1]
            break
    # Drop any query string or fragment.
    ident = ident.split("?", 1)[0].split("#", 1)[0]
    # Strip an 'arxiv:' prefix (case-insensitive), then leading/trailing slashes.
    if ident.lower().startswith("arxiv:"):
        ident = ident[len("arxiv:") :]
    ident = ident.strip("/")
    # Strip a trailing '.pdf' left over from a /pdf/<id>.pdf URL.
    if ident.lower().endswith(".pdf"):
        ident = ident[:-4]
    if not ident or " " in ident or not any(ch.isdigit() for ch in ident):
        sys.exit(f"ERROR: '{raw}' does not look like an arXiv ID or URL")
    return ident


def _text(elem: ET.Element | None) -> str:
    """Return an element's stripped text, or '' when the element or text is absent."""
    if elem is None or elem.text is None:
        return ""
    return elem.text.strip()


def _http_get(url: str, *, what: str) -> bytes:
    """GET a URL and return the body, exiting with a clear message on failure."""
    req = Request(url, headers={"User-Agent": _USER_AGENT})  # noqa: S310  fixed https arXiv host
    try:
        with urlopen(req, timeout=_TIMEOUT) as resp:  # noqa: S310  fixed https arXiv host
            return resp.read()
    except HTTPError as exc:
        sys.exit(f"ERROR: arXiv returned HTTP {exc.code} fetching {what} ({url})")
    except URLError as exc:
        sys.exit(f"ERROR: could not reach arXiv to fetch {what}: {exc.reason}")


def fetch_metadata(arxiv_id: str) -> PaperMeta:
    """Query the arXiv API and return bibliographic metadata for an ID."""
    body = _http_get(_API_URL + arxiv_id, what="metadata")
    try:
        root = ET.fromstring(body)  # noqa: S314  arXiv API response over HTTPS
    except ET.ParseError as exc:
        sys.exit(f"ERROR: could not parse arXiv API response: {exc}")

    entry = root.find(f"{_ATOM}entry")
    if entry is None:
        sys.exit(f"ERROR: no arXiv record found for id '{arxiv_id}'")

    title = _text(entry.find(f"{_ATOM}title"))
    if "/api/errors" in _text(entry.find(f"{_ATOM}id")) or title.lower() == "error":
        summary = _text(entry.find(f"{_ATOM}summary")) or "unknown error"
        sys.exit(f"ERROR: arXiv rejected id '{arxiv_id}': {summary}")

    authors = [
        _text(name)
        for author in entry.findall(f"{_ATOM}author")
        if (name := author.find(f"{_ATOM}name")) is not None
    ]
    year = _text(entry.find(f"{_ATOM}published")).split("-", 1)[0]
    primary = entry.find(f"{_ARXIV}primary_category")
    category = primary.get("term", "") if primary is not None else ""

    return PaperMeta(
        arxiv_id=arxiv_id,
        title=" ".join(title.split()),  # collapse the wrapped whitespace arXiv inserts
        authors=", ".join(a for a in authors if a),
        year=year,
        category=category,
    )


def download_pdf(arxiv_id: str, out_dir: str, *, force: bool) -> tuple[str, int]:
    """Download the PDF for an ID into out_dir; return (path, bytes_written)."""
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, arxiv_id.replace("/", "_") + ".pdf")

    if os.path.exists(out_path) and not force:
        size = os.path.getsize(out_path)
        print("[already downloaded; pass --force to re-fetch]", file=sys.stderr)
        return out_path, size

    data = _http_get(_PDF_URL + arxiv_id, what="PDF")
    if not data.startswith(b"%PDF-"):
        sys.exit(
            f"ERROR: content from {_PDF_URL}{arxiv_id} is not a PDF. arXiv may "
            "still be generating it (try again shortly), or the ID is wrong."
        )

    with open(out_path, "wb") as fh:
        fh.write(data)
    return out_path, len(data)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download a paper PDF and its metadata from arXiv.",
    )
    parser.add_argument("ref", help="arXiv URL, 'arxiv:ID', or bare ID")
    parser.add_argument(
        "--out-dir",
        default="raw/pdfs",
        help="Directory to save the PDF into (default: raw/pdfs).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-download even if the target file already exists.",
    )
    args = parser.parse_args()

    arxiv_id = normalize_arxiv_id(args.ref)
    meta = fetch_metadata(arxiv_id)
    out_path, size = download_pdf(arxiv_id, args.out_dir, force=args.force)

    print(f"arXiv ID: {meta.arxiv_id}")
    print(f"Title:    {meta.title}")
    print(f"Authors:  {meta.authors}")
    print(f"Year:     {meta.year}")
    print(f"Category: {meta.category}")
    print(f"Saved:    {out_path} ({size} bytes)")


if __name__ == "__main__":
    main()
