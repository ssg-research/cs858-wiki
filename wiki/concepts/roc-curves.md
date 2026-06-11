---
title: "ROC curves and detection metrics"
type: concept
description: "TPR/FPR trade-offs, ROC curves, AUC, and balanced accuracy for score-thresholding detectors; why security applications evaluate at low false-positive rates and what average-case metrics hide."
tags:
  - evaluation
  - statistics
  - privacy
---

# ROC curves and detection metrics

## Definition

A binary detector that outputs a score and thresholds it makes two kinds of
error: false positives (flagging a negative) and false negatives (missing a
positive). Sweeping the threshold traces the Receiver Operating Characteristic
(ROC) curve, the true-positive rate (TPR) achieved at every false-positive
rate (FPR). Two common summaries compress the curve to a scalar: AUC, the area
under the ROC curve, and balanced accuracy, the accuracy on a 50/50 mix of
positives and negatives at one threshold. TPR/FPR analysis is preferred over
precision/recall when the prevalence of positives in the wild is unknown,
because TPR and FPR do not depend on it.

Both summaries are average-case: AUC integrates over all FPRs, and balanced
accuracy weighs the two error types equally. Security detection tasks (spam
filtering, malware detection, intrusion detection) instead operate at very low
FPRs, since a detector that false-alarms on even a small fraction of the
overwhelmingly benign traffic is useless. Evaluating in that regime means
reading the ROC curve at small FPR values, which a log-log plot makes visible
and a linear plot hides.

## Papers that use this concept

- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — argues membership inference must be evaluated by TPR at low FPR on log-scale ROC curves, and re-ranks prior attacks under that metric.

## Variants and traps

- Two detectors can have identical AUC or balanced accuracy and behave
  completely differently at low FPR; aggregate rankings do not transfer to the
  low-FPR regime.
- A detector confident only about negatives can post a high balanced accuracy
  while never confidently identifying a positive.
- "Accuracy" on a balanced benchmark says little about deployment, where the
  class balance is rarely 50/50.

## See also

- [Likelihood-ratio test](likelihood-ratio-test.md)
- [Membership inference](membership-inference.md)
