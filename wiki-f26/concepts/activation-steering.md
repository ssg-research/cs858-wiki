---
title: "Activation steering"
type: concept
description: "Controlling an LLM's behavior at inference by adding, subtracting, or projecting out a concept direction in its hidden activations; steering vectors, activation addition, inference-time intervention, and the limits of single-direction control."
tags:
  - interpretability
  - llm-safety
  - language-models
---

# Activation steering

## Definition

Activation steering controls a model's behavior by intervening on its hidden
activations at inference, rather than by changing the prompt or the weights. A
concept direction is added to or subtracted from the activations at one or more
layers to strengthen or suppress that concept in the output, or projected out to
remove it. Difference vectors between activations on paired prompts give such
directions without any optimization (Turner et al., 2023), and steering a
truthfulness direction has been used to make a model's answers more truthful (Li
et al., 2023). The intervention is cheap and targeted, which makes it attractive
for safety; a single direction need not transfer across contexts, and a steer
can perturb unrelated behavior.

## Papers that use this concept

- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — its "Representation Control" adds, subtracts, or projects out reading and contrast vectors in activations to steer concepts such as honesty and harmlessness.

## See also

- [Linear representation hypothesis](linear-representation-hypothesis.md)
- [Contrastive prompt pairs](contrastive-prompt-pairs.md)
- [Red teaming (language models)](red-teaming.md)

## References

- Li, K., Patel, O., Viégas, F., Pfister, H., and Wattenberg, M. "Inference-Time
  Intervention: Eliciting Truthful Answers from a Language Model." 2023.
- Turner, A., Thiergart, L., Udell, D., Leech, G., Mini, U., and MacDiarmid, M.
  "Activation Addition: Steering Language Models Without Optimization."
  arXiv:2308.10248, 2023.
