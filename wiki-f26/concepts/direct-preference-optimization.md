---
title: "Direct preference optimization (DPO)"
type: concept
description: "A preference-based alignment method that fine-tunes a language model directly on pairwise preference data with a classification-style loss, without a separate reward model or reinforcement-learning loop; an alternative to the reward-model-plus-PPO pipeline of RLHF."
tags:
  - alignment
  - rlhf
---

# Direct preference optimization (DPO)

## Definition

Direct preference optimization aligns a language model to pairwise human
preferences, a preferred response versus a dispreferred one, without training a
separate reward model or running a reinforcement-learning loop (Rafailov et al.,
2023). It rewrites the KL-regularized reward-maximization objective behind
[RLHF](rlhf.md) so that the optimal policy can be fit directly with a binary
classification loss over preference pairs. The model's own log-probabilities,
measured relative to a frozen reference model, stand in for an implicit reward,
and a [KL term](kl-divergence.md) keeps the policy close to that reference.

DPO targets the same goal as RLHF, a policy that favors human-preferred outputs
while staying near a reference model, but reaches it with ordinary supervised
optimization rather than online sampling and reward estimation. RLHF and DPO are
the two dominant preference-optimization recipes behind instruction following and
safety behavior in deployed models.

## Papers that use this concept

- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — names DPO as part of the standard alignment stack; its KL-regularized preference formulation is one basis for the paper's token-wise constrained fine-tuning objective.

## See also

- [Reinforcement learning from human feedback (RLHF)](rlhf.md)
- [Instruction tuning](instruction-tuning.md)
- [Safety training (LLM harmlessness)](safety-training.md)

## References

- Rafailov, R., Sharma, A., Mitchell, E., Manning, C. D., Ermon, S., and Finn, C.
  "Direct Preference Optimization: Your Language Model is Secretly a Reward
  Model." Advances in Neural Information Processing Systems (NeurIPS), 36, 2023.
