---
title: "Reinforcement learning from human feedback (RLHF)"
type: concept
description: "Aligning a language model to human preferences via a learned reward model and policy optimization with a KL penalty toward the base model; the dominant method behind both instruction following and safety behavior."
tags:
  - alignment
  - rlhf
---

# Reinforcement learning from human feedback (RLHF)

## Definition

RLHF aligns a language model with human preferences. Annotators rank model
outputs, a reward model is trained to predict those rankings, and the policy
(the language model) is then optimized to maximize predicted reward (Christiano
et al., 2017; Ouyang et al., 2022). The optimization carries a
KL-divergence penalty that keeps the policy close to the base model and often a
term retaining the pretraining loss. RLHF underlies both instruction following
and safety behavior in models such as InstructGPT and the helpful-and-harmless
assistant (Bai et al., 2022). Because the base model and pretraining objective
stay in the loss, alignment adjusts the base model rather than replacing it.

## Papers that use this concept

- [Jailbroken: How Does LLM Safety Training Fail?](../papers/wei-2023-jailbroken.md) — the persistence of the pretraining objective inside the RLHF loss is central to its argument that scaling will not remove "competing objectives."
- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — uses the KL-penalty view of alignment to argue that current safety alignment concentrates in the first few output tokens.
- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — targets honesty and harmlessness in RLHF-aligned models and steers them at inference rather than through the alignment loss.

## See also

- [Instruction tuning](instruction-tuning.md)
- [Safety training (LLM harmlessness)](safety-training.md)
- [Language model pretraining](language-model-pretraining.md)

## References

- Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., and Amodei, D.
  "Deep Reinforcement Learning from Human Preferences." Advances in Neural
  Information Processing Systems (NeurIPS), 30, 2017.
- Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P.,
  Zhang, C., Agarwal, S., Slama, K., Ray, A., et al. "Training Language Models
  to Follow Instructions with Human Feedback." Advances in Neural Information
  Processing Systems (NeurIPS), 35, 2022.
- Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N., Drain,
  D., Fort, S., Ganguli, D., Henighan, T., et al. "Training a Helpful and
  Harmless Assistant with Reinforcement Learning from Human Feedback."
  arXiv:2204.05862, 2022.
