---
title: "Robust optimization"
type: concept
description: "Optimizing for the worst case within an uncertainty set, expressed as a min-max (saddle-point) problem; its origin in operations research and the role of Danskin's theorem in differentiating the outer objective."
tags:
  - robust-optimization
  - adversarial-robustness
  - adversarial-training
---

## [Wiki Home](../README.md)

# Robust optimization

## Definition

Robust optimization minimizes loss against the worst case within an uncertainty
set rather than against a fixed input. This gives a min-max (saddle-point)
objective: an inner maximization over perturbations in the set, nested in an
outer minimization over parameters. The formulation goes back to Wald's work on
statistical decision theory (Wald, 1945) and is a textbook subject in
operations research (Ben-Tal et al., 2009).

In adversarial ML, the inner maximization is the search for an
[adversarial example](adversarial-examples.md), and the outer minimization is
[adversarial training](adversarial-training.md). A small saddle-point value is a
guarantee: if no perturbation in the set raises the loss, no allowed attack
succeeds.

Both problems are hard for neural networks, since the outer problem is non-convex
and the inner problem non-concave. Danskin's theorem supplies a descent direction
for the outer problem as the gradient at an inner maximizer, which justifies the
attack-then-train recipe. The theorem assumes exact maximizers of a smooth
function, so for non-smooth networks solved approximately it holds only as an
approximation.

## Papers that use this concept

- [Towards Deep Learning Models Resistant to Adversarial Attacks](../papers/madry-2018-pgd.md) — adopts the saddle-point formulation as its central object and invokes Danskin's theorem to justify training on inner maximizers.

## Variants and traps

- Danskin's theorem assumes the inner maximum is attained exactly and the
  function is well behaved. In practice the inner problem is solved
  approximately and the network is non-smooth, so the guarantee is heuristic
  rather than exact.
- A min-max value is only as meaningful as its uncertainty set. A tiny or badly
  chosen perturbation set makes the robustness guarantee vacuous.

## See also

- [Adversarial training](adversarial-training.md)
- [Adversarial threat model](adversarial-threat-model.md)
- [Empirical risk minimization](empirical-risk-minimization.md)
- [Adversarial examples](adversarial-examples.md)

## References

- Wald, A. "Statistical Decision Functions Which Minimize the Maximum Risk."
  Annals of Mathematics, 1945.
- Ben-Tal, A., El Ghaoui, L., and Nemirovski, A. *Robust Optimization*.
  Princeton University Press, 2009.
