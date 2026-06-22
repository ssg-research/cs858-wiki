---
title: "Decoding and sampling strategies"
type: concept
description: "How an autoregressive LLM turns next-token distributions into text at inference: greedy decoding, temperature, top-k and top-p (nucleus) sampling, and prefilling the first response tokens; the inference-time controls available to a user, developer, or attacker."
tags:
  - language-models
  - llm
---

# Decoding and sampling strategies

## Definition

An autoregressive language model emits one token at a time, each drawn from a
distribution over the vocabulary conditioned on the prompt and the tokens
generated so far. A decoding strategy decides how to turn that distribution into
an actual token. Greedy decoding takes the single most probable token; sampling
draws a token at random from the distribution. Three knobs shape sampling:
temperature rescales the logits so the distribution is flatter (more random) or
sharper (more deterministic); top-k restricts the draw to the `k` highest
probability tokens; top-p, or nucleus sampling, restricts it to the smallest set
of tokens whose probabilities sum past `p`. These are inference-time settings and
do not change the model weights.

Prefilling forces a response to begin with a fixed string, so the model continues
from chosen opening tokens rather than picking its own first token. A locally
served open model exposes full control over decoding and prefilling; some hosted
interfaces expose prefilling for steerability. Because the same controls are
available to whoever calls the model, they are also an attack surface.

## Papers that use this concept

- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — the decoding-parameter exploit and prefilling attacks it unifies operate entirely through these inference-time controls.
- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — candidate generation drives the attack, varying temperature and top-k sampling and conditioning on internet text to surface more diverse memorized samples.
- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](../papers/jang-2022-knowledge-unlearning.md) — measures extraction with greedy decoding and compares against a differentially private decoding baseline that interpolates the logits toward uniform before nucleus sampling.
- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-watermark.md) — embeds the watermark inside the sampling step by biasing green-list logits, and finds that beam search "irons in" a stronger watermark at lower quality cost than multinomial sampling.

## See also

- [Language model pretraining](language-model-pretraining.md)
- [Jailbreak (LLM)](jailbreak.md)
