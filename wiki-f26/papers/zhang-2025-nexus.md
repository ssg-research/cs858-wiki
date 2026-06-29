---
title: "Secure Transformer Inference Made Non-interactive"
authors:
  - Zhang, Jiawen
  - Yang, Xinpeng
  - He, Lipeng
  - Chen, Kejia
  - Lu, Wen-jie
  - Wang, Yinghao
  - Hou, Xiaoyang
  - Liu, Jian
  - Ren, Kui
  - Yang, Xiaohu
year: 2025
section: "Leakage Resistance (Client Data): Software"
primary: true
doi: "10.14722/ndss.2025.230868"
tags:
  - secure-inference
  - homomorphic-encryption
  - cryptography
  - privacy
  - defense
  - language-models
---

---

## [Wiki Home](../README.md)

---

# Secure Transformer Inference Made Non-interactive

## High-level overview

Running a transformer as a cloud service usually means the client sends its
prompt to the server in the clear and trusts the server with it.
[Secure inference](../concepts/secure-inference.md) removes that disclosure: the
client obtains the model's prediction while the server learns nothing about the
input and the client learns nothing about the weights beyond the result.
Protocols that did this for transformers had been interactive, with client and
server exchanging many rounds of messages and large volumes of data because the
nonlinear layers were evaluated with
[secure two-party computation](../concepts/secure-multiparty-computation.md).
This paper presents NEXUS, the first non-interactive protocol for secure
transformer inference: the client speaks once, sending a single encrypted input
and receiving a single encrypted result with no further communication while the
server computes.

NEXUS has the client encrypt its input under
[RNS-CKKS fully homomorphic encryption](../concepts/homomorphic-encryption.md), a
scheme whose ciphertexts support both addition and multiplication, so the server
evaluates the whole model, linear and nonlinear layers alike, on encrypted data
without any round trip. To keep that affordable the paper introduces packing and
compression primitives that keep a ciphertext's
[SIMD slots](../concepts/ciphertext-packing.md) fully used, and a secure argmax
whose cost grows with the logarithm of the vocabulary size rather than linearly,
so even the vocabulary-sized output layer over tens of thousands of tokens stays
tractable under encryption.

Against interactive baselines, NEXUS cuts bandwidth by more than two orders of
magnitude while keeping runtime comparable, and its non-interactive structure
admits a GPU implementation the interactive baselines cannot use, at accuracy
close to plaintext inference on the reported tasks.

**Threat Model:** Two parties run a single round of communication: a client
holding a private input and a server holding a private model. Both are
[semi-honest](../concepts/secure-multiparty-computation.md) (honest-but-curious)
and computationally bounded, so each follows the protocol exactly but may try to
infer the other's secret from its own view. A corrupted server must learn
nothing about the client's input; a corrupted client must learn nothing about
the model's weights beyond what the returned prediction reveals. The model's
architecture is treated as public; the protected secrets are the input values
and the weight values. Security is argued in the simulation paradigm, each
party's view shown reproducible from its own input and the output alone, so only
homomorphic ciphertexts and the final result cross the wire. The guarantee does
not cover a malicious party that deviates from the protocol. By design the
protocol returns only the argmax label rather than the full logit vector,
limiting the residual [membership-inference](../concepts/membership-inference.md)
leakage carried through the output itself.

## Why read this

<!-- instructor: confirm -->

NEXUS is the first secure transformer-inference protocol to remove interaction
entirely, recasting a problem the field had treated as communication-bound into
one bound by server computation. That shift is what lets it apply GPU and
FHE-accelerator speedups the interactive protocols structurally cannot. It is
also a clear worked example of evaluating every layer of a real transformer,
attention, GELU, softmax, layer normalization, and a vocabulary-sized argmax,
under a single homomorphic-encryption scheme.

## Basic Background

### Transformers and the layers evaluated under encryption

The models are transformers such as BERT and GPT,
[pretrained language models](../concepts/language-model-pretraining.md): a stack
of attention and feed-forward blocks ending in a linear layer that produces one
logit per vocabulary token, with the prediction read off by argmax (Devlin et
al., 2018; Radford et al., 2019). Inference interleaves
linear operations, the large matrix products in attention and the feed-forward
network, with nonlinear ones: softmax, the GELU activation, layer normalization,
and the final argmax. The split matters here because the two kinds of layer have
very different costs under encryption.

### Secure inference and its cost

[Secure inference](../concepts/secure-inference.md) runs the model so the server
never sees the input and the client never sees the weights, returning only the
prediction. Its cost is measured in three quantities: local computation, the
number of communication rounds, and total bandwidth. A protocol is interactive
when client and server exchange many rounds; it is non-interactive when the
client sends one message and receives one reply, which removes round-trip latency
at the price of heavier server computation.

### Homomorphic encryption

[Homomorphic encryption](../concepts/homomorphic-encryption.md) lets a party
compute on ciphertexts so that the decrypted result equals the function applied
to the plaintexts. A fully homomorphic scheme supports addition and
multiplication to arbitrary depth, refreshing accumulated ciphertext noise with a
costly bootstrapping step (Gentry, 2009); a leveled scheme supports a fixed
multiplicative depth. NEXUS uses RNS-CKKS, a fully homomorphic scheme for
approximate real-number arithmetic (Cheon et al., 2017; Cheon et al., 2018),
which fits the floating-point nature of neural-network computation and avoids the
separate fixed-point truncation that secret-sharing protocols need.

### SIMD packing of ciphertexts

A CKKS ciphertext holds many values in independent
[SIMD slots](../concepts/ciphertext-packing.md), so one homomorphic add or
multiply acts on the whole batch, but combining values across slots requires a
rotation. How densely a matrix or activation map fills the available slots sets
the per-value compute and the ciphertext bandwidth, which is why slot-level
packing is a central concern for any HE-based protocol.

### Secure computation and secret sharing

The interactive baselines evaluate nonlinear layers with
[secure two-party computation](../concepts/secure-multiparty-computation.md):
values are secret-shared between client and server, who exchange messages to
compute comparisons and exponentials. This is efficient in local compute but
spends communication rounds and bandwidth.

### Prediction outputs and membership-inference leakage

Returning a model's full probability vector leaks information that
[membership-inference](../concepts/membership-inference.md) attacks exploit
(Shokri et al., 2017). Returning only the most likely label, the argmax, leaks
less. Computing that argmax under encryption, over a vocabulary of tens of
thousands of tokens, is a distinct cost in any such protocol.

## Reading guidance

- Section II.A: the one-paragraph threat model. Note that both parties are
  assumed semi-honest and computationally bounded, and exactly what each is
  allowed to learn.
- Sections II.C and II.D: the RNS-CKKS background and the homomorphic sign
  primitive. Note how many of the nonlinear layers route through it.
- Section III: the matrix-multiplication protocol and its SIMD compression.
  Attention anchor: the offline-online split (Section III.C) moves work into an
  input-independent preprocessing phase; note what is assumed to run "only once,
  unless the model changes" and how that bears on the non-interactive claim.
- Section IV.A: the secure argmax and SIMD slot folding, the source of the
  logarithmic-versus-linear advantage over Phoenix.
- Section IV.B: how GELU, softmax, and layer normalization are evaluated under
  encryption.
- Section V and Figure 7: where bootstrapping is placed in the pipeline. Note its
  cost relative to the other operations and what governs where it runs.
- Sections VI.C and VI.D, Tables III-IV and Figure 9: the microbenchmarks and the
  end-to-end numbers. Attention anchor: NEXUS reports zero communication for the
  nonlinear functions but large single-machine runtimes; note the quantity being
  traded against bandwidth and where the GPU version recovers it.
- Section VI.E: the error and accuracy-versus-latency analysis. Note that both
  accuracy and latency hinge on the polynomial degree used inside bootstrapping.
- Section VII: the map of interactive transformer protocols and non-interactive
  CNN protocols, which fixes what was and was not available before this work.
- Appendix D: the formal simulation-based security statement and the semi-honest
  definition the paper adopts from Delphi.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [BumbleBee: Secure Two-party Inference Framework for Large Transformers](https://eprint.iacr.org/2023/1678) — the interactive two-party baseline this non-interactive approach is measured against.

</details>

<details>
<summary><h2>Paper Context</h2></summary>

Secure inference was developed first for
[convolutional networks](../concepts/convolutional-neural-network.md). One line
of work keeps the model and data encrypted under homomorphic encryption and
evaluates the network on ciphertexts; another secret-shares the computation
between client and server and relies on interaction. Hybrid systems split the
work, using homomorphic encryption or secret sharing for the linear layers and
interactive two-party computation for the nonlinear ones, as in Gazelle and
Delphi (Juvekar et al., 2018; Mishra et al., 2020), with MiniONN and Cheetah
refining the packing and the protocols (Liu et al., 2017; Huang et al., 2022).
Across these designs the nonlinear layers, evaluated interactively, dominate the
round count and the bandwidth.

Transformers enlarged the problem along two axes the CNN protocols had not
stressed: attention multiplies large matrices by large matrices rather than by
vectors, and the output layer ranges over a vocabulary of tens of thousands of
tokens. A sequence of two-party protocols adapted secure inference to
transformers, among them Iron, BOLT, and BumbleBee, each cutting the cost of
encrypted matrix multiplication and of GELU, softmax, and layer normalization
(Hao et al., 2022; Pang et al., 2024; Lu et al., 2023). Others replaced the
troublesome nonlinearities with cheaper polynomials or ReLU at the price of
retraining the model, as in THE-X and MPCFormer (Chen et al., 2022; Li et al.,
2023), or moved to a three-party setting with an added trust assumption, as in
PUMA, Sigma, and Privformer (Dong et al., 2023; Gupta et al., 2023; Akimoto et
al., 2023). These protocols stayed interactive, and the reported state of the art
consumed tens of gigabytes of bandwidth and thousands of rounds per inference,
which makes wide-area deployment slow and, under per-token cloud pricing,
expensive.

Non-interactivity had been reached only for convolutional networks. A separate
line evaluates a CNN entirely under fully homomorphic encryption, with no
interaction, by approximating or reducing the ReLU activations and tuning where
bootstrapping runs, among them CryptoNAS, DeepReduce, HEMET, AutoFHE, and SpENCNN
(Ghodsi et al., 2020; Jha et al., 2021; Lou and Jiang, 2021; Ao and Boddeti,
2024; Ran et al., 2023). For the discrete final selection, the non-interactive
argmax of Phoenix compares every element against the others and so scales
linearly with the number of classes (Jovanovic et al., 2022). None of these
methods supports the nonlinear functions a transformer needs, and a linear-cost
argmax over a full vocabulary is impractical.

</details>

---
<details>
<summary><h4>References</h4></summary>

Entries read off this paper's bibliography (PDF pages 14-17).

- Akimoto, Y., Fukuchi, K., Akimoto, Y., and Sakuma, J. "Privformer:
  Privacy-preserving Transformer with MPC." IEEE European Symposium on Security
  and Privacy (EuroS&P), 2023.
- Ao, W. and Boddeti, V. N. "AutoFHE: Automated Adaption of CNNs for Efficient
  Evaluation over FHE." USENIX Security Symposium, 2024.
- Chen, T., Bao, H., Huang, S., Dong, L., Jiao, B., Jiang, D., Zhou, H., Li, J.,
  and Wei, F. "THE-X: Privacy-Preserving Transformer Inference with Homomorphic
  Encryption." Findings of the Association for Computational Linguistics (ACL),
  2022.
- Cheon, J. H., Kim, A., Kim, M., and Song, Y. "Homomorphic Encryption for
  Arithmetic of Approximate Numbers." ASIACRYPT, 2017.
- Cheon, J. H., Han, K., Kim, A., Kim, M., and Song, Y. "A Full RNS Variant of
  Approximate Homomorphic Encryption." Selected Areas in Cryptography (SAC),
  2018.
- Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. "BERT: Pre-training of
  Deep Bidirectional Transformers for Language Understanding." arXiv:1810.04805,
  2018.
- Dong, Y., Lu, W.-j., Zheng, Y., Wu, H., Zhao, D., Tan, J., Huang, Z., Hong, C.,
  Wei, T., and Cheng, W. "PUMA: Secure Inference of LLaMA-7B in Five Minutes."
  arXiv:2307.12533, 2023.
- Gentry, C. "A Fully Homomorphic Encryption Scheme." PhD thesis, Stanford
  University, 2009.
- Ghodsi, Z., Veldanda, A. K., Reagen, B., and Garg, S. "CryptoNAS: Private
  Inference on a ReLU Budget." Advances in Neural Information Processing Systems
  (NeurIPS), 2020.
- Gupta, K., Jawalkar, N., Mukherjee, A., Chandran, N., Gupta, D., Panwar, A.,
  and Sharma, R. "SIGMA: Secure GPT Inference with Function Secret Sharing."
  Cryptology ePrint Archive, 2023.
- Hao, M., Li, H., Chen, H., Xing, P., Xu, G., and Zhang, T. "Iron: Private
  Inference on Transformers." Advances in Neural Information Processing Systems
  (NeurIPS), 2022.
- Huang, Z., Lu, W.-j., Hong, C., and Ding, J. "Cheetah: Lean and Fast Secure
  Two-Party Deep Neural Network Inference." USENIX Security Symposium, 2022.
- Jha, N. K., Ghodsi, Z., Garg, S., and Reagen, B. "DeepReduce: ReLU Reduction
  for Fast Private Inference." International Conference on Machine Learning
  (ICML), 2021.
- Jovanovic, N., Fischer, M., Steffen, S., and Vechev, M. "Private and Reliable
  Neural Network Inference." ACM Conference on Computer and Communications
  Security (CCS), 2022.
- Juvekar, C., Vaikuntanathan, V., and Chandrakasan, A. "GAZELLE: A Low Latency
  Framework for Secure Neural Network Inference." USENIX Security Symposium,
  2018.
- Li, D., Shao, R., Wang, H., Guo, H., Xing, E. P., and Zhang, H. "MPCFormer:
  Fast, Performant and Private Transformer Inference with MPC." International
  Conference on Learning Representations (ICLR), 2023.
- Liu, J., Juuti, M., Lu, Y., and Asokan, N. "Oblivious Neural Network
  Predictions via MiniONN Transformations." ACM Conference on Computer and
  Communications Security (CCS), 2017.
- Lou, Q. and Jiang, L. "HEMET: A Homomorphic-Encryption-Friendly
  Privacy-Preserving Mobile Neural Network Architecture." International
  Conference on Machine Learning (ICML), 2021.
- Lu, W.-j., Huang, Z., Gu, Z., Li, J., Liu, J., Ren, K., Hong, C., Wei, T., and
  Chen, W. "BumbleBee: Secure Two-Party Inference Framework for Large
  Transformers." Cryptology ePrint Archive, Paper 2023/1678, 2023.
- Mishra, P., Lehmkuhl, R., Srinivasan, A., Zheng, W., and Popa, R. A. "Delphi: A
  Cryptographic Inference Service for Neural Networks." USENIX Security
  Symposium, 2020.
- Pang, Q., Zhu, J., Möllering, H., Zheng, W., and Schneider, T. "BOLT:
  Privacy-Preserving, Accurate and Efficient Inference for Transformers." IEEE
  Symposium on Security and Privacy (S&P), 2024.
- Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I.
  "Language Models are Unsupervised Multitask Learners." OpenAI blog, 2019.
- Ran, R., Luo, X., Wang, W., Liu, T., Quan, G., Xu, X., Ding, C., and Wen, W.
  "SpENCNN: Orchestrating Encoding and Sparsity for Fast Homomorphically
  Encrypted Neural Network Inference." International Conference on Machine
  Learning (ICML), 2023.
- Shokri, R., Stronati, M., Song, C., and Shmatikov, V. "Membership Inference
  Attacks Against Machine Learning Models." IEEE Symposium on Security and
  Privacy (S&P), 2017.

</details>
