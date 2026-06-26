---
title: "No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML"
authors:
  - Zhang, Ziqi
  - Gong, Chen
  - Cai, Yifeng
  - Yuan, Yuanyuan
  - Liu, Bingyan
  - Li, Ding
  - Guo, Yao
  - Chen, Xiangqun
year: 2024
section: "Leakage Resistance (Training Data): Hardware"
primary: true
arxiv: "2310.07152"
tags:
  - trusted-execution-environment
  - hardware-security
  - model-extraction
  - membership-inference
  - privacy
  - defense
  - evaluation
---

### [Wiki Home](../README.md)

# No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML

## High-level overview

On-device machine learning ships a trained model to a phone or IoT device, where
the party holding the device can read its weights directly. That
white-box access makes two attacks cheap: [model
stealing](../concepts/model-extraction.md) (MS), which reproduces a model's
weights or functionality, and the [membership inference
attack](../concepts/membership-inference.md) (MIA), which recovers whether a
record was in the training set. Hosting the whole model in a [trusted execution
environment](../concepts/trusted-execution-environment.md) (TEE) downgrades both
to the harder black-box setting, but a TEE runs a deep network up to about 50
times slower than a GPU. TEE-Shielded DNN Partition (TSDP) is the class of
defenses that splits the difference: a privacy-sensitive subset of the network
runs inside the TEE while the rest is offloaded to the device's untrusted GPU for
speed (see [model partitioning](../concepts/model-partitioning.md)). Every TSDP
scheme assumes the offloaded part exposes no more than a black-box interface.

This paper is the first systematic security evaluation of that assumption. It
surveys TSDP schemes published from 2018 to 2023, sorts them into five partition
strategies by which part of the network the TEE shields, and benchmarks a
representative of each with both MS and MIA under one practical adversary. The
measurements run against the schemes: model stealing reaches several times the
accuracy of the shielding-whole-model baseline, and membership inference stays
consistently above it, close to fully white-box quality. The deployed partitions
do not deliver the black-box-level protection they claim. The "sweet spot"
partition, the one giving the most security at the least utility cost, shifts
across models and datasets, so it cannot be set in advance. The paper closes with
TeeSlice, a partition-before-training design that isolates privacy-bearing weights
into small slices and reaches shielding-whole-model security at over ten times
less TEE overhead with no accuracy loss.

**Threat Model:** A model owner (the defender) ships a model to a device whose
rich execution environment, the ordinary operating system, applications, and the
device user, is adversarial. The adversary reads, and in principle can tamper
with, the offloaded part of the model running outside the TEE, and observes the
TEE's inputs and outputs, which return predicted labels only (label-only outputs).
It cannot break the TEE, whose internal data and computation are assumed secure,
and side channels against the TEE are out of scope. Beyond the device the
adversary holds public pretrained models and datasets, used to infer the protected
model's architecture and to initialize a surrogate, plus a query budget against
the deployed label-only model under one percent of the training-set size. The
protected assets are the model, against extraction, and the training-data privacy
that model leakage would expose, against membership inference. The defender's
claim, which the paper measures, is that shielding a privacy-sensitive subset
downgrades white-box MS and MIA to the black-box label-only setting, matching the
protection of shielding the entire model.

## Why read this

<!-- instructor: confirm -->

This is a systematization-and-attack paper: it takes a family of deployed hardware
defenses at their word, builds one practical adversary, and shows that placing
part of a model in a TEE while offloading the rest leaks most of what the
shielding was meant to protect. The result reframes on-device model protection as
a question of which weights carry privacy, not how many layers sit in the enclave,
and shows that the answer shifts with the model and the dataset. It pairs a
negative result about existing schemes with a constructive alternative, a useful
template for the security evaluation of a defense class.

## Basic Background

### On-device ML and trusted execution environments

On-device ML runs a model on the end user's hardware for latency and privacy,
which also hands the device owner the model file. A
[trusted execution environment](../concepts/trusted-execution-environment.md) is a
hardware-isolated region, an enclave, that holds code and data so the rest of the
system, including a malicious operating system, cannot read or alter them.
Commodity examples are Intel SGX (McKeen et al., 2013), AMD SEV (Kaplan et al.,
2016), and Arm TrustZone (Alves, 2004). The hardware outside the enclave, the
normal OS and applications and the accelerators it drives, is the rich execution
environment, and on a user device it is what the adversary controls.

### Partitioning a model across a TEE and a GPU

A whole model inside a TEE is secure but slow, so TSDP runs only part of the
network in the enclave and offloads the rest to the GPU (see
[model partitioning](../concepts/model-partitioning.md)). The schemes differ in
which part they shield: a block of layers, the largest-magnitude weights, or the
non-linear layers with the linear ones obfuscated before offloading. More shielded
computation buys more protection and costs more latency, the trade-off every
partition must resolve.

### Model stealing and membership inference

[Model stealing](../concepts/model-extraction.md), or model extraction, reproduces
a deployed model's parameters or functionality from external access; early attacks
solved simple model families from prediction-API outputs (Tramèr et al., 2016),
and later ones trained accurate or high-fidelity copies across architectures and
data distributions (Orekondy et al., 2019; Jagielski et al., 2020). The
[membership inference attack](../concepts/membership-inference.md) predicts whether
a specific example was in the training set, the standard privacy audit; a common
construction trains [shadow models](../concepts/shadow-models.md) that imitate the
target to calibrate the decision (Shokri et al., 2017), later recast as a
calibrated likelihood-ratio test (Carlini et al., 2022). The paper's central
framing is the
[white-box versus black-box](../concepts/white-box-black-box.md) gap: shielding is
meant to deny the adversary the weights and force the harder query-only attack.

### Public models and transfer learning

The benchmarked models are standard
[convolutional networks](../concepts/convolutional-neural-network.md), including
ResNet, VGG, and AlexNet, built by
[transfer learning](../concepts/transfer-learning.md): a public backbone
pretrained on a large dataset, then fine-tuned on the task. The same public
backbones are an adversary resource, supplying a near-equivalent model from which
to read architecture and initialize a surrogate.

### Differential privacy as the formal alternative

[Differential privacy](../concepts/differential-privacy.md) (DP) bounds any single
training example's influence on a model and so caps membership-inference success
with a provable guarantee (Dwork and Roth, 2014). It addresses data privacy rather
than model stealing, and its accuracy cost is the reason the on-device line looks
to hardware instead.

<details>
<summary><h2>Paper Context</h2></summary>

Putting a model on a user's device exposes its weights, turning model stealing and
membership inference into cheap white-box attacks. The algorithmic protections do
not transfer well to this setting. Cryptographic secure-inference protocols built
on [secure multiparty computation](../concepts/secure-multiparty-computation.md)
or [homomorphic encryption](../concepts/homomorphic-encryption.md) are too heavy
for mobile and IoT hardware (Gilad-Bachrach et al., 2016; Juvekar et al., 2018);
differential privacy bounds membership leakage but costs accuracy and does nothing
against model stealing (Dwork and Roth, 2014); and shielding a whole network in a
TEE is secure but slow, up to roughly 50 times the GPU latency (Lee et al., 2019).
That cost is what motivates partitioning the model.

The partition line begins with running a network jointly across a TEE and a GPU,
offloading the heavy linear algebra to the GPU under verification and blinding
while the enclave preserves integrity and privacy (Tramèr and Boneh, 2019).
Successors kept a privacy-sensitive subset in the enclave and offloaded the rest,
differing in what they shield: deep layers (Mo et al., 2020), shallow layers split
across enclaves (Elgamal and Nahrstedt, 2020), intermediate layers (Shen et al.,
2022), the large-magnitude weights of each layer (Hou et al., 2022), and the
non-linear layers with the offloaded linear layers obfuscated by matrix transforms
and filter permutation (Sun et al., 2020). These schemes share one premise: the
offloaded part leaks no more than a black-box query interface, so the shielded
subset is enough to downgrade white-box attacks.

The attacks that test such a premise were established separately. Model stealing
recovered parameters from prediction APIs for simple families (Tramèr et al.,
2016) and grew into accurate, high-fidelity functionality theft across mismatched
architectures and data (Orekondy et al., 2019; Jagielski et al., 2020). Membership
inference read the train-versus-test behavior gap, tied to overfitting (Shokri et
al., 2017; Yeom et al., 2018) and sharpened into a hypothesis test evaluated at low
false-positive rates (Carlini et al., 2022). An on-device adversary also holds
public pretrained models and datasets, which transfer-learning attacks convert
into knowledge of a target's architecture and weights (Wang et al., 2018; Chen et
al., 2022).

</details>

## Reading guidance

- Section 2: the TEE assumptions, the label-only output assumption, and the
  defender's goal of downgrading white-box attacks to black-box ones. Attention
  anchor: note exactly what the threat model grants the adversary (public
  models and datasets, the offloaded weights, a sub-one-percent query budget) and
  what it puts out of scope (TEE side channels).
- Section 3, Table 1 and Figure 1: the literature taxonomy and the five partition
  categories, with the representative scheme implemented for each.
- Sections 3.3 and 3.4, Figure 2: the three-phase attack pipeline (surrogate
  initialization, then model stealing, then membership inference) and the
  No-Shield (white-box) and Black-box (shielding-whole-model) baselines that bound
  every measurement.
- Section 3.5, Table 2: the headline comparison; read the relative-accuracy row,
  which scales each scheme's attack accuracy against the black-box baseline.
- Section 4: the security-versus-utility trade-off and the search for a "sweet
  spot" configuration. Attention anchor: note how stable that best configuration
  is across the model and dataset pairs.
- Section 5: TeeSlice and the partition-before-training strategy, the paper's
  proposed design.
- Section 6: TeeSlice measured against the same attacks and baselines, including
  the overhead figures and the NLP extension.
- Section 7: the related-work map, separating TEE-in-GPU hardware, side channels,
  whole-model shielding, and TSDP for training from the inference setting studied
  here.
- Appendix A: the meta-review and the authors' response, including the reviewers'
  concern about the one-time-pad feature-encryption assumption in TeeSlice.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [Slalom: Fast, Verifiable and Private Execution of Neural Networks in Trusted Hardware](https://arxiv.org/abs/1806.03287) — the foundational TEE-plus-accelerator partition idea this line of defenses descends from.

</details>

### [Wiki Home](../README.md)

<details>
<summary><h2>References</h2></summary>

Entries read off this paper's bibliography (PDF pages 15-18).

- Alves, T. "TrustZone: Integrated Hardware and Software Security." White paper, 2004.
- Carlini, N., Chien, S., Nasr, M., Song, S., Terzis, A., and Tramèr, F. "Membership Inference Attacks From First Principles." IEEE Symposium on Security and Privacy (S&P), 2022.
- Chen, Y., Shen, C., Wang, C., and Zhang, Y. "Teacher Model Fingerprinting Attacks Against Transfer Learning." USENIX Security Symposium, 2022.
- Dwork, C. and Roth, A. "The Algorithmic Foundations of Differential Privacy." Foundations and Trends in Theoretical Computer Science, 2014.
- Elgamal, T. and Nahrstedt, K. "Serdab: An IoT Framework for Partitioning Neural Networks Computation across Multiple Enclaves." IEEE/ACM International Symposium on Cluster, Cloud and Internet Computing (CCGRID), 2020.
- Gilad-Bachrach, R., Dowlin, N., Laine, K., Lauter, K. E., Naehrig, M., and Wernsing, J. "CryptoNets: Applying Neural Networks to Encrypted Data with High Throughput and Accuracy." International Conference on Machine Learning (ICML), 2016.
- Hou, J., Liu, H., Liu, Y., Wang, Y., Wan, P., and Li, X. "Model Protection: Real-Time Privacy-Preserving Inference Service for Model Privacy at the Edge." IEEE Transactions on Dependable and Secure Computing (TDSC), 2022.
- Jagielski, M., Carlini, N., Berthelot, D., Kurakin, A., and Papernot, N. "High Accuracy and High Fidelity Extraction of Neural Networks." USENIX Security Symposium, 2020.
- Juvekar, C., Vaikuntanathan, V., and Chandrakasan, A. P. "GAZELLE: A Low Latency Framework for Secure Neural Network Inference." USENIX Security Symposium, 2018.
- Kaplan, D., Powell, J., and Woller, T. "AMD Memory Encryption." White paper, 2016.
- Lee, T., Lin, Z., Pushp, S., Li, C., Liu, Y., Lee, Y., Xu, F., Xu, C., Zhang, L., and Song, J. "Occlumency: Privacy-Preserving Remote Deep-Learning Inference Using SGX." ACM International Conference on Mobile Computing and Networking (MobiCom), 2019.
- McKeen, F., Alexandrovich, I., Berenzon, A., Rozas, C. V., Shafi, H., Shanbhogue, V., and Savagaonkar, U. R. "Innovative Instructions and Software Model for Isolated Execution." Workshop on Hardware and Architectural Support for Security and Privacy (HASP), 2013.
- Mo, F., Shamsabadi, A. S., Katevas, K., Demetriou, S., Leontiadis, I., Cavallaro, A., and Haddadi, H. "DarkneTZ: Towards Model Privacy at the Edge Using Trusted Execution Environments." ACM International Conference on Mobile Systems, Applications, and Services (MobiSys), 2020.
- Orekondy, T., Schiele, B., and Fritz, M. "Knockoff Nets: Stealing Functionality of Black-Box Models." IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2019.
- Shen, T., Qi, J., Jiang, J., Wang, X., Wen, S., Chen, X., Zhao, S., Wang, S., Chen, L., Luo, X., Zhang, F., and Cui, H. "SOTER: Guarding Black-Box Inference for General Neural Networks at the Edge." USENIX Annual Technical Conference (ATC), 2022.
- Shokri, R., Stronati, M., Song, C., and Shmatikov, V. "Membership Inference Attacks Against Machine Learning Models." IEEE Symposium on Security and Privacy (S&P), 2017.
- Sun, Z., Sun, R., Lu, L., and Jha, S. "ShadowNet: A Secure and Efficient System for On-Device Model Inference." arXiv:2011.05905, 2020.
- Tramèr, F. and Boneh, D. "Slalom: Fast, Verifiable and Private Execution of Neural Networks in Trusted Hardware." International Conference on Learning Representations (ICLR), 2019.
- Tramèr, F., Zhang, F., Juels, A., Reiter, M. K., and Ristenpart, T. "Stealing Machine Learning Models via Prediction APIs." USENIX Security Symposium, 2016.
- Wang, B., Yao, Y., Viswanath, B., Zheng, H., and Zhao, B. Y. "With Great Training Comes Great Vulnerability: Practical Attacks Against Transfer Learning." USENIX Security Symposium, 2018.
- Yeom, S., Giacomelli, I., Fredrikson, M., and Jha, S. "Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting." IEEE Computer Security Foundations Symposium (CSF), 2018.

</details>
