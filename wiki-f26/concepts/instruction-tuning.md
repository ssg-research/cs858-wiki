---
title: "Instruction tuning"
type: concept
description: "Fine-tuning a pretrained language model to follow natural-language instructions rather than continue text; the instruction-following objective, its supervised and preference-optimization stages."
tags:
  - language-models
  - alignment
---

## [Wiki Home](../README.md)

# Instruction tuning

## Definition

Instruction tuning fine-tunes a pretrained language model so it responds to a
natural-language instruction instead of merely continuing the text. It starts
from supervised fine-tuning on instruction-response demonstrations and is
usually followed by preference optimization
([RLHF](rlhf.md)). The result treats the prompt as a request to satisfy, which
is what makes a base model into an assistant. InstructGPT (Ouyang et al., 2022)
is the canonical recipe. Instruction following is one training objective among
several that a deployed model balances, alongside language modeling and safety.

## Papers that use this concept

- [Jailbroken: How Does LLM Safety Training Fail?](../papers/wei-2023-jailbroken.md) — instruction following is one of the "competing objectives"; attacks such as refusal suppression exploit the model's drive to obey formatting instructions.
- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — analyzes how supervised and preference-based fine-tuning leave safety behavior concentrated in early tokens.
- [What Makes and Breaks Safety Fine-tuning? A Mechanistic Study](../papers/jain-2024-safety-finetuning.md) — takes the instruction-tuned model as the starting point and asks what safety fine-tuning changes on top of it.

## See also

- [Language model pretraining](language-model-pretraining.md)
- [Reinforcement learning from human feedback (RLHF)](rlhf.md)
- [Safety training (LLM harmlessness)](safety-training.md)

## References

- Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P.,
  Zhang, C., Agarwal, S., Slama, K., Ray, A., et al. "Training Language Models
  to Follow Instructions with Human Feedback." Advances in Neural Information
  Processing Systems (NeurIPS), 35, 2022.
