---
title: "ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks"
authors:
  - Tang, Minxue
  - Dai, Anna
  - DiValentin, Louis
  - Ding, Aolin
  - Hass, Amin
  - Gong, Neil Zhenqiang
  - Chen, Yiran
  - Li, Hai "Helen"
year: 2024
section: "Model Theft Resistance (+ On-Device Private Inference): Software"
primary: true
tags:
  - model-extraction
  - defense
  - threat-model
  - optimization
  - computer-vision
---

[Home page](../README.md)

# ModelGuard: Information-Theoretic Defense Against Model Extraction Attacks

## High-level overview

A classifier served through a prediction API can be copied by
[model extraction](../concepts/model-extraction.md): an adversary queries the
Machine-Learning-as-a-Service (MLaaS) system, collects the returned confidence
vectors, and trains a substitute model that reproduces the target's parameters or
its functionality. One defense family, prediction perturbation, alters the
confidence vectors the API returns so that a substitute trained on them comes out
worse, while honest users still get useful predictions. Earlier perturbation
defenses set the alteration heuristically. They pay a large utility cost for the
protection they buy, and an adaptive attacker, one that knows the defense is in
place and tries to undo it, recovers much of the signal before training.

This work introduces ModelGuard, a prediction-perturbation defense derived from a
constrained optimization problem: choose the perturbed confidence vector that
maximizes the loss an attacker incurs when training a substitute, subject to
utility constraints that bound the per-query distortion (in `ℓ1` norm) and keep
the top-1 label unchanged. The formulation unifies the parameter-stealing and the
functionality-stealing goals into a single objective, so one defense covers both.
Two variants solve it under different assumptions about the attacker's recovery
step. ModelGuard-W assumes a weak adaptive attacker that trains directly on the
perturbed outputs.
ModelGuard-S targets the optimal recovery, the Bayes estimator that an
unboundedly capable adaptive attacker would use, and defends an
information-theoretic lower bound on the attacker's loss. Decoded: an
"information-theoretic defense" here perturbs the outputs to minimize the
[mutual information](../concepts/mutual-information.md) between the clean
predictions and the ones returned, so the bound on what the attacker can recover
holds against any recovery procedure, not one fixed attack. Minimizing that
mutual information under the distortion budget is a rate-distortion problem.
Across image-classification benchmarks, and against a strong
Bayes-estimator adaptive attack the paper also constructs to stress-test
defenses, ModelGuard-S reports a better privacy-utility balance than prior
perturbation defenses.

**Threat Model:** The adversary mounts query-based model extraction against a
victim's prediction API over [black-box](../concepts/white-box-black-box.md)
access: it submits inputs and reads back the confidence-score vector over the
classes, with no side channel exposing anything more. It cannot read the
confidential training set, but it knows the input domain and queries with natural
or synthetic data from a similar domain, and in the strong case it knows the
target's architecture and uses the same one for its substitute. Its query budget
is unlimited, so it may repeat any query, which lets it average out a randomized
defense and reduces the problem to defeating a deterministic one. It is adaptive:
it knows the perturbation mechanism, can reproduce it, and applies a recovery
function to the returned vectors to estimate the clean predictions before
training the substitute toward a parameter-stealing or functionality-stealing
goal. The defender controls the prediction API and perturbs each returned vector
under two utility constraints, a bounded `ℓ1` distortion and an unchanged top-1
label, plus the validity constraint that the output stay a probability vector. It
protects the confidentiality of the model's parameters and functionality, and its
claim for the information-theoretic variant is a lower bound on the attacker's
substitute-training loss that holds against the optimal recovery, while honest
users keep high utility.

## Why read this

<!-- instructor: confirm -->
The paper gives the first general optimization formulation for defending against
adaptive model extraction, and shows that output perturbation, long treated as a
bag of heuristics, can be posed as a single objective with utility constraints
that covers both parameter-stealing and functionality-stealing. Its
information-theoretic variant earns a guarantee against the optimal recovery an
attacker could use rather than against one fixed attack, which is the property
most prior perturbation defenses lacked. The reduction of the defense to a
rate-distortion problem connects model-stealing defense to classical information
theory.

## Basic Background

### Model extraction and MLaaS

[Model extraction](../concepts/model-extraction.md), or model stealing,
reproduces an asset of a deployed model from external access, usually the
[black-box](../concepts/white-box-black-box.md) query interface of a prediction
API in the Machine-Learning-as-a-Service (MLaaS) setting, where a client sends
inputs and receives outputs and pays per query. Attacks split by what they
recover: the exact parameters, the architecture or hyperparameters, or the
model's functionality, a substitute that matches task accuracy without matching
internals. The returned outputs may be hard top-1 labels or full confidence
vectors over the classes; richer outputs make extraction easier and are what a
perturbation defense alters.

### Training a substitute by distillation

Functionality stealing trains the substitute on the target's own responses, which
is [knowledge distillation](../concepts/knowledge-distillation.md) in adversarial
form: a student is fit to a teacher's output distribution rather than to
ground-truth labels. The substitute is typically a
[convolutional neural network](../concepts/convolutional-neural-network.md)
trained by [stochastic gradient descent](../concepts/stochastic-gradient-descent.md)
on a cross-entropy or squared-error loss against the returned vectors. Because the
attacker fits the returned vectors, perturbing those vectors changes what the
substitute learns.

### Information theory: entropy and mutual information

[Mutual information](../concepts/mutual-information.md) `I(X;Y)` measures how much
observing one variable reduces uncertainty about another, and it relates to
conditional entropy by `I(X;Y) = H(X) - H(X|Y)`, so lowering the mutual
information between a secret and an observable raises the secret's conditional
entropy given that observable. It is the
[KL divergence](../concepts/kl-divergence.md) between the joint distribution and
the product of the marginals. The same quantity is the rate term in
rate-distortion theory, where minimizing the information a compressed
representation carries about a source, subject to a bound on a distortion measure,
gives the most compact representation within the allowed distortion (Cover, 1999).

### Distortion metrics and downstream utility

The [`ℓ1` norm](../concepts/lp-norms.md) of the difference between two probability
vectors, the summed absolute change across classes, is a standard way to measure
how far one has moved from the other. Preserving a classifier's top-1 (argmax)
label holds its accuracy fixed while still letting the rest of the confidence
vector change. Confidence values also feed downstream uses such as
out-of-distribution detection, whose quality is read from the area under a
[ROC curve](../concepts/roc-curves.md) (AUROC).

<details>
<summary><h2>Paper Context</h2></summary>

By 2024 model extraction was an established threat against deployed prediction
APIs. Early attacks solved the parameters or a functionally exact equation of
simple model families from their confidence outputs (Tramèr et al., 2016). Later
attacks stole the functionality of deep networks from queries alone, using
natural data, as in the [Knockoff Nets](orekondy-2019-knockoff-nets.md)
functionality-stealing attack (Orekondy et al., 2019) and Copycat CNN
(Correia-Silva et al., 2018), or synthetic data (Juuti et al., 2019; Truong et
al., 2021). One line pushed extraction to high fidelity, recovering a substitute
that matches the victim prediction for prediction (Jagielski et al., 2020), and
another connected query selection to active learning to cut the query count
(Chandrasekaran et al., 2020). A stolen substitute is also a stepping stone:
white-box access to it yields transferable adversarial examples against the
target (Papernot et al., 2017).

Defenses against extraction fall into four families. Detection flags an attacker
from the distribution of its queries, which fails when the attacker queries with
natural in-domain data (Juuti et al., 2019; Pal et al., 2021; Kesarwani et al.,
2018). Information monitoring tracks how much each user has learned and throttles,
charges, or refuses once a threshold is crossed, which collaborating attackers
split across accounts evade (Kesarwani et al., 2018; Dziedzic et al., 2022; Yan
et al., 2021). Watermarking plants an owner-verifiable marker so the owner can
later claim a copy, but it does not stop a thief who keeps the substitute private
or uses it for downstream attacks (Adi et al., 2018; Cao et al., 2021; Jia et
al., 2020). Prediction perturbation alters the returned outputs to enlarge the
substitute's training loss or redirect its gradients (Lee et al., 2019; Orekondy
et al., 2019; Kariyappa and Qureshi, 2020; Mazeika et al., 2022); it makes the
fewest assumptions about the attacker and applies to any extraction goal.

The perturbation defenses set their alteration heuristically, and their reported
trade-off between protection and utility was a recurring weakness. They were also
evaluated mainly against attackers that take the returned outputs at face value.
Adaptive attackers, which know a defense is present and try to undo it, narrowed
the gains: a neural network trained to map perturbed outputs back to clean ones
recovers much of the signal (Lee et al., 2019), and a defense-penetrating attack
adds a detector that identifies the defense before recovering (Chen et al.,
2023). How to perturb outputs with a guarantee that survives an attacker who knows the
mechanism had received little attention.

</details>

## Reading guidance

- Section 2 (Threat Model): the attacker's goal, knowledge, and capability, and
  the adaptive attacker that applies a recovery function to the returned outputs
  before training. Note the unlimited-query-budget assumption and how it lets the
  defender restrict attention to deterministic perturbation.
- Section 3.1 to 3.2 (Overview, Objective and Constraints): the single objective
  that covers both stealing goals, the two utility constraints (`ℓ1` distortion,
  top-1 preserved), and the simplex validity constraint. Attention anchor:
  Lemma 1 reduces the parameter-stealing defense to the functionality objective
  under a smoothness assumption; note exactly what is assumed.
- Section 3.3 (ModelGuard-W): the weak-attacker approximation that the recovered
  predictions equal the perturbed ones, and the reduction to linear programming.
- Section 3.4 (Bayes Attack): the optimal recovery as the Bayes estimator and the
  brute-force lookup-table attack, then Partial Bayes Attack, which shrinks the
  sampling space to make the attack runnable.
- Section 3.5 (ModelGuard-S): the information-theoretic lower bound (Lemma 2), the
  reformulation as minimizing mutual information, and the online vector
  quantization that solves the rate-distortion problem one query at a time.
  Attention anchor: the contrast between non-ordered and ordered incremental
  quantization; note what consistency across repeated queries denies the
  attacker.
- Section 4 (Experiments), with the figures and tables: the four datasets
  (Caltech256, CUB200, CIFAR100, CIFAR10) and the baseline defenses (Top-1,
  Rounding, RevSig, Adaptive Misinformation, MAD). Attention anchor: the utility
  axis combines `ℓ1` distortion with a downstream OOD-detection AUROC; note which
  utility metric is reported in which figure.
- Section 5 (Related Works): the four defense families and where prediction
  perturbation sits among them.
- Section 6 (Conclusion, Limitations, and Future Work): the gap between the
  runnable Partial Bayes Attack and the perfect Bayes Attack, and the restriction
  of the evaluation to classification.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [Beowulf: Mitigating Model Extraction Attacks Via Reshaping Decision Regions](https://dl.acm.org/doi/pdf/10.1145/3658644.3670267) — a different defense lever against extraction, reshaping the target's decision regions rather than perturbing the returned probabilities.

</details>

[Home page](../README.md)

<details>
<summary><h2>References</h2></summary>

- Adi, Y., Baum, C., Cisse, M., Pinkas, B., and Keshet, J. "Turning Your Weakness Into a Strength: Watermarking Deep Neural Networks by Backdooring." USENIX Security Symposium, 2018.
- Cao, X., Jia, J., and Gong, N.Z. "IPGuard: Protecting Intellectual Property of Deep Neural Networks via Fingerprinting the Classification Boundary." ACM Asia Conference on Computer and Communications Security (AsiaCCS), 2021.
- Chandrasekaran, V., Chaudhuri, K., Giacomelli, I., Jha, S., and Yan, S. "Exploring Connections Between Active Learning and Model Extraction." USENIX Security Symposium, 2020.
- Chen, Y., Guan, R., Gong, X., Dong, J., and Xue, M. "D-DAE: Defense-Penetrating Model Extraction Attacks." IEEE Symposium on Security and Privacy (S&P), 2023.
- Correia-Silva, J.R., Berriel, R.F., Badue, C., de Souza, A.F., and Oliveira-Santos, T. "Copycat CNN: Stealing Knowledge by Persuading Confession with Random Non-Labeled Data." International Joint Conference on Neural Networks (IJCNN), 2018.
- Cover, T.M. "Elements of Information Theory." John Wiley & Sons, 1999.
- Dziedzic, A., Kaleem, M.A., Lu, Y.S., and Papernot, N. "Increasing the Cost of Model Extraction with Calibrated Proof of Work." arXiv:2201.09243, 2022.
- Jagielski, M., Carlini, N., Berthelot, D., Kurakin, A., and Papernot, N. "High Accuracy and High Fidelity Extraction of Neural Networks." USENIX Security Symposium, 2020.
- Jia, H., Choquette-Choo, C.A., Chandrasekaran, V., and Papernot, N. "Entangled Watermarks as a Defense Against Model Extraction." arXiv:2002.12200, 2020.
- Juuti, M., Szyller, S., Marchal, S., and Asokan, N. "PRADA: Protecting Against DNN Model Stealing Attacks." IEEE European Symposium on Security and Privacy (EuroS&P), 2019.
- Kariyappa, S. and Qureshi, M.K. "Defending Against Model Stealing Attacks With Adaptive Misinformation." IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020.
- Kesarwani, M., Mukhoty, B., Arya, V., and Mehta, S. "Model Extraction Warning in MLaaS Paradigm." Annual Computer Security Applications Conference (ACSAC), 2018.
- Lee, T., Edwards, B., Molloy, I., and Su, D. "Defending Against Neural Network Model Stealing Attacks Using Deceptive Perturbations." IEEE Security and Privacy Workshops (SPW), 2019.
- Mazeika, M., Li, B., and Forsyth, D. "How to Steer Your Adversary: Targeted and Efficient Model Stealing Defenses with Gradient Redirection." International Conference on Machine Learning (ICML), 2022.
- Orekondy, T., Schiele, B., and Fritz, M. "Knockoff Nets: Stealing Functionality of Black-Box Models." IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019.
- Orekondy, T., Schiele, B., and Fritz, M. "Prediction Poisoning: Towards Defenses Against DNN Model Stealing Attacks." arXiv:1906.10908, 2019.
- Pal, S., Gupta, Y., Kanade, A., and Shevade, S. "Stateful Detection of Model Extraction Attacks." arXiv:2107.05166, 2021.
- Papernot, N., McDaniel, P., Goodfellow, I., Jha, S., Celik, Z.B., and Swami, A. "Practical Black-Box Attacks Against Machine Learning." ACM Asia Conference on Computer and Communications Security (AsiaCCS), 2017.
- Tramèr, F., Zhang, F., Juels, A., Reiter, M.K., and Ristenpart, T. "Stealing Machine Learning Models via Prediction APIs." USENIX Security Symposium, 2016.
- Truong, J.-B., Maini, P., Walls, R.J., and Papernot, N. "Data-Free Model Extraction." IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2021.
- Yan, H., Li, X., Li, H., Li, J., Sun, W., and Li, F. "Monitoring-Based Differential Privacy Mechanism Against Query Flooding-Based Model Extraction Attack." IEEE Transactions on Dependable and Secure Computing (TDSC), 2021.

</details>
