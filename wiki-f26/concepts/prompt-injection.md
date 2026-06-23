---
title: "Prompt injection"
type: concept
description: "Adversarial instructions placed in a prompt or in content the model ingests that override the intended task; direct vs indirect injection, payload splitting, and the overlap with jailbreaks."
tags:
  - prompt-injection
  - llm-safety
  - attack
---

[Home page](../README.md)

# Prompt injection

## Definition

Prompt injection supplies instructions, inside the user prompt or inside
external content the model reads, that override the application's intended
behavior. Direct injection comes from the user; indirect injection hides
instructions in retrieved documents or tool output the model ingests
([Greshake et al., 2023](../papers/greshake-2023-indirect-prompt-injection.md)).
Prompt injection overlaps with the [jailbreak](jailbreak.md):
both steer the model through its input, but injection emphasizes hijacking a
task or application, while a jailbreak emphasizes bypassing a safety refusal.
Construction techniques such as payload splitting, which breaks a sensitive
phrase into innocuous-looking substrings, appear on both sides (Kang et al.,
2023).

## Papers that use this concept

- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](../papers/greshake-2023-indirect-prompt-injection.md) — introduces and names indirect prompt injection, where retrieved content carries the instructions.
- [Jailbroken: How Does LLM Safety Training Fail?](../papers/wei-2023-jailbroken.md) — its "prefix injection" and payload-splitting attacks draw on prompt-injection techniques.
- [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](../papers/zou-2024-poisonedrag.md) — contrasted against prompt injection: it injects misleading content treated as a retrieved fact, not instructions, and argues this is both more effective and harder to detect for RAG.

## See also

- [Jailbreak (LLM)](jailbreak.md)
- [Safety training (LLM harmlessness)](safety-training.md)

[Home page](../README.md)

## References

- Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., and Fritz, M.
  "Not what you've signed up for: Compromising Real-World LLM-Integrated
  Applications with Indirect Prompt Injection." arXiv:2302.12173, 2023.
- Kang, D., Li, X., Stoica, I., Guestrin, C., Zaharia, M., and Hashimoto, T.
  "Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security
  Attacks." arXiv:2302.05733, 2023.
