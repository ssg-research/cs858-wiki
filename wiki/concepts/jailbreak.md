---
title: "Jailbreak (LLM)"
type: concept
description: "A prompt engineered to elicit behavior a safety-trained LLM was trained to refuse; restricted behavior, refusal, input-agnostic and human-readable construction, and the distinction from adversarial examples that cause misclassification."
tags:
  - jailbreak
  - llm-safety
  - attack
---

# Jailbreak (LLM)

## Definition

A jailbreak is a prompt crafted to make a [safety-trained](safety-training.md)
language model produce a restricted behavior it was trained to refuse, such as
harmful instructions or leaked personal data. The model already holds the
underlying capability; the jailbreak routes around the refusal rather than
teaching the model anything new. A jailbreak differs from an
[adversarial example](adversarial-examples.md), which perturbs an input to cause
a misclassification: a jailbreak elicits an unsafe capability, and the prompts
are usually human-readable and input-agnostic. Early jailbreaks spread
informally after ChatGPT's release, including role-play personas such as "DAN"
(walkerspider, 2022; Burgess, 2023).

## Papers that use this concept

- [Jailbroken: How Does LLM Safety Training Fail?](../papers/wei-2023-jailbroken.md) — proposes two failure modes of safety training and uses them as principles for constructing jailbreaks.
- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — explains prefilling, adversarial-suffix, and decoding-parameter jailbreaks as ways of getting past a shallow refusal prefix.
- [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](../papers/zou-2024-poisonedrag.md) — names jailbreaking as orthogonal: it steers a RAG answer through corrupted retrieved content rather than by bypassing a safety refusal.
- [Representation Engineering: A Top-Down Approach to AI Transparency](../papers/zou-2023-representation-engineering.md) — tests whether its internal harmfulness direction stays consistent when the model is jailbroken by manual prompts or adversarial suffixes.

## See also

- [Safety training (LLM harmlessness)](safety-training.md)
- [Prompt injection](prompt-injection.md)
- [Red teaming (language models)](red-teaming.md)

## References

- walkerspider. "DAN is my new friend." Reddit r/ChatGPT, 2022.
- Burgess, M. "The Hacking of ChatGPT is Just Getting Started." Wired, 2023.
