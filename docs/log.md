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

## [2026-06-19 22:45] infra | student-facing wiki pass; align generation contract

Reworked the published wiki to read for students rather than for the wiki's
producers. `wiki/README.md`: replaced the producer-facing intro and the
duplicated lead-in with a two-line student intro and a short reading-list
lead-in, moved the build stats line to a page footer, reordered the reading-list
table to Theme / Topic / Primary Reading / Essential Readings (number column
kept), and rendered each row's essential readings as a bulleted list so the two
papers read as distinct entries. Renamed the per-paper schema headings on the
three companion pages: "Why this paper is assigned" to "Why read this",
"Background — Tier 1 (warm-up)" to "Basic Background", and "Background — Tier 2
(field context)" to "Paper Context". Rewrote the "Why read this" paragraphs on
`carlini-2022-lira` and `abadi-2016-dp-sgd` to stand alone, since they had
referenced the paper's slot in the course sequence. Rewrote the papers and
concepts index intros to drop page-schema and build language. A three-agent
prose audit (general-purpose subagents) confirmed the 21 concept pages were
already clean.

Traced the course-relative framing to the generation contract, which asked for
"the paper's role in the course's argument," and fixed it at the source:
`docs/ops/generate-paper-summary.md`, `.claude/commands/generate-paper-summary.md`,
and `docs/writing-style.md` now use the new heading names, reframe "Why read
this" as the paper's own significance, and carry a new "Every page stands alone"
rule. `docs/ops/lint.md` still describes the retired Tier-2-as-questions format
and needs a separate pass. Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-21 13:26] generate-paper-summary | Jailbroken: How Does LLM Safety Training Fail?

Compiled the reading companion for Wei, Haghtalab, and Steinhardt (2023), arXiv
2307.02483, as `wiki/papers/wei-2023-jailbroken.md` under the "Jailbreaking LLMs"
topic. Created seven concept pages to seed the LLM-safety cluster:
`language-model-pretraining`, `instruction-tuning`, `rlhf`, `safety-training`,
`jailbreak`, `red-teaming`, and `prompt-injection`, and added back-links from the
reused `white-box-black-box` and `adversarial-examples` pages. Updated the papers,
concepts, and top-level indexes (Papers: 4, Concepts: 28). The "Why read this"
framing was supplied by the instructor.

Also changed the workflow so a paper's `section` is taken verbatim from the
canonical Theme/Topic reading list in `wiki/README.md` rather than invented or
asked for (`docs/ops/generate-paper-summary.md`,
`.claude/commands/generate-paper-summary.md`), and brought the three existing
paper pages' `section` values and the papers index into exact agreement with
their reading-list Topics. check-links (41 files) and markdownlint clean.
Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-21 14:56] generate-paper-summary | Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection

Compiled the reading companion for Greshake et al. (2023), arXiv:2302.12173, as
`wiki/papers/greshake-2023-indirect-prompt-injection.md` (Topic "Indirect Prompt
Injection in AI Agents", taken verbatim from the reading list). Created two new
concept stubs, `retrieval-augmented-generation` and `llm-tool-use`, and reused
the existing `prompt-injection`, `jailbreak`, `language-model-pretraining`,
`instruction-tuning`, `rlhf`, `safety-training`, and `white-box-black-box` pages.
Added the reciprocal "Papers that use this concept" entries and an inline link in
`prompt-injection`, and a backward cross-link from `wei-2023-jailbroken` (which
cites this earlier work). Reconciled the stale v1 citation title ("More than
You've Asked For...") to the canonical arXiv v2 title in both `prompt-injection`
and `wei-2023-jailbroken`. Updated the papers, concepts, and top-level indexes
(Papers: 5, Concepts: 30) and removed the row's under-construction marker. The
"Why read this" framing was chosen by the instructor (the "named the attack
class" option). check-links (44 files) and markdownlint clean.
Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-21 15:59] generate-paper-summary | Safety Alignment Should Be Made More Than Just a Few Tokens Deep

Compiled the paper page `qi-2024-shallow-safety-alignment.md` (Topic: "Safety
Alignment and Guardrails", reading-list row 4) from arXiv 2406.05946. Added three
new concept pages: `kl-divergence`, `decoding-strategies`, and
`direct-preference-optimization`; reused and back-linked seven existing concepts
(safety-training, rlhf, language-model-pretraining, instruction-tuning, jailbreak,
stochastic-gradient-descent, adversarial-training). Paper Context sets up the
adversarial-training defense lineage and cross-links `madry-2018-pgd` per the
instructor; the "Why read this" uses the instructor-chosen diagnosis-to-fix angle.
Updated the papers, concepts, and top-level indexes (Papers: 6, Concepts: 33) and
removed the row's under-construction marker. check-links (48 files) and
markdownlint clean. Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-21 16:42] generate-paper-summary | Extracting Training Data from Large Language Models

Compiled the reading companion for Carlini et al., "Extracting Training Data from
Large Language Models" (arXiv 2012.07805, USENIX Security 2021) as
`wiki/papers/carlini-2021-extracting-training-data.md`, section "Training-data
Extraction from LLMs" (reading-list row 6). Added one new concept page,
`perplexity`; reused and back-linked seven existing concepts
(language-model-pretraining, decoding-strategies, memorization,
membership-inference, likelihood-ratio-test, white-box-black-box,
differential-privacy). Cross-linked `abadi-2016-dp-sgd` (DP-SGD) backward from
the page, and added a backward link from `carlini-2022-lira` to this page where it
cites the extraction attack. "Why read this" confirmed with the instructor, with
jargon trimmed at their direction. Updated the
papers, concepts, and top-level indexes (Papers: 7, Concepts: 34) and removed the
row's under-construction marker. check-links (50 files) and markdownlint clean.
Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-21 18:04] generate-paper-summary | Knowledge Unlearning for Mitigating Privacy Risks in Language Models

Compiled `wiki/papers/jang-2022-knowledge-unlearning.md` (Jang et al., ICLR 2023;
arXiv 2210.01504), section "Unlearning for Generative AI" (reading-list row 8).
Added one new concept page, `machine-unlearning` (exact vs approximate unlearning,
the right-to-be-forgotten motivation, relation to DP); reused and back-linked
seven existing concepts (language-model-pretraining, stochastic-gradient-descent,
decoding-strategies, perplexity, memorization, membership-inference,
differential-privacy). Cross-linked `carlini-2021-extracting-training-data` and
`abadi-2016-dp-sgd` backward from the page; no existing page cites this paper, so
no backward sweep was needed. "Why read this" supplied by the instructor (RTBF
importance plus the method's empirical-only, domain-dependent limits). Updated the
papers, concepts, and top-level indexes (Papers: 8, Concepts: 35) and removed the
row's under-construction marker. check-links (52 files) and markdownlint clean.
Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-21 18:31] generate-paper-summary | Knockoff Nets: Stealing Functionality of Black-Box Models

Compiled `wiki/papers/orekondy-2019-knockoff-nets.md` (Orekondy, Schiele, Fritz;
CVPR 2019; arXiv 1812.02766). Section "Model Extraction / Stealing" (row 9, theme
"Model Extraction and Distillation"), read verbatim from the reading list. Year
keyed to the CVPR 2019 venue (verified via DBLP), not the 2018 arXiv submission
the API reports. Created five concept pages: `model-extraction` and
`knowledge-distillation` (fuller, central), plus stubs `convolutional-neural-network`,
`transfer-learning`, and `reinforcement-learning`. Reused and back-linked
`white-box-black-box`, `kl-divergence`, and `stochastic-gradient-descent`. No
existing page cites this paper, so no backward sweep was needed. "Why read this"
supplied by the instructor (longest-standing SOTA / reference point for
classification model extraction; works across distributions and architectures).
Updated the papers, concepts, and top-level indexes (Papers: 9, Concepts: 40) and
removed the row's under-construction marker. check-links (58 files) and
markdownlint clean. Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-21 19:01] generate-paper-summary | DAWN: Dynamic Adversarial Watermarking of Neural Networks

Compiled `wiki/papers/szyller-2019-dawn.md` (Szyller, Atli, Marchal, Asokan;
arXiv 1906.00830; 2019). Section "Model Watermarking / Fingerprinting" (row 10,
theme "Model Extraction and Distillation"), read verbatim from the reading list.
Created three concept pages: `model-watermarking` and `backdoor-attacks` (central
to the paper), plus the stub `cryptographic-commitment` for the ownership-proof
protocol; the trusted-execution-environment idea was glossed inline rather than
given its own page. Reused and back-linked `model-extraction`, `memorization`,
`white-box-black-box`, and `convolutional-neural-network`. Added a backward
cross-link to the compiled `orekondy-2019-knockoff-nets` page (Knockoff is one of
the two extraction attacks DAWN tests against). The "dawn" grep hit on
`carlini-2021-extracting-training-data` is the author name "Dawn Song," not a
DAWN citation, so no backward sweep was needed. "Why read this" supplied by the
instructor (preventing extraction without losing utility is hard while detecting
it is easier; first defense to treat the whole system rather than the model in
isolation, largely model-independent). Updated the papers, concepts, and
top-level indexes (Papers: 10, Concepts: 43) and removed the row's
under-construction marker. check-links (62 files) and markdownlint clean. Model:
Opus 4.8, `claude-opus-4-8`.

## [2026-06-21 19:37] generate-paper-summary | Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks

Compiled `wiki/papers/wang-2019-neural-cleanse.md` (Wang, Yao, Shan, Li,
Viswanath, Zheng, Zhao; IEEE S&P 2019; DOI 10.1109/SP.2019.00031; no arXiv).
Section "Training-data Poisoning" (row 11, theme "Data Integrity and
Supply-Chain Security"), read verbatim from the reading list. Created one concept
page, `data-poisoning`, as the section's umbrella concept (availability vs
targeted/integrity poisoning, with backdoors as the trigger-conditioned subclass);
the MAD/anomaly-index outlier test and neuron pruning were glossed inline rather
than given their own pages, since they are the paper's method. Reused and
back-linked `backdoor-attacks` (the existing concept from the DAWN compile),
`convolutional-neural-network`, `white-box-black-box`, `transfer-learning`,
`lp-norms`, `stochastic-gradient-descent`, and `adversarial-examples`. No backward
cross-links into other compiled paper pages were needed (Neural Cleanse's cited
prior work has no pages yet). Disambiguated three colliding "Liu" citations with
initials (Y. Liu 2018 Trojaning, K. Liu 2018 Fine-Pruning, Y. Liu 2017 Neural
Trojans). "Why read this" drafted as a candidate marked `<!-- instructor: confirm
-->`, pending the instructor's framing. Updated the papers, concepts, and
top-level indexes (Papers: 11, Concepts: 44) and removed the row's
under-construction marker. Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-21 20:16] generate-paper-summary | PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models

Compiled the PoisonedRAG (Zou et al., 2024; arXiv:2402.07867) reading companion
at `wiki/papers/zou-2024-poisonedrag.md`, Topic "Preference Manipulation / RAG
Poisoning" (row 12, read verbatim from the reading list). The threat-model
paragraph foregrounds the unusual lifecycle position: data poisoning that lands
in the inference-time retrieval corpus, after training yet ahead of any user
prompt, with black-box vs white-box settings keyed to the attacker's knowledge of
the retriever. Created one new concept stub, `dense-retrieval`: the existing
`retrieval-augmented-generation` page covers the context-window /
instruction-boundary angle but not the embedding-similarity retrieval mechanism
that the attack's retrieval condition and white-box optimization depend on.
Reused and back-linked 11 existing concepts (`retrieval-augmented-generation`,
`data-poisoning`, `backdoor-attacks`, `prompt-injection`, `jailbreak`,
`white-box-black-box`, `adversarial-examples`, `transferability`, `perplexity`,
`roc-curves`, `language-model-pretraining`). Added forward cross-links from the
paper page to the already-compiled `greshake-2023-indirect-prompt-injection` and
`wei-2023-jailbroken` pages (cited as contemporaneous related work); no backward
sweep targets, since no existing page cites PoisonedRAG. Three citation arXiv IDs
absent from the paper's bibliography (Carlini et al. 2023, Jain et al. 2023, Alon
and Kamfonas 2023) were verified against the arXiv API rather than reconstructed
from memory. "Why read this" written from the instructor's supplied framing
(first data-poisoning attack on an LLM system through its knowledge base, with the
corruption landing after training rather than at inference-prompt time). Updated
the papers, concepts, and top-level indexes (Papers: 12, Concepts: 45) and removed
the row's under-construction marker. markdownlint clean (16 files),
`check-links.py` clean (66 files). Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-21 21:03] infra | merge content batch (PR #6), retire batching note

PR #6 (`content/add-papers` into `main`) merged on GitHub as squash commit
`85d2e55`, closing out the batch of nine papers and twenty-six concept pages
compiled since the branch opened. Fast-forwarded local `main` to match. Removed
the "Temporary note (content batch in progress)" block from `AGENTS.md`'s Git
Workflow section, since the batch it described is complete; future paper
compiles resume the standard one-branch-one-PR workflow. Model: Sonnet 4.6,
`claude-sonnet-4-6`.

## [2026-06-23 02:24] generate-paper-summary | Representation Engineering: A Top-Down Approach to AI Transparency

Compiled reading companion #13 (`wiki/papers/zou-2023-representation-engineering.md`,
arXiv 2310.01405), section "Mechanistic Interpretability for AI safety," framed as
top-down interpretability/transparency with a white-box, analyst-controlled threat
model. Created five concept pages: `mechanistic-interpretability`,
`linear-representation-hypothesis`, `linear-probing`, `activation-steering`,
`contrastive-prompt-pairs`. Reused eight: `language-model-pretraining`,
`instruction-tuning`, `rlhf`, `safety-training`, `jailbreak`, `red-teaming`,
`white-box-black-box`, `memorization` (RepE added to each one's "Papers that use
this concept" list). Added one backward cross-link from the paper page to
`carlini-2021-extracting-training-data` (RepE cites it; used in the memorization
background); no existing paper page cites RepE, so no reciprocal link was added.
All citation entries (31 on the paper page, plus the concept-page references) were
read off the paper's own bibliography this session (PDF pages 30-38); arXiv IDs
surfaced there include TruthfulQA 2109.07958, Activation Addition 2308.10248, and
Induction Heads 2209.11895. Bibliographic metadata (title, authors, year, arXiv
ID) came from the instructor-supplied verified list, not re-resolved. Indexes
updated (Papers: 13, Concepts: 50) and the row-13 under-construction marker
removed. Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-23 02:52] generate-paper-summary | SoK: Unintended Interactions among Machine Learning Defenses and Risks

Compiled the reading companion for paper 14 (Cross-Cutting Topics). Created two
concept pages: `group-fairness` and `model-explanations`. Reused eleven existing
concept pages, adding this paper to each one's "Papers that use this concept"
list: `adversarial-examples`, `adversarial-training`, `data-poisoning`,
`backdoor-attacks`, `model-extraction`, `membership-inference`,
`differential-privacy`, `model-watermarking`, `memorization`,
`empirical-risk-minimization`, `white-box-black-box`. Added six backward
cross-links from the paper page to compiled papers the SoK cites: `madry-2018-pgd`,
`carlini-2022-lira`, `carlini-2021-extracting-training-data`, `abadi-2016-dp-sgd`,
`orekondy-2019-knockoff-nets`, `szyller-2019-dawn`. Verified that the SoK does not
cite `wang-2019-neural-cleanse` or `jang-2022-knowledge-unlearning`, so neither was
linked; no existing paper page cites this SoK, so no reciprocal link was added. The
required threat-model paragraph is written as a scope paragraph, since a SoK has no
single threat model. All twenty citation entries on the paper page were read off
the SoK bibliography this session (PDF pages 15-19); where that bibliography printed
"First-author et al.", the reference entry uses that form rather than reconstructing
names from memory. Indexes updated (Papers: 14, Concepts: 52), the row-14
under-construction marker removed, and `14: "duddu-2024-unintended-interactions"`
added to the `build-paper-table.py` READY dict. Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-23 03:05] generate-paper-summary | A Watermark for Large Language Models

Compiled the reading companion for paper 15 (Cross-Cutting Topics, Topic "Media
Forensics and Proactive Provenance"). Created one concept page, `llm-watermarking`,
framing output/text watermarking for provenance as a family (decoding-time
logit/sampling biasing versus post-hoc editing, statistical detection) kept
general so it does not stand in for this founding paper; no entropy concept page
was created, since the audience's probability fluency covers next-token-distribution
entropy and the paper's "spike entropy" is its own construct. Reused five existing
concept pages, adding this paper to each one's "Papers that use this concept" list:
`language-model-pretraining`, `decoding-strategies`, `perplexity`, `roc-curves`,
and `model-watermarking` (the last carries the model-weight-watermarking contrast).
No backward cross-links were added: the only paper page matching a search for this
work, `zou-2024-poisonedrag`, matched on the coauthor surname "Kirchenbauer" in an
unrelated reference (Jain et al., 2023), not a citation of this paper, and no
existing paper page cites it. All twenty-three citation entries on the paper page
were read off this paper's bibliography this session (arXiv 2301.10226v4, PDF pages
13-17); `doi:` is omitted because the arXiv PDF prints none for the paper. Indexes
updated (Papers: 15, Concepts: 53), the row-15 under-construction marker and dagger
removed, and `15: "kirchenbauer-2023-llm-watermark"` added to the
`build-paper-table.py` READY dict. The "Why read this" section carries an
`<!-- instructor: confirm -->` marker on a drafted candidate. Model: Opus 4.8,
`claude-opus-4-8`.

## [2026-06-23 03:23] generate-paper-summary | Examining Zero-Shot Vulnerability Repair with Large Language Models

Compiled the reading companion for Pearce et al. (IEEE S&P 2023, arXiv 2112.02125),
reading-list paper 16 under "AI for Cybersecurity". Created four concept stubs:
`software-vulnerability` (CWE), `automated-program-repair`, `code-language-models`
(Codex / code completion), and `zero-shot-prompting`. Reused
`language-model-pretraining` (the pretrained base of the code models),
`white-box-black-box` (black-box API access), and `decoding-strategies` (the
temperature / top-p sweep), adding a reciprocal role line to each. No backward
cross-links were added: the two paper pages matching a search for "Pearce" matched
unrelated authors (Adam Pearce in `zou-2023-representation-engineering`, Will Pearce
in `zou-2024-poisonedrag`), not this work, and no existing paper page cites it; this
paper's bibliography cites no compiled wiki paper. The fifteen citation entries on
the paper page were read off this paper's bibliography this session (PDF pages
14-15); `doi:` is omitted because the arXiv PDF prints none. Indexes updated (Papers:
16, Concepts: 57), the row-16 under-construction link and dagger replaced, and
`16: "pearce-2023-vulnerability-repair"` added to the `build-paper-table.py` READY
dict. The "Why read this" section carries an `<!-- instructor: confirm -->` marker on
a drafted candidate. Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-23 03:44] generate-paper-summary | Secure Transformer Inference Made Non-interactive

Compiled the reading companion for Zhang et al. (NDSS 2025, IACR ePrint 2024/136,
DOI 10.14722/ndss.2025.230868), reading-list paper 17 and the first of the Part-2
cluster on cryptographic and hardware defenses, under "Leakage Resistance (Client
Data): Software". NEXUS is the first non-interactive protocol for secure transformer
inference, built on RNS-CKKS fully homomorphic encryption. Created four general,
reusable cryptography concept stubs written for reuse by the later cluster papers
(secure inference, trusted execution, zero-knowledge proofs, attestation):
`homomorphic-encryption` (partially/leveled/fully HE, CKKS, bootstrapping),
`secure-multiparty-computation` (2PC, garbled circuits, secret sharing, semi-honest
vs malicious, the simulation paradigm), `secure-inference` (the private-inference
problem setting across HE/MPC/TEE instantiations and its round/bandwidth cost axes),
and `ciphertext-packing` (SIMD batching of homomorphic ciphertexts). Reused
`language-model-pretraining` (the pretrained BERT/GPT transformers run under
encryption), `membership-inference` (the logit-vector leakage that motivates
returning only the argmax label), and `convolutional-neural-network` (the models
prior secure-inference protocols targeted before transformers), adding a reciprocal
role line to each. No backward cross-links: none of this paper's cited works has a
wiki paper page, and no existing page cites it. The DOI is printed on the PDF title
page; `arxiv:` is omitted because the paper is not on arXiv. The 24 citation entries
on the paper page were read off this paper's bibliography this session (PDF pages
14-17). Indexes updated (Papers: 17, Concepts: 61), the row-17 under-construction
link and dagger replaced, and `17: "zhang-2025-nexus"` added to the
`build-paper-table.py` READY dict. The "Why read this" section carries an
`<!-- instructor: confirm -->` marker on a drafted candidate. Model: Opus 4.8,
`claude-opus-4-8`.

## [2026-06-23 04:00] generate-paper-summary | BliMe: Verifiably Secure Outsourced Computation with Hardware-Enforced Taint Tracking

Compiled reading companion 18 (`elatali-2024-blime`, NDSS 2024, arXiv 2204.09649),
the hardware paper in the "Leakage Resistance (Client Data)" theme. Created two
general, reusable hardware-security concept stubs seeded for the rest of the Part-2
cluster: `trusted-execution-environment` (enclaves, isolation, remote attestation,
SGX / TrustZone / SEV / Sanctum, and their side-channel and run-time-attack limits)
and `taint-tracking` (dynamic information-flow tracking, software vs hardware tag
bits, explicit vs implicit flows, the confidentiality / integrity dual). The later
hardware papers (No Privacy Left Outside, ASGARD) reuse these. Reused
`secure-inference` (the outsourced-computation framing; added the hardware
instantiation as a reciprocal role line and a TEE see-also link) and
`homomorphic-encryption` (the FHE baseline whose overhead motivates the hardware
approach). `secure-multiparty-computation` was considered but not linked: the paper
neither builds on nor centrally compares against MPC. No backward cross-links: none
of this paper's cited works has a wiki page, and no existing page (duddu-2024
included) cites it. The DOI is read off the PDF title page; `arxiv:` retained. The
22 citation entries on the paper page were read off this paper's bibliography this
session (PDF pages 14-16). Indexes updated (Papers: 18, Concepts: 63), the row-18
under-construction link and dagger replaced, and `18: "elatali-2024-blime"` added
to the `build-paper-table.py` READY dict. The "Why read this" section carries an
`<!-- instructor: confirm -->` marker on a drafted candidate. Model: Opus 4.8,
`claude-opus-4-8`.

## [2026-06-23 04:09] generate-paper-summary | Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs

Compiled paper 19 (`bao-2025-dp-zo`, USENIX Security 2025) as software-side
training-data leakage resistance via differential privacy. Created one concept
page, `zeroth-order-optimization` (gradient-free two-point/SPSA estimation and the
MeZO line for memory-efficient LLM fine-tuning), and reused nine existing pages:
`differential-privacy`, `privacy-budget`, `gaussian-mechanism`, `gradient-clipping`,
`stochastic-gradient-descent`, `membership-inference`, `memorization`,
`language-model-pretraining`, and `transfer-learning`. Used `transfer-learning`
rather than `instruction-tuning` for the fine-tuning prerequisite, since the paper
does task-specific supervised fine-tuning, not instruction following; no PEFT/LoRA
or federated-learning page, as the paper centrally uses neither. Backward
cross-links to three compiled pages it cites: `abadi-2016-dp-sgd` (DP-SGD),
`carlini-2022-lira` (membership inference), and
`carlini-2021-extracting-training-data` (training-data extraction); no existing page
cites this paper. No arXiv ID and no DOI on the PDF title page, so both are omitted
from frontmatter. The 15 citation entries were read off this paper's bibliography
this session (USENIX Security 2025 proceedings, pages 16-21); the Carlini et al.
extraction paper is listed there as a 2020 preprint and is cited by its USENIX
Security 2021 publication. Indexes updated (Papers: 19, Concepts: 64), the row-19
under-construction link and dagger replaced, and `19: "bao-2025-dp-zo"` added to the
`build-paper-table.py` READY dict. The "Why read this" section carries an
`<!-- instructor: confirm -->` marker on a drafted candidate. Model: Opus 4.8,
`claude-opus-4-8`.

## [2026-06-23 04:29] generate-paper-summary | No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML

Compiled `wiki/papers/zhang-2024-tee-shielded.md` (reading-list #20, "Leakage
Resistance (Training Data): Hardware") from arXiv 2310.07152 (IEEE S&P 2024).
Created one concept page, `model-partitioning` (splitting a DNN across a TEE and an
untrusted accelerator, the on-device TSDP setting, and the security-versus-utility
trade-off), and reused ten existing pages: `trusted-execution-environment`,
`model-extraction`, `membership-inference`, `white-box-black-box`,
`convolutional-neural-network`, `transfer-learning`, `shadow-models`,
`differential-privacy`, `secure-multiparty-computation`, and
`homomorphic-encryption`. Did not create a `side-channel-attacks` page: the paper
explicitly puts TEE side channels out of scope, so the existing
`trusted-execution-environment` page covers that limit and inline glossing
suffices. Backward cross-links to two compiled pages it cites:
`orekondy-2019-knockoff-nets` (model stealing, ref [79]) and `carlini-2022-lira`
(membership inference, ref [18]); the paper does not cite BliMe or the Carlini 2021
LLM-extraction page, and no existing page cites this paper. The 21 citation entries
were read off this paper's bibliography this session (PDF pages 15-18). arXiv prints
the v1 year as 2023, but the venue is IEEE S&P 2024, so frontmatter uses year 2024;
no DOI on the title page, so it is omitted. Indexes updated (Papers: 20, Concepts:
65), the row-20 under-construction link and dagger replaced, and
`20: "zhang-2024-tee-shielded"` added to the `build-paper-table.py` READY dict. The
"Why read this" section carries an `<!-- instructor: confirm -->` marker on a
drafted candidate. Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-23 04:42] generate-paper-summary | ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks

Compiled `wiki/papers/tang-2024-modelguard.md` (Tang et al., USENIX Security 2024;
Duke University and Accenture). The paper is not on arXiv, so the frontmatter omits
`arxiv:`; the title page prints no DOI, so `doi:` is omitted too, and `year` is 2024.
Created one concept page, `mutual-information` (the information-leakage measure the
defense minimizes, with its rate-distortion role), and reused eight existing
concepts: `model-extraction`, `white-box-black-box`, `knowledge-distillation`,
`convolutional-neural-network`, `stochastic-gradient-descent`, `kl-divergence`,
`lp-norms`, and `roc-curves`, adding ModelGuard to each one's "Papers that use this
concept" list. The only backward cross-link is `orekondy-2019-knockoff-nets`
(Knockoff Nets, cited as ref [35]); DAWN (Szyller et al., 2019) is absent from this
paper's bibliography, so it gets no citation or link despite the topical adjacency,
and no existing page cites this paper. The 21 citation entries were read off the
paper's bibliography this session (PDF pages 14-15). Indexes updated (Papers: 21,
Concepts: 66), the row-21 under-construction link and dagger replaced with the new
page, and `21: "tang-2024-modelguard"` added to the `build-paper-table.py` READY
dict. The "Why read this" section carries an `<!-- instructor: confirm -->` marker
on a drafted candidate. Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-23 04:56] generate-paper-summary | ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments

Compiled `wiki/papers/moon-2025-asgard.md` (Moon et al., NDSS 2025; Yonsei
University). The paper is not on arXiv, so the frontmatter omits `arxiv:`; the
title page prints `doi: 10.14722/ndss.2025.240449` and the venue year is 2025.
Created one concept page, `hardware-virtualization` (hypervisors and the Arm
virtualization extensions, EL2, two-stage address translation, and the IOMMU, the
substrate beneath virtualization-based TEEs), and reused five existing concepts:
`trusted-execution-environment`, `model-partitioning`, `model-extraction`,
`convolutional-neural-network`, and `membership-inference`, adding ASGARD to each
one's "Papers that use this concept" list. Backward cross-links go to
`zhang-2024-tee-shielded` (the TSDP in-security study, cited as ref [95]) and
`carlini-2021-extracting-training-data` (training-data leakage, ref [16]); the
paper does not cite Knockoff Nets or any other compiled extraction page, and no
existing page cites this paper. The 17 citation entries were read off this paper's
bibliography this session (PDF pages 14-16). Indexes updated (Papers: 22, Concepts:
67), the row-22 under-construction link and dagger replaced with the new page, and
`22: "moon-2025-asgard"` added to the `build-paper-table.py` READY dict. The "Why
read this" section carries an `<!-- instructor: confirm -->` marker on a drafted
candidate. Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-23 05:08] generate-paper-summary | zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference

Compiled `wiki/papers/qu-2025-zkgpt.md` (Qu et al., USENIX Security 2025; IACR
ePrint 2025/1184; NUS and HKUST), reading-list paper 23 and the first of the
"Regulatory Compliance" theme, under section "Regulatory Compliance: Software".
zkGPT applies zero-knowledge proofs to LLM-inference integrity: a service provider
proves a claimed output is the correct result of running a committed model on a
given input, hiding the weights, with a succinct non-interactive proof. The paper
is not on arXiv, and the title page prints no DOI (only an ISBN and a USENIX URL),
so the frontmatter omits both `arxiv:` and `doi:`; `year` is 2025. Created one
general, reusable concept page, `zero-knowledge-proof` (prover/verifier,
completeness/soundness/zero-knowledge, interactive vs non-interactive via
Fiat-Shamir, succinct proofs / zk-SNARKs, and the arithmetic-circuit model with the
quantization it forces on ML), written for reuse by the final cluster paper (PAL*M,
property attestation); verifiable computation was folded into this page rather than
given its own. Reused `cryptographic-commitment` (the polynomial commitment that
fixes the model) and `language-model-pretraining` (the pretrained GPT-2 transformer
whose layers form the proof circuit), adding zkGPT to each one's "Papers that use
this concept" list. No backward cross-links: zkGPT's bibliography cites none of the
compiled wiki pages (NEXUS / `zhang-2025-nexus` is absent, confirmed by scanning the
full reference list), and no existing page cites zkGPT. The 26 citation entries on
the paper page were read off this paper's bibliography this session (PDF pages
15-18); both supplied supplementary readings were verified present in-bib (Garg et
al., CCS 2023; Abbaszadeh et al., 2024). Indexes updated (Papers: 23, Concepts: 68),
the row-23 under-construction link and dagger replaced with the new page, and
`23: "qu-2025-zkgpt"` added to the `build-paper-table.py` READY dict. The "Why read
this" section carries an `<!-- instructor: confirm -->` marker on a drafted
candidate. Model: Opus 4.8, `claude-opus-4-8`.

## [2026-06-23 05:20] generate-paper-summary | PAL*M: Property Attestation for Large Generative Models

Compiled `wiki/papers/chantasantitam-2026-palm.md` (Chantasantitam et al., 2026;
arXiv 2601.16199), reading-list #24, "Regulatory Compliance: Hardware", the
trusted-hardware counterpart to zkGPT. Created one concept page,
`remote-attestation` (the root of trust, the signed measurement/quote, and
property-based attestation with reference values from a trusted authority). Reused
eight existing concept pages with reciprocal links: `trusted-execution-environment`,
`zero-knowledge-proof`, `cryptographic-commitment`, `secure-multiparty-computation`,
`hardware-virtualization`, `language-model-pretraining`, `differential-privacy`, and
`group-fairness`. Added backward cross-links to `elatali-2024-blime` (cited as a
side-channel mitigation) and `zhang-2024-tee-shielded` (cited in the
TEE-confidentiality thread), the only compiled papers in PAL*M's bibliography; the
SoK (`duddu-2024-unintended-interactions`) and `qu-2025-zkgpt` are not cited, and no
existing page cites PAL*M since it is the newest. The 25 citation entries were read
off this paper's bibliography this session (PDF pages 13-14). Indexes updated
(Papers: 24, Concepts: 69); the row-24 under-construction link and dagger were
replaced with the new page, the now-unused dagger footnote line was removed (this
was the last placeholder), and `24: "chantasantitam-2026-palm"` was added to the
`build-paper-table.py` READY dict. The "Why read this" section carries an
`<!-- instructor: confirm -->` marker on a drafted candidate. Model: Opus 4.8,
`claude-opus-4-8`.

## [2026-06-23 06:19] review+fix | adversarial review of the 12 new reading companions

Ran independent adversarial review (three clean-context Opus 4.8 reviewers, one
per four-paper cluster, each fact-checking threat models and headline numbers
against the source PDFs), then a second-engine Codex review of all twelve pages.
Combined verdict: zero blockers on factual accuracy (every threat model and
headline result verified against the PDFs; no fabricated citations, no invented
arXiv IDs, no follow-up work cited as background). The findings were cardinal-rule
creep and citation hygiene. Applied fixes across eight paper pages and one concept
page: demoted reading-guidance bullets that taught a construction down to neutral
anchors (NEXUS, Representation Engineering, PAL\*M); re-scoped a ModelGuard Basic
Background subsection from paper-specific construction to generic prerequisites;
trimmed headline numbers and construction detail out of three "Why read this"
sections (NEXUS, zkGPT, PAL\*M); abstracted the NEXUS overview bandwidth figures to
orders of magnitude; corrected the zkGPT overview (a "smaller proof" claim became a
communication claim, since the compared scheme is interactive VOLE) and made the
zkGPT threat model state that cross-query model continuity rests on a published,
persistent commitment; corrected the BliMe "Why read this" so it no longer implies
arbitrary server software can usefully compute on blinded data (non-compliant
operations fault, and useful computation must be BliMe-compliant); disambiguated
two distinct "Yu et al., 2019" citations on the BliMe page (2019a for OISA, 2019b
for STT); de-passivized a paragraph and trimmed a thesis-preview clause on the SoK
page; softened a TEE-shielded threat-model verb (the adversary reads, and in
principle can tamper, rather than "manipulates"); and scoped a four-method
attribution citation on the model-explanations concept page to Integrated
Gradients alone. check-links clean (102 files); markdownlint clean (97 files); no
prose em-dashes. Noted for the instructor, not changed: "et al."-truncated
reference author lists on the SoK and PAL\*M pages, the zkLLM venue on the zkGPT
page, the ASGARD image-size figure (faithful to the paper's abstract), and a
pre-existing openpyxl pyright stub warning on `build-paper-table.py`. Model:
Opus 4.8, `claude-opus-4-8`.

## [2026-06-23 10:56] update-table | wiki/papers/README.md

Updated the papers list table in `wiki/papers/README.md` to include columns for Paper Title, Authors, Section, and Year by parsing the frontmatter of each paper file. Model: Gemini 3.1 Pro (High).

## [2026-06-23 11:03] update-table | wiki/papers/README.md

Updated the papers list table in `wiki/papers/README.md` to format authors using 'et al.' when there are more than two authors. Did not add publication column as that information is not available in the frontmatter. Model: Gemini 3.1 Pro (High).

## [2026-06-23 13:21] rename | wiki to wiki-f26

Renamed the `wiki` folder to `wiki-f26` and updated all internal references in playbooks, scripts, and commands to use the new path. Hard-coded paths in Bash scripts were extracted to `WIKI_DIR` variables where possible. Model: Gemini 3.1 Pro (High).

## [2026-06-23 13:57] update | Add home links to paper and concept pages (Gemini 3.1 Pro)

## [2026-06-23 14:04] infra | Mandate syncing main first in AGENTS.md (Gemini 3.1 Pro)

## [2026-06-23 17:35] fix | Collapse deeper-context sections behind `<details>` (#15)

Wrapped Paper Context, References, and Supplementary readings on all 24 paper
pages in a collapsed `<details>` block to shorten the visible page (issue #15,
PR 1 of 3). The section heading is an inline `<h2>` inside `<summary>`, so it
stays an H2 and acts as the click-to-expand toggle; the body stays Markdown so
its relative links remain checkable by `scripts/check-links.py`. Updated the
schema to match: the page-template skeleton, the per-section descriptions, and
the "Required" note in `docs/ops/generate-paper-summary.md`, and the "Format by
section" list in `docs/writing-style.md` (added a Supplementary readings
bullet). markdownlint clean (24 paper pages plus the two schema files);
`check-links.py` clean (102 files). Model: Opus 4.8, `claude-opus-4-8`.
