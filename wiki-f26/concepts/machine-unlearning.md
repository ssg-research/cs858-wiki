---
title: "Machine unlearning"
type: concept
description: "Removing the influence of a chosen subset of training data from an already-trained model without full retraining; exact vs approximate unlearning, the right-to-be-forgotten motivation, and the relation to differential privacy."
tags:
  - machine-unlearning
  - privacy
  - right-to-be-forgotten
---

### [Wiki Home](../README.md)

# Machine unlearning

## Definition

Machine unlearning removes the influence of a specified subset of training data
from an already-trained model, producing a model that approximates one trained
as if those examples had never been included, without paying the full cost of
retraining from scratch (Cao and Yang, 2015). The motivation is regulatory and
individual: data-protection regimes such as the EU General Data Protection
Regulation grant a "right to be forgotten," the entitlement to have one's
personal data deleted (Mantelero, 2013). For a deployed model that means erasing
the data's imprint on the parameters, not only the stored records.

Two families divide the area. Exact unlearning re-derives a model provably
equivalent in distribution to one that never saw the deleted data; the canonical
recipe shards the training set so only the affected shard is retrained
(Bourtoule et al., 2021). Approximate unlearning instead edits the parameters of
the existing model to drop the deleted data's influence, trading the equivalence
guarantee for speed (Ginart et al., 2019; Golatkar et al., 2020; Graves et al.,
2021). Early work centered on image classifiers, where the unit of forgetting is
usually a whole class. Forgetting is sometimes cast as a relaxation of
differential privacy, replacing a prior worst-case bound on every example's
influence with after-the-fact removal of specific examples on request (Jagielski
et al., 2022).

## Papers that use this concept

- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](../papers/jang-2022-knowledge-unlearning.md) — proposes gradient ascent on target token sequences as an approximate, post-hoc unlearning method for language models, and defines an empirical test for when a sequence counts as forgotten.
- [What Makes and Breaks Safety Fine-tuning? A Mechanistic Study](../papers/jain-2024-safety-finetuning.md) — unlearning is one of the three safety fine-tuning protocols it compares, among the stronger ones in its analysis.

## Variants and traps

- Exact and approximate unlearning make different claims: only exact unlearning
  carries a formal equivalence certificate, so approximate methods need an
  operational test of when an example counts as forgotten.
- Unlearning the parameters is a separate act from deleting the source records;
  a model can still leak data whose training file was removed.
- Forgetting a whole class in a classifier and forgetting one specific example
  or sequence are different difficulty regimes.

## See also

- [Differential privacy](differential-privacy.md)
- [Memorization](memorization.md)
- [Language model pretraining](language-model-pretraining.md)

### [Wiki Home](../README.md)

## References

- Bourtoule, L., Chandrasekaran, V., Choquette-Choo, C.A., Jia, H., Travers, A.,
  Zhang, B., Lie, D., and Papernot, N. "Machine Unlearning." IEEE Symposium on
  Security and Privacy (S&P), 2021.
- Cao, Y. and Yang, J. "Towards Making Systems Forget with Machine Unlearning."
  IEEE Symposium on Security and Privacy (S&P), 2015.
- Ginart, A., Guan, M., Valiant, G., and Zou, J.Y. "Making AI Forget You: Data
  Deletion in Machine Learning." Advances in Neural Information Processing
  Systems (NeurIPS), 2019.
- Golatkar, A., Achille, A., and Soatto, S. "Eternal Sunshine of the Spotless
  Net: Selective Forgetting in Deep Networks." IEEE/CVF Conference on Computer
  Vision and Pattern Recognition (CVPR), 2020.
- Graves, L., Nagisetty, V., and Ganesh, V. "Amnesiac Machine Learning." AAAI
  Conference on Artificial Intelligence, 2021.
- Jagielski, M., Thakkar, O., Tramèr, F., Ippolito, D., Lee, K., Carlini, N.,
  Wallace, E., Song, S., Thakurta, A., Papernot, N., et al. "Measuring Forgetting
  of Memorized Training Examples." arXiv:2207.00099, 2022.
- Mantelero, A. "The EU Proposal for a General Data Protection Regulation and the
  Roots of the 'Right to be Forgotten'." Computer Law & Security Review, 29(3),
  2013.
