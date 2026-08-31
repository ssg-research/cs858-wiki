---
title: "Transformer"
type: concept
description: "The architecture under nearly every modern language and vision model: stacked blocks of self-attention and a position-wise feed-forward network, joined by residual connections and layer normalization; the residual-stream view interpretability uses, and the softmax, GELU, and normalization nonlinearities that dominate the cost of running one under encryption or inside a proof."
tags:
  - machine-learning
  - language-models
  - architecture
---

## [Wiki Home](../README.md)

# Transformer

## Definition

A transformer maps a sequence of tokens to a sequence of vectors through a stack
of identical blocks (Vaswani et al., 2017). Each token is first looked up in an
embedding table, giving a vector per position. Every block then applies two
operations in turn. **Self-attention** lets each position gather information from
the others: the block projects each position into a query, a key, and a value,
scores every query against every key, passes those scores through a
[softmax](softmax.md) to get mixing weights, and returns the weighted sum of the
values. The **feed-forward network** then transforms each position on its own
through a widening and narrowing pair of linear maps with a nonlinearity between
them, usually GELU. Both operations are wrapped in a residual connection, which
adds the block's output back to its input, and in layer normalization, which
rescales a vector to fixed mean and variance. A final linear map turns the last
block's vectors into [logits](softmax.md) over the vocabulary.

Two properties follow from that design and matter downstream. Because attention
reaches every position directly, the whole sequence is processed in parallel, and
a token's influence on a later token does not have to pass through the
intervening steps. Because every block adds to its input rather than replacing
it, the vectors flowing through the stack form a *residual stream* that each
block reads from and writes to, which is the picture
[mechanistic interpretability](mechanistic-interpretability.md) works in.

The same block is reused everywhere. An autoregressive
[language model](language-model-pretraining.md) is a decoder-only stack whose
attention is masked so a position may only see earlier ones; vision transformers
apply the same stack to image patches.

## Papers that use this concept

- [Extracting Training Data from Large Language Models](../papers/carlini-2021-extracting-training-data.md) — GPT-2, the target it extracts from, is a decoder-only stack of these blocks.
- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](../papers/jang-2022-knowledge-unlearning.md) — the GPT-Neo and OPT models it unlearns from are transformer language models.
- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-llm-watermark.md) — watermarks at the point where the final linear map produces the vocabulary logits.
- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../papers/pearce-2023-vulnerability-repair.md) — the code models it prompts are transformers pretrained on source code.
- [What Makes and Breaks Safety Fine-tuning? A Mechanistic Study](../papers/jain-2024-safety-finetuning.md) — reads safety behavior off the residual stream, and corroborates on small transformers it trains itself.
- [Secure Transformer Inference Made Non-interactive](../papers/zhang-2025-nexus.md) — the block's nonlinear pieces, softmax, GELU, and layer normalization, are what makes encrypted inference expensive.
- [zkGPT: An Efficient Non-interactive Zero-knowledge Proof Framework for LLM Inference](../papers/qu-2025-zkgpt.md) — the same nonlinear pieces are what an arithmetic circuit cannot express directly.
- [PAL*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — the pretrain-then-adapt pipeline it attests is the standard transformer lifecycle.
- [ASGARD: Protecting On-Device Deep Neural Networks with Virtualization-Based Trusted Execution Environments](../papers/moon-2025-asgard.md) — the on-device workloads it shields include transformer backbones alongside convolutional ones.

## Variants and traps

- Encoder-only, decoder-only, and encoder-decoder stacks are the same block wired
  differently, and papers often say "transformer" for whichever they mean. Which
  one is in play decides whether the model can see later tokens.
- Matrix multiplication is the cheap part. For cryptographic and hardware
  backends the binding cost is softmax, GELU, and layer normalization, because
  each needs comparison, exponentiation, division, or a square root rather than
  the additions and multiplications those backends do natively.
- "Attention" names both the operation inside a block and the interpretability
  artifact people plot. An attention weight says which positions were mixed, and
  reading it as an explanation of the model's reasoning is a further claim.

## See also

- [Language model pretraining](language-model-pretraining.md)
- [Softmax and logits](softmax.md)
- [Mechanistic interpretability](mechanistic-interpretability.md)
- [Convolutional neural network](convolutional-neural-network.md)

## References

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N.,
  Kaiser, Ł., and Polosukhin, I. "Attention Is All You Need." Advances in Neural
  Information Processing Systems (NIPS), 2017.
