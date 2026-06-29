---
title: "Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks"
authors:
  - Wang, Bolun
  - Yao, Yuanshun
  - Shan, Shawn
  - Li, Huiying
  - Viswanath, Bimal
  - Zheng, Haitao
  - Zhao, Ben Y.
year: 2019
section: "Training-data Poisoning"
primary: true
doi: "10.1109/SP.2019.00031"
tags:
  - backdoor
  - poisoning
  - computer-vision
  - threat-model
---

---

### [Wiki Home](../README.md)

---

# Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks

## High-level overview

A backdoored image classifier behaves normally on ordinary inputs but
misclassifies any input carrying a small adversary-chosen pattern, the *trigger*,
into an adversary-chosen *target label*. Because the trigger can be a tiny patch
of pixels and clean accuracy is unaffected, a backdoor can sit undetected in a
deployed model indefinitely. Neural Cleanse is the first general method to take a
trained classifier with no side information and decide whether it hides a
backdoor, recover what the trigger looks like, and patch the model so the
backdoor no longer fires.

Detection rests on one observation. In a clean model, turning inputs of many
classes into a chosen target requires a substantial change to each input; the
trigger is instead a small, label-independent shortcut, so for the infected label
the minimal change that flips inputs into it is an abnormally small outlier
against the other labels. Once a backdoor is found and its trigger reconstructed,
the paper develops three mitigations: an input filter on backdoor-neuron
activations, and two ways to patch the model (neuron pruning and unlearning) so
the trigger stops working.

The techniques are evaluated on handwritten-digit recognition (MNIST),
traffic-sign recognition (GTSRB), and two face-recognition models (one with a
large label space, one built by transfer learning), against two injection methods
from prior work (BadNets and Trojan Attack) and several adaptive attack variants.
Headline results at abstract level: the method separates infected from clean
models, the reconstructed triggers match the originals in which internal neurons
they activate, and the patches drive attack success down to low single-digit
percentages while preserving clean accuracy.

**Threat Model:** The adversary is whoever produced the model: an outsourced or
compromised training provider, or a third party redistributing a tampered
pretrained model. They control the training process (data, labels, configuration)
or a post-training modification, and use it to plant a backdoor so that any input
bearing the trigger is classified into the target label, while the model stays
accurate on clean inputs and so passes the user's ordinary validation. The
defender receives only the trained model and a set of correctly labeled clean
samples, plus the compute to test and modify the model; they do not hold the
poisoned training data, the trigger, or the target label, and retraining from
scratch is assumed infeasible. The defender's claim is to decide whether the
model is backdoored (and if so, which label is targeted), recover a trigger that
reproduces the behavior, and patch the model to disable the backdoor without
degrading clean accuracy.

## Why read this

Neural Cleanse set the template that the backdoor-defense literature still
follows: detect, reverse-engineer the trigger, then patch, all from the trained
model alone. It is worth reading for how a single sharp geometric intuition (the
infected label is "too easy" to reach) is turned into a concrete, testable
detector, and for its discipline in stress-testing that detector against an
attacker who knows how it works.

## Basic Background

### Deep image classifiers

The models under defense are
[convolutional neural networks](../concepts/convolutional-neural-network.md)
(CNNs) for image classification: each maps an input image to a probability
distribution over a fixed set of labels and predicts the highest-probability one.
They are trained by
[stochastic gradient descent](../concepts/stochastic-gradient-descent.md) on a
cross-entropy loss. One of the evaluated models is built by
[transfer learning](../concepts/transfer-learning.md), in which a backbone
pretrained on a large dataset is fine-tuned on a smaller target task, a routine
default in vision.

### Backdoors and how they are planted

A [backdoor](../concepts/backdoor-attacks.md) is a hidden behavior trained into a
model that fires only when a specific trigger is present in the input. The usual
way to plant one is [data poisoning](../concepts/data-poisoning.md): mixing
trigger-stamped, deliberately mislabeled samples into the training set so the
model learns the trigger-to-target association alongside its real task (Gu et al.,
2017). A later method injects a backdoor without the original training data by
crafting triggers that maximally excite chosen internal neurons (Y. Liu et al.,
2018). Both leave clean-input accuracy intact, which is what makes a backdoor
hard to notice.

### Backdoors versus adversarial examples

A backdoor is distinct from an
[adversarial example](../concepts/adversarial-examples.md). An adversarial example
is crafted per input against a fixed model at test time, and the same
perturbation generally does not transfer to other inputs. A backdoor trigger is
planted at training time and is input-agnostic: the same trigger added to almost
any input forces the target label.

### Measuring the size of a trigger

The detector compares triggers by how much of the image they occupy, measured by
an [ℓ1 norm](../concepts/lp-norms.md) over a continuous mask. A smaller norm means
a more compact trigger, the quantity whose distribution across labels the outlier
test examines.

### What the defender can see

The defender has [white-box](../concepts/white-box-black-box.md) access to the
trained model (its weights, and therefore its gradients and internal neuron
activations) but not to the data it was trained on. This access is what lets the
method optimize over inputs and inspect which neurons a trigger excites.

## Reading guidance

- Section II and Figure 1: the definition of a backdoor and the attack model. Note
  the line the paper draws between a backdoor and ordinary data poisoning, and
  what the defender is and is not assumed to have.
- Section III and Figure 2: the geometric intuition, a decision-boundary
  "shortcut" into the infected label. Attention anchor: the intuition is drawn on
  a one-dimensional, three-class cartoon; note what it assumes in order to carry
  over to real, high-dimensional models.
- Section IV, Equation 3: the trigger reverse-engineering objective, a
  misclassification term plus an ℓ1 size penalty on the mask. Attention anchor: the
  mask is made continuous so it can enter the optimization; note that choice and
  how it shapes the trigger that is recovered.
- Section IV (outlier detection): the Median Absolute Deviation test and the
  anomaly-index threshold of 2 used to call a label infected; note where that
  threshold comes from.
- Section V, Figures 18 and 19: detection across the four applications and two
  injection methods, and the separation between infected and clean models.
- Section V-C and Table V: how closely the reverse-engineered trigger matches the
  real one in the neurons it activates. Attention anchor: note the contrast
  between BadNets and Trojan models here.
- Section VI: the three mitigations (input filter, neuron pruning, unlearning) and
  what each costs in clean accuracy.
- Section VII: adaptive counter-measures (larger triggers, multiple triggers,
  source-label-specific or "partial" backdoors). Attention anchor: note which
  variant the base method struggles with and what change it needs to handle it.

<details>
<summary><h2>Paper Context</h2></summary>

By 2019 the opacity of deep networks was a recognized obstacle: a trained model
is a sequence of weights with no human-readable account of its behavior, so there
is no general way to verify how it acts on inputs outside a test set. That gap is
what makes a hidden, trigger-activated behavior possible to embed and hard to
find. Two injection methods had established backdoors as a concrete threat.
BadNets poisoned the training set with trigger-stamped, relabeled images and
reported attack success above 99% with negligible loss on clean inputs (Gu et al.,
2017). The Trojan Attack removed the need for the original training data by
selecting triggers that drive specific internal neurons, building a strong
trigger-to-output association from few samples (Y. Liu et al., 2018). A more
restricted variant assumed the attacker could pollute only a limited portion of
the training set (Chen et al., 2017). These attacks were demonstrated across
vision tasks from digit and traffic-sign recognition to face recognition.

Defenses were thin and assumed the hard part was already done. Fine-Pruning
removed backdoors by pruning neurons left dormant on clean inputs (K. Liu et al.,
2018), and an earlier proposal sanitized models against injected Trojans (Y. Liu
et al., 2017); both assumed the model was already known to be infected and offered
no way to decide whether a given model carried a backdoor or which label it
targeted. The Trojan Attack paper itself sketched detection ideas without a
working general method.

Backdoors sat beside an older and broader line on
[data poisoning](../concepts/data-poisoning.md), where an adversary corrupts
training data to degrade accuracy or force targeted errors, and where defenses
focused on sanitizing the training set by finding samples that shift performance
most (Steinhardt et al., 2017; Jagielski et al., 2018). Those defenses assume
access to the poisoned data and target poison that visibly changes accuracy, so
they fit poorly to triggers that leave clean accuracy untouched. Backdoors are
also distinct from the test-time evasion threat of adversarial examples (Szegedy
et al., 2014), against which a separate and by then well-worn cycle of defenses
and breaks had played out. No general tool existed to detect and repair a backdoor
from the trained model alone.

</details>

### [Wiki Home](../README.md)

<details>
<summary><h4>References</h4></summary>

- Chen, X., Liu, C., Li, B., Lu, K., and Song, D. "Targeted Backdoor Attacks on Deep Learning Systems Using Data Poisoning." arXiv:1712.05526, 2017.
- Gu, T., Dolan-Gavitt, B., and Garg, S. "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain." Machine Learning and Computer Security Workshop, 2017. arXiv:1708.06733.
- Jagielski, M., Oprea, A., Biggio, B., Liu, C., Nita-Rotaru, C., and Li, B. "Manipulating Machine Learning: Poisoning Attacks and Countermeasures for Regression Learning." IEEE Symposium on Security and Privacy (S&P), 2018.
- Liu, K., Dolan-Gavitt, B., and Garg, S. "Fine-Pruning: Defending Against Backdooring Attacks on Deep Neural Networks." International Symposium on Research in Attacks, Intrusions, and Defenses (RAID), 2018.
- Liu, Y., Ma, S., Aafer, Y., Lee, W.-C., Zhai, J., Wang, W., and Zhang, X. "Trojaning Attack on Neural Networks." Network and Distributed System Security Symposium (NDSS), 2018.
- Liu, Y., Xie, Y., and Srivastava, A. "Neural Trojans." IEEE International Conference on Computer Design (ICCD), 2017.
- Steinhardt, J., Koh, P.W., and Liang, P.S. "Certified Defenses for Data Poisoning Attacks." Advances in Neural Information Processing Systems (NIPS), 2017.
- Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I., and Fergus, R. "Intriguing Properties of Neural Networks." International Conference on Learning Representations (ICLR), 2014.

</details>
