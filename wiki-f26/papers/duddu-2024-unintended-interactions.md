---
title: "SoK: Unintended Interactions among Machine Learning Defenses and Risks"
authors:
  - Duddu, Vasisht
  - Szyller, Sebastian
  - Asokan, N.
year: 2024
section: "Unintended Interactions among ML Defenses and Risks"
primary: true
arxiv: "2312.04542"
tags:
  - machine-learning
  - privacy
  - fairness
  - memorization
  - survey
---

[Home page](../README.md)

# SoK: Unintended Interactions among Machine Learning Defenses and Risks

## High-level overview

A machine learning model faces several risks at once. An adversary may evade it
at test time, poison its training data, steal its functionality, infer whether a
record was in its training set, or expose discriminatory behaviour across groups.
Each risk has its own defenses. Deploying a defense against one risk routinely
changes the model's susceptibility to a different, unrelated risk, sometimes
lowering it and sometimes raising it. Adding [adversarial training](../concepts/adversarial-training.md)
to resist evasion, for instance, makes [membership inference](../concepts/membership-inference.md)
easier (Song et al., 2019; Hayes, 2020). This systematization of knowledge (SoK)
collects these unintended interactions and explains them within one framework.

The framework rests on a single conjecture: two properties of how a model fits
its training data, [overfitting](../concepts/empirical-risk-minimization.md) and
[memorization](../concepts/memorization.md), are the common causes underlying the
interactions. A defense takes effect by inducing or suppressing overfitting or
memorization, and that same change moves the model's exposure to other risks. The
paper identifies a small set of underlying factors, drawn from the characteristics
of the training data, the training algorithm, and the model, that govern
overfitting and memorization, and uses them as a shared vocabulary for reasoning
about any defense and any risk together. It surveys the published interactions and
situates each within this framework, then distills a guideline for conjecturing
the direction of an interaction that has not yet been studied.

Across the literature the framework accommodates the reported interactions,
spanning seven defenses and eight risks drawn from security, privacy, and
fairness. Using the guideline, the paper conjectures two previously unstudied
interactions and validates them empirically: enforcing
[group fairness](../concepts/group-fairness.md) lowers the success of data
reconstruction, and releasing [model explanations](../concepts/model-explanations.md)
raises the success of distribution (property) inference.

**Threat Model:** A SoK has no single threat model; its scope is a population of
settings. The defenses are deployed by a model owner: adversarial training,
outlier removal, [differential privacy](../concepts/differential-privacy.md),
group fairness, [model watermarking](../concepts/model-watermarking.md),
fingerprinting, and the release of explanations. The risks are pursued by an
adversary or arise as a property of the model: evasion, poisoning, unauthorized
model ownership through [model extraction](../concepts/model-extraction.md),
membership inference, data reconstruction, attribute inference, distribution
inference, and discriminatory behaviour. The settings range over
[white-box and black-box](../concepts/white-box-black-box.md) access, train-time
and inference-time action, and take classifiers as the primary object with
generative models discussed as an extension. The framework's claim is explanatory
and predictive rather than adversarial: overfitting, memorization, and the factors
that drive them are the common causes that determine whether deploying a given
defense increases or decreases susceptibility to a given risk, and the guideline
uses them to conjecture the direction of an unstudied interaction. The framework
asserts correlation, not causation, and its conjectures are checked empirically.

## Why read this

<!-- instructor: confirm -->

Most of trustworthy machine learning is built one defense and one risk at a time,
and this paper is the first to ask, systematically, what a defense does to the
risks it was never designed for. It reduces a sprawling and often contradictory
literature to two underlying causes, overfitting and memorization, and a handful
of factors, turning scattered empirical observations into a single account that
also predicts interactions no one has measured. It is a model of what a
systematization can do: organize a field, expose its gaps, and yield testable
conjectures. It received a Distinguished Paper award at IEEE S&P 2024.

## Basic Background

### Risks and defenses in trustworthy machine learning

Trustworthy machine learning studies a model's exposure across security, privacy,
and fairness. Security risks include
[evasion](../concepts/adversarial-examples.md), where crafted perturbations force
a misclassification (Goodfellow et al., 2015);
[data poisoning](../concepts/data-poisoning.md) and
[backdoors](../concepts/backdoor-attacks.md), which corrupt training data to
control predictions; and unauthorized model ownership through
[model extraction](../concepts/model-extraction.md), which rebuilds a deployed
model's functionality from query access
([Knockoff Nets](orekondy-2019-knockoff-nets.md); Orekondy et al., 2019). Privacy
risks include [membership inference](../concepts/membership-inference.md), which
tests whether a record was in the training set
([likelihood-ratio formulation](carlini-2022-lira.md); Shokri et al., 2017;
Carlini et al., 2022), along with data reconstruction (model inversion), attribute
inference, and distribution (property) inference; for generative models the
privacy failure is verbatim reproduction of
[training data](carlini-2021-extracting-training-data.md) (Carlini et al., 2021).
Fairness concerns a model's discriminatory behaviour across sensitive subgroups.
The corresponding defenses include
[adversarial training](../concepts/adversarial-training.md)
([PGD](madry-2018-pgd.md); Madry et al., 2018), outlier removal,
[differential privacy](../concepts/differential-privacy.md) via DP-SGD
([DP-SGD](abadi-2016-dp-sgd.md); Abadi et al., 2016),
[model watermarking](../concepts/model-watermarking.md) and fingerprinting for
ownership ([DAWN](szyller-2019-dawn.md); Szyller et al., 2019),
[group fairness](../concepts/group-fairness.md) constraints, and
[model explanations](../concepts/model-explanations.md).

### Overfitting and memorization

A model [overfits](../concepts/empirical-risk-minimization.md) when it fits its
training set more closely than the underlying distribution; the gap between
training and test loss, the generalization error, measures it.
[Memorization](../concepts/memorization.md) is the per-example version: a model
can fit individual records, especially outliers and the long tail of the data
distribution, and some such memorization is necessary for accuracy (Feldman, 2020;
Zhang et al., 2017). Both leave traces in what an adversary can observe, namely the
model's predictions, its intermediate activations, its gradients, and its
parameters. Most of the risks above feed on those traces.

### Group fairness and explanations

[Group fairness](../concepts/group-fairness.md) constrains a model to behave
equitably across groups defined by a sensitive attribute, under statistical
metrics such as demographic parity or equalized odds (Hardt et al., 2016),
enforced by pre-processing the data, constraining the objective, or
post-processing the outputs. [Model explanations](../concepts/model-explanations.md)
release auxiliary information with each prediction: a feature attribution, the
influential training records behind a prediction, or a counterfactual that would
change the outcome. Neither defense requires retraining, and both expose
information about the model's decision boundary and training data.

<details>
<summary><h2>Paper Context</h2></summary>

Individual interactions were documented before any unifying account. Adversarial
training, applied to resist evasion, raises a model's vulnerability to membership
inference (Song et al., 2019; Hayes, 2020). Differential privacy has a disparate
impact on accuracy across subgroups (Bagdasaryan et al., 2019), and fairness
constraints interact with privacy risks (Chang and Shokri, 2021). Each result studied one
defense against one risk, with no shared explanation of why the interaction arose.

Several systematizations had mapped the risk and defense landscape without
treating the interactions among them. SoKs organized security and privacy in
machine learning broadly (Papernot et al., 2018) and inference attacks on training
data specifically (Salem et al., 2023). Surveys of multilateral tradeoffs in
trustworthy machine learning catalogued tensions between accuracy, robustness,
fairness, and privacy without naming their underlying causes (Gittens et al.,
2022). The direct precursor to this paper enumerated conflicts among protection
mechanisms, showing that combining defenses can make each less effective (Szyller
and Asokan, 2023). A contemporaneous SoK examined the interplay of fairness,
interpretability, and privacy (Ferry et al., 2023).

</details>

## Reading guidance

- Section 2: the catalogue of risks (evasion, poisoning, unauthorized model
  ownership, the four privacy inference risks, discriminatory behaviour) and
  defenses (adversarial training, outlier removal, watermarking, fingerprinting,
  differential privacy, group fairness, explanations), plus the notation used
  throughout. A reference list to skim and return to.
- Section 3: the framework. The conjecture that overfitting (3.1) and
  memorization (3.2) are the underlying causes, the factors that influence each,
  and the relationship between the two (3.3). The justification for selecting
  these two properties as the causes is stated briefly; note what it rests on.
- Section 4, Tables 2 and 3: the survey, relating each defense and risk to the
  factors and situating known interactions in the framework. Table 3 marks
  whether each interaction is empirically shown, theoretically shown, or only
  conjectured, and flags exceptions; note which cells are evidence and which are
  conjecture.
- Section 4.4: the guideline (G1 to G4) for inferring the direction of an
  interaction from a shared factor, and how a dominant factor is chosen when
  factors disagree.
- Section 5: the two interactions conjectured from the guideline and then
  validated, with a separate threat model stated for each experiment. Section 5.3
  reasons about interactions the paper does not evaluate.
- Section 6: related surveys, and the orthogonal line of work on tradeoffs within
  a single defense.
- Section 7: the discussion of completeness, the correlation-not-causation caveat,
  and how the framework would extend to new causes, defenses, and generative
  models.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [Conflicting Interactions Among Protection Mechanisms for Machine Learning Models](https://arxiv.org/abs/2207.01991) — the precursor from two of the same authors; it documents that combining defenses can make each less effective, the observation this SoK generalizes into a framework.
- [Combining Machine Learning Defenses without Conflicts](https://arxiv.org/abs/2411.09776) — a later follow-up that builds on this systematization to compose multiple defenses while avoiding the conflicts it catalogues.

</details>

[Home page](../README.md)

<details>
<summary><h2>References</h2></summary>

- Abadi, M., Chu, A., Goodfellow, I., McMahan, H. B., Mironov, I., Talwar, K.,
  and Zhang, L. "Deep Learning with Differential Privacy." ACM Conference on
  Computer and Communications Security (CCS), 2016.
- Bagdasaryan, E., et al. "Differential Privacy Has Disparate Impact on Model
  Accuracy." Advances in Neural Information Processing Systems (NeurIPS), 2019.
- Carlini, N., Tramèr, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K.,
  Roberts, A., Brown, T., Song, D., Erlingsson, Ú., et al. "Extracting Training
  Data from Large Language Models." USENIX Security Symposium, 2021.
- Carlini, N., Chien, S., Nasr, M., Song, S., Terzis, A., and Tramèr, F.
  "Membership Inference Attacks From First Principles." IEEE Symposium on Security
  and Privacy (S&P), 2022.
- Chang, H. and Shokri, R. "On the Privacy Risks of Algorithmic Fairness." IEEE
  European Symposium on Security and Privacy (EuroS&P), 2021.
- Feldman, V. "Does Learning Require Memorization? A Short Tale about a Long
  Tail." ACM Symposium on Theory of Computing (STOC), 2020.
- Ferry, J., Aïvodji, U., Gambs, S., Huguet, M.-J., and Siala, M. "SoK: Taming
  the Triangle, On the Interplays between Fairness, Interpretability and Privacy
  in Machine Learning." arXiv:2312.16191, 2023.
- Gittens, A., et al. "An Adversarial Perspective on Accuracy, Robustness,
  Fairness, and Privacy: Multilateral-Tradeoffs in Trustworthy ML." IEEE Access,
  10, 2022.
- Goodfellow, I. J., Shlens, J., and Szegedy, C. "Explaining and Harnessing
  Adversarial Examples." International Conference on Learning Representations
  (ICLR), 2015.
- Hardt, M., et al. "Equality of Opportunity in Supervised Learning." Advances in
  Neural Information Processing Systems (NeurIPS), 2016.
- Hayes, J. "Trade-offs between Membership Privacy & Adversarially Robust
  Learning." arXiv:2006.04622, 2020.
- Madry, A., Makelov, A., Schmidt, L., Tsipras, D., and Vladu, A. "Towards Deep
  Learning Models Resistant to Adversarial Attacks." International Conference on
  Learning Representations (ICLR), 2018. arXiv:1706.06083.
- Orekondy, T., et al. "Knockoff Nets: Stealing Functionality of Black-Box
  Models." IEEE Conference on Computer Vision and Pattern Recognition (CVPR),
  2019.
- Papernot, N., et al. "SoK: Security and Privacy in Machine Learning." IEEE
  European Symposium on Security and Privacy (EuroS&P), 2018.
- Salem, A., et al. "SoK: Let the Privacy Games Begin! A Unified Treatment of Data
  Inference Privacy in Machine Learning." IEEE Symposium on Security and Privacy
  (S&P), 2023.
- Shokri, R., Stronati, M., Song, C., and Shmatikov, V. "Membership Inference
  Attacks Against Machine Learning Models." IEEE Symposium on Security and Privacy
  (S&P), 2017.
- Song, L., et al. "Privacy Risks of Securing Machine Learning Models against
  Adversarial Examples." ACM Conference on Computer and Communications Security
  (CCS), 2019.
- Szyller, S. and Asokan, N. "Conflicting Interactions among Protection Mechanisms
  for Machine Learning Models." AAAI Conference on Artificial Intelligence, 2023.
- Szyller, S., Atli, B. G., Marchal, S., and Asokan, N. "DAWN: Dynamic Adversarial
  Watermarking of Neural Networks." arXiv:1906.00830, 2019.
- Zhang, C., Bengio, S., Hardt, M., Recht, B., and Vinyals, O. "Understanding Deep
  Learning Requires Rethinking Generalization." International Conference on
  Learning Representations (ICLR), 2017.

</details>
