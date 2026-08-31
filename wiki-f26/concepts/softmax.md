---
title: "Softmax and logits"
type: concept
description: "The raw per-class scores a network's last layer emits and the map that turns them into a probability distribution; its shift-invariance and rank preservation, its second role as the mixing weights inside attention, what a prediction API leaks by returning the vector rather than the top label, and why it is the expensive operation under encryption and inside proof circuits."
tags:
  - machine-learning
  - architecture
---

## [Wiki Home](../README.md)

# Softmax and logits

## Definition

A classifier's or language model's last layer emits one unbounded real number per
class or per vocabulary token. These are the **logits**. The **softmax** turns
them into a probability distribution: exponentiate each logit, then divide by the
sum of the exponentials. The result is non-negative and sums to one, which is
what makes it usable as a distribution and what pairs it with the
[cross-entropy loss](cross-entropy.md).

Two properties explain most of how it is used. Softmax is monotone, so it
preserves the ranking of the logits and the arg-max is the same before and after;
turning logits into probabilities changes what the model reports, never which
class it picks. It is also shift-invariant: adding a constant to every logit
leaves the output unchanged, so logits are meaningful only up to an offset, and
implementations subtract the maximum before exponentiating to avoid overflow.
[Temperature](temperature.md) divides the logits before the softmax, which is the
one knob that does change the distribution's shape.

The same operation appears twice more. Inside a
[transformer's](transformer.md) self-attention, a softmax over query-key scores
produces the weights each position uses to mix the others. And at a deployed
prediction API, the softmax output is what a caller gets back: the full
confidence vector, a truncated top-k, or only the arg-max label. That choice is a
leakage decision, since the vector carries the model's relative scores for every
class it did not pick.

## Papers that use this concept

- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — the confidence the model assigns to a candidate's true label is the observable, and the attack rescales it before fitting a distribution to it.
- [Deep Learning with Differential Privacy](../papers/abadi-2016-dp-sgd.md) — in its transfer-learning setting only the softmax layer and the fully connected layers above it are trained privately, which is part of what the reported epsilon covers.
- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-llm-watermark.md) — the watermark is added to the logits before the softmax, which is why it needs no change to the weights.
- [Secure Transformer Inference Made Non-interactive](../papers/zhang-2025-nexus.md) — softmax is one of the nonlinearities that homomorphic evaluation cannot take at face value.
- [zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference](../papers/qu-2025-zkgpt.md) — the softmax inside attention needs comparison and division, which an arithmetic circuit expresses only at a cost.

## Variants and traps

- A softmax probability is not a calibrated confidence. It is what the model's
  scores normalize to, and a model can assign near-certainty to an answer it gets
  wrong; a claim that reads a probability as a likelihood of correctness needs
  separate evidence.
- "Logits" also names the log-odds transform `log(p / (1 - p))` in statistics.
  Privacy papers use that second sense deliberately, rescaling a confidence into
  log-odds so its distribution across models is closer to Gaussian.
- Softmax is cheap on a GPU and expensive nearly everywhere else in this course.
  Exponentiation, division, and the maximum it subtracts are all comparisons or
  transcendental operations, which homomorphic encryption, multiparty protocols,
  and proof circuits have to approximate or emulate.

## See also

- [Cross-entropy loss](cross-entropy.md)
- [Temperature](temperature.md)
- [Transformer](transformer.md)
- [White-box and black-box access](white-box-black-box.md)
