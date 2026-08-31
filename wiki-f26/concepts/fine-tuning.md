---
title: "Fine-tuning"
type: concept
description: "Continuing gradient training of an already-pretrained model on a smaller task-, domain-, or behavior-specific dataset; full versus parameter-efficient updates such as LoRA, and why the step that adapts a model is also the step that can undo properties an earlier stage installed."
tags:
  - machine-learning
  - language-models
  - training
---

## [Wiki Home](../README.md)

# Fine-tuning

## Definition

Fine-tuning continues training a model whose weights already encode broad
capability, using a smaller dataset chosen for a particular task, domain, or
behavior. It costs a small fraction of pretraining because the general
representations are already there and only need adjusting. In vision it is the
second half of [transfer learning](transfer-learning.md): take an
ImageNet-pretrained backbone and fit it to a target task with far less
task-specific data. For language models it is the whole post-pretraining
pipeline, and the stages have their own names,
[instruction tuning](instruction-tuning.md), preference optimization
([RLHF](rlhf.md) or [DPO](direct-preference-optimization.md)), and
[safety training](safety-training.md), but each is a fine-tuning run.

Full fine-tuning updates every weight. Parameter-efficient fine-tuning updates a
small subset of weights, or small modules added alongside frozen ones, and
low-rank adaptation (LoRA) is the common instance (Hu et al., 2022). The
distinction is not only about cost: it changes how much of the model an
adaptation can move, and it changes what an adversary with fine-tuning access can
reach.

Three consequences make fine-tuning recur in this course. A fine-tuning run is
constrained only by its own objective and data, so a property installed by an
earlier stage can degrade as a side effect, which is how a safety-aligned model
loses its refusals under fine-tuning on data unrelated to safety
([Qi et al., 2024](../papers/qi-2024-shallow-safety-alignment.md)). The
fine-tuning set is usually the smallest and most sensitive data in the pipeline,
so it is the data a [memorization](memorization.md) or extraction attack has the
best odds against. And offering fine-tuning as a hosted service hands an outside
party a weight-update capability, which is a stronger position than any prompt.

## Papers that use this concept

- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](../papers/qi-2024-shallow-safety-alignment.md) — treats fine-tuning as both the attack (a few gradient steps strip alignment) and the defense (an objective that constrains early-token drift during it).
- [What Makes and Breaks Safety Fine-tuning? A Mechanistic Study](../papers/jain-2024-safety-finetuning.md) — compares three safety fine-tuning protocols to ask what each changes inside the model.
- [Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs](../papers/bao-2025-dp-zo.md) — the run it makes private is a fine-tuning run, and the memory cost of backpropagating per-example gradients through one is the problem its zeroth-order optimizer sidesteps.
- [Knowledge Unlearning for Mitigating Privacy Risks in Language Models](../papers/jang-2022-knowledge-unlearning.md) — its unlearning is a fine-tuning run with the sign of the objective flipped on the sequences to be forgotten.
- [Knockoff Nets: Stealing Functionality of Black-Box Models](../papers/orekondy-2019-knockoff-nets.md) — both the victim models and the knockoff are pretrained backbones fine-tuned on a task.
- [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](../papers/wang-2019-neural-cleanse.md) — one evaluated model is built this way, and one of its two patches retrains the model on the reconstructed trigger to disable the backdoor.
- [No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML](../papers/zhang-2024-tee-shielded.md) — the models it defends are public backbones fine-tuned on a task, and those same public backbones are an adversary resource for reconstructing the shielded portion.
- [PAL*M: Property Attestation for Large Generative Models](../papers/chantasantitam-2026-palm.md) — parameter-efficient fine-tuning is one of the pipeline operations its attestation has to cover.
- [A Watermark for Large Language Models](../papers/kirchenbauer-2023-llm-watermark.md) — the machine-generated-text detectors it is set against are themselves language models fine-tuned for the detection task.
- [Examining Zero-Shot Vulnerability Repair with Large Language Models](../papers/pearce-2023-vulnerability-repair.md) — deliberately does without it, prompting off-the-shelf models so the result does not depend on a repair-specific training set.

## Variants and traps

- Fine-tuning and [unlearning](machine-unlearning.md) both edit a trained model,
  and both are gradient runs, but they answer different questions. Fine-tuning
  asks what the model should now do; unlearning asks what influence should now be
  absent, which is a claim about the model's history and is harder to verify.
- "Fine-tuning attack" covers two different capabilities. One is an adversary
  supplying harmful fine-tuning data on purpose; the other is a benign developer
  whose ordinary fine-tuning degrades safety by accident. A defense that stops
  the first need not address the second.
- Parameter-efficient fine-tuning constrains where the update lands, which is
  often mistaken for constraining how much the behavior can move. A small number
  of updated parameters can still change a model's refusals.

## See also

- [Transfer learning](transfer-learning.md)
- [Instruction tuning](instruction-tuning.md)
- [Safety training (LLM harmlessness)](safety-training.md)
- [Machine unlearning](machine-unlearning.md)
- [Language model pretraining](language-model-pretraining.md)

## References

- Hu, E. J., et al. "LoRA: Low-Rank Adaptation of Large Language Models."
  International Conference on Learning Representations (ICLR), 2022.
