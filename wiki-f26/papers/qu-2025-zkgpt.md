---
title: "zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference"
authors:
  - Qu, Wenjie
  - Sun, Yijun
  - Liu, Xuanming
  - Lu, Tao
  - Guo, Yanpei
  - Chen, Kai
  - Zhang, Jiaheng
year: 2025
section: "Regulatory Compliance: Software"
primary: true
tags:
  - zero-knowledge-proof
  - cryptography
  - language-models
  - machine-learning
---

---

## [Wiki Home](../README.md)

---

# zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference

## High-level overview

A user who queries a commercial language model through an API cannot check which
model answered. The provider has a cost incentive to swap in a smaller, cheaper
model and return lower-quality output, and the weights are trade secrets, so the
provider will not publish them for inspection. zkGPT closes this gap with a
[zero-knowledge proof](../concepts/zero-knowledge-proof.md): the provider
produces a short cryptographic proof that a claimed output is the correct result
of running one fixed, [committed](../concepts/cryptographic-commitment.md)
model on the user's input, and anyone can check the proof quickly without
learning the weights. The proof is non-interactive, a single string the prover
publishes via the Fiat-Shamir transform that a verifier checks offline, and
succinct, small and fast to verify relative to the inference it certifies.

The obstacle is that proof backends work over arithmetic circuits, which offer
only addition and multiplication in a finite field, while a
[transformer](../concepts/language-model-pretraining.md) interleaves large
matrix multiplications with non-arithmetic operations: the GeLU activation,
softmax inside attention, and layer normalization, which need comparison,
division, square root, and exponentiation. The non-linear layers, awkward to
arithmetize, dominate the proving cost. zkGPT builds a proof system specialized
for GPT-style models on the sumcheck and GKR interactive-proof protocols and the
Lasso lookup argument, treating the linear and non-linear layers separately. On
GPT-2 it proves an inference in under 25 seconds and emits a proof of about 101
KB. The reported prover time is roughly 279x faster than Hao et al. (USENIX
Security 2024) and 185x faster than the Plonk-based ZKML system (EuroSys 2024);
against the concurrent VOLE-based framework of Lu et al. it reports faster
proving and far less prover-to-verifier communication.

**Threat Model:** A prover, the model provider, wants to convince a skeptical
verifier that a claimed output y equals the model's inference on a given input x,
for a model whose weights w are bound by a public commitment. Public are the
commitment, the function f (the architecture and inference computation), the
input x, and the claimed output y; private is the witness w, the weights. The
adversary is a dishonest prover that may deviate arbitrarily from the honest
computation. Soundness: if y is not the correct output of the committed model on
x, no prover produces an accepting proof except with negligible probability.
Completeness: an honest prover always convinces the verifier. Zero-knowledge: the
proof reveals nothing about w beyond the truth of the statement, so the weights
stay secret. Each proof binds its output to the committed weights; when the
provider publishes one commitment in advance and answers every query against it,
that commitment is what prevents serving different queries with different models
or swapping in a cheaper model after the fact. The guarantee is about integrity
of the computation, not confidentiality of the user's input, which the verifier
supplies and already knows.

## Why read this

<!-- instructor: confirm -->

zkGPT is the first zero-knowledge proof system to make proving full GPT-2
inference practical, taking it from far too slow to interactive-scale latency. It
is a clear worked example of casting an entire transformer,
the large matrix multiplications and the awkward non-linear layers alike, into the
arithmetic-circuit model that proof systems require, and of why the non-linear
layers rather than the matrix products dominate the cost. The construction also
shows how the sumcheck and GKR line of interactive proofs combines with a modern
lookup argument to reach a succinct, publicly verifiable, non-interactive proof.

## Basic Background

### Transformer inference and quantization

The model is a [transformer](../concepts/language-model-pretraining.md) such as
GPT-2: a stack of blocks, each combining matrix multiplication, attention, the
GeLU activation, and layer normalization (Vaswani et al., 2017; Radford et al.,
2019; Ba et al., 2016; Hendrycks and Gimpel, 2016). A proof system operates over a
finite field, so before the computation can be proved its real-valued weights and
activations are quantized, mapped to integers with a shared scale, as in zkCNN
(Liu et al., 2021). Quantization is what lets floating-point addition and
multiplication be approximated by integer arithmetic the circuit can express.

### Zero-knowledge proofs

A [zero-knowledge proof](../concepts/zero-knowledge-proof.md) lets a prover
convince a verifier that a computation on a secret witness was performed correctly
while revealing nothing about the witness, with completeness, soundness, and the
zero-knowledge property (Goldwasser et al., 1985). A public-coin interactive
protocol becomes a single non-interactive proof through the Fiat-Shamir transform,
which derives the verifier's challenges from a hash of the transcript (Fiat and
Shamir, 1986). A succinct proof is small and fast to verify relative to the
computation it certifies.

### Committing to the model

A [cryptographic commitment](../concepts/cryptographic-commitment.md) is a binding,
hiding token published for a value and opened later. zkGPT commits to the weights
with a polynomial commitment, a commitment to the polynomial encoding of the weight
tensors, so the proof is tied to one fixed model and the verifier never sees the
weights themselves. The commitment is what makes "the committed model" a
well-defined object the prover cannot change between queries.

### Proof systems for arithmetic circuits

The computation is expressed as an arithmetic circuit over a finite field. The
sumcheck protocol (Lund et al., 1992) and the GKR protocol for layered circuits
(Goldwasser et al., 2015) prove such circuits with a verifier far cheaper than
re-execution, and a dedicated interactive proof certifies matrix multiplication in
time linear in the matrix size (Thaler, 2013). Operations that resist
arithmetization, range checks and table lookups, are handled by lookup arguments,
which let the prover show that secret values lie in a public table; zkGPT uses the
Lasso lookup argument (Setty et al., 2024).

## Reading guidance

- Abstract and Section 1: the problem and the actors. Note who the prover and
  verifier are (the service provider versus a user or regulator) and exactly what
  each side knows and keeps secret.
- Section 2: the GKR protocol, the machine-learning-friendly circuit, and the Lasso
  lookup protocol, the primitives the construction reuses. Note the quantization
  scheme that maps real numbers to field integers and where rounding enters.
- Section 3: the split into linear and non-linear layers and the two optimizations,
  constraint fusion and circuit squeeze. This is the roadmap for the construction.
- Section 4: the per-layer constraints and the matrix-multiplication proof.
  Attention anchor: the GeLU treatment introduces an approximation the authors call
  z-GeLU as a design choice; note what is being approximated and that the accuracy
  comparison is deferred to Appendix C.
- Section 7: the end-to-end GPT-2 timings and the comparisons to ZKML, Hao et al.,
  and zkLLM. Note which cost each comparison reports, prover time, proof size, or
  communication.
- Section 8: the map of zero-knowledge ML systems, from decision trees and CNNs to
  LLMs, and the separate proof-of-training line.
- Section 9: the discussion and limitations. Attention anchor: the reliance on
  quantization is stated as a limitation; note what it rules out (proving
  floating-point inference directly) and that the authors flag it as shared across
  zero-knowledge ML systems.
- Appendix B: the completeness and soundness argument, reduced to the soundness of
  GKR and Lasso. Note the cases the soundness proof splits the cheating prover into.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [Experimenting with Zero-Knowledge Proofs of Training](https://dl.acm.org/doi/10.1145/3576915.3623202) — proving how a model was trained, the training-time counterpart to proving inference.
- [Zero-Knowledge Proofs of Training for Deep Neural Networks](https://dl.acm.org/doi/abs/10.1145/3658644.3670316) — a later, scaled proof-of-training system for deep networks, the same compliance goal at training time.

</details>

<details>
<summary><h2>Paper Context</h2></summary>

Zero-knowledge proofs for machine learning began with small models and vision.
Verified decision-tree predictions came first (Zhang et al., 2020), followed by a
line on verifiable convolutional-network inference: vCNN compiled a CNN to a
zk-SNARK (Lee et al., 2020), ZEN built an optimizing compiler for zero-knowledge
network inference (Feng et al., 2021), Mystique converted between proof
representations for ML workloads (Weng et al., 2021), and zkCNN designed a
specialized sumcheck-based protocol for convolutions (Liu et al., 2021), later
sharpened with modular sumcheck proofs (Balbás et al., 2023). A separate effort
scaled trustless DNN inference with general-purpose proofs (Kang et al., 2022).
Across these systems the recurring cost is proving the non-arithmetic operations of
the non-linear layers, and most rely on quantization to reach the field at all.

Transformers enlarged the problem. ZKML compiled ML inference into a Plonk-based
proof system and could prove GPT-2, but needed more than an hour per proof (Chen et
al., 2024). Concurrent work pushed on the non-linear layers: one system used digit
decomposition to prove non-linear functions in neural networks (Hao et al., 2024),
zkLLM targeted the attention layer with digit decomposition and a GPU
implementation (Sun et al., 2024), and a further framework gave an extensible
interactive scheme for neural networks (Lu et al., 2024). The interactive,
VOLE-based schemes in this group exchange gigabytes of data between prover and
verifier and do not convert to a non-interactive, publicly downloadable proof.

A neighboring compliance goal is to prove how a model was trained rather than how it
answers, which is harder than proving inference. Several systems study
zero-knowledge proofs of training: an early exploration of the problem (Garg et al.,
2023), a scaled proof-of-training system for deep networks (Abbaszadeh et al.,
2024), a confidential proof of fair tree training (Shamsabadi et al., 2023), and
trustless audits that reveal neither data nor model (Waiwitlikhit et al., 2024).
These target the same auditability aim at training time.

</details>

---
<details>
<summary><h4>References</h4></summary>

Entries read off this paper's bibliography (PDF pages 15-18).

- Abbaszadeh, K., Pappas, C., Katz, J., and Papadopoulos, D. "Zero-Knowledge Proofs of Training for Deep Neural Networks." Cryptology ePrint Archive, 2024.
- Ba, J. L., Kiros, J. R., and Hinton, G. E. "Layer Normalization." arXiv:1607.06450, 2016.
- Balbás, D., Fiore, D., González Vasco, M. I., Robissout, D., and Soriente, C. "Modular Sumcheck Proofs with Applications to Machine Learning and Image Processing." ACM Conference on Computer and Communications Security (CCS), 2023.
- Chen, B.-J., Waiwitlikhit, S., Stoica, I., and Kang, D. "ZKML: An Optimizing System for ML Inference in Zero-Knowledge Proofs." European Conference on Computer Systems (EuroSys), 2024.
- Feng, B., Qin, L., Zhang, Z., Ding, Y., and Chu, S. "ZEN: An Optimizing Compiler for Verifiable, Zero-Knowledge Neural Network Inferences." Cryptology ePrint Archive, 2021.
- Fiat, A., and Shamir, A. "How to Prove Yourself: Practical Solutions to Identification and Signature Problems." Conference on the Theory and Application of Cryptographic Techniques (CRYPTO), 1986.
- Garg, S., Goel, A., Jha, S., Mahloujifar, S., Mahmoody, M., Policharla, G.-V., and Wang, M. "Experimenting with Zero-Knowledge Proofs of Training." ACM Conference on Computer and Communications Security (CCS), 2023.
- Goldwasser, S., Kalai, Y. T., and Rothblum, G. N. "Delegating Computation: Interactive Proofs for Muggles." Journal of the ACM, 62(4):1-64, 2015.
- Goldwasser, S., Micali, S., and Rackoff, C. "The Knowledge Complexity of Interactive Proof-Systems." ACM Symposium on Theory of Computing (STOC), 1985.
- Hao, M., Chen, H., Li, H., Weng, C., Zhang, Y., Yang, H., and Zhang, T. "Scalable Zero-Knowledge Proofs for Non-Linear Functions in Machine Learning." USENIX Security Symposium, 2024.
- Hendrycks, D., and Gimpel, K. "Gaussian Error Linear Units (GELUs)." arXiv:1606.08415, 2016.
- Kang, D., Hashimoto, T., Stoica, I., and Sun, Y. "Scaling up Trustless DNN Inference with Zero-Knowledge Proofs." arXiv:2210.08674, 2022.
- Lee, S., Ko, H., Kim, J., and Oh, H. "vCNN: Verifiable Convolutional Neural Network Based on zk-SNARKs." Cryptology ePrint Archive, 2020.
- Liu, T., Xie, X., and Zhang, Y. "zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy." ACM Conference on Computer and Communications Security (CCS), 2021.
- Lu, T., Wang, H., Qu, W., Wang, Z., He, J., Tao, T., Chen, W., and Zhang, J. "An Efficient and Extensible Zero-Knowledge Proof Framework for Neural Networks." Cryptology ePrint Archive, 2024.
- Lund, C., Fortnow, L., Karloff, H., and Nisan, N. "Algebraic Methods for Interactive Proof Systems." Journal of the ACM, 39(4):859-868, 1992.
- Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I. "Language Models are Unsupervised Multitask Learners." OpenAI blog, 2019.
- Setty, S., Thaler, J., and Wahby, R. "Unlocking the Lookup Singularity with Lasso." Annual International Conference on the Theory and Applications of Cryptographic Techniques (EUROCRYPT), 2024.
- Shamsabadi, A. S., Wyllie, S. C., Franzese, N., Dullerud, N., Gambs, S., Papernot, N., Wang, X., and Weller, A. "Confidential-PROFITT: Confidential Proof of Fair Training of Trees." International Conference on Learning Representations (ICLR), 2023.
- Sun, H., Li, J., and Zhang, H. "zkLLM: Zero Knowledge Proofs for Large Language Models." 2024.
- Thaler, J. "Time-Optimal Interactive Proofs for Circuit Evaluation." Annual Cryptology Conference (CRYPTO), 2013.
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., and Polosukhin, I. "Attention Is All You Need." Advances in Neural Information Processing Systems (NeurIPS), 2017.
- Waiwitlikhit, S., Stoica, I., Sun, Y., Hashimoto, T., and Kang, D. "Trustless Audits without Revealing Data or Models." International Conference on Machine Learning (ICML), 2024.
- Weng, C., Yang, K., Xie, X., Katz, J., and Wang, X. "Mystique: Efficient Conversions for Zero-Knowledge Proofs with Applications to Machine Learning." USENIX Security Symposium, 2021.
- Zhang, J., Fang, Z., Zhang, Y., and Song, D. "Zero Knowledge Proofs for Decision Tree Predictions and Accuracy." ACM Conference on Computer and Communications Security (CCS), 2020.

</details>
