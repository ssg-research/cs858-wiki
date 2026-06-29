---
title: "Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs"
authors:
  - Bao, Ergute
  - Jiang, Yangfan
  - Wei, Fei
  - Xiao, Xiaokui
  - Li, Zitao
  - Li, Yaliang
  - Ding, Bolin
year: 2025
section: "Leakage Resistance (Training Data): Software"
primary: true
tags:
  - differential-privacy
  - privacy
  - defense
  - language-models
  - zeroth-order-optimization
---

---

### [Wiki Home](../README.md)

---

# Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs

## High-level overview

Fine-tuning a pretrained large language model on a sensitive dataset can leak
that dataset: the released model is open to
[membership inference](../concepts/membership-inference.md) and training-data
extraction. Differentially private fine-tuning removes that risk by adapting the
model under an (epsilon, delta) guarantee that bounds any single fine-tuning
record's influence on what is released. The standard method,
[DP-SGD](abadi-2016-dp-sgd.md), works on per-example first-order gradients
(Abadi et al., 2016), but computing those gradients by backpropagation through
an LLM is memory-heavy, and for billion-parameter models the gradient step alone
can exceed a high-end GPU. This paper fine-tunes under differential privacy with
[zeroth-order optimization](../concepts/zeroth-order-optimization.md) instead: a
gradient-free optimizer that estimates a descent direction from forward-pass
loss differences along random perturbation directions, so it needs roughly the
memory of inference rather than of backpropagation. The method, DP-AggZO,
aggregates multiple per-record zeroth-order direction estimates before clipping
and adding [Gaussian noise](../concepts/gaussian-mechanism.md), which
concentrates the per-record update so DP's required clipping injects far less
bias than clipping a single high-variance estimate.

DP-AggZO improves the privacy-utility trade-off of private zeroth-order
fine-tuning. Across a masked language model (RoBERTa) and autoregressive models
(the OPT family), on classification and generation tasks, it consistently beats
the prior differentially private zeroth-order baseline (DPZO) at the same
privacy budget, and it matches or surpasses the state-of-the-art first-order
private optimizer (DP-AdamW) while using far less memory; on the 355M-parameter
model it leads DP-AdamW across the benchmark tasks. On the largest model
studied, the first-order baselines run out of memory on a 96 GB GPU, while
DP-AggZO fine-tunes within that budget, at the cost of extra forward passes per
update and with memory held at the single-estimate DPZO level.

**Threat Model:** A defense under differential privacy, so the guarantee is
attack-agnostic rather than tied to a named adversary strategy. The protected
secret is the presence and content of any single record in the private
fine-tuning dataset; adjacent datasets differ in one record (record-level DP).
The adversary is as strong as the definition allows: it observes the released
fine-tuned model, may query its outputs, knows the training algorithm and the
random perturbation directions as public information, and may control every
other fine-tuning record. The defender claims (epsilon, delta)-differential
privacy for what the fine-tuning run releases, which bounds the success of any
membership inference or data-reconstruction attempt against the fine-tuning
data, present or future. As in DP-SGD, the privacy reasoning is on the noisy
per-iteration update, not on the final parameters; the pretrained base model is
treated as public.

## Why read this

<!-- instructor: confirm -->

Differentially private fine-tuning has been bottlenecked by the memory cost of
per-example gradients, which pushes large-model private training onto hardware
many groups lack. This paper shows that a gradient-free optimizer, far cheaper
in memory but inherently noisier, can be made into a competitive private
fine-tuner, in places matching or beating the first-order state of the art at a
fraction of the memory. The analysis connecting clipping bias to the convergence
rate is of independent interest, and reframes the memory-versus-utility tension
that has shaped private fine-tuning.

## Basic Background

### Differential privacy and its machinery

[Differential privacy](../concepts/differential-privacy.md) (DP) is a property
of a randomized algorithm: adding or removing any single input record changes
the output distribution by at most a bounded factor, set by the privacy
parameters (epsilon, delta) (Dwork et al., 2006). The standard way to make a
function private is to add noise scaled to its sensitivity, the most one record
can change the output; the [Gaussian mechanism](../concepts/gaussian-mechanism.md)
does this with normal noise. A quantity with no a priori sensitivity bound, such
as a gradient or a loss-difference estimate, is first forced into one by
[clipping](../concepts/gradient-clipping.md) it to a fixed norm per record. Each
private step spends part of a [privacy budget](../concepts/privacy-budget.md);
composition theorems and a privacy accountant bound the total leakage across the
thousands of steps a fine-tuning run takes, and sampling each batch at random
amplifies the per-step guarantee. Iterative training is commonly analyzed with
Rényi differential privacy, an accounting framework that tracks the Rényi
divergence between the output distributions on adjacent datasets and composes
tightly (Mironov, 2017).

### Training and fine-tuning a pretrained language model

A language model is first
[pretrained](../concepts/language-model-pretraining.md) on a large corpus by
next-token prediction, producing a base model. Adapting that base model to a
specific task on a smaller labeled dataset is fine-tuning, the language-model
instance of [transfer learning](../concepts/transfer-learning.md). Fine-tuning
minimizes the task loss with
[stochastic gradient descent](../concepts/stochastic-gradient-descent.md) or an
adaptive variant such as AdamW, estimating the gradient on a minibatch and
stepping against it. For neural networks the gradient comes from
backpropagation, which caches intermediate activations and gradients and so
costs several times the memory of a forward pass; for a large model this is the
dominant memory expense of fine-tuning. The models in this paper, the masked
language model RoBERTa and the autoregressive OPT family, are standard
open-source pretrained checkpoints.

### Zeroth-order optimization

[Zeroth-order optimization](../concepts/zeroth-order-optimization.md) replaces
the exact gradient with an estimate built only from loss values. For a random
direction z, the scaled loss difference along z approximates the directional
derivative, and multiplying it by z gives an estimate of the gradient that is
correct in expectation as the perturbation scale shrinks. This two-point,
simultaneous-perturbation estimator dates to stochastic approximation (Spall,
1992). Applied to LLM fine-tuning as MeZO, it needs only forward passes and
stores a random seed rather than the perturbation vector, cutting memory to
roughly that of inference, up to an order of magnitude below backpropagation
(Malladi et al., 2023). The estimate is high-variance, since a few random
directions probe a parameter space of millions of dimensions, so zeroth-order
methods converge more slowly than first-order ones.

### What private fine-tuning defends against

A fine-tuned model can leak its fine-tuning data.
[Membership inference](../concepts/membership-inference.md) predicts whether a
specific record was in the training set (Shokri et al., 2017), and derived as a
likelihood-ratio test it identifies members reliably even at low false-positive
rates ([LiRA](carlini-2022-lira.md); Carlini et al., 2022). Large language
models also [memorize](../concepts/memorization.md) individual training
sequences verbatim, which a black-box attacker can pull back out
([training-data extraction](carlini-2021-extracting-training-data.md); Carlini
et al., 2021). Differential privacy is the principled counter to both: bounding
any record's influence provably caps the success of any such attack, which is
the guarantee this line of work targets.

## Reading guidance

- Section 2: preliminaries on DP, DP-SGD, MeZO, and DPZO; skim if the basic
  background is familiar. Equations 6 and 7 define the zeroth-order
  loss-difference estimate.
- Section 4 and Lemma 2: the convergence analysis that ties clipping error to
  the convergence rate of DPZO. Figure 1 plots the distribution of the
  loss-difference estimates; note how heavy its tail is relative to the clipping
  thresholds prior work suggested.
- Section 5 and Algorithm 1: the method in one box. Figure 2 illustrates the
  aggregation idea, and Lemma 3 bounds the aggregate vector's norm.
- Section 5.3, Lemmas 4 and 5: the convergence rate and the Rényi DP guarantee.
  The accounting also spends budget on releasing the dataset size; note how
  much.
- Section 6, Tables 1 and 2: utility across models, tasks, and budgets, with
  DP-AdamW, DPZO, and non-DP references. The OOM entries mark where first-order
  baselines fail; Table 3 is the memory comparison.
- Figure 4: the clipping error over the course of training for each method; note
  how large it grows under the previously suggested thresholds.
- Figure 5: how utility changes with the number of aggregated directions, and
  where it saturates.
- Section 7: related work, placing the method among the DP fine-tuning,
  zeroth-order, and clipping lines.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [PrivateFL: Accurate, Differentially Private Federated Learning via Personalized Data Transformation](https://www.usenix.org/system/files/usenixsecurity23-yang-yuchen.pdf) — a different lever on the DP utility problem, applied in federated learning.
- [Local and Central Differential Privacy for Robustness and Privacy in Federated Learning](https://arxiv.org/abs/2009.03561) — the local-versus-central DP distinction that frames where the noise is added.

</details>

<details>
<summary><h2>Paper Context</h2></summary>

Differentially private deep learning standardized on DP-SGD, which clips
per-example gradients and adds Gaussian noise to their sum
([DP-SGD](abadi-2016-dp-sgd.md); Abadi et al., 2016). Bringing it to large
language models works but is expensive: fine-tuning a pretrained model under DP
can reach high accuracy (Li et al., 2022; Yu et al., 2024), yet the per-example
gradients DP-SGD requires multiply the memory of an already large
backpropagation, and for billion-parameter models the gradient computation alone
can exceed a high-end GPU. A separate line studies the bias that per-example
clipping injects into the optimization, and how to reduce it, for first-order
private training (Xiao et al., 2023). Parameter-efficient variants such as
DP-LoRA and DP-prefix tuning cut the cost but do not by themselves improve
utility at a fixed budget (Li et al., 2022; Yu et al., 2024).

Zeroth-order optimization offered a different lever on memory. Estimating a
descent direction from loss differences rather than backpropagation has roots in
stochastic approximation and control theory (Spall, 1992; Duchi et al., 2013),
and MeZO showed it scales to LLM fine-tuning with the memory footprint of
inference, at the price of slower, noisier convergence (Malladi et al., 2023).

MeZO was quickly taken up by the privacy community, since the loss-difference
update is a low-dimensional, bounded object that composes cleanly with DP.
Several differentially private zeroth-order methods appeared close together,
clipping and noising the scalar loss-difference estimate to obtain a private
update (DPZero, Zhang et al., 2024; Tang et al., 2024), including a
contemporaneous variant that draws multiple independent zeroth-order estimates
per step and clips each one (Liu et al., 2025). These methods inherit MeZO's
memory savings over DP-SGD, reported at around an eightfold reduction on a
355M-parameter model, but a utility gap to first-order private training remained
on several benchmarks when this paper appeared.

</details>

### [Wiki Home](../README.md)

<details>
<summary><h4>References</h4></summary>

Entries read off the paper's bibliography (USENIX Security 2025 proceedings,
pages 16-21); the Carlini et al. extraction paper is listed there as a 2020
preprint and is cited here by its USENIX Security 2021 publication.

- Abadi, M., Chu, A., Goodfellow, I. J., McMahan, H. B., Mironov, I., Talwar,
  K., and Zhang, L. "Deep Learning with Differential Privacy." ACM Conference on
  Computer and Communications Security (CCS), 2016.
- Carlini, N., Chien, S., Nasr, M., Song, S., Terzis, A., and Tramèr, F.
  "Membership Inference Attacks From First Principles." IEEE Symposium on
  Security and Privacy (S&P), 2022.
- Carlini, N., Tramèr, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee,
  K., Roberts, A., Brown, T., Song, D., Erlingsson, Ú., et al. "Extracting
  Training Data from Large Language Models." USENIX Security Symposium, 2021.
- Duchi, J. C., Jordan, M. I., Wainwright, M. J., and Wibisono, A. "Optimal
  Rates for Zero-Order Convex Optimization: The Power of Two Function
  Evaluations." IEEE Transactions on Information Theory, 61, 2013.
- Dwork, C., McSherry, F., Nissim, K., and Smith, A. "Calibrating Noise to
  Sensitivity in Private Data Analysis." Theory of Cryptography Conference
  (TCC), 2006.
- Li, X., Tramèr, F., Liang, P., and Hashimoto, T. "Large Language Models Can Be
  Strong Differentially Private Learners." International Conference on Learning
  Representations (ICLR), 2022.
- Liu, Z., Lou, J., Bao, W., Hu, Y., Li, B., Qin, Z., and Ren, K.
  "Differentially Private Zeroth-Order Methods for Scalable Large Language Model
  Finetuning." Network and Distributed System Security Symposium (NDSS), 2025.
- Malladi, S., Gao, T., Nichani, E., Damian, A., Lee, J. D., Chen, D., and
  Arora, S. "Fine-Tuning Language Models with Just Forward Passes." Advances in
  Neural Information Processing Systems (NeurIPS), 2023.
- Mironov, I. "Rényi Differential Privacy." IEEE Computer Security Foundations
  Symposium (CSF), 2017.
- Shokri, R., Stronati, M., Song, C., and Shmatikov, V. "Membership Inference
  Attacks Against Machine Learning Models." IEEE Symposium on Security and
  Privacy (S&P), 2017.
- Spall, J. C. "Multivariate Stochastic Approximation Using a Simultaneous
  Perturbation Gradient Approximation." IEEE Transactions on Automatic Control,
  37(3), 1992.
- Tang, X., Panda, A., Nasr, M., Mahloujifar, S., and Mittal, P. "Private
  Fine-tuning of Large Language Models with Zeroth-Order Optimization."
  arXiv:2401.04343, 2024.
- Xiao, H., Xiang, Z., Wang, D., and Devadas, S. "A Theory to Instruct
  Differentially-Private Learning via Clipping Bias Reduction." IEEE Symposium
  on Security and Privacy (S&P), 2023.
- Yu, D., Naik, S., Backurs, A., Gopi, S., Inan, H. A., Kamath, G., Kulkarni,
  J., Lee, Y. T., Manoel, A., Wutschitz, L., Yekhanin, S., and Zhang, H.
  "Differentially Private Fine-tuning of Language Models." Journal of Privacy
  and Confidentiality, 14(2), 2024.
- Zhang, L., Li, B., Thekumparampil, K. K., Oh, S., and He, N. "DPZero: Private
  Fine-Tuning of Language Models without Backpropagation." arXiv:2310.09639,
  2024.

</details>
