---
title: "Membership Inference Attacks From First Principles"
authors:
  - Carlini, Nicholas
  - Chien, Steve
  - Nasr, Milad
  - Song, Shuang
  - Terzis, Andreas
  - Tramèr, Florian
year: 2022
section: "Membership Inference"
primary: true
arxiv: "2112.03570"
doi: "10.1109/SP46214.2022.9833649"
tags:
  - membership-inference
  - privacy
  - evaluation
  - attack
---

# Membership Inference Attacks From First Principles

## High-level overview

A [membership inference attack](../concepts/membership-inference.md) queries a
trained model to predict whether a specific example was in its training set. It
is the simplest attack on training-data privacy and the de facto tool for
auditing whether a model leaks its data. This paper makes two coupled
contributions, one methodological and one technical. The methodological
contribution is an argument about measurement: membership inference attacks had
been evaluated by average-case metrics such as balanced accuracy and
[AUC](../concepts/roc-curves.md), but privacy is a worst-case property, so an
attack should be judged by its true-positive rate at very low false-positive
rates (whether it can identify even a few members with near-zero false
accusations), read off a log-scale ROC curve. Re-evaluated this way, most prior
attacks fail outright, and their accuracy rankings do not predict their low-FPR
rankings.

The technical contribution is the Likelihood Ratio Attack (LiRA). "First
principles" here means deriving the attack from optimal hypothesis testing
rather than from heuristics: membership inference is recast as a
[likelihood-ratio test](../concepts/likelihood-ratio-test.md) between two
worlds, models trained with the target example and models trained without it.
The two per-example loss distributions are estimated by training
[shadow models](../concepts/shadow-models.md) and fitting Gaussians to
logit-scaled model confidences. At a false-positive rate of 0.1%, LiRA is
roughly ten times more powerful than prior attacks, while also dominating them
on the old average-case metrics, and it remains effective against
well-generalizing models that earlier attacks could barely touch. The paper
ships an online variant (shadow models trained per query) and a cheaper offline
variant, with code released, and closes by arguing that a body of prior
conclusions about memorization, defenses, and "private" training algorithms
needs re-examination under the new metric.

**Threat Model:** A training-data privacy setting: the adversary does not
modify any input, and the training process is untouched. The
adversary holds a candidate example with its label and wants to learn one bit,
whether that example was in the target model's training set. Access is
[black-box](../concepts/white-box-black-box.md): the adversary queries the
trained model and observes its confidence outputs, with no access to weights or
gradients. The adversary can sample from the underlying data distribution and
train its own shadow models, and in the strongest setting knows the target's
architecture and training setup; the paper measures how the attack degrades
when the shadow data is disjoint or the architecture, optimizer, and
augmentations are guessed wrong. The privacy claim under attack is membership
secrecy, and the attack is judged by its true-positive rate at low
false-positive rates.

## Why this paper is assigned

Privacy, like security, is a worst-case property: an attack that confidently
identifies a few members has succeeded even if its average accuracy is
unremarkable. This paper resets how membership inference is evaluated and, in
the process, shows that years of accumulated results were measured with the
wrong instrument. It pairs with the Madry paper as the course's second case
study in what a security claim actually means.

## Background — Tier 1 (warm-up)

### Training, confidence, and the generalization gap

A classifier is trained by
[empirical risk minimization](../concepts/empirical-risk-minimization.md):
[stochastic gradient descent](../concepts/stochastic-gradient-descent.md)
drives down the cross-entropy loss on the training set. The softmax layer turns
the network's raw outputs (logits) into per-class confidences, and the loss on
an example is the negative log of the confidence assigned to its true label.
Training therefore makes training examples low-loss by construction, and the
gap between training and test accuracy (the generalization gap) measures how
much lower. That asymmetry between seen and unseen data is the signal every
membership inference attack feeds on.

### Memorization

[Memorization](../concepts/memorization.md) is the stronger, per-example form
of that asymmetry. Deep networks can fit even randomly labeled data (Zhang et
al., 2021), and some memorization of rare or atypical examples may be necessary
for good generalization (Feldman, 2020). Examples differ widely: an outlier's
presence in the training set can change the model's behavior on it far more
than an inlier's presence does. Per-example differences of this kind are why a
single global decision rule treats examples unequally.

### Membership inference

[Membership inference](../concepts/membership-inference.md) is formalized as a
security game: a challenger trains a model on a sampled dataset, flips a coin
to hand the adversary either a training-set member or a fresh point, and the
adversary must guess which (Yeom et al., 2018). The attack class began as
tracing attacks on genomic data, where identifying one individual in a medical
dataset is itself the privacy violation (Homer et al., 2008), and was brought
to machine learning models with query access (Shokri et al., 2017). The
baseline attack thresholds the model's loss on the candidate example (Yeom et
al., 2018). Membership inference also serves as the foundation of stronger
attacks, such as training-data extraction, which need its predictions to be
precise (Carlini et al., 2021).

### Shadow models

A [shadow model](../concepts/shadow-models.md) is a model the adversary trains
itself, on data sampled from the same distribution as the target's training
set, to imitate the target's behavior (Shokri et al., 2017). Anything the
adversary can measure on its shadow models, such as how a model's loss on an
example behaves when the example is or is not in the training set, becomes a
calibration resource for attacking the real target.

### Hypothesis testing

A [likelihood-ratio test](../concepts/likelihood-ratio-test.md) decides between
two hypotheses by comparing how probable the observation is under each. The
Neyman-Pearson lemma states that thresholding this ratio is the most powerful
test at any fixed false-positive rate (Neyman and Pearson, 1933). The lemma
presupposes that both distributions are known, so applying it in practice means
estimating them, exactly or parametrically.

### Evaluating binary detectors

A detector that outputs a score and thresholds it trades off true positives
against false positives as the threshold moves; the
[ROC curve](../concepts/roc-curves.md) traces that trade-off, and AUC and
balanced accuracy compress it into one number. Detection systems in security,
such as spam and malware classifiers, conventionally operate at very low
false-positive rates, because one false alarm among thousands of benign events
destroys a detector's usefulness. The same machinery evaluates a membership
inference attack, with the attacker as the detector.

### Defenses

[Differential privacy](../concepts/differential-privacy.md) bounds the
influence any single training example can have on the trained model, and
thereby provably caps the success of any membership inference attack (Dwork
and Roth, 2014). Its standard implementation for deep learning is
[DP-SGD](abadi-2016-dp-sgd.md), which clips per-example gradients and adds
noise (Abadi et al., 2016). The
strength of the guarantee is set by the privacy parameter epsilon, and
membership inference attacks double as empirical audits of how tight such
guarantees are in practice (Jagielski et al., 2020; Nasr et al., 2021).

## Background — Tier 2 (field context)

Membership inference predates machine learning. It was first demonstrated on
genomic data, where an individual's presence in a study cohort could be
detected from published aggregate statistics (Homer et al., 2008), then
sharpened into likelihood-ratio form (Sankararaman et al., 2009) and given a
general theory of traceability from noisy statistics (Dwork et al., 2015). The
statistics community thus already treated tracing as a hypothesis-testing
problem with formally optimal tests. The attack arrived in machine learning
with shadow models and query access to a trained model (Shokri et al., 2017),
and was connected to overfitting through the simple loss-threshold baseline
(Yeom et al., 2018).

By late 2021 the attack literature was large. Attack variants refined features,
per-class calibration, and entropy measures (Salem et al., 2018; Song and
Mittal, 2021; Jayaraman et al., 2021), and a per-example line of work
calibrated each example's score against its own difficulty (Sablayrolles et
al., 2019; Long et al., 2020), continued concurrently with this paper (Watson
et al., 2021; Ye et al., 2021). Nearly all of it was evaluated by balanced
accuracy or AUC. At the same time, membership inference had become standard
auditing practice: production privacy audits were built on attack libraries
such as TensorFlow Privacy's membership inference tests (Song and Marn, 2020)
and ML Privacy Meter (Murakonda and Shokri, 2020), so an audit's conclusions
were only as strong as the attacks it ran.

Memorization results showed deep
networks can fit random labels (Zhang et al., 2021) and that fitting the long
tail of a data distribution may be necessary for accuracy (Feldman, 2020;
Feldman and Zhang, 2020), implying real models carry per-example information
an attacker might recover. Differential privacy offered the principled
counterweight (Dwork and Roth, 2014), with
[DP-SGD](abadi-2016-dp-sgd.md) as its deep-learning instantiation (Abadi et
al., 2016) and attacks repurposed as empirical lower bounds on its guarantees
(Jagielski et al., 2020; Nasr et al., 2021). Meanwhile, unease about average-case reasoning was
already articulated within the privacy community (Steinke and Ullman, 2020),
and the older security literature on spam, malware, and intrusion detection
had long operated at low false-positive rates as a matter of course. The
accumulated membership inference results, nearly all evaluated by
average-case metrics on small overfit models, had not been re-examined under
either standard.

## Reading guidance

- Section II: background on training-data privacy; skim if the Tier-1 material
  is familiar.
- Section III-A, Definition 1: the membership inference security game.
  Definition 1 grants the adversary sampling access to the underlying data
  distribution; note where the attack later relies on it.
- Section III-B: the case against balanced accuracy and AUC. The hypothetical
  Attack A versus Attack B comparison carries the argument.
- Section IV: the derivation of LiRA. Figures 3 and 4 show the per-example
  loss distributions and the effect of logit scaling; Algorithm 1 is the whole
  attack in one box; the online/offline distinction matters for cost.
- Section V and Table I: re-evaluation of eight prior attacks. Note which
  attacks change rank between balanced accuracy and TPR at low FPR.
- Section VI and Table II: the ablation; which components produce the gains,
  and Figure 9 for how many shadow models are enough.
- Figure 7: train-test gap versus attack success across training
  configurations.
- Appendix A: [DP-SGD](abadi-2016-dp-sgd.md) against the attack; note the
  epsilon values at which the attack is and is not stopped.
- Section VIII: the authors' list of prior conclusions they argue need
  re-examination.

## Motivating questions

1. What should it mean for a membership inference attack to "succeed," and how
   does the paper argue success should be measured?
2. Can an attack with high average accuracy be useless to a practical
   adversary, and can a low-accuracy attack be dangerous?
3. What does the strongest attack need to know about the target model, its
   training data, and its training procedure, and how gracefully does it
   degrade when each assumption fails?
4. Is overfitting required for membership inference, or are well-generalizing
   models also vulnerable?
5. What do these results change about how the privacy of a trained model
   should be audited?

## References

Entries read off the paper's bibliography (arXiv 2112.03570v2, pages 14-16);
venue for Shokri et al. confirmed via DBLP.

- Abadi, M., Chu, A., Goodfellow, I., McMahan, H. B., Mironov, I., Talwar, K.,
  and Zhang, L. "Deep Learning with Differential Privacy." ACM Conference on
  Computer and Communications Security (CCS), 2016.
- Carlini, N., Tramèr, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee,
  K., Roberts, A., Brown, T., Song, D., Erlingsson, Ú., et al. "Extracting
  Training Data from Large Language Models." USENIX Security Symposium, 2021.
- Dwork, C. and Roth, A. "The Algorithmic Foundations of Differential
  Privacy." Foundations and Trends in Theoretical Computer Science, 9(3-4),
  2014.
- Dwork, C., Smith, A., Steinke, T., Ullman, J., and Vadhan, S. "Robust
  Traceability from Trace Amounts." IEEE Symposium on Foundations of Computer
  Science (FOCS), 2015.
- Feldman, V. "Does Learning Require Memorization? A Short Tale about a Long
  Tail." ACM Symposium on Theory of Computing (STOC), 2020.
- Feldman, V. and Zhang, C. "What Neural Networks Memorize and Why:
  Discovering the Long Tail via Influence Estimation." arXiv:2008.03703, 2020.
- Homer, N., Szelinger, S., Redman, M., Duggan, D., Tembe, W., Muehling, J.,
  Pearson, J. V., Stephan, D. A., Nelson, S. F., and Craig, D. W. "Resolving
  Individuals Contributing Trace Amounts of DNA to Highly Complex Mixtures
  Using High-Density SNP Genotyping Microarrays." PLoS Genetics, 4(8), 2008.
- Jagielski, M., Ullman, J., and Oprea, A. "Auditing Differentially Private
  Machine Learning: How Private is Private SGD?" arXiv:2006.07709, 2020.
- Jayaraman, B., Wang, L., Evans, D., and Gu, Q. "Revisiting Membership
  Inference under Realistic Assumptions." Proceedings on Privacy Enhancing
  Technologies (PoPETs), 2021.
- Long, Y., Wang, L., Bu, D., Bindschaedler, V., Wang, X., Tang, H., Gunter,
  C. A., and Chen, K. "A Pragmatic Approach to Membership Inferences on
  Machine Learning Models." IEEE European Symposium on Security and Privacy
  (EuroS&P), 2020.
- Murakonda, S. K. and Shokri, R. "ML Privacy Meter: Aiding Regulatory
  Compliance by Quantifying the Privacy Risks of Machine Learning."
  arXiv:2007.09339, 2020.
- Nasr, M., Song, S., Thakurta, A., Papernot, N., and Carlini, N. "Adversary
  Instantiation: Lower Bounds for Differentially Private Machine Learning."
  arXiv:2101.04535, 2021.
- Neyman, J. and Pearson, E. S. "On the Problem of the Most Efficient Tests of
  Statistical Hypotheses." Philosophical Transactions of the Royal Society of
  London, 231(694-706), 1933.
- Sablayrolles, A., Douze, M., Schmid, C., Ollivier, Y., and Jégou, H.
  "White-box vs Black-box: Bayes Optimal Strategies for Membership Inference."
  International Conference on Machine Learning (ICML), 2019.
- Salem, A., Zhang, Y., Humbert, M., Berrang, P., Fritz, M., and Backes, M.
  "ML-Leaks: Model and Data Independent Membership Inference Attacks and
  Defenses on Machine Learning Models." 2018.
- Sankararaman, S., Obozinski, G., Jordan, M. I., and Halperin, E. "Genomic
  Privacy and Limits of Individual Detection in a Pool." Nature Genetics,
  41(9), 2009.
- Shokri, R., Stronati, M., Song, C., and Shmatikov, V. "Membership Inference
  Attacks Against Machine Learning Models." IEEE Symposium on Security and
  Privacy, 2017.
- Song, S. and Marn, D. "Introducing a New Privacy Testing Library in
  TensorFlow." TensorFlow Blog, 2020.
- Song, L. and Mittal, P. "Systematic Evaluation of Privacy Risks of Machine
  Learning Models." USENIX Security Symposium, 2021.
- Steinke, T. and Ullman, J. "The Pitfalls of Average-Case Differential
  Privacy." DifferentialPrivacy.org, 2020.
- Watson, L., Guo, C., Cormode, G., and Sablayrolles, A. "On the Importance of
  Difficulty Calibration in Membership Inference Attacks." arXiv:2111.08440,
  2021.
- Ye, J., Maddi, A., Murakonda, S. K., and Shokri, R. "Enhanced Membership
  Inference Attacks against Machine Learning Models." arXiv:2111.09679, 2021.
- Yeom, S., Giacomelli, I., Fredrikson, M., and Jha, S. "Privacy Risk in
  Machine Learning: Analyzing the Connection to Overfitting." IEEE Computer
  Security Foundations Symposium (CSF), 2018.
- Zhang, C., Bengio, S., Hardt, M., Recht, B., and Vinyals, O. "Understanding
  Deep Learning (Still) Requires Rethinking Generalization." Communications of
  the ACM, 64(3), 2021.
