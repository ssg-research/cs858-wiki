---
title: "Safety training (LLM harmlessness)"
type: concept
description: "Training a deployed LLM to refuse a designated set of restricted behaviors; refusal responses, RLHF-for-harmlessness, Constitutional AI / AI feedback, and the narrower input coverage relative to pretraining."
tags:
  - alignment
  - safety
  - llm-safety
---

# Safety training (LLM harmlessness)

## Definition

Safety training is the stage that makes a deployed language model refuse a
designated set of restricted behaviors, such as producing harmful content,
abetting crime, or leaking personally identifiable information. The trained
response is a refusal: a short, characteristic decline. It is implemented by
preference optimization toward harmlessness ([RLHF](rlhf.md)) and by AI feedback
against a written policy (Constitutional AI; Bai et al., 2022), and is often
paired with input and output filtering. Safety training covers a narrower range
of inputs than [pretraining](language-model-pretraining.md) or
[instruction tuning](instruction-tuning.md), which is why a deployed model can
retain a capability while refusing to exercise it on the prompts safety training
anticipated.

## Papers that use this concept

- [Jailbroken: How Does LLM Safety Training Fail?](../papers/wei-2023-jailbroken.md) — the paper's subject; it asks why safety training fails to suppress restricted behavior under adversarial prompts.
- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — argues current safety training is "shallow," changing mostly the first few output tokens, and proposes ways to make it deeper.
- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — reads a harmfulness direction and steers it to suppress harmful outputs, including under an adversarial suffix.

## See also

- [Reinforcement learning from human feedback (RLHF)](rlhf.md)
- [Jailbreak (LLM)](jailbreak.md)
- [Red teaming (language models)](red-teaming.md)

## References

- Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen,
  A., Goldie, A., Mirhoseini, A., McKinnon, C., et al. "Constitutional AI:
  Harmlessness from AI Feedback." arXiv:2212.08073, 2022.
- Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P.,
  Zhang, C., Agarwal, S., Slama, K., Ray, A., et al. "Training Language Models
  to Follow Instructions with Human Feedback." Advances in Neural Information
  Processing Systems (NeurIPS), 35, 2022.
