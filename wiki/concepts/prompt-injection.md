---
title: "Prompt injection"
type: concept
description: "Adversarial instructions placed in a prompt or in content the model ingests that override the intended task; direct vs indirect injection, payload splitting, and the overlap with jailbreaks."
tags:
  - prompt-injection
  - llm-safety
  - attack
---

# Prompt injection

## Definition

Prompt injection supplies instructions, inside the user prompt or inside
external content the model reads, that override the application's intended
behavior. Direct injection comes from the user; indirect injection hides
instructions in retrieved documents or tool output the model ingests (Greshake
et al., 2023). Prompt injection overlaps with the [jailbreak](jailbreak.md):
both steer the model through its input, but injection emphasizes hijacking a
task or application, while a jailbreak emphasizes bypassing a safety refusal.
Construction techniques such as payload splitting, which breaks a sensitive
phrase into innocuous-looking substrings, appear on both sides (Kang et al.,
2023).

## Papers that use this concept

- [Jailbroken: How Does LLM Safety Training Fail?](../papers/wei-2023-jailbroken.md) — its "prefix injection" and payload-splitting attacks draw on prompt-injection techniques.

## See also

- [Jailbreak (LLM)](jailbreak.md)
- [Safety training (LLM harmlessness)](safety-training.md)

## References

- Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., and Fritz, M.
  "More than You've Asked For: A Comprehensive Analysis of Novel Prompt
  Injection Threats to Application-Integrated Large Language Models."
  arXiv:2302.12173, 2023.
- Kang, D., Li, X., Stoica, I., Guestrin, C., Zaharia, M., and Hashimoto, T.
  "Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security
  Attacks." arXiv:2302.05733, 2023.
