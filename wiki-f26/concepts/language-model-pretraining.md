---
title: "Language model pretraining"
type: concept
description: "Autoregressive next-token pretraining of a language model on a large corpus; the pretraining objective, the pretraining distribution, and the base model that exists before any alignment."
tags:
  - language-models
  - pretraining
---

### [Wiki Home](../README.md)

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
- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — measures alignment as the per-token gap from the base model, which past the first few tokens is small.
- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — exploits the next-token objective directly: the likelihood the model is trained to maximize is what makes memorized sequences extractable.
- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](../papers/jang-2022-knowledge-unlearning.md) — negates the next-token training objective, running gradient ascent to raise the loss on the sequences to forget.
- [PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models](../papers/zou-2024-poisonedrag.md) — turns on the pretraining knowledge cutoff that motivates retrieval augmentation, the surface the attack then corrupts.
- [What Makes and Breaks Safety Fine-tuning? A Mechanistic Study](../papers/jain-2024-safety-finetuning.md) — analyzes safety fine-tuning relative to the pretrained, then instruction-tuned, transformer it starts from, and corroborates its synthetic findings on pretrained Llama models.
- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-llm-watermark.md) — operates on the next-token distribution an autoregressive language model emits, biasing it at each step so the generated text carries the mark.
- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../papers/pearce-2023-vulnerability-repair.md) — the off-the-shelf code models it prompts are pretrained on source code, and repair is driven by that pretrained base alone, with no fine-tuning.
- [Secure Transformer Inference Made Non-interactive](../papers/zhang-2025-nexus.md) — the models it runs under encryption are pretrained transformers (BERT, GPT); secure inference returns their prediction without revealing the client's input or the server's weights.
- [Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs](../papers/bao-2025-dp-zo.md) — privately fine-tunes pretrained RoBERTa and OPT checkpoints, treating the pretrained base model as public.
- [zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference](../papers/qu-2025-zkgpt.md) — the inference it proves is a pretrained GPT-2 transformer; its blocks of matrix multiplication, attention, GeLU, and layer normalization are the layers compiled into the proof circuit.
- [PAL\*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — the generative models whose operations it attests are pretrained transformer LLMs; its property catalogue spans their training, fine-tuning, quantization, evaluation, and chat-session inference.

## See also

- [Instruction tuning](instruction-tuning.md)
- [Reinforcement learning from human feedback (RLHF)](rlhf.md)

### [Wiki Home](../README.md)

## References

- Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P.,
  Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. "Language Models
  are Few-Shot Learners." Advances in Neural Information Processing Systems
  (NeurIPS), 33:1877-1901, 2020.
