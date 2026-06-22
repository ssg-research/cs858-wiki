---
title: "Entropy (information theory)"
type: concept
description: "Shannon entropy as a measure of how spread out or uncertain a discrete distribution is; maximal under a uniform distribution, zero under a point mass, and the per-position uncertainty of a language model's next-token distribution."
tags:
  - statistics
  - machine-learning
---

# Entropy (information theory)

## Definition

The Shannon entropy of a discrete probability distribution `p` is
`H(p) = - sum_k p_k * log(p_k)`, a measure of how spread out, or uncertain, the
distribution is. It is maximal when `p` is uniform over its outcomes and minimal
(zero) when all mass sits on a single outcome. Entropy is reported in bits when
the logarithm is base 2 and in nats when it is the natural logarithm.

For a language model, the entropy of the next-token distribution at a position
measures how many continuations are plausible. A low-entropy position has one
nearly certain next token, so the model is effectively forced; a high-entropy
position has many comparable candidates, so the choice is genuinely open. This
distinction governs any scheme that perturbs token selection, since there is room
to alter a choice only where the distribution is spread out.

## Papers that use this concept

- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-watermark.md) — detectability depends on the entropy of the generated text: high-entropy spans carry a strong watermark at little quality cost, while near-deterministic low-entropy spans carry almost no watermark signal. The paper introduces its own "spike entropy" variant to state its bounds.

## See also

- [Perplexity](perplexity.md)
- [KL divergence](kl-divergence.md)
