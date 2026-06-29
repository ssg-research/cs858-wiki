# Writing style for CS858 wiki pages

The house style for every page in `wiki/`: paper pages and concept pages. The
`/generate-paper-summary` operation requires it
([playbook](ops/generate-paper-summary.md)). Read it before drafting.

The principles here are adapted from the `scientific-writing` skill. Its LaTeX
and venue mechanics do not apply, but its rules on voice, precision, and
citation do.

## Audience

Write for a graduate student in an 800-level course at a strong CS program. The
reader is fluent in general machine learning, probability, and algorithms, and
reads research papers routinely. What they lack is exposure to this specific
subfield, and AI security students arrive from many home communities
(statistics, ML, systems security, cryptography), so terminology that is plain
in one community is opaque in another. Decode such terms in one clause on first
use. Write for a capable peer who is new to the topic, not for a general
audience and not for a reader who needs convincing that the topic matters. Do
not popularize.

## Register

- Terse and declarative. State the fact and move on.
- Active voice. Avoid "has been shown to," "is believed to," and similar.
- Short sentences. Do not chain three clauses where two sentences will do.
- Positive framing. Say what something *is*, not what it is not. Do not define
  or characterize a thing by negating an alternative the reader had no reason to
  assume; that contrast is dead weight and cutting it loses nothing. Negate only
  to correct a misconception the reader is likely to hold, and even then prefer
  the explicit form to a bare "X, not Y." See Banned moves.
- Use "However," to mark a contrast. Avoid "Yet," and "Despite this," as
  sentence openers.
- Consistent terminology. Do not vary a technical term for stylistic variety; if
  the page says "perturbation," it stays "perturbation."
- Precision over generality. Name the concrete object, not the abstract
  category: "the ℓ-infinity ball of radius epsilon," not "a notion of closeness."
- Gloss imported jargon on first use, in one clause, so the reader need not open
  a cited paper to parse the sentence.
- No em-dashes in prose (see `AGENTS.md`). The list-separator pattern
  `[text](link) — description` is the one exception.

## Links

Basic Background is written at **Wikipedia link density**: nearly every
technical term a reader new to the subfield might not know is a relative link
to a concept page, including general machinery like stochastic gradient
descent or white-box access. Tiny stub concept pages exist to make this
possible; link to them rather than glossing a term inline for the third time.

## Citations

- Any claim about prior work or the state of the field carries an inline
  author-year citation at the end of the clause: "(Goodfellow et al., 2015)."
- Do not open a sentence with author names. State the finding, then cite it.
- Every page that cites anything ends with a References section holding
  one full entry per cited work: authors, title, venue, year, and the arXiv ID
  when the source you read prints one.
- Bibliographic data comes from a source read this session (the citing paper's
  bibliography pages or the cited work's arXiv page). Never reconstruct an
  entry from memory; if you cannot verify it, do not cite it.
- On a paper page, background citations are restricted to work prior to or
  contemporaneous with the paper. Follow-up work is never background.

## Banned moves

These are the failure modes that make a page read as generic machine output.
Each example is from a rejected draft.

- Essay openers that locate the paper rhetorically. Rejected: "This paper sits
  where test-time security meets optimization." Open with the content itself.
- Metaphor used as structure. Rejected: "Section 2 is the conceptual spine."
  Name the section's actual role: "Section 2 states the formulation the rest of
  the paper instantiates."
- Second-person coaching and reader management. Rejected: "make sure you can
  state it in your own words," "do not skim the figures," "you should be able to
  see." State the content and trust the reader.
- Manufactured stakes and rhetorical questions inside prose. Keep prose
  declarative; questions live only in the motivating-questions section.
- Quiz-style or trick motivating questions, and questions whose premise the
  field disputes. Rejected: a question that sounds answerable but whose honest
  answer is "it depends on a contested definition." Motivating questions are
  high-level reading goals, nothing more.
- Stating the field's open tensions as authored questions. Students generate
  those themselves; the page places a neutral attention anchor in reading
  guidance instead ("the justification for X is one sentence; note what it
  is").
- Newspaper drama. Rejected: "Deep learning raised the stakes and broke the
  assumptions," "these attacks are the empirical face of the problem," "would
  survive contact with either standard," and open-question closers staged for
  tension ("whether X was possible was open"). Field context states what
  changed, what failed, and what had not been done, in flat declaratives.
- Filler intensifiers. Rejected: "is doing real work," "carries the central
  argument," "a striking challenge." Cut them.
- Definition by gratuitous negation: the "X, not Y" construction where Y was
  never in play. Rejected: "a training-data privacy setting, not an evasion one"
  on a page that never raises evasion. State what the thing is; the negated
  alternative is dead weight. The one license to negate is correcting a
  misconception the reader actually holds, and even then write the explicit form
  ("unlike Y, which one would expect because Z, this is X") rather than dropping
  a bare "X, not Y" in for emphasis or drama. The negation is a deliberate tool,
  not a default. Acceptable, because the negated alternative is the likely wrong
  assumption: "sensitivity is the worst case over all adjacent datasets, not an
  average."
- "Adversarial attack" as a generic phrase. Every attack is adversarial by
  definition, and authors who write it usually mean an adaptive attack. Write
  "adaptive attack" or plain "attack" by meaning. Terms of art stay:
  "adversarial example," "adversarial training," "adversarial robustness,"
  "adversarial perturbation." A cited paper's title is kept verbatim.

## Role terminology

One canonical word per shared role, used consistently within a page's
High-level overview (its body and the Threat Model paragraph). Consistency
beats specificity: name a role once, then reuse the canonical word rather than
re-listing its instances ("a regulator, auditor, or customer" becomes the
"verifier" after first use).

| Canonical term | Role |
|---|---|
| **adversary** | the malicious party; normalizes the plain noun "attacker." Keep terms of art ("membership inference attack," "first-order adversary") and scare-quoted "adversary" where the actor may be benign |
| **defender** | the party making the protective claim |
| **model owner** | party whose stake is ownership or IP of the weights |
| **model provider** | party that serves or deploys the model to others |
| **prover** / **verifier** | proof producer / proof checker |
| **client** / **server** | private-input party / outsourced-compute party (secure-computation framing) |
| **victim** | the attacked target, distinct from the defender |
| **user** | benign end consumer of a deployed model |

Provider versus owner is not a hard split: one entity is often both, so use the
term for the relation the threat model emphasizes. Do not back-fill a role a
paper lacks; some papers have no defender, some no adversary. Genuinely unique
roles keep their own word (a differential-privacy curator, a watermark
detector, an initiator).

## Format by section

- **High-level overview.** One to three paragraphs, a contextualized abstract:
  problem, named approach, headline results at abstract level, decoded
  terminology. About 350 words of body prose, then a separate bolded paragraph
  beginning `**Threat Model:**` that names the adversary, its knowledge, its
  capability and budget, its timing, and the defender's claim; the Threat Model
  paragraph is additional to the 350 and may run longer. No methods walkthrough,
  no per-experiment numbers, and no fact another section owns: state each fact
  once, and do not repeat in the body what the Threat Model paragraph, Basic
  Background, or Paper Context carries. Tighten the Threat Model paragraph the
  same way, defining a role once and then using the role word rather than
  re-listing its instances.
- **Why read this.** Two to four declarative sentences on why the paper is worth
  reading on its own terms, instructor-owned. No hooks, and no reference to the
  paper's slot in the course sequence.
- **Basic Background.** `###` subsections, one per prerequisite cluster, two to
  five sentences each, Wikipedia link density. Covers the general ML and training
  machinery the paper assumes as well as the subfield-specific concepts. Never
  the paper's own content.
- **Paper Context.** Two to four declarative paragraphs: the state of the field
  when the paper appeared. What had been tried, what had broken, what was
  unsettled. Prior or contemporaneous citations only. Not questions. Renders
  inside a collapsed `<details>` block, the heading as its toggle.
- **Reading guidance.** A bullet list keyed by section, figure, or table, one
  line each, placed late in the page. Includes one or two neutral attention
  anchors pointing at where to slow down, without stating why it is contested.
- **Motivating questions.** Staff-side archive only (`agent_docs/`); not on
  the student-facing page. Three to five high-level pre-questions per paper,
  answerable by reading it. Students generate their own.
- **Supplementary readings.** Optional. Extra readings the instructor supplied,
  one bullet each with a one-line "why it's here" framing. Renders inside a
  collapsed `<details>` block, the heading as its toggle.
- **References.** Full bibliographic entries for everything cited on the page.
  Renders inside a collapsed `<details>` block, the heading as its toggle.
- **Concept pages.** Same register. Definitions are declarative and
  self-contained, 50 to 500 words; stubs are valid.

## Process

- Outline the points first, then write the prose. Do not ship the outline.
- Revise a section as one block, not sentence by sentence, so the voice stays
  consistent.
