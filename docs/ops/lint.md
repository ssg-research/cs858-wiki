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
WIKI_DIR="wiki-f26"
for f in $(ls $WIKI_DIR/concepts/*.md 2>/dev/null | grep -v README); do
  for k in title type tags description; do
    grep -q "^$k:" "$f" || echo "concept $f missing: $k"
  done
done
for f in $(ls $WIKI_DIR/papers/*.md 2>/dev/null | grep -v README); do
  for k in title authors year section tags; do
    grep -q "^$k:" "$f" || echo "paper $f missing: $k"
  done
done
```

Any output names a page missing a required field. Should be silent.

## 3. Stale stats

Verify the `wiki-f26/README.md` stats header matches actual file counts.

```bash
WIKI_DIR="wiki-f26"
echo "Papers:   $(ls $WIKI_DIR/papers/*.md 2>/dev/null | grep -v README | wc -l | tr -d ' ')"
echo "Concepts: $(ls $WIKI_DIR/concepts/*.md 2>/dev/null | grep -v README | wc -l | tr -d ' ')"
grep "Last compiled" $WIKI_DIR/README.md
```

If counts disagree or the date is stale, update `wiki-f26/README.md`.

## 4. Index coverage

Every non-`README` page must be listed in its directory's `README.md`, and
every `README.md` entry must point at a real file. `check-links.py` catches the
second half (dangling index links). For the first half:

```bash
WIKI_DIR="wiki-f26"
for f in $(ls $WIKI_DIR/papers/*.md | grep -v README | xargs -n1 basename | sed 's/\.md$//'); do
  grep -q "($f.md)" $WIKI_DIR/papers/README.md || echo "MISSING FROM PAPERS INDEX: $f"
done
for f in $(ls $WIKI_DIR/concepts/*.md | grep -v README | xargs -n1 basename | sed 's/\.md$//'); do
  grep -q "($f.md)" $WIKI_DIR/concepts/README.md || echo "MISSING FROM CONCEPTS INDEX: $f"
done
```

## 5. Pedagogy checks (cannot be automated — read the pages)

These are CS858-specific and the reason the wiki exists. Read each changed paper
page and confirm:

- **No pre-digestion.** No "Summary," "Key findings," "Contributions," "Results,"
  "TLDR," or "Motivating questions" section. This is the most important check;
  flag any violation.
- **Every claim about the world carries a source.** Priority ("the first"),
  influence ("set the template the literature still follows"), and
  exhaustiveness ("the only known way") are facts about a literature. Each is
  attributed to the paper where the paper claims it, carries an author-year
  citation where a cited work settles it, or is cut. Terse declarative prose
  reads the same either way, so check the claim rather than the sentence.
- **No section speaks in the instructor's voice.** The page never states why the
  paper is on the syllabus or why it repays the reader's time. That is a fact
  about a course decision, and a page written from the paper can only guess it.
- **Basic Background is prerequisite-only.** It explains background concepts,
  not what the paper does to them.
- **No authored tensions as questions.** Reading guidance places neutral
  attention anchors; open-tension questions are for students to generate.
- **The Threat Model paragraph carries a threat model.** Every sentence names
  the adversary, its knowledge, capability, budget or timing, the trusted set,
  or the defender's claim. Test each sentence counterfactually: replace the
  paper's approach with a different one meeting the same goal, and drop any
  sentence that stops holding, because it described the approach. A defender's
  claim is what the defender asserts, never the paper's verdict on it.
- **"Trusted" is used in the trusted-computing-base sense.** A component is
  trusted when the guarantee assumes it behaves correctly and fails silently
  otherwise. A component that is attested, measured, verified, isolated, or
  encrypted is not thereby trusted; it is checked instead of trusted. Confirm
  the page names what each trusted component is trusted *for*.
- **A formal instantiation reads as an instantiation.** Where the paper fixes a
  requirement with one formalization (an ℓ-infinity ball at a fixed epsilon, a
  simulation-paradigm definition), the page states the requirement first and the
  formalization as this paper's choice. A page whose threat model is denser than
  the paper's own main-body statement has merged the two layers.
- **Reading guidance is targeted, not a roadmap.** Three bullets, five at the
  absolute most, ordered by position in the paper, each naming one precise locus,
  together covering where the assumptions are pinned down, where the mechanism
  lives, and where the claim is settled. Test each bullet: could a student
  satisfy it from a summary of the paper? If yes, it is a table-of-contents
  entry and it goes.

A quick grep surfaces the obvious schema violations:

```bash
WIKI_DIR="wiki-f26"
grep -rniE '^#+ .*(summary|key (findings|contributions)|results|tl;?dr|motivating questions|why read this|why this paper)' $WIKI_DIR/papers/
```

Any hit is a candidate violation; read it and confirm.

The Threat Model paragraphs are short enough to read in one pass; dump them all
and review each against the three checks above:

```bash
WIKI_DIR="wiki-f26"
for f in $WIKI_DIR/papers/*.md; do
  case "$f" in *README.md) continue;; esac
  echo "### $(basename "$f")"
  awk '/^\*\*Threat Model:\*\*/{p=1} p{print} p&&/^$/{exit}' "$f"
done
```

Grepping that dump for trust and result vocabulary gives a review queue rather
than a verdict; read every hit in context:

```bash
WIKI_DIR="wiki-f26"
for f in $WIKI_DIR/papers/*.md; do
  case "$f" in *README.md) continue;; esac
  awk -v F="$(basename "$f")" '/^\*\*Threat Model:\*\*/{p=1} p{print F": "$0} p&&/^$/{exit}' "$f"
done | grep -inE "trust|attest|we show|is shown|demonstrat|outperform|overhead|faster|reduces"
```

Priority and influence vocabulary is greppable across the whole page, and gives
a review queue rather than a verdict. Read every hit against the paper:

```bash
WIKI_DIR="wiki-f26"
grep -rinE "the (first|only)|first (to|work|paper|defense|attack|system|approach)|only known|remains the|set the (template|terms)|standard (practice|check)|seminal|canonical|widely cited|most (common|durable|practical)" \
  $WIKI_DIR/papers/ $WIKI_DIR/concepts/
```

A hit is legitimate when the paper makes the claim about itself and the page
attributes it. It is a violation when the page asserts it in its own voice.

Reading guidance length is mechanical, so check it directly:

```bash
WIKI_DIR="wiki-f26"
for f in $WIKI_DIR/papers/*.md; do
  case "$f" in *README.md) continue;; esac
  n=$(awk '/^## Reading guidance/{f=1;next} /^<details>|^## /{if(f)exit} f&&/^- /{c++} END{print c+0}' "$f")
  [ "$n" -gt 5 ] && echo "TOO MANY READING-GUIDANCE BULLETS ($n): $f"
done
```

## 6. Orphan concept pages

Concept pages with no incoming link from any paper page (a concept nobody
needs yet):

```bash
WIKI_DIR="wiki-f26"
for f in $(ls $WIKI_DIR/concepts/*.md | grep -v README | xargs -n1 basename | sed 's/\.md$//'); do
  count=$(grep -rl "concepts/$f.md" $WIKI_DIR/papers/ 2>/dev/null | wc -l | tr -d ' ')
  [ "$count" = "0" ] && echo "ORPHAN CONCEPT: $f"
done
```

Not always wrong (a concept may be seeded ahead of the paper that needs it), but
worth reviewing.

## 7. Markdownlint

```bash
WIKI_DIR="wiki-f26"
npx --no-install markdownlint-cli2 "$WIKI_DIR/**/*.md" "docs/**/*.md"
```

Must be 0 errors. `--no-install` uses the existing global install and skips the
install prompt; if it errors with "not found," substitute `--yes` to fetch from
npm. The bare `markdownlint` / `markdownlint-cli2` binaries are not on PATH.

## 8. Em-dash check

Em-dashes are prohibited in prose. Use commas or shorter sentences. Exception:
the `[text](link) — description` list-separator pattern is allowed.

```bash
WIKI_DIR="wiki-f26"
grep -rn '—' $WIKI_DIR/ --include="*.md" | grep -v ') —' | head -20
```

## 9. Scripts lint (ruff + types)

The published artifact is `wiki-f26/`, but the tooling in `scripts/` must stay clean
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
