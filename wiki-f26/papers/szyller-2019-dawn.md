---
title: "DAWN: Dynamic Adversarial Watermarking of Neural Networks"
authors:
  - Szyller, Sebastian
  - Atli, Buse Gul
  - Marchal, Samuel
  - Asokan, N.
year: 2019
section: "Model Watermarking / Fingerprinting"
primary: true
arxiv: "1906.00830"
tags:
  - watermarking
  - model-extraction
  - backdoor
  - ip-protection
  - threat-model
  - computer-vision
---

[Home page](../README.md)

# DAWN: Dynamic Adversarial Watermarking of Neural Networks

## High-level overview

A trained model exposed through a prediction API can be copied by
[model extraction](../concepts/model-extraction.md): an adversary queries the
API, collects the returned labels, and trains a surrogate that reproduces the
victim's functionality. Existing
[model watermarking](../concepts/model-watermarking.md) schemes embed an
ownership marker into the model at training time, so the owner can later prove a
suspect model is a copy. Against extraction they fail, because the adversary, not
the owner, trains the surrogate, and nothing the owner placed in the original
model is guaranteed to carry over.

This work introduces DAWN (Dynamic Adversarial Watermarking of Neural Networks),
a watermarking approach for deterring intellectual-property theft via model
extraction. DAWN is a component placed in front of the prediction API rather than
a change to the protected model. For a small, client-specific fraction of
incoming queries (under 0.5%), it returns a deliberately altered label instead of
the model's true prediction. If a client uses its query responses to train a
surrogate, those altered query-label pairs act as a [backdoor](../concepts/backdoor-attacks.md)
trigger set that the surrogate learns. The owner can then query a suspected model
with that trigger set and check whether the planted responses reappear, turning a
property the adversary unknowingly trained into evidence of theft. The label
changes are keyed and deterministic, so repeated or near-identical queries get
consistent answers and an adversary cannot single out the altered ones. The
watermark is also specific to each client, so a verified mark links a surrogate
back to the client whose queries trained it.

The paper reports that DAWN watermarks every surrogate produced by two
extraction attacks, including the functionality-stealing attack of
[Knockoff Nets](orekondy-2019-knockoff-nets.md) (Orekondy et al., 2019), lets the
owner demonstrate ownership with high confidence, and costs honest clients a
negligible drop in accuracy (0.03 to 0.5%). Decoded terminology: the "watermark"
here is a trigger set (a backdoor), not a marker embedded in the weights; the
"oracle" is the ground-truth labeling function the model approximates; and the
"adversary" is a model thief who trains the surrogate, so the watermark is
embedded by the attacker rather than by the defender.

**Threat Model:** The adversary mounts model extraction against a victim's
prediction API over [black-box](../concepts/white-box-black-box.md) query access:
it submits inputs (natural or synthetic), reads back labels, and treats each
returned label as ground truth, having no prior expectation of what any single
query's correct label should be. It chooses its own surrogate architecture,
training data, and training process, and it serves the resulting surrogate
through its own prediction API (a surrogate kept for purely private use is out of
scope, since ownership demonstration needs query access to the suspect). The
adversary may try to remove or evade the mark: discarding queries it suspects are
watermarked, adding noise to its training inputs, probing for the watermarking
decision boundary, or splitting the extraction across several colluding clients.
The defender operates the API and need not be the model's trainer; it cannot
alter the protected model's training and cannot choose trigger inputs from the
whole input space, only from what clients actually submit. Its claim is that any
surrogate accurate enough to be useful necessarily carries an embedded,
client-specific watermark, which the owner can verify through a trusted judge and
a public commitment establishing priority, while honest clients see almost no
loss of accuracy.

## Why read this

Preventing model extraction without sacrificing utility has proven very hard,
while detecting it after the fact is more tractable. DAWN is the first defense to
treat the deployed system as a whole rather than the model in isolation, placing
its mechanism at the prediction API instead of inside the trained model. The
result is a watermarking technique that is largely independent of the model it
protects.

## Basic Background

### Model extraction and prediction-API access

[Model extraction](../concepts/model-extraction.md) (model stealing) reproduces
an asset of a deployed model from external access, usually the
[black-box](../concepts/white-box-black-box.md) query interface of a
prediction API, where inputs go in and labels or probability vectors come back.
The variant DAWN addresses is functionality stealing: training a *surrogate*
model that matches the victim's task accuracy, trained on the victim's own
responses to the adversary's queries. The adversary may use natural or synthetic
query data and is free to pick a surrogate architecture different from the
victim's.

### Image classification with convolutional networks

The protected models and surrogates are
[convolutional neural networks](../concepts/convolutional-neural-network.md)
(CNNs) for image classification, each mapping an image to a probability
distribution over a fixed set of classes. The evaluation spans standard
image datasets and backbones (for example ResNet and DenseNet), covering both
small networks and larger pretrained ones.

### Model watermarking

[Model watermarking](../concepts/model-watermarking.md) embeds an owner-verifiable
marker in a model so the owner can later claim ownership of a copy. White-box
schemes hide the marker in the weights; black-box schemes verify it through the
prediction API. The black-box schemes relevant here verify ownership by querying
a secret *trigger set* and checking that the model returns the planted responses.

### Backdoors and model overcapacity

A black-box watermark is a [backdoor](../concepts/backdoor-attacks.md): a model
trained to return chosen, incorrect outputs on a trigger set while behaving
normally elsewhere. Backdoors embed because deep networks have the
[capacity to memorize](../concepts/memorization.md) a subset of inputs with
arbitrary labels without harming the primary task. The same effect is what makes
a small set of deliberately mislabeled query responses stick in a surrogate
trained on them.

### Proving ownership: commitments and a trusted verifier

Demonstrating ownership needs more than a matching trigger set; it needs proof
that the claimant held the model first. A
[cryptographic commitment](../concepts/cryptographic-commitment.md) published on
a public, time-stamped bulletin board (such as a blockchain) fixes the owner's
model and per-client secrets before any dispute, giving proof of priority. A
trusted judge, which can be realized inside a trusted execution environment (an
isolated hardware enclave that runs verification code with integrity and
confidentiality guarantees), runs the verification on the secret values and the
suspect API and reports the verdict.

<details>
<summary><h2>Paper Context</h2></summary>

DNN watermarking emerged between 2017 and 2019. The first scheme embedded a
marker directly into a trained network's weights, which required white-box access
to verify and could be removed by lightly retraining the model (Uchida et al.,
2017). Black-box-verifiable schemes followed, all based on backdooring: the owner
trains the model on a chosen trigger set of mislabeled inputs and proves
ownership by querying that trigger set through the prediction API (Adi et al.,
2018; Zhang et al., 2018; Le Merrer et al., 2017; Darvish Rouhani et al., 2019).
These schemes carry empirical and theoretical guarantees, but each assumes the
owner controls training and can draw the trigger set from the whole input space.

Backdooring itself came from the poisoning and Trojan literature: a model trained
to misclassify inputs that carry a chosen trigger while classifying everything
else normally (Gu et al., 2017; Chen et al., 2017; Liu et al., 2018). The
enabling property is overcapacity, the demonstrated ability of deep networks to
fit a subset of inputs with arbitrary labels without measurably hurting the
primary task (Zhang et al., 2017).

In parallel, model extraction was established as a realistic threat against
deployed APIs. Early work solved the parameters of simple model families from
their confidence outputs, producing near-exact copies (Tramèr et al., 2016).
Later attacks stole the functionality of complex DNNs from queries alone, using
natural data, synthetic data, or a surrogate architecture unlike the victim's
(Papernot et al., 2017; Correia-Silva et al., 2018; Juuti et al., 2019; Orekondy
et al., 2019). Proposed defenses tried to flag extraction from the distribution
of a client's queries or to perturb the returned predictions, but were confined
to simple models or to specific attacks (Kesarwani et al., 2018; Quiring et al.,
2018; Lee et al., 2018). Against this backdrop, existing watermarks were shown
ineffective at protecting models from extraction, because the surrogate is
trained by the adversary rather than the owner (Zhang et al., 2018).

</details>

## Reading guidance

- Section 2 (Background): the model-extraction attack model and the backdoor-based
  watermarking formalism, including the trigger set, the backdoor function, and
  the oracle the model approximates.
- Section 3 (Problem Statement) and Table 1: the adversary model, the assumptions,
  and the requirements W1 to W4 and X1 to X3. Attention anchor: note the two
  challenges DAWN faces that training-time watermarking does not (the defender
  cannot pick the trigger set from the whole input space, and the adversary
  controls training), and which requirement is new here.
- Section 3.2 (Assumptions): the assumption that the adversary has no prior
  expectation about any query's correct label and treats returned labels as ground
  truth. Attention anchor: this assumption is what the indistinguishability of the
  altered labels rests on; note exactly what it claims.
- Section 4 (Dynamic Adversarial Watermarks): how a watermark is generated,
  embedded, and verified, and how ownership is demonstrated. Figure 2 and Equation
  3 set the relationship between trigger-set size and verification confidence.
- Section 4.1.3 with Section 6.2: the mapping function that keeps the
  watermarking decision stable under small input changes. Attention anchor: note
  the trade-off its tolerance parameter controls and what an adversary could do at
  each extreme.
- Section 5 (Experimental Setup) and Table 2: the datasets and the low- versus
  high-capacity models.
- Section 7: the results against the two extraction attacks, with the reported
  ownership confidence and the accuracy cost to honest clients.
- Sections 8 and 9.2 (Limitations): the evasion strategies (discarding queries,
  adding noise) and what each costs the adversary. Attention anchor: the argument
  for why some evasions are not considered realistic turns on which adversary goal
  each one sacrifices; note that cost.

## Motivating questions

1. Why are watermarks embedded into the model at training time ineffective once a
   model's functionality is stolen through its prediction API?
2. What does it mean to embed a watermark by altering API responses rather than by
   training the protected model, and what guarantee does that give the owner?
3. What does the defense cost the honest clients of the API, and what does it cost
   an adversary who tries to avoid or remove the watermark?
4. Beyond detecting that a model was stolen, what additional information can a
   client-specific watermark provide?
5. What has to be trusted, and what has to be assumed about the adversary, for an
   ownership claim to hold up?

[Home page](../README.md)

<details>
<summary><h2>References</h2></summary>

- Adi, Y., Baum, C., Cisse, M., Pinkas, B., and Keshet, J. "Turning Your Weakness Into a Strength: Watermarking Deep Neural Networks by Backdooring." USENIX Security Symposium, 2018.
- Chen, X., Liu, C., Li, B., Lu, K., and Song, D. "Targeted Backdoor Attacks on Deep Learning Systems Using Data Poisoning." arXiv:1712.05526, 2017.
- Correia-Silva, J.R., Berriel, R.F., Badue, C., de Souza, A.F., and Oliveira-Santos, T. "Copycat CNN: Stealing Knowledge by Persuading Confession with Random Non-Labeled Data." International Joint Conference on Neural Networks (IJCNN), 2018.
- Darvish Rouhani, B., Chen, H., and Koushanfar, F. "DeepSigns: An End-to-End Watermarking Framework for Ownership Protection of Deep Neural Networks." International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS), 2019.
- Gu, T., Dolan-Gavitt, B., and Garg, S. "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain." arXiv:1708.06733, 2017.
- Juuti, M., Szyller, S., Marchal, S., and Asokan, N. "PRADA: Protecting Against DNN Model Stealing Attacks." IEEE European Symposium on Security and Privacy (EuroS&P), 2019.
- Kesarwani, M., Mukhoty, B., Arya, V., and Mehta, S. "Model Extraction Warning in MLaaS Paradigm." Annual Computer Security Applications Conference (ACSAC), 2018.
- Le Merrer, E., Perez, P., and Trédan, G. "Adversarial Frontier Stitching for Remote Neural Network Watermarking." arXiv:1711.01894, 2017.
- Lee, T., Edwards, B., Molloy, I., and Su, D. "Defending Against Model Stealing Attacks Using Deceptive Perturbations." arXiv:1806.00054, 2018.
- Liu, Y., Ma, S., Aafer, Y., Lee, W.-C., Zhai, J., Wang, W., and Zhang, X. "Trojaning Attack on Neural Networks." Network and Distributed System Security Symposium (NDSS), 2018.
- Orekondy, T., Schiele, B., and Fritz, M. "Knockoff Nets: Stealing Functionality of Black-Box Models." IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2019.
- Papernot, N., McDaniel, P., Goodfellow, I., Jha, S., Celik, Z.B., and Swami, A. "Practical Black-Box Attacks against Machine Learning." ACM Asia Conference on Computer and Communications Security (AsiaCCS), 2017.
- Quiring, E., Arp, D., and Rieck, K. "Forgotten Siblings: Unifying Attacks on Machine Learning and Digital Watermarking." IEEE European Symposium on Security and Privacy (EuroS&P), 2018.
- Tramèr, F., Zhang, F., Juels, A., Reiter, M.K., and Ristenpart, T. "Stealing Machine Learning Models via Prediction APIs." USENIX Security Symposium, 2016.
- Uchida, Y., Nagai, Y., Sakazawa, S., and Satoh, S. "Embedding Watermarks into Deep Neural Networks." ACM International Conference on Multimedia Retrieval (ICMR), 2017.
- Zhang, C., Bengio, S., Hardt, M., Recht, B., and Vinyals, O. "Understanding Deep Learning Requires Rethinking Generalization." International Conference on Learning Representations (ICLR), 2017. arXiv:1611.03530.
- Zhang, J., Gu, Z., Jang, J., Wu, H., Stoecklin, M.Ph., Huang, H., and Molloy, I. "Protecting Intellectual Property of Deep Neural Networks with Watermarking." ACM Asia Conference on Computer and Communications Security (AsiaCCS), 2018.

</details>
