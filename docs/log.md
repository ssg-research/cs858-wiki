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

## [2026-06-22 10:37] generate-paper-summary | Representation Engineering: A Top-Down Approach to AI Transparency

Compiled the reading companion for Zou et al. (2023), arXiv:2310.01405, as
`wiki/papers/zou-2023-representation-engineering.md`, Topic "Mechanistic
Interpretability for AI safety" (row 13, theme "Cross-Cutting Topics", read
verbatim from the reading list). Created five new concept pages seeding the
interpretability cluster: `distributed-representations`,
`principal-component-analysis` (stub), `linear-probing`, `activation-steering`,
and `mechanistic-interpretability`. No existing page cites this work, so no
backward cross-link sweep was needed; the two essential readings (Arditi et al.
2024 refusal direction, Zou et al. 2024 circuit breakers) are 2024 follow-up
work, so they sit in Supplementary readings rather than Paper Context. The threat
model is framed around white-box access to internal activations and the dual-use
of representation control. "Why read this" follows the instructor's framing that
interpretability is one of the few routes to learning how and why a model works,
rendered to fit the paper's top-down, representation-level position rather than
the bottom-up circuit-level program it contrasts itself with. Updated the papers,
concepts, and top-level indexes (Papers: 13, Concepts: 50) and removed the row's
under-construction marker. markdownlint clean (9 files), `check-links.py` clean
(72 files). Work on branch `content/papers-13-18`. Model: Opus 4.8,
`claude-opus-4-8`.

## [2026-06-21 21:03] infra | merge content batch (PR #6), retire batching note

PR #6 (`content/add-papers` into `main`) merged on GitHub as squash commit
`85d2e55`, closing out the batch of nine papers and twenty-six concept pages
compiled since the branch opened. Fast-forwarded local `main` to match. Removed
the "Temporary note (content batch in progress)" block from `AGENTS.md`'s Git
Workflow section, since the batch it described is complete; future paper
compiles resume the standard one-branch-one-PR workflow. Model: Sonnet 4.6,
`claude-sonnet-4-6`.

## [2026-06-22 11:23] generate-paper-summary | SoK: Unintended Interactions among Machine Learning Defenses and Risks

Compiled the reading companion for Duddu, Szyller, and Asokan (2023),
arXiv:2312.04542 (IEEE S&P 2024), as
`wiki/papers/duddu-2023-unintended-interactions.md`, Topic "Unintended
Interactions among ML Defenses and Risks" (row 14, theme "Cross-Cutting Topics",
read verbatim from the reading list). Because the SoK spans the whole field, the
High-level overview stays at the level of the framework's claim (overfitting and
memorization conjectured as the two shared causes of cross-effects, mediated by
data/algorithm/model factors) rather than the dense taxonomy and symbols; the
threat model is written as a meta-model over the many per-risk adversaries.
Created six new concept pages backfilling the shared layer with first-class risk
and defense families: `overfitting`, `algorithmic-fairness`, `feature-attribution`,
`data-reconstruction`, `property-inference`, and `attribute-inference` (the last
two cross-disambiguated against each other and against membership inference);
fingerprinting and outlier removal were glossed inline against existing pages.
Reused and added reciprocal "Papers that use this concept" backlinks on eleven
existing concepts (`adversarial-examples`, `data-poisoning`, `backdoor-attacks`,
`model-extraction`, `membership-inference`, `adversarial-training`,
`model-watermarking`, `differential-privacy`, `empirical-risk-minimization`,
`memorization`, `white-box-black-box`). No existing page cites this 2023 SoK, so
no backward paper cross-link sweep was needed; the two essential readings
(Szyller and Asokan 2023 conflicting interactions, and the 2024 combining-defenses
follow-up) sit in Supplementary readings. Paper Context cites only prior or
contemporaneous interaction studies, with author lists rendered as the SoK's own
bibliography prints them (first author + et al. where it abbreviates) rather than
reconstructed. "Why read this" follows the instructor's framing (techniques are
studied in isolation, but a deployed system faces many risks at once and a defense
against one can shift vulnerability to another), rendered on the paper's own terms.
Updated the papers, concepts, and top-level indexes (Papers: 14, Concepts: 56) and
removed the row's under-construction marker. markdownlint clean (21 files),
`check-links.py` clean (79 files). Work on branch `content/papers-13-18`. Model:
Opus 4.8, `claude-opus-4-8`.
