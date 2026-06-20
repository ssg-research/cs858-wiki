# Change log

Append-only, chronological (oldest at the top, newest at the bottom). One entry
per operation that adds, removes, or substantially edits wiki pages. Format:

```text
## [YYYY-MM-DD HH:MM] <operation> | <subject>
```

Get the timestamp with `date "+%Y-%m-%d %H:%M"` rather than guessing. Operations:
`generate-paper-summary`, `add-concept`, `query`, `lint`, `reconcile`, `setup`.
Body: 2-5 sentences on what was done, plus the model used (for traceability,
since exact reproduction is not possible; see AGENTS.md).

---

## [2026-06-09 00:00] setup | wiki scaffold created

Initialized the CS858 wiki structure: `wiki/papers/`, `wiki/concepts/`, index
and log files, the `/generate-paper-summary` workflow, and supporting scripts
copied and adapted from the research-wiki. No paper or concept pages yet.

## [2026-06-10 22:21] generate-paper-summary | Towards Deep Learning Models Resistant to Adversarial Attacks

Compiled the first paper page, `wiki/papers/madry-2018-pgd.md` (Madry et al.,
ICLR 2018; arXiv 1706.06083), under a new "Adversarial Robustness" section.
Created the five foundational concept pages it depends on: `adversarial-examples`,
`adversarial-threat-model`, `fgsm`, `adversarial-training`, and
`robust-optimization`. The section and the "Why this paper is assigned" framing
(security-guarantee angle, plus the instructor's note that this is one of the
first papers to put adversarial training and robustness on conclusive footing)
were instructor-supplied. Updated all three indexes and recounted stats to
1 paper, 5 concepts. Model: Claude Opus 4.8 (1M context), `claude-opus-4-8[1m]`.

## [2026-06-10 22:39] generate-paper-summary | Rewrote madry-2018-pgd; added writing-style guide

Rewrote the Madry et al. page and the five concept pages to a terser, expert
register after instructor feedback that the first draft read as generic AI prose.
Tier-1 Background now uses `###` subsections and includes an ML and training
primer (ERM, SGD, input versus parameter gradients); Reading guidance is a
section-keyed bullet list; prior-work claims carry author-year citations. Encoded
the rules in a new `docs/writing-style.md`, referenced from
`docs/ops/generate-paper-summary.md` and `CLAUDE.md`. Link and markdownlint
checks rerun clean. Model: Claude Opus 4.8 (1M context), `claude-opus-4-8[1m]`.

## [2026-06-10 23:17] reconcile | page philosophy redesign + madry-2018-pgd second rewrite

Redesigned the paper-page contract after instructor review of the first
compile. New philosophy: the page orients, the paper teaches. Pages now open
with a High-level overview (a contextualized abstract, headline results
allowed, ending in a bolded Threat Model paragraph). Tier-2 Background is
declarative field context at publication time (prior work only, properly
cited), replacing the open-questions format. Motivating questions are three to
five high-level pre-questions; the field's open tensions are never authored,
only pointed at via neutral attention anchors in Reading guidance, which moved
late in the page. Tier-1 is now written at Wikipedia link density, backed by
stub concept pages. Citations get full References sections read off the cited
paper's bibliography. Updated `docs/ops/generate-paper-summary.md` (full
rewrite with intent and pedagogical ground rules), `docs/writing-style.md`,
`AGENTS.md`, and the `/generate-paper-summary` command. Rewrote
`wiki/papers/madry-2018-pgd.md` to the new schema and added seven stub
concepts: `empirical-risk-minimization`, `stochastic-gradient-descent`,
`projected-gradient-descent`, `lp-norms`, `white-box-black-box`,
`transferability`, `gradient-masking`. Stats now 1 paper, 12 concepts.
Model: Fable 5, `claude-fable-5`.

## [2026-06-10 23:30] generate-paper-summary | Membership Inference Attacks From First Principles

Compiled `wiki/papers/carlini-2022-lira.md` (Carlini et al., IEEE S&P 2022;
arXiv 2112.03570; DOI 10.1109/SP46214.2022.9833649, venue confirmed via DBLP)
under a new "Membership Inference" section. First page produced under the
redesigned contract from the start. Created six concept pages:
`membership-inference`, `shadow-models`, `likelihood-ratio-test`, `roc-curves`,
`memorization`, and `differential-privacy`; added reciprocal paper links to
`empirical-risk-minimization`, `stochastic-gradient-descent`, and
`white-box-black-box`. Instructor supplied the section and the
evaluation-methodology "Why assigned" framing. References read off the paper's
bibliography (pp. 14-16); Shokri et al. venue (S&P 2017) confirmed via DBLP.
Stats now 2 papers, 18 concepts. Model: Fable 5, `claude-fable-5`.

## [2026-06-10 23:40] generate-paper-summary | Deep Learning with Differential Privacy

Compiled `wiki/papers/abadi-2016-dp-sgd.md` (Abadi et al., ACM CCS 2016;
arXiv 1607.00133; DOI 10.1145/2976749.2978318, venue and DOI
instructor-supplied) under a new "Differential Privacy" section. Created three
concept pages: `gaussian-mechanism`, `privacy-budget`, and `gradient-clipping`;
added reciprocal paper links to `differential-privacy`,
`stochastic-gradient-descent`, `empirical-risk-minimization`, `memorization`,
`membership-inference`, and `white-box-black-box`. Instructor supplied the
section and a merged "Why assigned" framing (first provable guarantee,
difficult in practice, yet the basis of nearly every deployed private system,
federated learning especially). References read off the paper's bibliography
(pp. 10-11). Stats now 3 papers, 21 concepts. Model: Fable 5,
`claude-fable-5`.

## [2026-06-10 23:44] reconcile | cross-link lira -> dp-sgd; codify backward paper links

Linked the three DP-SGD mentions on `carlini-2022-lira.md` (Tier-1 Defenses,
Tier-2, Reading guidance) to `abadi-2016-dp-sgd.md`, which did not exist when
that page was compiled. Codified the rule in the op doc's citation convention:
cited prior work with a wiki page gets a relative link (and new compiles sweep
existing pages that cite the new paper), while forward links to follow-up work
stay off paper pages and route through the concept layer. Model: Fable 5,
`claude-fable-5`.

## [2026-06-10 23:54] lint | sweep newspaper-drama phrasing; ban it in the style doc

Instructor flagged dramatic register on the DP-SGD page ("raised the stakes
and broke the assumptions," "the empirical face of the problem," staged
open-question closers). Grep sweep found 14 instances of the pattern across
all three paper pages and two concept pages; rewrote each as flat declaratives
(worst on `abadi-2016-dp-sgd.md`, also `carlini-2022-lira.md` Tier-2,
`madry-2018-pgd.md` Tier-2, `likelihood-ratio-test.md`,
`empirical-risk-minimization.md`). Added "Newspaper drama" to the banned moves
in `docs/writing-style.md` with the rejected examples. Model: Fable 5,
`claude-fable-5`.

## [2026-06-18 13:00] lint | ban definition by gratuitous negation

Instructor flagged "a training-data privacy setting, not an evasion one" on
`carlini-2022-lira.md`: defining a thing by negating an alternative (evasion)
the page never raises. Swept every paper and concept page for the "X, not Y"
pattern; the only other gratuitous instance was `likelihood-ratio-test.md`
("is not merely a good attack, it is the optimal one"). Fixed both; left the
legitimate negations (factual statements and misconception-corrections in
"Variants and traps"). Added "Definition by gratuitous negation" to the banned
moves in `docs/writing-style.md` with a rejected and an accepted example, and
reinforced it in the `generate-paper-summary` playbook and `AGENTS.md`. Model:
Opus 4.8, `claude-opus-4-8[1m]`.

## [2026-06-18 13:00] infra | feature-branch workflow; protect main

Replaced the long-lived `dev` branch (spent once PR #1 merged) with a
feature-branch + pull-request model and rewrote the `AGENTS.md` Git Workflow
section to match. Protected `main` on GitHub: merges land only via pull request
(zero required approvals, no CI gate), direct pushes and force-pushes are
rejected, the branch cannot be deleted, and protection applies to admins too.
Model: Opus 4.8, `claude-opus-4-8[1m]`.

## [2026-06-19 17:34] infra | standalone reading-list index; xlsx-to-table converter

Made `wiki/` self-contained for publication as a github.io submodule and rebuilt
the landing page around the full course reading list. Copied the instructor
syllabus to `docs/CS858-F26-papers-stripped.xlsx` (kept the `UpdatedList` sheet
only) and added `scripts/build-paper-table.py`, a one-time converter that reads
the sheet and emits the Part 1 / Part 2 sections as HTML tables. Markdown tables
cannot express the spreadsheet's vertical cell merges, so each theme is rendered
with an HTML `rowspan`; the full-width Part banners become headings. Columns are
number, paper, theme, topic, and essential readings. Papers are renumbered
sequentially in reading-list order, so numbering stays monotonic while the
spreadsheet's theme order is preserved. The three written companions link to
their pages, the other 21 link to a new `wiki/under-construction.md` placeholder
and carry a dagger marker. Essential-reading hyperlinks (arXiv, USENIX, IEEE,
ACM) are lifted from the sheet.
Replaced the "Papers by section" table in `wiki/README.md` with this reading
list and removed the "How pages are made" section; stripped the
`/generate-paper-summary` build notes from the papers and concepts indexes so no
published page references anything outside `wiki/`. Extended
`scripts/check-links.py` to resolve relative HTML `href`/`src` targets, added
`openpyxl` to the dev dependency group, and set `MD033: false` in the
markdownlint config. Model: Opus 4.8, `claude-opus-4-8`.
