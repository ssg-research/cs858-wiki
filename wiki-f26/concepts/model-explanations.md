---
title: "Model explanations"
type: concept
description: "Post-hoc explanations released with a model's prediction: feature attribution, influence-based, and counterfactual/recourse explanations; what they reveal about the decision boundary and training data, and the attack surface they open."
tags:
  - interpretability
  - defense
---

[Home page](../README.md)

# Model explanations

## Definition

A model explanation is auxiliary information released alongside a prediction to
make a model's computation interpretable. Three families recur. Feature
attribution assigns each input feature a contribution to the prediction; standard
methods include Integrated Gradients (Sundararajan et al., 2017), DeepLIFT,
SmoothGrad, and Grad-CAM. Influence-based explanations
return the training records most responsible for a prediction, estimated through
influence functions (Koh and Liang, 2017). Counterfactual, or recourse,
explanations give the minimal change to an input that would flip its outcome.

None of these require retraining the model. All of them expose information about
the model's decision boundary and its training data, which is what lets the same
release serve transparency and double as an attack surface for inference and
extraction.

## Papers that use this concept

- [SoK: Unintended Interactions among Machine Learning Defenses and Risks](../papers/duddu-2024-unintended-interactions.md) — treats explanations as a transparency defense and surveys how releasing them raises susceptibility to privacy and security risks.

## See also

- [Mechanistic interpretability](mechanistic-interpretability.md)
- [Membership inference](membership-inference.md)
- [Memorization](memorization.md)

[Home page](../README.md)

## References

- Sundararajan, M., et al. "Axiomatic Attribution for Deep Networks."
  International Conference on Machine Learning (ICML), 2017.
- Koh, P. W. and Liang, P. "Understanding Black-box Predictions via Influence
  Functions." International Conference on Machine Learning (ICML), 2017.
