---
title: "Language model pretraining"
type: concept
description: "Autoregressive next-token pretraining of a language model on a large corpus; the pretraining objective, the pretraining distribution, and the base model that exists before any alignment."
tags:
  - language-models
  - pretraining
---

# Language model pretraining

## Definition

A large language model is first trained to predict the next token over a large,
diverse text corpus, an objective called autoregressive language modeling.
Maximizing the likelihood of natural text produces a base model with broad
capabilities and an implicit sense of which continuations are probable, its
pretraining distribution. Generation decodes one token at a time from this
distribution, so a continuation that would be improbable in natural text is also
improbable for the model. The capabilities a base model picks up in pretraining,
including reading uncommon formats and encodings, are far broader than any later
alignment stage revisits. The canonical instance is GPT-3 (Brown et al., 2020).

## Papers that use this concept

- [Jailbroken: How Does LLM Safety Training Fail?](../papers/wei-2023-jailbroken.md) — both proposed failure modes are framed against the pretraining objective and the breadth of the pretraining distribution.

## See also

- [Instruction tuning](instruction-tuning.md)
- [Reinforcement learning from human feedback (RLHF)](rlhf.md)

## References

- Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P.,
  Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. "Language Models
  are Few-Shot Learners." Advances in Neural Information Processing Systems
  (NeurIPS), 33:1877-1901, 2020.
