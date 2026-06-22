---
title: "SoK: Unintended Interactions among Machine Learning Defenses and Risks"
authors:
  - Duddu, Vasisht
  - Szyller, Sebastian
  - Asokan, N.
year: 2023
section: "Unintended Interactions among ML Defenses and Risks"
primary: true
arxiv: "2312.04542"
tags:
  - sok
  - trustworthy-ml
  - security
  - privacy
  - fairness
  - overfitting
  - memorization
---

# SoK: Unintended Interactions among Machine Learning Defenses and Risks

## High-level overview

A machine learning model faces many risks at once, spanning security (evasion,
poisoning, model theft), privacy (membership, attribute, and distribution
inference, and data reconstruction), and fairness (discriminatory behavior).
Each risk has its own defenses, and most are designed and evaluated against that
one risk in isolation. A defense effective against its target risk can, as a side
effect, raise or lower the model's susceptibility to a different, unrelated risk.
A known example is that adversarial training, deployed for robustness, makes
membership inference easier. This paper calls such side effects **unintended
interactions** and asks how to foresee them rather than rediscover each one by
accident.

The paper is a systematization of knowledge (SoK): it organizes a scattered
literature under one framework instead of contributing a new attack or defense.
Its central conjecture is that two phenomena, **overfitting** (the train-test
generalization gap) and **memorization** (per-example fitting of training
records), are the shared underlying causes of these interactions. A defense
changes how much a model overfits or memorizes, and that change propagates to
every other risk that also depends on overfitting or memorization. To make this
concrete, the framework identifies a set of **factors**, properties of the
training data, the training algorithm, and the model, that influence overfitting
and memorization, and expresses each defense and each risk in terms of those
shared factors. The paper surveys existing literature and situates the
interactions reported there within the framework, distinguishing which are backed
by empirical evidence, which by theory, and which are only conjectured. It then
offers a guideline for conjecturing the direction of an unstudied interaction
from the factors a defense and a risk share, and applies it to two previously
unexplored interactions, validating both empirically on a tabular dataset: group
fairness lowers data-reconstruction success, and releasing explanations raises
distribution-inference success. Terms that travel differently across communities
are pinned down: a "risk" is a security, privacy, or fairness threat to the
deployed model; "observables" are what an adversary can read off the model
(predictions, intermediate activations, gradients, parameters); and an
"interaction" is correlational, an association between a defense's effectiveness
and a risk's susceptibility, not a proof of causation.

**Threat Model:** This is a meta-level paper, so it does not posit one adversary
but reasons over many at once. The defender is a model owner who deploys a single
defense to mitigate one target risk: adversarial training against evasion,
outlier removal against poisoning, watermarking or fingerprinting against model
theft, differential privacy against inference and reconstruction, group fairness
against discriminatory behavior, or releasing explanations for transparency. A
separate adversary then mounts a different risk against the same model, with the
access that risk assumes: an evasion adversary perturbs inputs at test time
within a bounded budget; a poisoning adversary alters training data; a model-theft
adversary queries the model and trains a surrogate; inference and reconstruction
adversaries read observables under black-box (outputs only) or white-box
(activations, gradients, parameters) access. Discriminatory behavior is a property
of the model rather than the act of an adversary. The defender's claim is that
the deployed defense mitigates its target risk; the paper's claim is the
conjecture that the same defense's effect on overfitting and memorization, through
shared factors, raises or lowers susceptibility to the other risks. That claim is
correlational and is demonstrated empirically for two interactions, not proved in
general.

## Why read this

Most attacks and defenses are studied one at a time, against a single risk. A
deployed model faces many risks together, and a defense chosen to mitigate one
can quietly raise or lower its exposure to others. This paper is the first
systematic attempt to map those cross-effects across security, privacy, and
fairness, and to explain them through two shared causes, overfitting and
memorization, rather than treating each interaction as a separate surprise.

## Basic Background

### The three families of risk

The paper organizes risks into security, privacy, and fairness. Security risks
include evasion, where an adversary perturbs an input to force a misclassification
([adversarial examples](../concepts/adversarial-examples.md)); poisoning, where an
adversary corrupts training data to change what the model learns
([data poisoning](../concepts/data-poisoning.md)), with
[backdoor attacks](../concepts/backdoor-attacks.md) as the trigger-conditioned
case; and model theft, where an adversary reproduces a model's functionality from
query access ([model extraction](../concepts/model-extraction.md)). Privacy risks
include [membership inference](../concepts/membership-inference.md) (was this
record in the training set?),
[attribute inference](../concepts/attribute-inference.md) (the value of a hidden
sensitive attribute of a record),
[property or distribution inference](../concepts/property-inference.md) (a global
property of the training distribution), and
[data reconstruction](../concepts/data-reconstruction.md) (recovering whole
records). Fairness concerns discriminatory behavior, where a model's performance
differs across sensitive subgroups
([algorithmic fairness](../concepts/algorithmic-fairness.md)).

### The defenses

Each risk family has defenses the paper tracks.
[Adversarial training](../concepts/adversarial-training.md) trains on perturbed
inputs to resist evasion. Outlier removal discards training records that look
like poisons or backdoors, treating them as distribution outliers.
[Model watermarking](../concepts/model-watermarking.md) embeds an
owner-verifiable marker so a stolen copy can be claimed, while fingerprinting
instead derives a signature from an already-trained model to test whether a
suspect model was derived from it, without retraining.
[Differential privacy](../concepts/differential-privacy.md), realized for deep
learning as DP-SGD, bounds any single record's influence to limit inference and
reconstruction. Group fairness constrains the model to behave equitably across
subgroups. Releasing post-hoc
[explanations](../concepts/feature-attribution.md) adds transparency by exposing
how a prediction depends on its inputs.

### Overfitting, memorization, and generalization

The framework rests on two notions of how a model fits its data.
[Overfitting](../concepts/overfitting.md) is the aggregate gap between training
and test performance, the failure to generalize from the
[empirical risk](../concepts/empirical-risk-minimization.md) minimized during
training to the true distribution.
[Memorization](../concepts/memorization.md) is per-example: the degree to which a
model's behavior on a specific record depends on that record being in the
training set, pronounced for outliers and rare, long-tail examples. The two are
related but not the same, and a model with a small generalization gap can still
memorize individual records.

### Adversary access and observables

What an adversary can do depends on its access, described on the
[white-box / black-box](../concepts/white-box-black-box.md) spectrum: black-box
access exposes only the model's outputs, while white-box access exposes internal
activations, gradients, and parameters. The paper calls the quantities an
adversary reads off the model "observables," and many privacy attacks succeed
precisely because observables are distinguishable for different inputs,
subgroups, or training distributions.

## Paper Context

By the early 2020s, trustworthy machine learning had matured into largely
separate threads. Security studied evasion, poisoning, and model theft; privacy
studied inference and reconstruction attacks; fairness studied subgroup
disparities. Each thread accumulated its own attacks, defenses, and surveys, and
broad systematizations treated these risks and their defenses as parallel topics
rather than interacting ones (Papernot et al., 2018; Mehrabi et al., 2021).

Individual tensions between corners of this space had surfaced. The connection
between overfitting and membership inference was made explicit early, framing
generalization as a privacy-relevant quantity (Yeom et al., 2018). Securing a
model against adversarial examples with robust training was then shown to raise
its membership-inference exposure (Song et al., 2019; Hayes, 2020), and
differential privacy was found to degrade accuracy unevenly across subgroups,
putting privacy in tension with fairness (Bagdasaryan et al., 2019). These
results arrived case by case, each a pairwise finding about one defense and one
risk.

A few works looked across more than two corners at once. Multilateral trade-offs
among accuracy, robustness, fairness, and privacy were studied under differential
privacy (Gittens et al., 2022), and the privacy-fairness trade-off was examined
in federated learning (Chen et al., 2023). The interplay among fairness,
interpretability, and privacy was surveyed as a triangle (Ferry et al., 2023),
conflicts among protection mechanisms such as watermarking, adversarial training,
and differential privacy were catalogued (Szyller and Asokan, 2023), and
explanations were studied as both a defense and an attack surface in adversarial
settings (Noppel and Wressnegger, 2024). These efforts remained tied to specific
risks, defenses, or interactions, and stopped short of isolating the shared
underlying causes that would let an interaction be anticipated rather than
observed (Gittens et al., 2022).

## Reading guidance

- Section 2: the catalog of risks (labeled R, P, F) and defenses (RD, PD, FD),
  plus the notation. The symbols are dense; Table 9 in Appendix A is the key, and
  skimming it first makes Sections 4 and 5 readable.
- Section 3 and Table 1: the framework itself, overfitting and memorization as the
  two conjectured causes, and the factors of the data, algorithm, and model that
  influence them. Figure 1 illustrates the four combinations of overfitting and
  memorization on a synthetic dataset.
- Section 4 and Tables 2 and 3: the core. Table 2 expresses each defense and each
  risk in terms of the shared factors; Table 3 surveys which interactions prior
  work has actually examined. Note that Table 3 marks each interaction as
  empirical, theoretical, or only conjectured, and how many cells are left
  unexplored.
- Section 4.4: the guideline (G1 to G4) for conjecturing an interaction's
  direction from the factors a defense and a risk share. The guideline leans on
  picking a "dominant" factor using expert knowledge; note where that judgment
  enters and what rests on it.
- Section 5: the two unexplored interactions conjectured and then validated
  empirically, with the threat model stated for each. These are demonstrations of
  the framework on one tabular dataset, not a broad evaluation.
- Sections 6 and 7: related work, then completeness and limitations. The authors
  state that the framework captures correlation rather than causation and do not
  claim the two causes are exhaustive; note how they frame what would extend or
  break the framework.

## Motivating questions

1. The paper conjectures two underlying causes for these cross-effects. What are
   they, and what is the argument that two such phenomena sit beneath risks as
   different as evasion, membership inference, and discriminatory behavior?
2. What does it mean for a defense and a risk to "interact" in this framework, and
   how does sharing a factor let the framework conjecture whether a defense raises
   or lowers a given risk?
3. What does the framework offer a practitioner who must deploy several defenses
   on one model at the same time?
4. Across the map of interactions, how much rests on measurement, how much on
   theory, and how much on conjecture, and why might that distribution matter?
5. The framework describes correlations among factors. What would it take to move
   from these correlations to a causal account of an interaction?

## Supplementary readings

- [Conflicting Interactions Among Protection Mechanisms for Machine Learning Models](https://arxiv.org/abs/2207.01991) — an earlier, narrower study by two of the same authors on how protection mechanisms conflict when combined; a direct precursor to this framework.
- [Combining Machine Learning Defenses without Conflicts](https://arxiv.org/abs/2411.09776) — follow-up work on composing multiple defenses while avoiding the conflicts this SoK maps.

## References

- Bagdasaryan, E., et al. "Differential Privacy Has Disparate Impact on Model
  Accuracy." Advances in Neural Information Processing Systems (NeurIPS), 2019.
- Chen, H., Zhu, T., Zhang, T., Zhou, W., and Yu, P. S. "Privacy and Fairness in
  Federated Learning: On the Perspective of Tradeoff." ACM Computing Surveys,
  56(2), 2023.
- Ferry, J., Aïvodji, U., Gambs, S., Huguet, M.-J., and Siala, M. "SoK: Taming
  the Triangle – On the Interplays between Fairness, Interpretability and Privacy
  in Machine Learning." arXiv:2312.16191, 2023.
- Gittens, A., et al. "An Adversarial Perspective on Accuracy, Robustness,
  Fairness, and Privacy: Multilateral-Tradeoffs in Trustworthy ML." IEEE Access,
  10:120850–120865, 2022.
- Hayes, J. "Trade-offs between Membership Privacy & Adversarially Robust
  Learning." arXiv:2006.04622, 2020.
- Mehrabi, N., et al. "A Survey on Bias and Fairness in Machine Learning." ACM
  Computing Surveys, 54(6), 2021.
- Noppel, M. and Wressnegger, C. "SoK: Explainable Machine Learning in Adversarial
  Environments." IEEE Symposium on Security and Privacy (S&P), 2024.
- Papernot, N., et al. "SoK: Security and Privacy in Machine Learning." IEEE
  European Symposium on Security and Privacy (EuroS&P), 2018.
- Song, L., et al. "Privacy Risks of Securing Machine Learning Models against
  Adversarial Examples." ACM Conference on Computer and Communications Security
  (CCS), 2019.
- Szyller, S. and Asokan, N. "Conflicting Interactions Among Protection Mechanisms
  for Machine Learning Models." AAAI Conference on Artificial Intelligence, 2023.
- Yeom, S., et al. "Privacy Risk in Machine Learning: Analyzing the Connection to
  Overfitting." IEEE Computer Security Foundations Symposium (CSF), 2018.
