---
title: "LLM watermarking"
type: concept
description: "Embedding a hidden, human-imperceptible signal in a generative model's output text so machine-generated text can later be detected for provenance: decoding-time logit/sampling biasing (green-list/red-list) versus post-hoc text editing, statistical detection from the text alone, and the contrast with watermarking model weights."
tags:
  - watermarking
  - provenance
  - language-models
---

# LLM watermarking

## Definition

LLM watermarking embeds a hidden signal into the text a language model
generates, so that a passage can later be attributed to a machine source. The
signal is meant to be imperceptible to a human reader while remaining
algorithmically detectable, often from a short span of text and without access
to the model that produced it. The goal is provenance, separating
machine-generated text from human-written text, which distinguishes it from
[model watermarking](model-watermarking.md), where the marked object is the
trained model itself and the goal is to prove ownership of a copy. Marking the
output of a generative process is a form of linguistic steganography, the task
of hiding information inside natural-language text (Atallah et al., 2001).

Two broad families exist. Decoding-time schemes bias the generation process
itself, for example by pseudo-randomly partitioning the vocabulary into a "green
list" and a "red list" at each step and promoting green-list tokens, so the
output carries an over-representation of marked tokens. Post-hoc schemes edit
already-written text, substituting synonyms or rewriting spans with a masked
language model. Detection is a statistical test on the embedded signal and
typically requires a secret key or scheme but not the generating model. The
strength of the mark depends on the entropy of the text: high-entropy passages,
where many continuations are plausible, can be marked with little quality loss,
while near-deterministic passages carry almost no signal. Watermarking discrete
text has historically been harder than watermarking continuous media such as
images or audio (Katzenbeisser and Petitcolas, 2000).

## Papers that use this concept

- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-llm-watermark.md) — introduces a decoding-time green-list/red-list logit bias with statistical (z-test) detection from the text alone, the canonical generation-time text watermark.

## Variants and traps

- Output or text watermarking marks the generated content; model watermarking
  marks the model's weights or behavior. The two solve different problems
  (provenance versus ownership) and assume different access.
- Robustness is the central question: edits, paraphrasing, and rewriting with
  another model can weaken or remove the signal, and the cost an attacker pays
  to do so is what a scheme's security argument turns on.

## See also

- [Model watermarking](model-watermarking.md)
- [Decoding strategies](decoding-strategies.md)
- [Perplexity](perplexity.md)

## References

- Atallah, M. J., Raskin, V., Crogan, M., Hempelmann, C., Kerschbaum, F., Mohamed, D., and Naik, S. "Natural Language Watermarking: Design, Analysis, and a Proof-of-Concept Implementation." Information Hiding (Lecture Notes in Computer Science), 2001.
- Katzenbeisser, S. and Petitcolas, F. A. P. "Information Hiding Techniques for Steganography and Digital Watermarking." Artech House, 2000.
