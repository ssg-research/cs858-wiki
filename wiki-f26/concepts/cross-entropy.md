---
title: "Cross-entropy loss"
type: concept
description: "The standard training objective for classifiers and language models: the negative log probability the model assigns to the correct answer, read off a softmax over the logits; its equivalence to maximum likelihood and to a KL divergence, and its per-example value as the signal privacy attacks measure."
tags:
  - machine-learning
  - optimization
---

## [Wiki Home](../README.md)

# Cross-entropy loss

## Definition

A classifier's last layer emits one real number per class, called the logits.
The softmax function exponentiates the logits and normalizes them, producing a
probability distribution over the classes. The cross-entropy loss on a labelled
example is the negative logarithm of the probability the model assigned to that
example's true label. It is zero when the model puts all its mass on the correct
class and grows without bound as that probability falls toward zero.

Averaged over a training set, this loss is the objective that
[empirical risk minimization](empirical-risk-minimization.md) drives down with
[stochastic gradient descent](stochastic-gradient-descent.md). Minimizing it is
the same as maximizing the likelihood the model assigns to the training labels,
and it equals the [KL divergence](kl-divergence.md) from the predicted
distribution to the one-hot label distribution plus a constant that the
parameters cannot change. Fitting a student to a teacher's full soft
distribution instead of a one-hot label is the same loss with a different
target, which is [knowledge distillation](knowledge-distillation.md).

An autoregressive language model applies the identical loss at every token
position, over the vocabulary rather than a label set; this is what "next-token
loss" names. Its per-token average, exponentiated, is
[perplexity](perplexity.md).

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — the outer minimization drives this loss down over the parameters while the inner maximization drives the same loss up over the input, so one quantity defines both halves of its saddle-point problem.
- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — the per-example loss on a candidate point is the observable its hypothesis test reads, and training makes members low-loss by construction.
- [Knockoff Nets: Stealing Functionality of Black-Box Models](../papers/orekondy-2019-knockoff-nets.md) — the knockoff is fit to the victim's returned probability vectors under this loss, which is how a transfer set becomes a trained substitute.
- [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](../papers/wang-2019-neural-cleanse.md) — its classifiers are trained by minimizing it, and it recovers a candidate trigger by minimizing a classification loss over an input mask instead of over the weights.
- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — reads the loss position by position, since where the per-token loss and its gradient concentrate is where fine-tuning moves the model.
- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — the substitute is fit to the returned confidence vectors under this loss, so perturbing those vectors changes what the substitute learns.
- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — the per-sequence value under the target model, set against the same value under a reference model, is the ranking signal that separates memorized text from merely fluent text.
- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](../papers/jang-2022-knowledge-unlearning.md) — runs the same objective backwards, taking gradient ascent steps on the sequences to be forgotten.
- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-llm-watermark.md) — its exponential, perplexity, is the yardstick for how much watermarking costs the text's quality.

## Variants and traps

- Entropy, cross-entropy, and KL divergence are three different quantities and
  the names invite conflation. Entropy scores one distribution; cross-entropy
  scores a predicted distribution against a target; the
  [KL divergence](kl-divergence.md) is their difference, and it is the
  cross-entropy that a trainer actually computes.
- The averaged loss and the per-example loss carry different information. The
  average is the training objective; the per-example value is what
  [membership inference](membership-inference.md) and
  [memorization](memorization.md) measurements read, and two models with the same
  average can assign very different losses to the same point.

## See also

- [Softmax and logits](softmax.md)

- [Empirical risk minimization](empirical-risk-minimization.md)
- [KL divergence](kl-divergence.md)
- [Perplexity](perplexity.md)
- [Temperature](temperature.md)
