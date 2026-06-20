---
title: "Deep Learning with Differential Privacy"
authors:
  - Abadi, Martín
  - Chu, Andy
  - Goodfellow, Ian
  - McMahan, H. Brendan
  - Mironov, Ilya
  - Talwar, Kunal
  - Zhang, Li
year: 2016
section: "Differential Privacy"
primary: true
arxiv: "1607.00133"
doi: "10.1145/2976749.2978318"
tags:
  - differential-privacy
  - privacy
  - defense
  - dp-sgd
---

# Deep Learning with Differential Privacy

## High-level overview

Neural networks are trained on datasets that may contain sensitive records, and
a trained model's parameters can encode fine details of individual examples.
This paper trains deep networks under
[differential privacy](../concepts/differential-privacy.md), the formal
guarantee that the trained model's distribution changes by at most a bounded
factor when any single training example is added or removed. Its algorithm,
now universally called DP-SGD, modifies
[stochastic gradient descent](../concepts/stochastic-gradient-descent.md) in
two places: each example's gradient is
[clipped](../concepts/gradient-clipping.md) to a fixed norm (bounding any one
example's influence, its sensitivity), and calibrated Gaussian noise is added
to the summed gradients before the update (the
[Gaussian mechanism](../concepts/gaussian-mechanism.md)). Terminology note:
the "privacy budget" is the pair (epsilon, delta) the training run is allowed
to spend, an "accountant" is the procedure that tracks spending across steps,
and the paper's "lot" is the sampling unit noise is added over, distinct from
the computational batch.

The paper's second contribution is the moments accountant, a tighter way to
track the [privacy budget](../concepts/privacy-budget.md) across thousands of
training steps. Generic composition theorems made deep training spend its
budget far too fast; tracking higher moments of the privacy loss gives bounds
tight enough that, in the paper's running example, the same training run costs
epsilon of roughly 1.3 instead of 9.3. With both pieces implemented in
TensorFlow, the paper reports 97% test accuracy on MNIST and 73% on CIFAR-10
at single-digit budgets ((8, 10^-5)-differential privacy, with 90% on MNIST
at epsilon as small as 0.5), against non-private baselines of about 98.3% and
80%. The CIFAR-10 model trains only its fully connected layers privately, on
top of convolutional layers pre-trained on a dataset treated as public.

**Threat Model:** A defense paper, and the guarantee is attack-agnostic: it
does not name an adversary strategy, it bounds what any adversary can learn.
The protected secret is one training record's presence and content; adjacent
datasets differ in a single image-label pair. The adversary is as strong as
the definition allows: [white-box](../concepts/white-box-black-box.md) access
to the released model parameters, full knowledge of the training mechanism,
arbitrary auxiliary information, and possibly control of every other training
record. The defender claims (epsilon, delta)-differential privacy for the
entire released parameter vector, which then bounds the success of any present
or future attack, including [membership
inference](../concepts/membership-inference.md). The guarantee says nothing
about secrets shared across many records, and its strength degrades as epsilon
grows.

## Why read this

Empirical defenses hold only until a stronger attack arrives. This paper instead
gives a defense with a proof, a training algorithm whose privacy guarantee holds
against any adversary, including future ones. Using it in practice is difficult,
since clipping and noise cost accuracy and the budget constrains how long a model
can train, yet differential privacy remains the only known way to actually
guarantee training-data privacy, and nearly every modern private training
system, federated learning especially, builds on this algorithm in some form.

## Basic Background

### Training neural networks

Training minimizes the average loss over the training set, the
[empirical risk minimization](../concepts/empirical-risk-minimization.md)
objective, using
[stochastic gradient descent](../concepts/stochastic-gradient-descent.md):
estimate the gradient on a batch of examples, step against it, repeat. For
deep networks the loss is non-convex, so training finds a local minimum, and
no tight characterization exists of how the final parameters depend on any
one training example. Noise added to the finished model must therefore be
scaled to a loose worst case, which destroys the model's utility; enforcing
privacy inside the training loop avoids this.

### Why trained models leak

A network's capacity lets it [memorize](../concepts/memorization.md)
individual training examples, and what is memorized can be recovered: model
inversion reconstructs recognizable face images from a facial recognition
model's outputs (Fredrikson et al., 2015), and
[membership inference](../concepts/membership-inference.md) predicts whether
a specific record was trained on. Regularization may reduce such leakage but
provides no guarantee.

### Differential privacy

[Differential privacy](../concepts/differential-privacy.md) is a property of
a randomized algorithm: for any two adjacent datasets (differing in one
record) the probability of any output set changes by at most a factor of
e^epsilon, plus slack delta (Dwork et al., 2006a; Dwork et al., 2006b). Three
properties of the definition are used throughout this literature:
composability (private components
compose into a private system), group privacy (graceful degradation for
correlated records), and robustness to auxiliary information (the guarantee
does not depend on what the adversary already knows). The standard reference
is Dwork and Roth (2014).

### Sensitivity and the Gaussian mechanism

The basic recipe for making a function private is additive noise scaled to its
sensitivity, the most any single record can change its output; adding Gaussian
noise calibrated this way yields the
[Gaussian mechanism](../concepts/gaussian-mechanism.md) (Dwork et al., 2006b).
A gradient has no a priori sensitivity bound, which is the gap
[gradient clipping](../concepts/gradient-clipping.md) closes: rescaling every
example's gradient to a maximum norm C makes C the sensitivity by
construction.

### The privacy budget and composition

Each noisy step leaks a little, and the leaks accumulate. Composition theorems
bound the total: the basic theorem adds the epsilons, and the strong
composition theorem does better over many steps (Dwork et al., 2010; Kairouz
et al., 2015). A privacy accountant tracks the accumulated
[budget](../concepts/privacy-budget.md) during execution (McSherry, 2009).
Random sampling of each batch amplifies privacy, since a record absent from a
batch leaks nothing in that step. How tightly the accountant adds up thousands
of sampled Gaussian steps decides how long a network can train before its
budget is exhausted.

## Paper Context

Privacy-preserving learning is older than deep learning. Privacy-preserving
data mining was posed around 2000, in both randomization and cryptographic
forms (Agrawal and Srikant, 2000; Lindell and Pinkas, 2000). The
then-dominant data-release notion, k-anonymity (Sweeney, 2002), generalizes
and suppresses identifying attributes; on high-dimensional data, achieving it
destroys most of the data's mining utility for little privacy gain (Aggarwal,
2005; Brickell and Shmatikov, 2008). Differential privacy emerged
from the theory community as the rigorous alternative: privacy as a property
of the computation rather than of the released data, with noise calibrated to
sensitivity (Dwork et al., 2006a), the (epsilon, delta) relaxation (Dwork et
al., 2006b), and a decade of supporting machinery, including strong
composition (Dwork et al., 2010; Kairouz et al., 2015), the privacy accountant
(McSherry, 2009), and a textbook treatment (Dwork and Roth, 2014).

Differentially private machine learning then developed almost entirely on
convex problems. Private empirical risk minimization was solved by output and
objective perturbation (Chaudhuri et al., 2011; Kifer et al., 2012) and by
noisy gradient methods with tight error bounds (Bassily et al., 2014),
including a direct DP-SGD precursor (Song et al., 2013). The first end-to-end
differentially private learning system was a recommender built on the Netflix
Prize data, which worked by privatizing sufficient statistics of the task
(McSherry and Mironov, 2009), a route unavailable for models with no such
statistics.

Deep networks fall outside the assumptions of this line of work: the loss is
non-convex, parameters number in the millions, and training takes many passes
over datasets that are increasingly crowdsourced and sensitive. Model
inversion demonstrated the leakage on such models, recovering recognizable
images from a face recognition model (Fredrikson et al., 2015). The one
attempt at private deep learning before this paper, a distributed protocol
perturbing shared gradient updates, spent its budget per parameter, and its
total privacy loss per participant exceeded several thousand epsilon (Shokri
and Shmatikov, 2015). No published method trained a deep network to useful
accuracy at a single-digit budget. Tighter accounting tools, concentrated
differential privacy among them, were in concurrent development (Dwork and
Rothblum, 2016; Bun and Steinke, 2016).

## Reading guidance

- Section 2: the (epsilon, delta) definition, the Gaussian mechanism, and
  composition; everything after leans on these.
- Section 3.1 and Algorithm 1: the whole algorithm in one box. Each line maps
  to a concept: clipping bounds sensitivity, noise is the Gaussian mechanism,
  the accountant handles composition.
- Section 3.2 and Theorem 1: the moments accountant. Figure 2 shows what it
  buys over the strong composition theorem; proofs are in the appendix and can
  be deferred.
- Section 5.1: the accounting comparison in numbers.
- Section 5.2 and Figures 4 and 5: MNIST accuracy across (epsilon, delta)
  pairs and parameter sensitivity. The clipping threshold C has no formula;
  note how the paper chooses it.
- Section 5.3: CIFAR-10. Note which layers are trained privately and which are
  pre-trained on data the paper treats as public.
- Section 6: the map of prior private-learning approaches and the contrast
  with Shokri and Shmatikov (2015).

## Motivating questions

1. What does it cost, in accuracy and in training mechanics, to train a deep
   network with a provable privacy guarantee?
2. Where in the training pipeline is privacy enforced, and why there rather
   than by perturbing the final trained model?
3. What determines how fast training spends its privacy budget, and what does
   tighter accounting of the same noise change?
4. What do epsilon and delta promise for a single training record at the
   values the paper reports?
5. Which parts of a realistic model does the paper train privately, and which
   does it source from data treated as public?

## References

Entries read off the paper's bibliography (arXiv 1607.00133v2, pages 10-11).

- Aggarwal, C. C. "On k-Anonymity and the Curse of Dimensionality." VLDB,
  2005.
- Agrawal, R. and Srikant, R. "Privacy-Preserving Data Mining." ACM SIGMOD,
  2000.
- Bassily, R., Smith, A. D., and Thakurta, A. "Private Empirical Risk
  Minimization: Efficient Algorithms and Tight Error Bounds." IEEE Symposium
  on Foundations of Computer Science (FOCS), 2014.
- Brickell, J. and Shmatikov, V. "The Cost of Privacy: Destruction of
  Data-Mining Utility in Anonymized Data Publishing." ACM SIGKDD (KDD), 2008.
- Bun, M. and Steinke, T. "Concentrated Differential Privacy: Simplifications,
  Extensions, and Lower Bounds." Theory of Cryptography Conference (TCC-B),
  2016 (cited by the paper as concurrent work).
- Chaudhuri, K., Monteleoni, C., and Sarwate, A. D. "Differentially Private
  Empirical Risk Minimization." Journal of Machine Learning Research, 12,
  2011.
- Dwork, C., McSherry, F., Nissim, K., and Smith, A. "Calibrating Noise to
  Sensitivity in Private Data Analysis." Theory of Cryptography Conference
  (TCC), 2006. (2006a)
- Dwork, C., Kenthapadi, K., McSherry, F., Mironov, I., and Naor, M. "Our
  Data, Ourselves: Privacy via Distributed Noise Generation." EUROCRYPT,
  2006. (2006b)
- Dwork, C. and Roth, A. "The Algorithmic Foundations of Differential
  Privacy." Foundations and Trends in Theoretical Computer Science, 9(3-4),
  2014.
- Dwork, C. and Rothblum, G. N. "Concentrated Differential Privacy."
  arXiv:1603.01887, 2016.
- Dwork, C., Rothblum, G. N., and Vadhan, S. "Boosting and Differential
  Privacy." IEEE Symposium on Foundations of Computer Science (FOCS), 2010.
- Fredrikson, M., Jha, S., and Ristenpart, T. "Model Inversion Attacks that
  Exploit Confidence Information and Basic Countermeasures." ACM Conference
  on Computer and Communications Security (CCS), 2015.
- Kairouz, P., Oh, S., and Viswanath, P. "The Composition Theorem for
  Differential Privacy." International Conference on Machine Learning (ICML),
  2015.
- Kifer, D., Smith, A. D., and Thakurta, A. "Private Convex Optimization for
  Empirical Risk Minimization with Applications to High-Dimensional
  Regression." Conference on Learning Theory (COLT), 2012.
- Lindell, Y. and Pinkas, B. "Privacy Preserving Data Mining." CRYPTO, 2000.
- McSherry, F. D. "Privacy Integrated Queries: An Extensible Platform for
  Privacy-Preserving Data Analysis." ACM SIGMOD, 2009.
- McSherry, F. and Mironov, I. "Differentially Private Recommender Systems:
  Building Privacy into the Netflix Prize Contenders." ACM SIGKDD (KDD),
  2009.
- Shokri, R. and Shmatikov, V. "Privacy-Preserving Deep Learning." ACM
  Conference on Computer and Communications Security (CCS), 2015.
- Song, S., Chaudhuri, K., and Sarwate, A. "Stochastic Gradient Descent with
  Differentially Private Updates." IEEE GlobalSIP, 2013.
- Sweeney, L. "k-Anonymity: A Model for Protecting Privacy." International
  Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10(5), 2002.
