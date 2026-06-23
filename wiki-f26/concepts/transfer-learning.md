---
title: "Transfer learning"
type: concept
description: "Reusing representations learned on one task to improve learning on another; in vision, ImageNet pretraining followed by fine-tuning, which reaches higher accuracy with less task-specific data and compute."
tags:
  - transfer-learning
  - computer-vision
  - machine-learning
---

[Home page](../README.md)

# Transfer learning

## Definition

Transfer learning reuses representations learned on one task to speed up or
improve learning on another. In computer vision the dominant form is ImageNet
pretraining: a [CNN](convolutional-neural-network.md) is first trained on the
large ImageNet / ILSVRC classification dataset (Deng et al., 2009; Russakovsky
et al., 2015), then its weights initialize a model that is fine-tuned on a
smaller target dataset. Because the pretrained features (edges, textures, object
parts) are broadly useful across vision tasks, fine-tuning from them reaches
higher accuracy with far less task-specific data and compute than training from
random initialization. Pretrained backbones are distributed as standard starting
points, so "start from ImageNet weights" is a routine default rather than a
design decision.

## Papers that use this concept

- [Knockoff Nets: Stealing Functionality of Black-Box Models](../papers/orekondy-2019-knockoff-nets.md) — both the victim models and the adversary's knockoff are initialized from ImageNet-pretrained weights before fine-tuning, so the attack inherits the same head start as the victim.
- [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](../papers/wang-2019-neural-cleanse.md) — one of the evaluated face-recognition models is built by transfer learning, fine-tuned from a pretrained backbone.
- [Unlocking the Power of Differentially Private Zeroth-order Optimization for Fine-tuning LLMs](../papers/bao-2025-dp-zo.md) — private fine-tuning of a pretrained language model on a downstream task, the language-model instance of the pretrain-then-fine-tune paradigm.
- [No Privacy Left Outside: On the (In-)Security of TEE-Shielded DNN Partition for On-Device ML](../papers/zhang-2024-tee-shielded.md) — public pretrained backbones build the victim and also initialize the adversary's surrogate, the on-device adversary's main resource.

## See also

- [Convolutional neural network](convolutional-neural-network.md)
- [Knowledge distillation](knowledge-distillation.md)

[Home page](../README.md)

## References

- Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., and Fei-Fei, L. "ImageNet: A Large-Scale Hierarchical Image Database." IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2009.
- Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., Huang, Z., Karpathy, A., Khosla, A., Bernstein, M., et al. "ImageNet Large Scale Visual Recognition Challenge." International Journal of Computer Vision (IJCV), 2015.
