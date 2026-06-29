---
title: "Towards Deep Learning Models Resistant to Adversarial Attacks"
authors:
  - Madry, Aleksander
  - Makelov, Aleksandar
  - Schmidt, Ludwig
  - Tsipras, Dimitris
  - Vladu, Adrian
year: 2018
section: "Adversarial Robustness of Classification Models"
primary: true
arxiv: "1706.06083"
tags:
  - adversarial-robustness
  - adversarial-training
  - robust-optimization
  - evasion
---

### [Wiki Home](../README.md)

# Towards Deep Learning Models Resistant to Adversarial Attacks

## High-level overview

Deep image classifiers can be fooled by
[adversarial examples](../concepts/adversarial-examples.md): inputs perturbed by
amounts too small for a human to notice but large enough to flip the model's
prediction. This paper reframes attacks and defenses as the two halves of one
min-max (saddle-point) problem from
[robust optimization](../concepts/robust-optimization.md). An inner maximization
finds the worst-case perturbation of an input within an allowed set, which is
what an attack is. An outer minimization trains the network against that worst
case, which is what [adversarial training](../concepts/adversarial-training.md)
is. Terminology note: in this literature an "adversary" is usually an algorithm,
not a person, and a "first-order adversary" is an attacker that uses only
gradients of the loss with respect to the input.

The paper reports that the inner maximization, though non-concave, is empirically
tractable, and that projected gradient descent (PGD) with random restarts behaves
as the strongest first-order attack. It reports that robust classification needs
noticeably larger networks than clean classification. Training against the PGD
adversary yields models that withstand the strongest attacks the authors
evaluate, above 89% robust accuracy on MNIST and around 46% on CIFAR-10, and the
trained models were released as public attack challenges. The method is now
called PGD adversarial training or Madry-style adversarial training, it remains
the reference baseline for empirical defenses, and "PGD" without qualification
usually means this paper's attack.

**Threat Model:** An evasion (test-time) setting. The adversary perturbs
individual inputs at classification time; the training data and the model are
untouched. Each perturbation must stay inside the
[ℓ-infinity ball](../concepts/lp-norms.md) of radius epsilon around the
original input, so no pixel may change by more than epsilon (0.3 on MNIST in
[0,1] scale, 8 on CIFAR-10 in [0,255] scale). The headline setting is
[white-box](../concepts/white-box-black-box.md): the adversary knows the
architecture and the weights and can compute gradients. Weaker black-box
(transfer) adversaries are evaluated as well. The defender's claim is accuracy
under the worst allowed perturbation, argued for the class of first-order
adversaries.

## Why read this

Most early defenses against adversarial examples were point countermeasures,
and many were broken shortly after publication. This paper instead fixes an
explicit class of adversaries and trains models to resist all of them, which
makes it one of the first works to establish adversarial training and
robustness on firm footing rather than as a heuristic. It is also a
well-constructed paper, worth reading as a model for arguing an empirical
security claim.

## Basic Background

### Training a classifier

A neural network classifier maps an input in R^d to one of k labels and is
trained by
[empirical risk minimization](../concepts/empirical-risk-minimization.md):
minimizing the average of a loss function (here cross-entropy) over the
training set, as a proxy for the expected loss over the data distribution. The
minimization runs by
[stochastic gradient descent](../concepts/stochastic-gradient-descent.md),
which estimates the gradient of the loss with respect to the parameters on a
small batch and steps against it. The same backpropagation machinery also
yields the gradient of the loss with respect to the *input*, and that input
gradient is what gradient-based attacks use.

### Measuring small perturbations

Perturbation size is measured with [ℓp norms](../concepts/lp-norms.md). The
ℓ-infinity norm of a perturbation is its largest per-coordinate change, so the
ℓ-infinity ball of radius epsilon contains every image whose pixels each differ
by at most epsilon from the original. The ball is a stand-in for perceptual
similarity, which has no closed form.

### The adversarial setting

An [adversarial example](../concepts/adversarial-examples.md) is a correctly
classified input perturbed, within the allowed ball, so that the model
misclassifies it (Szegedy et al., 2014; Goodfellow et al., 2015). A
[threat model](../concepts/adversarial-threat-model.md) makes "robust"
falsifiable by fixing the perturbation set and the adversary's knowledge:
[white-box adversaries see weights and gradients, black-box adversaries only
query or transfer](../concepts/white-box-black-box.md).
[Transferability](../concepts/transferability.md), the fact that adversarial
examples crafted on one model often fool another, is what makes black-box
attacks practical.

### Attack and defense primitives

The [Fast Gradient Sign Method](../concepts/fgsm.md) builds an ℓ-infinity
adversarial example in one gradient step (Goodfellow et al., 2015). Taking
several smaller steps and projecting back into the ball after each one is
[projected gradient descent](../concepts/projected-gradient-descent.md), the
standard method for constrained optimization, and it finds higher-loss points
than a single step (Kurakin et al., 2017). On the defense side,
[adversarial training](../concepts/adversarial-training.md) trains on attacked
inputs instead of clean ones (Goodfellow et al., 2015). A defense evaluated
only against weak attacks can fail by
[gradient masking](../concepts/gradient-masking.md): the gradients become
useless to the attacker without the worst-case loss actually being small.

### Worst-case optimization

[Robust optimization](../concepts/robust-optimization.md) minimizes the
worst-case loss over an uncertainty set, written as a min-max problem, and
predates deep learning by decades (Wald, 1945; Ben-Tal et al., 2009). Danskin's
theorem connects the two halves: the gradient of the loss evaluated at an inner
maximizer is a descent direction for the outer problem. Its assumptions, a
smooth function and an exact inner maximum, do not hold for ReLU networks
attacked approximately, so applying it there needs empirical justification.

<details>
<summary><h2>Paper Context</h2></summary>

Adversarial machine learning predates deep learning. Evasion of deployed
classifiers such as spam filters was formalized in the 2000s (Dalvi et al.,
2004; Globerson and Roweis, 2006), and gradient-based evasion of shallow models
was demonstrated before deep networks took over computer vision (Biggio et al.,
2013). For deep networks, imperceptible perturbations were shown to fool
state-of-the-art image classifiers and to transfer between models (Szegedy et
al., 2014); an explanation based on local linearity, the FGSM attack, and the
first adversarial training followed (Goodfellow et al., 2015).

By early 2017 the defense side was a fast-growing collection of one-off
countermeasures with a poor track record. Defensive distillation (Papernot et
al., 2016) was broken within a year by stronger optimization-based attacks
(Carlini and Wagner, 2017a). Ten published detection methods were bypassed in a
single study (Carlini and Wagner, 2017b), and ensembles of weak defenses were
shown to be no stronger than their parts (He et al., 2017). Models adversarially
trained against FGSM resisted FGSM but fell to iterative attacks, including at
ImageNet scale (Kurakin et al., 2017). There was no agreed standard for what a
robustness claim meant: a defense counted as robust if it survived the attacks
its authors chose to run.

Min-max formulations of adversarial training existed (Huang et al., 2015;
Shaham et al., 2018), but their inner maximization was either declared
intractable or replaced by a one-step linearization, and the resulting models
were evaluated only against weak adversaries. Robust optimization itself was a
mature field in operations research (Wald, 1945; Ben-Tal et al., 2009). Open at
the time: whether the non-concave inner problem of a deep network could be
solved well enough for the min-max guarantee to mean anything, and what an
evaluation would have to show before the security community, with its norms of
explicit threat models and adaptive adversaries, would accept an ML
benchmark-style robustness number.

</details>

## Reading guidance

- Sections 1 and 2: the saddle-point formulation (Equation 2.1) and how prior
  attacks and defenses map onto its inner and outer problems. The definition of
  the perturbation set S takes one paragraph; note what justifies the choice of
  the ℓ-infinity ball.
- Sections 3.1 and 3.2: the experimental study of the inner maximization, with
  Figures 1 and 2 as the supporting evidence, and the argument for treating PGD
  as the strongest first-order adversary.
- Section 4: the model-capacity experiments (Figure 4), separable from the rest
  of the argument.
- Section 5 with Tables 1 and 2: the robustness evaluation. Each row is a
  different attack and source network; the threat model behind each number is
  in the caption.
- Appendix A: the statement of Danskin's theorem; note which of its assumptions
  hold for a ReLU network attacked by an approximate maximizer.

### [Wiki Home](../README.md)

<details>
<summary><h2>References</h2></summary>

All entries read off the paper's bibliography (arXiv 1706.06083v4, pages
16-18).

- Ben-Tal, A., El Ghaoui, L., and Nemirovski, A. *Robust Optimization*.
  Princeton University Press, 2009.
- Biggio, B., Corona, I., Maiorca, D., Nelson, B., Šrndić, N., Laskov, P.,
  Giacinto, G., and Roli, F. "Evasion Attacks against Machine Learning at Test
  Time." ECML-PKDD, 2013.
- Carlini, N. and Wagner, D. "Towards Evaluating the Robustness of Neural
  Networks." IEEE Symposium on Security and Privacy, 2017. (2017a)
- Carlini, N. and Wagner, D. "Adversarial Examples Are Not Easily Detected:
  Bypassing Ten Detection Methods." ACM Workshop on Artificial Intelligence and
  Security (AISec), 2017. (2017b)
- Dalvi, N., Domingos, P., Sanghai, S., and Verma, D. "Adversarial
  Classification." ACM SIGKDD International Conference on Knowledge Discovery
  and Data Mining, 2004.
- Globerson, A. and Roweis, S. "Nightmare at Test Time: Robust Learning by
  Feature Deletion." International Conference on Machine Learning (ICML), 2006.
- Goodfellow, I. J., Shlens, J., and Szegedy, C. "Explaining and Harnessing
  Adversarial Examples." International Conference on Learning Representations
  (ICLR), 2015.
- He, W., Wei, J., Chen, X., Carlini, N., and Song, D. "Adversarial Example
  Defense: Ensembles of Weak Defenses Are Not Strong." USENIX Workshop on
  Offensive Technologies (WOOT), 2017.
- Huang, R., Xu, B., Schuurmans, D., and Szepesvári, C. "Learning with a Strong
  Adversary." arXiv:1511.03034, 2015.
- Kurakin, A., Goodfellow, I. J., and Bengio, S. "Adversarial Machine Learning
  at Scale." International Conference on Learning Representations (ICLR), 2017.
- Papernot, N., McDaniel, P. D., Wu, X., Jha, S., and Swami, A. "Distillation
  as a Defense to Adversarial Perturbations against Deep Neural Networks." IEEE
  Symposium on Security and Privacy, 2016.
- Shaham, U., Yamada, Y., and Negahban, S. "Understanding Adversarial Training:
  Increasing Local Stability of Supervised Models through Robust Optimization."
  Neurocomputing 307, 2018.
- Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow,
  I., and Fergus, R. "Intriguing Properties of Neural Networks." International
  Conference on Learning Representations (ICLR), 2014.
- Wald, A. "Statistical Decision Functions Which Minimize the Maximum Risk."
  Annals of Mathematics, 1945.

</details>
