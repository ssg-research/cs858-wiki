---
title: "Statistical hypothesis testing"
type: concept
description: "Deciding between a null hypothesis and its alternative from a test statistic and a threshold; p-values, type I and type II errors, and the one-proportion z-test for whether an observed count of successes exceeds chance."
tags:
  - hypothesis-testing
  - statistics
  - evaluation
---

# Statistical hypothesis testing

## Definition

A hypothesis test decides between a null hypothesis `H0` (the "nothing
interesting is happening" baseline) and an alternative, using a test statistic
computed from observed data. One picks a rejection threshold and rejects `H0`
when the statistic crosses it. Two errors are possible: a type I error (false
positive) rejects a true `H0`, and a type II error (false negative) fails to
reject a false `H0`. The false-positive rate is the significance level; one minus
the false-negative rate is the test's power. A p-value is the probability, under
`H0`, of a statistic at least as extreme as the one observed, so a small p-value
is strong evidence against `H0`.

The one-proportion z-test asks whether the number of "successes" in `T`
independent trials is larger than a hypothesized success probability `p0` would
predict. Under `H0` the count has mean `T*p0` and variance `T*p0*(1-p0)`, so the
standardized statistic `z = (count - T*p0) / sqrt(T*p0*(1-p0))` is approximately
standard normal for large `T`, and a chosen `z` threshold maps to a p-value
through the normal tail. The same machinery appears in detection and security as
a score threshold with a controlled false-positive rate.

## Papers that use this concept

- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-watermark.md) — detection is a one-proportion z-test on the count of "green" tokens against the null hypothesis that the text was produced with no knowledge of the green-list rule, giving an interpretable p-value and a controllable false-positive rate.

## See also

- [ROC curves and detection metrics](roc-curves.md)
- [Likelihood-ratio test](likelihood-ratio-test.md)
