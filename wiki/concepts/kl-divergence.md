---
title: "Kullback-Leibler divergence"
type: concept
description: "An asymmetric measure of how far one probability distribution sits from a reference; per-token KL between two language models' next-token distributions, the KL penalty in RLHF, and its role as the unit of 'distribution shift' from a base model."
tags:
  - statistics
  - machine-learning
  - alignment
---

# Kullback-Leibler divergence

## Definition

The Kullback-Leibler (KL) divergence `D_KL(P || Q)` measures how far a
distribution `P` is from a reference distribution `Q`. It is the expected
log-ratio `log(P/Q)` taken under `P`. It is zero exactly when `P` equals `Q`,
never negative, and asymmetric: `D_KL(P || Q)` and `D_KL(Q || P)` differ, so KL
is a divergence, not a distance metric.

For a language model, each step defines a categorical distribution over the
vocabulary for the next token given the context so far. The per-token KL between
two models at one position measures how differently they would continue from the
same prefix; aggregating it over positions quantifies how far one model's
generative distribution has moved from another's. This makes KL the natural unit
for "how much did alignment change the base model." It is the same quantity that
appears as the regularizer in [RLHF](rlhf.md), where a KL penalty against the
base model keeps the aligned policy from drifting too far. Minimizing the
cross-entropy of a model against data is equivalent to minimizing the KL from the
data distribution plus a constant, which is why the next-token training loss and
KL measurements read in the same currency.

## Papers that use this concept

- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — per-token KL between an aligned model and its base model is the measurement that localizes where alignment concentrates.
- [Knockoff Nets: Stealing Functionality of Black-Box Models](../papers/orekondy-2019-knockoff-nets.md) — training the knockoff to imitate the victim's predictions over the transfer set is equivalent to minimizing the KL divergence between the two models there.

## Variants and traps

- KL is asymmetric. "Forward" KL `D_KL(data || model)` and "reverse" KL
  `D_KL(model || data)` reward different failure modes, so the argument order
  matters.
- It is not a metric: no symmetry and no triangle inequality.
- "Spending KL" on a "KL budget" is common shorthand for how much total
  divergence from a reference a training procedure is permitted to accumulate.

## See also

- [Reinforcement learning from human feedback (RLHF)](rlhf.md)
- [Language model pretraining](language-model-pretraining.md)
