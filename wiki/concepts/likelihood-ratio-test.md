---
title: "Likelihood-ratio test"
type: concept
description: "Deciding between two hypotheses by the ratio of observation likelihoods; the Neyman-Pearson lemma makes the thresholded ratio the most powerful test at any fixed false-positive rate."
tags:
  - statistics
  - hypothesis-testing
  - privacy
---

# Likelihood-ratio test

## Definition

A likelihood-ratio test decides between two hypotheses by computing the ratio
of the observation's probability under each and comparing it to a threshold.
The Neyman-Pearson lemma gives the test its authority: among all tests with a
given false-positive rate, thresholding the likelihood ratio achieves the
highest true-positive rate (Neyman and Pearson, 1933). When a detection problem
can be cast as distinguishing two known distributions, the likelihood-ratio
test is not merely a good attack, it is the optimal one, and every other attack
is an approximation to it.

The lemma's premise is the catch: both distributions must be known. In
practice they are estimated, either nonparametrically from samples or by
fitting a parametric family such as a Gaussian. The quality of the test then
rests on the quality of the estimate, and parametric assumptions matter most in
the distribution tails, exactly where low false-positive operation lives.

## Papers that use this concept

- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — frames membership inference as a likelihood-ratio test between models trained with and without the target example; the attack is named for it.

## See also

- [ROC curves and detection metrics](roc-curves.md)
- [Membership inference](membership-inference.md)
- [Shadow models](shadow-models.md)

## References

- Neyman, J. and Pearson, E. S. "On the Problem of the Most Efficient Tests of
  Statistical Hypotheses." Philosophical Transactions of the Royal Society of
  London, 231(694-706), 1933.
