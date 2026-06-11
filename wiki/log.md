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
