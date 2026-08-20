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
- Reading guidance written as a table of contents. Rejected: "Section 5 and
  Table 1: the experimental setup and the datasets." A bullet that reports what
  a section contains is a listing any model generates for free, and a page full
  of them tells the student to read everything. Point at the specific thing a
  summary destroys: the exact quantifier, the assumption in one clause, the
  threshold with no derivation, the baseline chosen.
- Newspaper drama. Rejected: "Deep learning raised the stakes and broke the
  assumptions," "these attacks are the empirical face of the problem," "would
  survive contact with either standard," and open-question closers staged for
  tension ("whether X was possible was open"). Field context states what
  changed, what failed, and what had not been done, in flat declaratives.
- Filler intensifiers. Rejected: "is doing real work," "carries the central
  argument," "a striking challenge." Cut them.
- Unverified claims about the field. Priority ("the first defense to treat the
  deployed system as a whole"), influence ("set the template that the
  backdoor-defense literature still follows"), and exhaustiveness ("the only
  known way to guarantee training-data privacy") are claims about a literature,
  and compiling one paper is no evidence for any of them. Test: name the source.
  If the paper claims it, attribute it to the paper ("the authors position DAWN
  as the first approach to..."); if a cited work settles it, cite it; if
  neither, cut the claim and write what the paper does instead. The house
  register is the reason the rule is needed: terse declarative prose states a
  sourced claim and an invented one in the same voice, so nothing on the page
  marks the difference and later editorial passes read straight over the
  invented one.
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

## Trust vocabulary

In security and cryptography "trusted" is a term of art, and the general-English
sense of the word is wrong everywhere on these pages. A component is **trusted**
when the guarantee assumes it behaves correctly, so that if it misbehaves the
guarantee fails and nothing detects it. The trusted components together are the
**trusted computing base** (TCB). Everything else is **untrusted**, which is a
statement about where the guarantee rests rather than a prediction that the
component will misbehave.

Two consequences:

- **Attested is the opposite of trusted.** A component is attested precisely
  because it is not trusted: its state is checked at run time instead of assumed.
  PAL\*M states the pattern plainly of the confidential VM it runs in: "TDs are
  not inherently trusted. Hence, TDX supports attestation." The same holds for
  *measured*, *verified*, *isolated*, and *encrypted*. Each is a mechanism that
  lets a party stop trusting something, so writing any of them as trust inverts
  the meaning.
- **Say what a component is trusted *for*.** Trust is never global. A CPU may be
  trusted to sign a measurement honestly and not to withstand a physical
  attacker; a hypervisor may be trusted for isolation and not for availability.
  Writing "trusted to X" forces the boundary to come out precise.

Call a component trusted only where the paper puts it in the TCB, and name the
whole trusted set when the paper does. Where a sentence needs the ordinary
English sense, write "relies on," "assumes," or "takes on faith."

## Format by section

- **Paper link.** One line directly under the H1: `**Paper:**` followed by a
  link to the paper itself. The link text names where it goes, `arXiv:ID` for a
  preprint and the venue and year otherwise. No other prose on the line.
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
  re-listing its instances. It stays one paragraph, pitched at the density of
  the paper's own main-body statement of its model, and it carries the threat
  model only: no protocol steps, no mechanism, no proof technique, no measured
  result. "Trusted" in it is the trusted-computing-base sense (see Trust
  vocabulary above), and a formal instantiation reads as this paper's
  instantiation of a requirement rather than as the requirement.
- **Basic Background.** `###` subsections, one per prerequisite cluster, two to
  five sentences each, Wikipedia link density. Covers the general ML and training
  machinery the paper assumes as well as the subfield-specific concepts. Never
  the paper's own content.
- **Paper Context.** Two to four declarative paragraphs: the state of the field
  when the paper appeared. What had been tried, what had broken, what was
  unsettled. Prior or contemporaneous citations only. Not questions. Renders
  inside a collapsed `<details>` block, the heading as its toggle.
- **Reading guidance.** Three bullets, five at the absolute most. One precise
  locus each (a numbered subsection, an equation, a definition, a figure, a
  table), ordered by position in the paper and together covering three roles:
  where the assumptions are pinned down, where the mechanism lives, where the
  claim is settled. The roles are a coverage requirement and a drafting rule, and
  never appear as labels on the page. At least one bullet is a
  neutral attention anchor pointing at where to slow down, without stating why
  the site is contested. Sits directly after Basic Background, above the
  collapsed blocks. Every bullet must be unsatisfiable from a summary of the
  paper; see the rule and its sources in
  [ops/generate-paper-summary.md](ops/generate-paper-summary.md).
- **Motivating questions.** Staff-side archive only (`agent_docs/`); not on
  the student-facing page. Three to five high-level pre-questions per paper,
  answerable by reading it. Students generate their own.
- **Essential Readings.** The slot's essential readings, taken verbatim from
  the spreadsheet column that also feeds the reading-list table, so the page and
  the table show the same set. One bullet each with a one-line "why it's here"
  framing. Renders inside a collapsed `<details>` block, the heading as its
  toggle.
- **References.** Full bibliographic entries for everything cited on the page.
  Renders inside a collapsed `<details>` block, the heading as its toggle.
- **Concept pages.** Same register. Definitions are declarative and
  self-contained, 50 to 500 words; stubs are valid.

## Process

- Outline the points first, then write the prose. Do not ship the outline.
- Revise a section as one block, not sentence by sentence, so the voice stays
  consistent.
