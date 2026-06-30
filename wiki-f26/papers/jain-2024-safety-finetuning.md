---
title: "What Makes and Breaks Safety Fine-tuning? A Mechanistic Study"
authors:
  - Jain, Samyak
  - Lubana, Ekdeep Singh
  - Oksuz, Kemal
  - Joy, Tom
  - Torr, Philip H. S.
  - Sanyal, Amartya
  - Dokania, Puneet K.
year: 2024
section: "Mechanistic Interpretability for AI safety"
primary: true
arxiv: "2407.10264"
tags:
  - interpretability
  - llm-safety
  - safety
  - alignment
  - jailbreak
---

## [Wiki Home](../README.md)

# What Makes and Breaks Safety Fine-tuning? A Mechanistic Study

## High-level overview

Safety fine-tuning aligns an instruction-tuned language model to refuse unsafe
requests, yet jailbreaks and adversarial inputs keep eliciting the content it
was trained to withhold. This paper asks two mechanistic questions: what does
safety fine-tuning change inside the model, and how do those inputs bypass the
change. To study both under controlled conditions, the authors build a synthetic
data-generating framework in which an input is a task (an *operator*, such as
"design") applied to a concept (an *operand*, such as "cycle" versus "bomb"),
with the surrounding text drawn from a probabilistic context-free grammar. The
design makes safety a property of the combination rather than of any token alone.
They train small transformers on this setup and corroborate the findings on
Llama-2 and Llama-3 chat models.

Three safety fine-tuning protocols are compared: supervised safety fine-tuning
(SSFT), direct preference optimization (DPO), and machine unlearning. The
headline is that safety fine-tuning makes a small, specialized change. It
minimally transforms the MLP weights so that unsafe-input activations are routed
into a direction the rest of the network barely reads, which separates safe and
unsafe inputs into distinct activation clusters and implements the model's
learned refusal. Stronger protocols (DPO and unlearning) push the clusters
farther apart and lower the model's local sensitivity on unsafe inputs.

The same mechanism accounts for the failures. Jailbreaks built on the taxonomy
of [Wei et al. (2023)](wei-2023-jailbroken.md), competing objectives and
mismatched generalization, and white-box attacks that optimize appended
embeddings, produce activations resembling those of safe inputs. The safety
transformation is therefore not triggered, and the model processes an unsafe
request as if it were safe. The result echoes a broader finding that safety
fine-tuning alters a model only minimally.

**Threat Model:** This is a mechanistic study that spans a defender and an
adversary. The defender is the model provider, which applies safety fine-tuning
(SSFT, DPO, or unlearning) after instruction tuning so the model refuses inputs
it deems unsafe; the claim under study is that refusal is implemented by a
minimal transformation of the MLP weights that clusters unsafe-input activations
apart from safe ones. The adversary supplies inputs that recover the refused
behavior: jailbreaks phrased as competing objectives or mismatched
generalization, which are human-readable prompts in the input space, and
white-box continuous-embedding attacks that optimize appended soft-token
embeddings against the model's gradients, in the manner of
[ℓp adversarial examples](../concepts/adversarial-examples.md). The analysis
itself is [white-box](../concepts/white-box-black-box.md) throughout: it reads
activations, weights, and gradients at every layer, on the synthetic models and
on Llama-2/3 chat. The adversary's leverage is that evasion needs only
activations that resemble safe inputs, never a direct defeat of the weights.

## Why read this

<!-- instructor: confirm -->
This paper gives a concrete, testable account of what safety fine-tuning changes
inside a language model, a small MLP-weight transformation that sorts inputs by
safety, and shows that the same mechanism explains why jailbreaks and adversarial
inputs evade it. The synthetic data framework, corroborated on Llama-2 and
Llama-3, is a clean template for a mechanistic claim that transfers from
controlled models to deployed ones.

## Basic Background

### The LLM training pipeline

A modern assistant is built in stages. A model is first
[pretrained](../concepts/language-model-pretraining.md) on a large corpus to
predict the next token, then
[instruction-tuned](../concepts/instruction-tuning.md) to follow natural-language
instructions, and finally given [safety training](../concepts/safety-training.md)
so it refuses a designated set of restricted requests. This paper analyzes what
that last stage changes relative to the instruction-tuned model it starts from.

### Safety fine-tuning protocols

Safety training is realized through several objectives. Supervised safety
fine-tuning trains on labeled safe and refusal responses, the supervised special
case of [instruction tuning](../concepts/instruction-tuning.md) (Ouyang et al.,
2022). [RLHF](../concepts/rlhf.md) optimizes a policy against a learned reward
model (Christiano et al., 2017; Ouyang et al., 2022), while
[direct preference optimization](../concepts/direct-preference-optimization.md)
fits the same preference data with a classification-style loss and no separate
reward model (Rafailov et al., 2023).
[Machine unlearning](../concepts/machine-unlearning.md) instead removes the
influence of unsafe responses from an already-trained model (Liu et al., 2024).

### Jailbreaks and adversarial inputs

A [jailbreak](../concepts/jailbreak.md) is a prompt that routes around an
LLM's refusal. The taxonomy of
[Wei et al. (2023)](wei-2023-jailbroken.md) attributes such failures to two
causes: competing objectives, where the model is asked to satisfy a safe and an
unsafe goal at once, and mismatched generalization, where an input falls outside
the narrow distribution covered by safety training. Distinct from these are
[adversarial examples](../concepts/adversarial-examples.md), small input
perturbations that change a model's output; in the
[white-box](../concepts/white-box-black-box.md) setting an attacker optimizes
them against the model's gradients
([projected gradient descent](../concepts/projected-gradient-descent.md);
[Madry et al., 2018](madry-2018-pgd.md)), and the same idea extends to optimizing
continuous embeddings appended to an LLM's input (Carlini et al., 2023).

### Mechanistic interpretability and linear structure

[Mechanistic interpretability](../concepts/mechanistic-interpretability.md) seeks
to explain a network's behavior in terms of its internal components rather than
its input-output map. One recurring premise is the
[linear representation hypothesis](../concepts/linear-representation-hypothesis.md),
that high-level concepts are encoded as linear directions in activation space. A
standard tool for inspecting a weight matrix is the
[singular value decomposition](../concepts/singular-value-decomposition.md), which
yields its four fundamental subspaces (column space, row space, and the two null
spaces); a vector in a matrix's null space is mapped to zero by it. This is the
linear-algebra vocabulary the paper's analysis assumes.

## Reading guidance

- Section 3 and Figures 1-2: the synthetic data-generating process (operators and
  operands, PCFG-sampled text, safety as a property of the combination) and how
  the input types are built: jailbreaks via competing objectives (JB-CO-Task,
  JB-CO-Text), mismatched generalization (JB-MisGen), and continuous-embedding
  attacks (Adv). Note the mapping back onto the jailbreak taxonomy.
- Section 4.1 and Figure 3: the activation-clustering measure and how separation
  between safe and unsafe clusters grows with stronger protocols and with depth;
  the bottom row repeats the measurement on Llama models.
- Section 4.2 and Figures 4-5: the parameter-space analysis of the change
  introduced by safety fine-tuning, framed through the fundamental subspaces.
  Attention anchor: note how "minimal" the transformation is taken to be, and
  exactly what is measured to support the claim that it is "specialized for unsafe
  samples."
- Section 4.3 and Figure 6: local Lipschitzness as a per-sample sensitivity
  probe, and how it moves in opposite directions for safe versus unsafe inputs.
- The "interventions via linear connectivity" paragraph at the end of Section
  4.2: the one interventional test, interpolating and extrapolating along the
  fitted transformation. Note what extrapolation beyond the fine-tuned model
  does.
- Section 5 and Figure 7: jailbreak and adversarial inputs re-run through the same
  feature-, function-, and parameter-space analyses. Attention anchor: the
  analysis keeps only successful attacks; note what that selection does to the
  comparison.
- Appendix B: the natural-language instantiation on Llama and the correspondence
  between synthetic inputs and real prompts. Note how much of the evidence is
  synthetic versus measured on a deployed model.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717) — locates refusal in a single activation direction; the paper's interpolation experiments relate directly to this single-direction account.
- [Improving Alignment and Robustness with Circuit Breakers](https://arxiv.org/abs/2406.04313) — a representation-level defense that remaps harmful internal states to resist jailbreaks and adversarial inputs, a constructive counterpart to this paper's diagnosis of how safety fine-tuning is bypassed.

</details>

<details>
<summary><h2>Paper Context</h2></summary>

By 2024, safety fine-tuning was the standard gate before a model's release, but
its robustness was unsettled. Jailbreaks reliably recovered restricted behavior:
the taxonomy of competing objectives and mismatched generalization organized the
phenomenon (Wei et al., 2023), and automated procedures produced transferable
attack strings (Zou et al., 2023), black-box attacks in few queries (Chao et al.,
2023), and adaptive attacks on aligned models (Andriushchenko et al., 2024).
Continuous-embedding and adversarial-input attacks defeated alignment under
white-box access (Carlini et al., 2023).

A parallel line found that fine-tuning changes a model only slightly while still
moving its behavior. Fine-tuning an aligned model could compromise its safety
even without intent to (Qi et al., 2023), catastrophic forgetting could be cast
as implicit inference (Kotha et al., 2023), and safety alignment proved brittle
to pruning and low-rank edits (Wei et al., 2024). Mechanistic studies of
fine-tuning found that it tends to enhance mechanisms already present in the base
model rather than install new ones (Jain et al., 2023b; Prakash et al., 2024),
including a case study on DPO and toxicity (Lee et al., 2024), and refusal itself
was localized to a single direction in activation space (Arditi et al., 2024).

Synthetic, controlled data had meanwhile become a workbench for mechanistic
analysis of transformers. Probabilistic context-free grammars served as a
tractable model of language for studying what transformers learn (Allen-Zhu and
Li, 2023; Hahn and Goyal, 2023), and bijective-map and group-operation tasks
exposed learned algorithms directly (Ramesh et al., 2023; Chughtai et al., 2023),
all read through the residual-stream view of transformer computation (Elhage et
al., 2021). What had not been done was to connect the minimal-change observations
to the robustness failures in a single mechanistic account.

</details>

<details>
<summary><h4>References</h4></summary>

- Allen-Zhu, Z. and Li, Y. "Physics of Language Models: Part 1, Context-Free
  Grammar." arXiv:2305.13673, 2023.
- Andriushchenko, M., Croce, F., and Flammarion, N. "Jailbreaking Leading
  Safety-Aligned LLMs with Simple Adaptive Attacks." arXiv:2404.02151, 2024.
- Arditi, A., Obeso, O., Syed, A., Paleka, D., Rimsky, N., Gurnee, W., and Nanda,
  N. "Refusal in Language Models Is Mediated by a Single Direction."
  arXiv:2406.11717, 2024.
- Carlini, N., Nasr, M., Choquette-Choo, C. A., Jagielski, M., Gao, I., Awadalla,
  A., Koh, P. W., Ippolito, D., Lee, K., Tramèr, F., et al. "Are Aligned Neural
  Networks Adversarially Aligned?" arXiv:2306.15447, 2023.
- Chao, P., Robey, A., Dobriban, E., Hassani, H., Pappas, G. J., and Wong, E.
  "Jailbreaking Black Box Large Language Models in Twenty Queries." 2023.
- Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., and Amodei, D.
  "Deep Reinforcement Learning from Human Preferences." Advances in Neural
  Information Processing Systems (NeurIPS), 30, 2017.
- Chughtai, B., Chan, L., and Nanda, N. "A Toy Model of Universality: Reverse
  Engineering How Networks Learn Group Operations." International Conference on
  Machine Learning (ICML), 2023.
- Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., Askell,
  A., Bai, Y., Chen, A., Conerly, T., et al. "A Mathematical Framework for
  Transformer Circuits." Transformer Circuits Thread, 2021.
- Hahn, M. and Goyal, N. "A Theory of Emergent In-Context Learning as Implicit
  Structure Induction." arXiv:2303.07971, 2023.
- Jain, S., Kirk, R., Lubana, E. S., Dick, R. P., Tanaka, H., Grefenstette, E.,
  Rocktäschel, T., and Krueger, D. S. "Mechanistically Analyzing the Effects of
  Fine-tuning on Procedurally Defined Tasks." arXiv:2311.12786, 2023b.
- Kotha, S., Springer, J. M., and Raghunathan, A. "Understanding Catastrophic
  Forgetting in Language Models via Implicit Inference." arXiv:2309.10105, 2023.
- Lee, A., Bai, X., Pres, I., Wattenberg, M., Kummerfeld, J. K., and Mihalcea, R.
  "A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and
  Toxicity." 2024.
- Liu, S., Yao, Y., Jia, J., Casper, S., Baracaldo, N., Hase, P., Xu, X., Yao,
  Y., Li, H., Varshney, K. R., et al. "Rethinking Machine Unlearning for Large
  Language Models." arXiv:2402.08787, 2024.
- Madry, A., Makelov, A., Schmidt, L., Tsipras, D., and Vladu, A. "Towards Deep
  Learning Models Resistant to Adversarial Attacks." International Conference on
  Learning Representations (ICLR), 2018.
- Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang,
  C., Agarwal, S., Slama, K., Ray, A., et al. "Training Language Models to Follow
  Instructions with Human Feedback." Advances in Neural Information Processing
  Systems (NeurIPS), 35, 2022.
- Prakash, N., Shaham, T. R., Haklay, T., Belinkov, Y., and Bau, D. "Fine-tuning
  Enhances Existing Mechanisms: A Case Study on Entity Tracking." arXiv:2402.14811,
  2024.
- Qi, X., Zeng, Y., Xie, T., Chen, P.-Y., Jia, R., Mittal, P., and Henderson, P.
  "Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not
  Intend To!" arXiv:2310.03693, 2023.
- Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., and Finn, C.
  "Direct Preference Optimization: Your Language Model Is Secretly a Reward
  Model." arXiv:2305.18290, 2023.
- Ramesh, R., Khona, M., Dick, R. P., Tanaka, H., and Lubana, E. S. "How Capable
  Can a Transformer Become? A Study on Synthetic, Interpretable Tasks."
  arXiv:2311.12997, 2023.
- Wei, A., Haghtalab, N., and Steinhardt, J. "Jailbroken: How Does LLM Safety
  Training Fail?" Advances in Neural Information Processing Systems (NeurIPS),
  2023.
- Wei, B., Huang, K., Huang, Y., Xie, T., Qi, X., Xia, M., Mittal, P., Wang, M.,
  and Henderson, P. "Assessing the Brittleness of Safety Alignment via Pruning
  and Low-Rank Modifications." arXiv:2402.05162, 2024.
- Zou, A., Wang, Z., Kolter, J. Z., and Fredrikson, M. "Universal and
  Transferable Adversarial Attacks on Aligned Language Models." arXiv:2307.15043,
  2023.

</details>
