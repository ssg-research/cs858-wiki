---
title: "Mutual information"
type: concept
description: "A measure of how much observing one random variable reduces uncertainty about another; the KL divergence between a joint distribution and the product of its marginals, its entropy decomposition, and its use as an information-leakage measure and the rate term in rate-distortion."
tags:
  - statistics
  - machine-learning
  - model-extraction
---

## [Wiki Home](../README.md)

# Mutual information

## Definition

The mutual information `I(X;Y)` between two random variables measures how much
knowing one reduces uncertainty about the other. It is the
[KL divergence](kl-divergence.md) between the joint distribution `P(X,Y)` and the
product of the marginals `P(X)P(Y)`, so it is zero exactly when `X` and `Y` are
independent, never negative, and symmetric in its two arguments. The canonical
formalization is Shannon's, presented in standard texts (Cover, 1999).

Mutual information decomposes through entropy: `I(X;Y) = H(X) - H(X|Y) =
H(Y) - H(Y|X)`, where `H(X)` is the entropy of `X` and `H(X|Y)` is the
conditional entropy remaining after `Y` is observed. Reducing the mutual
information between a secret and an observable therefore raises the conditional
entropy of the secret given the observable, which is why the quantity reads as
an information-leakage measure in security and privacy: it upper-bounds how much
any function of the observable can reveal about the secret. The same quantity is
the rate term in rate-distortion theory, where minimizing `I(X;\hat{X})` subject
to a bound on a distortion measure between a source `X` and its compressed
representation `\hat{X}` gives the smallest description that stays within the
allowed distortion.

## Papers that use this concept

- [ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks](../papers/tang-2024-modelguard.md) — the defense perturbs a model's returned predictions to minimize the mutual information between the clean predictions and the perturbed ones under a distortion budget, a rate-distortion formulation that bounds what an adaptive attacker can recover.

## See also

- [Kullback-Leibler divergence](kl-divergence.md)

## References

- Cover, T.M. "Elements of Information Theory." John Wiley & Sons, 1999.
