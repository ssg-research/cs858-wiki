# CS858 Wiki

Per-paper **reading companions** for CS858 (Trustworthy Machine Learning). Each
primary-reading paper gets one page that lowers the prerequisite load for
reading it and surfaces the open questions it sits inside. Pages deliberately do
**not** summarize the papers' own findings. That is what reading the paper is
for.

## Students — start here

Open the **[`wiki-f26/`](wiki-f26/README.md)** folder and begin at
[`wiki-f26/README.md`](wiki-f26/README.md). Every page renders here with working links;
follow them to the paper pages and the shared concept pages. You do not need any
special tool; it is plain Markdown.

## What's in this repo

- **[`wiki-f26/`](wiki-f26/README.md)** — the content: paper pages and shared concept
  pages, linked with plain relative Markdown links.
- **`docs/ops/`** — the operational playbooks (how the pages are produced).
- **`.claude/commands/`** — the `/generate-paper-summary` slash command.
- **`scripts/`** — an arXiv fetcher, a PDF reader, and a link checker.

[`AGENTS.md`](AGENTS.md) is the operator contract for whoever maintains the wiki.

## Maintainer setup

```bash
uv sync                                          # create the env, install tooling
uv run python3 scripts/fetch-arxiv.py <url|id>   # download a paper from arXiv
uv run python3 scripts/read-pdf.py <pdf>         # read a paper
uv run python3 scripts/check-links.py            # validate all links resolve
```

## Adding a paper

```text
/generate-paper-summary <arXiv-URL | arXiv-ID | pdf-path>
```

See [`docs/ops/generate-paper-summary.md`](docs/ops/generate-paper-summary.md)
for the full procedure and page schema.
