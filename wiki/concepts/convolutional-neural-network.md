---
title: "Convolutional neural network"
type: concept
description: "Neural networks for grid-structured data, especially images: learned convolutional filters, pooling, and a softmax classifier head; the standard image-classification backbones (AlexNet, VGG, ResNet, DenseNet)."
tags:
  - computer-vision
  - machine-learning
---

# Convolutional neural network

## Definition

A convolutional neural network (CNN) is a neural network for grid-structured
data, especially images. It is built from layers that slide learned
convolutional filters over the input, followed by nonlinearities and spatial
pooling, so early layers detect local patterns (edges, textures) and deeper
layers compose them into higher-level features. For classification, a CNN maps
an input image to a vector of class scores; a softmax normalizes those scores
into a posterior probability distribution over the K classes, and the prediction
is the highest-probability class. The network is trained by
[stochastic gradient descent](stochastic-gradient-descent.md) on a
cross-entropy loss against the labels.

Standard image-classification backbones differ mainly in depth and in how they
route signal and gradients through many layers: AlexNet (Krizhevsky et al.,
2012), VGG (Simonyan and Zisserman, 2014), ResNet with its residual skip
connections (He et al., 2016), and DenseNet (Huang et al., 2017). These names
recur as off-the-shelf architecture choices throughout the literature.

## Papers that use this concept

- [Knockoff Nets: Stealing Functionality of Black-Box Models](../papers/orekondy-2019-knockoff-nets.md) — both the victim models and the adversary's knockoff are CNN image classifiers; the study varies the knockoff's backbone relative to the victim's.
- [DAWN: Dynamic Adversarial Watermarking of Neural Networks](../papers/szyller-2019-dawn.md) — the protected models and the surrogates it watermarks are CNN image classifiers, evaluated on standard datasets and backbones.
- [Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks](../papers/wang-2019-neural-cleanse.md) — the models it inspects, tests, and patches are CNN image classifiers for digits, traffic signs, and faces.

## See also

- [Stochastic gradient descent](stochastic-gradient-descent.md)
- [Transfer learning](transfer-learning.md)

## References

- He, K., Zhang, X., Ren, S., and Sun, J. "Deep Residual Learning for Image Recognition." IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016.
- Huang, G., Liu, Z., van der Maaten, L., and Weinberger, K.Q. "Densely Connected Convolutional Networks." IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017.
- Krizhevsky, A., Sutskever, I., and Hinton, G.E. "ImageNet Classification with Deep Convolutional Neural Networks." Advances in Neural Information Processing Systems (NIPS), 2012.
- Simonyan, K. and Zisserman, A. "Very Deep Convolutional Networks for Large-Scale Image Recognition." arXiv:1409.1556, 2014.
