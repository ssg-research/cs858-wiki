---
title: "Safety Alignment Should Be Made More Than Just a Few Tokens Deep"
authors:
  - Qi, Xiangyu
  - Panda, Ashwinee
  - Lyu, Kaifeng
  - Ma, Xiao
  - Roy, Subhrajit
  - Beirami, Ahmad
  - Mittal, Prateek
  - Henderson, Peter
year: 2024
section: "Safety Alignment and Guardrails"
primary: true
arxiv: "2406.05946"
tags:
  - alignment
  - llm-safety
  - safety
  - jailbreak
  - defense
---

[Home page](../README.md)

# Safety Alignment Should Be Made More Than Just a Few Tokens Deep

## High-level overview

The safety alignment of current large language models is brittle: simple attacks,
and even well-intentioned fine-tuning, can return an aligned model to harmful
behavior. This paper argues that a single underlying property explains much of
that brittleness, which it names **shallow safety alignment**. A shallowly
aligned model adapts its generative distribution over only the first few output
tokens, enough to start a response with a refusal prefix such as "I cannot
fulfill your request." Past those opening tokens, its token-by-token behavior is
largely that of the unaligned base model it started from. Safety, in such a
model, is a thin shell over the first few tokens.

Through case studies on open models such as Llama-2 (Touvron et al., 2023) and
Gemma (Gemma Team, 2024), the paper gives evidence that current alignment is
shallow in this sense, measuring per-token [KL divergence](../concepts/kl-divergence.md)
between an aligned model and its base model and finding the change concentrated in
the earliest token positions. It then uses this one notion to account for a
cluster of separately discovered exploits: adversarial-suffix attacks, prefilling
attacks, decoding-parameter exploits, and fine-tuning attacks all turn out to
work by getting past, or rewriting, those first few tokens.

On the constructive side, the paper introduces two prototype mitigations that
push alignment deeper. A data-augmentation scheme trains the model to recover,
returning to a refusal, even after a harmful response has already begun, so that
suppression of harmful content extends beyond the opening tokens. A token-wise
constrained fine-tuning objective holds the early-token distribution close to the
aligned model during downstream fine-tuning. At an abstract level, deepening the
alignment improves robustness to several inference-time exploits, and the
constraint keeps safety durable through both adversarial and benign fine-tuning,
at utility comparable to standard fine-tuning.

**Threat Model:** The paper is defense-side, but it characterizes a family of
adversaries against a [safety-aligned](../concepts/safety-training.md) model. The
adversary seeks to elicit restricted (harmful) content; in the fine-tuning case
the "adversary" may be a benign developer whose ordinary fine-tuning degrades
safety as a side effect. Capability spans the exploits the paper unifies:
inference-time control over [decoding](../concepts/decoding-strategies.md)
(prefilling the first response tokens, or varying temperature, top-k, and top-p),
input-only access (optimizing an adversarial suffix appended to a prompt), and
post-deployment fine-tuning access (a few gradient steps on a small dataset,
through an open model or a hosted fine-tuning interface), including with benign
fine-tuning data. The defender claims that alignment whose effect reaches beyond
the first few tokens, and a fine-tuning objective that constrains early-token
drift, resist these exploits better than standard alignment at comparable
utility. The defenses are presented as prototypes, not as a guarantee against all
adaptive attacks.

## Why read this

A weakness shared across aligned LLMs turns out to have a measurable cause and a
tractable fix. The paper reframes safety alignment from cataloguing individual
attacks to diagnosing why alignment is brittle, then deepening it directly. Its
constrained fine-tuning objective is, short of re-running a full alignment
pipeline, among the most practical known ways to keep a model's safety from
unraveling under later fine-tuning.

## Basic Background

### Autoregressive generation and decoding

A language model is [pretrained](../concepts/language-model-pretraining.md) to
predict the next token over a large corpus, producing a base model with broad
capabilities. Turning the resulting next-token distributions into text is the job
of a [decoding strategy](../concepts/decoding-strategies.md): greedy decoding, or
sampling controlled by temperature, top-k, and top-p. Prefilling forces the
response to begin with a chosen string, so generation continues from those tokens
rather than the model's own first choice. These decoding controls are set at
inference and do not change the weights.

### Safety alignment of LLMs

A base model becomes an assistant through
[instruction tuning](../concepts/instruction-tuning.md): supervised fine-tuning on
demonstrations, usually followed by preference optimization such as
[RLHF](../concepts/rlhf.md) or
[direct preference optimization](../concepts/direct-preference-optimization.md).
Both carry a KL penalty that keeps the aligned policy close to the base model.
[Safety training](../concepts/safety-training.md) is the part of this process that
makes the model refuse a designated set of restricted behaviors, producing the
characteristic refusal response. A [jailbreak](../concepts/jailbreak.md) is a
prompt or procedure that routes around that refusal to surface a capability the
model already holds.

### Measuring how much alignment changed the model

Because alignment adjusts a base model rather than replacing it, "how much did it
change" is a quantitative question. The [KL divergence](../concepts/kl-divergence.md)
between the aligned and base models' next-token distributions, computed per token
position, measures where along a response the two models disagree. The per-token
cross-entropy (next-token) loss and the
[gradient](../concepts/stochastic-gradient-descent.md) norm at each position give
a parallel view during fine-tuning: which token positions carry the largest loss
and drive the largest weight updates.

<details>
<summary><h2>Paper Context</h2></summary>

By 2024, aligned LLMs had been shown vulnerable to a varied and growing set of
exploits, mostly studied in isolation. Adversarial-suffix attacks optimize a
string appended to a prompt so the model opens with an affirmative response (Zou
et al., 2023). Prefilling forces a non-refusal opening directly. Decoding-parameter
exploits sample repeatedly under varied temperature and top-k or top-p until a
harmful completion appears (Huang et al., 2023). Fine-tuning attacks strip
alignment with a few gradient steps on a small harmful dataset (Qi et al., 2023;
Zhan et al., 2023), and even benign fine-tuning can cause safety to regress (Qi
et al., 2023; He et al., 2024).

A parallel line questioned how deep alignment really runs. The Superficial
Alignment Hypothesis held that alignment mainly adjusts the style and format of
interaction and can be learned from very few examples (Zhou et al., 2023). Related
work observed that the token-level differences alignment introduces are
concentrated early in a sequence and fade as generation continues (Lin et al.,
2024; Zhang and Wu, 2024), an asymmetry some had begun to exploit to build attacks
(Zhao et al., 2024).

Two defense traditions framed the response. In adversarial machine learning, the
canonical defense is to train against the attack:
[adversarial training](../concepts/adversarial-training.md) augments training with
worst-case perturbed inputs so the model learns to resist them (Goodfellow et al.,
2015), formalized as a saddle-point problem
([Towards Deep Learning Models Resistant to Adversarial Attacks](madry-2018-pgd.md);
Madry et al., 2018). In LLM deployment, safety was often handled at the system
boundary, with input and output classifiers screening prompts and responses (Inan
et al., 2023). The alignment itself came from the supervised and
preference-optimization stack, RLHF (Ouyang et al., 2022) and DPO (Rafailov et
al., 2023), whose KL penalty keeps the aligned policy near the base model.

</details>

## Reading guidance

- Section 2 and Figure 1: the per-token KL divergence between aligned and base
  models on harmful inputs, the central measurement behind the "shallow" claim.
- Table 1: what the harmfulness rate of an unaligned base model does once a
  refusal prefix is prefilled into its decoding.
- Section 2.3.1: the inference-stage exploits (prefilling, adversarial suffix,
  random sampling over decoding parameters) recast under one lens.
- Section 2.3.2 and Figure 3: per-token loss, gradient norm, and KL during a
  fine-tuning attack, and where along the response the change concentrates.
- Section 3: the data-augmentation approach ("safety recovery examples"). Note how
  this training scheme relates to defenses you have seen for classifiers, and what
  about the safety setting makes the construction different.
- Section 4 and Table 3: the token-wise constrained fine-tuning objective and its
  results against fine-tuning attacks and on benign downstream tasks. Note which
  token positions receive the strong constraint, and the justification given for
  that choice.
- Section 5: related work, placing the paper among the superficial-alignment and
  token-dynamics lines.

<details>
<summary><h2>Supplementary readings</h2></summary>

- [Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674) — the system-boundary approach to safety, screening prompts and responses with a separate classifier rather than changing the model's alignment.
- [SecAlign: Defending Against Prompt Injection with Preference Optimization](https://arxiv.org/abs/2410.05451) — a preference-optimization defense that hardens the model itself, a useful contrast to deepening safety alignment.

</details>

[Home page](../README.md)

<details>
<summary><h2>References</h2></summary>

- Goodfellow, I. J., Shlens, J., and Szegedy, C. "Explaining and Harnessing
  Adversarial Examples." International Conference on Learning Representations
  (ICLR), 2015.
- Gemma Team, Mesnard, T., Hardin, C., Dadashi, R., Bhupatiraju, S., Pathak, S.,
  Sifre, L., Rivière, M., Kale, M. S., Love, J., et al. "Gemma: Open Models Based
  on Gemini Research and Technology." arXiv:2403.08295, 2024.
- He, L., Xia, M., and Henderson, P. "What's in Your 'Safe' Data?: Identifying
  Benign Data that Breaks Safety." arXiv:2404.01099, 2024.
- Huang, Y., Gupta, S., Xia, M., Li, K., and Chen, D. "Catastrophic Jailbreak of
  Open-source LLMs via Exploiting Generation." arXiv:2310.06987, 2023.
- Inan, H., Upasani, K., Chi, J., Rungta, R., Iyer, K., Mao, Y., Tontchev, M.,
  Hu, Q., Fuller, B., Testuggine, D., et al. "Llama Guard: LLM-based Input-Output
  Safeguard for Human-AI Conversations." arXiv:2312.06674, 2023.
- Lin, B. Y., Ravichander, A., Lu, X., Dziri, N., Sclar, M., Chandu, K.,
  Bhagavatula, C., and Choi, Y. "The Unlocking Spell on Base LLMs: Rethinking
  Alignment via In-Context Learning." International Conference on Learning
  Representations (ICLR), 2024.
- Madry, A., Makelov, A., Schmidt, L., Tsipras, D., and Vladu, A. "Towards Deep
  Learning Models Resistant to Adversarial Attacks." International Conference on
  Learning Representations (ICLR), 2018. arXiv:1706.06083.
- Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang,
  C., Agarwal, S., Slama, K., Ray, A., et al. "Training Language Models to Follow
  Instructions with Human Feedback." Advances in Neural Information Processing
  Systems (NeurIPS), 35, 2022.
- Qi, X., Zeng, Y., Xie, T., Chen, P.-Y., Jia, R., Mittal, P., and Henderson, P.
  "Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not
  Intend To!" arXiv:2310.03693, 2023.
- Rafailov, R., Sharma, A., Mitchell, E., Manning, C. D., Ermon, S., and Finn, C.
  "Direct Preference Optimization: Your Language Model is Secretly a Reward
  Model." Advances in Neural Information Processing Systems (NeurIPS), 36, 2023.
- Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y.,
  Bashlykov, N., Batra, S., Bhargava, P., Bhosale, S., et al. "Llama 2: Open
  Foundation and Fine-Tuned Chat Models." arXiv:2307.09288, 2023.
- Zhan, Q., Fang, R., Bindu, R., Gupta, A., Hashimoto, T., and Kang, D. "Removing
  RLHF Protections in GPT-4 via Fine-tuning." arXiv:2311.05553, 2023.
- Zhang, X. and Wu, J. "Dissecting Learning and Forgetting in Language Model
  Finetuning." International Conference on Learning Representations (ICLR), 2024.
- Zhao, X., Yang, X., Pang, T., Du, C., Li, L., Wang, Y.-X., and Wang, W. Y.
  "Weak-to-Strong Jailbreaking on Large Language Models." arXiv:2401.17256, 2024.
- Zhou, C., Liu, P., Xu, P., Iyer, S., Sun, J., Mao, Y., Ma, X., Efrat, A., Yu,
  P., Yu, L., et al. "LIMA: Less Is More for Alignment." Advances in Neural
  Information Processing Systems (NeurIPS), 36, 2023.
- Zou, A., Wang, Z., Kolter, J. Z., and Fredrikson, M. "Universal and
  Transferable Adversarial Attacks on Aligned Language Models." arXiv:2307.15043,
  2023.

</details>
