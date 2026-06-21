---
title: "Membership inference"
type: concept
description: "Attacks that predict whether a specific example was in a model's training set; the security game, the loss-threshold baseline, origins in genomic tracing, and the role of MIA as the standard privacy audit."
tags:
  - membership-inference
  - privacy
  - attack
---

# Membership inference

## Definition

A membership inference attack (MIA) takes a trained model and a candidate
example and predicts whether the example was in the model's training set. It is
formalized as a security game: a challenger trains a model on a sampled
dataset, then flips a coin and hands the adversary either a training-set member
or a fresh point from the same distribution; the adversary, given query access
to the model, must guess which it received (Yeom et al., 2018). Practical
attacks output a confidence score that is thresholded into a member/non-member
decision, so an attack defines a whole trade-off curve between true and false
positives rather than a single accuracy number.

The attack class began outside machine learning, as tracing attacks on genomic
data: an individual's presence in a study cohort could be detected from
published aggregate statistics, which is itself the privacy violation (Homer et
al., 2008). It was brought to machine learning models with query access by
Shokri et al. (2017). The simplest ML attack thresholds the model's loss on the
candidate, exploiting the fact that training drives down loss on training
examples (Yeom et al., 2018).

Membership inference matters twice over. Directly, membership can be sensitive
(presence in a medical dataset). Indirectly, it is the measurement instrument
of training-data privacy: production privacy audits are built on MIA libraries,
and stronger attacks such as training-data extraction use membership
predictions as a building block (Carlini et al., 2021).

## Papers that use this concept

- [Membership Inference Attacks From First Principles](../papers/carlini-2022-lira.md) — the attack class the paper re-derives as a hypothesis test and re-evaluates at low false-positive rates.
- [Deep Learning with Differential Privacy](../papers/abadi-2016-dp-sgd.md) — the canonical defense whose guarantee upper-bounds any membership inference attack.
- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — reduces training-data extraction to membership inference, ranking generated candidates by a calibrated membership signal.
- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](../papers/jang-2022-knowledge-unlearning.md) — measures privacy on targeted extraction rather than membership-inference recall, and contrasts the two as risk metrics.

## Variants and traps

- Membership inference predicts a bit about a known candidate example. It is
  distinct from training-data extraction (recovering examples outright) and
  from inferring aggregate properties of the training set.
- An attack's average accuracy and its ability to confidently identify any
  member are different quantities; an attack can excel at one and fail at the
  other.
- Predicting non-membership well is not the same as predicting membership
  well; the two error types have asymmetric value to a real adversary.

## See also

- [Shadow models](shadow-models.md)
- [Memorization](memorization.md)
- [ROC curves and detection metrics](roc-curves.md)
- [Differential privacy](differential-privacy.md)

## References

- Carlini, N., Tramèr, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee,
  K., Roberts, A., Brown, T., Song, D., Erlingsson, Ú., et al. "Extracting
  Training Data from Large Language Models." USENIX Security Symposium, 2021.
- Homer, N., Szelinger, S., Redman, M., Duggan, D., Tembe, W., Muehling, J.,
  Pearson, J. V., Stephan, D. A., Nelson, S. F., and Craig, D. W. "Resolving
  Individuals Contributing Trace Amounts of DNA to Highly Complex Mixtures
  Using High-Density SNP Genotyping Microarrays." PLoS Genetics, 4(8), 2008.
- Shokri, R., Stronati, M., Song, C., and Shmatikov, V. "Membership Inference
  Attacks Against Machine Learning Models." IEEE Symposium on Security and
  Privacy, 2017.
- Yeom, S., Giacomelli, I., Fredrikson, M., and Jha, S. "Privacy Risk in
  Machine Learning: Analyzing the Connection to Overfitting." IEEE Computer
  Security Foundations Symposium (CSF), 2018.
