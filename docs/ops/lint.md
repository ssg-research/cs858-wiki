# Operation: Lint

**Trigger:** Instructor asks to lint, audit, or check the wiki.

Read-only. Report all findings and ask for instructions; do not auto-fix.

Run each check from the repo root. Checks are ordered by severity: structural
first, style last.

---

## 1. Broken links (core structural check)

Every relative Markdown link between pages must resolve to a real file.

```bash
uv run python3 scripts/check-links.py
```

Exit code 0 = clean. Any output lists the file, the broken target, and the
resolved path that does not exist. This is the link check that matters at any
scale and needs no graph manifest.

## 2. Frontmatter completeness

Every concept page needs `title`, `type`, `tags`, `description`. Every paper
page needs `title`, `authors`, `year`, `section`, `tags`.

```bash
for f in $(ls wiki/concepts/*.md 2>/dev/null | grep -v README); do
  for k in title type tags description; do
    grep -q "^$k:" "$f" || echo "concept $f missing: $k"
  done
done
for f in $(ls wiki/papers/*.md 2>/dev/null | grep -v README); do
  for k in title authors year section tags; do
    grep -q "^$k:" "$f" || echo "paper $f missing: $k"
  done
done
```

Any output names a page missing a required field. Should be silent.

## 3. Stale stats

Verify the `wiki/README.md` stats header matches actual file counts.

```bash
echo "Papers:   $(ls wiki/papers/*.md 2>/dev/null | grep -v README | wc -l | tr -d ' ')"
echo "Concepts: $(ls wiki/concepts/*.md 2>/dev/null | grep -v README | wc -l | tr -d ' ')"
grep "Last compiled" wiki/README.md
```

If counts disagree or the date is stale, update `wiki/README.md`.

## 4. Index coverage

Every non-`README` page must be listed in its directory's `README.md`, and
every `README.md` entry must point at a real file. `check-links.py` catches the
second half (dangling index links). For the first half:

```bash
for f in $(ls wiki/papers/*.md | grep -v README | xargs -n1 basename | sed 's/\.md$//'); do
  grep -q "($f.md)" wiki/papers/README.md || echo "MISSING FROM PAPERS INDEX: $f"
done
for f in $(ls wiki/concepts/*.md | grep -v README | xargs -n1 basename | sed 's/\.md$//'); do
  grep -q "($f.md)" wiki/concepts/README.md || echo "MISSING FROM CONCEPTS INDEX: $f"
done
```

## 5. Pedagogy checks (cannot be automated — read the pages)

These are CS858-specific and the reason the wiki exists. Read each changed paper
page and confirm:

- **No pre-digestion.** No "Summary," "Key findings," "Contributions," "Results,"
  or "TLDR" section. No Tier-2 question that states the paper's own position.
  This is the most important check; flag any violation.
- **Tier-1 is prerequisite-only.** It explains background concepts, not what the
  paper does to them.
- **Tier-2 is questions.** A numbered list in interrogative form, each
  position-forcing, none generic; none settled by this paper alone.
- **Motivating questions are answerable by the paper.** Each should make a
  student want to read it, and reading it should resolve it. (Student discussion
  prompts are not wiki-authored, so they do not appear on the page.)

A quick grep surfaces the obvious schema violations:

```bash
grep -rniE '^#+ .*(summary|key (findings|contributions)|results|tl;?dr)' wiki/papers/
```

Any hit is a candidate violation; read it and confirm.

## 6. Orphan concept pages

Concept pages with no incoming link from any paper page (a concept nobody
needs yet):

```bash
for f in $(ls wiki/concepts/*.md | grep -v README | xargs -n1 basename | sed 's/\.md$//'); do
  count=$(grep -rl "concepts/$f.md" wiki/papers/ 2>/dev/null | wc -l | tr -d ' ')
  [ "$count" = "0" ] && echo "ORPHAN CONCEPT: $f"
done
```

Not always wrong (a concept may be seeded ahead of the paper that needs it), but
worth reviewing.

## 7. Markdownlint

```bash
npx --no-install markdownlint-cli2 "wiki/**/*.md" "docs/**/*.md"
```

Must be 0 errors. `--no-install` uses the existing global install and skips the
install prompt; if it errors with "not found," substitute `--yes` to fetch from
npm. The bare `markdownlint` / `markdownlint-cli2` binaries are not on PATH.

## 8. Em-dash check

Em-dashes are prohibited in prose. Use commas or shorter sentences. Exception:
the `[text](link) — description` list-separator pattern is allowed.

```bash
grep -rn '—' wiki/ --include="*.md" | grep -v ') —' | head -20
```

## 9. Scripts lint (ruff + types)

The published artifact is `wiki/`, but the tooling in `scripts/` must stay clean
too. Run the same linters pre-commit enforces:

```bash
uv run ruff check scripts/
uv run basedpyright scripts/
```

Both must pass with zero findings. Resolve them rather than suppressing; only
suppress a type error when there is genuinely no other way (prefer `cast()` at
`Any` boundaries). This check matters only when a script changed this session.

---

## Output

Report findings grouped by check number. For each: **Check**, **File**,
**Issue**, **Suggested fix**. Do not auto-fix. Present and wait for instructions.
