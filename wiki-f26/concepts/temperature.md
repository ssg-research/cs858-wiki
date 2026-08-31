---
title: "Temperature"
type: concept
description: "The scalar that divides a model's logits before the softmax, flattening or sharpening the distribution it produces; the randomness knob at decoding time, the softening knob in knowledge distillation, and an inference-time control available to whoever calls the model."
tags:
  - machine-learning
  - language-models
  - llm
---

## [Wiki Home](../README.md)

# Temperature

## Definition

A neural network's last layer emits logits, which a softmax turns into a
probability distribution. Temperature is a positive scalar that divides the
logits before that softmax. At temperature 1 the model's own distribution comes
out unchanged. Below 1 the distribution sharpens, concentrating mass on the
highest logit, and in the limit it becomes the arg-max, which is greedy
decoding. Above 1 it flattens toward uniform, raising the probability of
answers the model rates as unlikely. Temperature changes no weights; it is set
per call at inference.

Two settings use it for opposite purposes. In
[decoding](decoding-strategies.md), temperature is the randomness knob: low
temperature makes generation repetitive and near-deterministic, high temperature
makes it diverse and more prone to incoherence, and it composes with top-k and
top-p, which restrict which tokens may be drawn at all. In
[knowledge distillation](knowledge-distillation.md), a high temperature applied
to the teacher softens its output distribution so the student can see the
relative probabilities the teacher assigns to the classes it did not pick, which
is where most of the transferred information sits (Hinton et al., 2015).

Because temperature is exposed to whoever calls the model, it is also an
adversarial lever: repeated sampling at raised temperature explores completions
that greedy decoding never reaches, and reported results at one temperature need
not hold at another.

## Papers that use this concept

- [Jailbroken: How Does LLM Safety Training Fail?](../papers/wei-2023-jailbroken.md) — samples at temperature 0 so that attack outcomes are not confounded by decoding noise, and rechecks the strongest attacks at temperature 1.
- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — the decoding-parameter exploits it unifies raise temperature and resample until a completion escapes the refusal prefix.
- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — generates candidates under a decaying temperature so that early tokens are drawn diversely and later ones stay coherent.
- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../papers/pearce-2023-vulnerability-repair.md) — sweeps temperature to control how varied the candidate patches are, then ensembles across several settings.

## Variants and traps

- Sampling temperature and distillation temperature are the same operation put to
  different ends. One is a knob on the model that generates; the other is a knob
  on the teacher whose outputs another model is trained against.
- A result quoted without its temperature is underspecified. Temperature 0 fixes
  a single deterministic output, so a success rate measured there answers a
  different question than one measured over samples at temperature 1.

## See also

- [Decoding and sampling strategies](decoding-strategies.md)
- [Cross-entropy loss](cross-entropy.md)
- [Knowledge distillation](knowledge-distillation.md)

## References

- Hinton, G., Vinyals, O., and Dean, J. "Distilling the Knowledge in a Neural
  Network." arXiv:1503.02531, 2015.
