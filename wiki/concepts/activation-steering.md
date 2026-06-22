---
title: "Activation steering"
type: concept
description: "Changing a frozen model's behavior at inference by adding a vector to its hidden activations, with no weight updates; difference-of-activation steering vectors, activation addition (ActAdd), and inference-time intervention (ITI)."
tags:
  - interpretability
  - representations
  - control
  - llm-safety
---

# Activation steering

## Definition

Activation steering changes a frozen model's behavior at inference by adding a
fixed vector to its hidden activations at one or more layers, leaving the weights
unchanged. The steering vector is typically the difference between activations on
contrasting inputs, for example a concept present versus absent, and is added or
subtracted during the forward pass to push outputs toward or away from the
concept. Activation addition (ActAdd) builds such vectors from individual prompt
pairs (Turner et al., 2023), and inference-time intervention shifts activations
along directions tied to truthfulness to elicit more truthful answers (Li et al.,
2023). Because the intervention edits internal state rather than the input, it
requires access to the model's activations.

## Papers that use this concept

- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — its "representation control" generalizes steering with stronger baseline transformations and representation tuning, applied across many behaviors.

## See also

- [Distributed representations](distributed-representations.md)
- [Linear probing (probing classifiers)](linear-probing.md)
- [White-box vs. black-box access](white-box-black-box.md)

## References

- Li, K., Patel, O., Viégas, F., Pfister, H., and Wattenberg, M. "Inference-Time
  Intervention: Eliciting Truthful Answers from a Language Model." 2023.
- Turner, A., Thiergart, L., Udell, D., Leech, G., Mini, U., and MacDiarmid, M.
  "Activation Addition: Steering Language Models Without Optimization." 2023.
  arXiv:2308.10248.
