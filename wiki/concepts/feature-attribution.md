---
title: "Feature attribution and explanations"
type: concept
description: "Post-hoc explanations that attribute a prediction to its inputs or training data: attribution/saliency methods (Integrated Gradients, DeepLift, SmoothGrad, Grad-CAM), influence functions, and counterfactual/recourse explanations; transparency tools released alongside predictions that also enlarge the attack surface."
tags:
  - interpretability
  - explanations
  - transparency
---

# Feature attribution and explanations

## Definition

Post-hoc explanations annotate a model's prediction with additional information
about how it was reached. Three families recur. Attribution (saliency) methods
score how much each input attribute contributed to the output; Integrated
Gradients, DeepLift, SmoothGrad, and Grad-CAM are standard instances.
Influence-based explanations instead point to the training records most
responsible for a prediction. Recourse (counterfactual) explanations return the
minimal change to an input that would flip the outcome to a desired one.

Explanations are released alongside predictions to increase transparency, for
example to audit whether a model relies on a sensitive attribute. Because an
explanation exposes more of the model's internal sensitivity than a bare label,
it is also an extra channel an adversary can read or manipulate. This family is
distinct from [mechanistic interpretability](mechanistic-interpretability.md),
which reverse-engineers internal circuits, and from representation-level analysis
of activation directions; feature attribution explains individual input-output
behavior without claiming a mechanism.

## Papers that use this concept

- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2023-unintended-interactions.md) — treats releasing explanations as a transparency defense and traces how it interacts with privacy and security risks.

## See also

- [Mechanistic interpretability](mechanistic-interpretability.md)
- [Linear probing](linear-probing.md)

## References

- Sundararajan, M., et al. "Axiomatic Attribution for Deep Networks."
  International Conference on Machine Learning (ICML), 2017.
- Selvaraju, R. R., et al. "Grad-CAM: Visual Explanations from Deep Networks via
  Gradient-Based Localization." International Conference on Computer Vision
  (ICCV), 2017.
- Koh, P. W. and Liang, P. "Understanding Black-Box Predictions via Influence
  Functions." International Conference on Machine Learning (ICML), 2017.
