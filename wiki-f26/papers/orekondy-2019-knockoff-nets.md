---
title: "Knockoff Nets: Stealing Functionality of Black-Box Models"
authors:
  - Orekondy, Tribhuvanesh
  - Schiele, Bernt
  - Fritz, Mario
year: 2019
section: "Model Extraction / Stealing"
primary: true
arxiv: "1812.02766"
tags:
  - model-extraction
  - knowledge-distillation
  - computer-vision
  - threat-model
  - reinforcement-learning
---

[Home page](../README.md)

# Knockoff Nets: Stealing Functionality of Black-Box Models

## High-level overview

A deployed image classifier exposed through a prediction API answers queries,
image in and class probabilities out, while keeping its training data, its
architecture, and even the meaning of its output classes private. This work asks
how much of such a model's value an adversary can capture from that interface
alone. It formulates *functionality stealing*: training a substitute model, the
"knockoff," that matches the victim's accuracy on the victim's own task, without
recovering its weights and without reproducing it prediction for prediction. The
attack has two steps: query a set of images and collect the victim's posterior
probability vectors (its softmax outputs over the K classes), forming a
"transfer set" of image-prediction pairs, then train the knockoff on that
transfer set to imitate the victim's responses.

The adversary draws its query images from a large public image collection that
need not overlap the victim's training distribution. Two strategies decide what
to query: a random strategy that samples images independently, and an adaptive
strategy that casts query selection as a reinforcement-learning problem, learning
a policy that prefers images yielding informative responses to improve query
sample-efficiency. The reported observations: a knockoff trained on images from a
different distribution still recovers a large fraction of the victim's accuracy
(on the order of 0.81 to 0.96 times the victim's test accuracy across several
datasets in the hardest "open-world" setting, where the query pool and the
victim's classes barely overlap); this holds even when the knockoff uses a
different architecture than the victim; and the attack carries over to a
commercial image-analysis API, where a usable knockoff was trained for about $30
in queries.

**Threat Model:** The adversary has black-box query access to a deployed image
classifier: it submits images and reads back the posterior probability vector
over the victim's K classes, paying a cost per query. It does not know the
victim's architecture or hyperparameters, the data used to train and evaluate the
victim, or the semantics of the K output classes (which index corresponds to
which label). It acts only at inference time and changes nothing about the
victim's training. The adversary supplies its own pool of images, drawn from
public sources that may share little or nothing with the victim's training
distribution, and picks its own, possibly different, architecture for the
knockoff. Its objective is a substitute that performs the victim's task well,
measured on the victim's held-out test distribution, while keeping the number of
paid queries small. The defender's implicit claim, that keeping the model and its
data confidential protects the model's value, is what the attack tests; the paper
also considers a defender that degrades its responses by truncating or rounding
the probabilities it returns.

## Why read this

For years this was the strongest and most durable result in black-box model
extraction, and it remains the reference point for stealing classification
models. Its lasting claim is that a working copy can be trained even when the
adversary's architecture and query data differ entirely from the victim's, with
no access to the victim's training set, internals, or output-class semantics.

## Basic Background

### Image classification with convolutional networks

The victim and the knockoff are
[convolutional neural networks](../concepts/convolutional-neural-network.md)
(CNNs) for image classification: each maps an image to a posterior probability
distribution over a fixed set of K classes, and is trained by
[stochastic gradient descent](../concepts/stochastic-gradient-descent.md) on a
cross-entropy loss against labels. The experiments use standard backbones,
including ResNet (He et al., 2016) and VGG (Simonyan and Zisserman, 2014), which
function as interchangeable architecture choices.

### Transfer learning and ImageNet pretraining

Both the victim models and the knockoff are built by
[transfer learning](../concepts/transfer-learning.md): a backbone pretrained on
the large ImageNet / ILSVRC dataset (Deng et al., 2009; Russakovsky et al., 2015)
is then fine-tuned on a task. ImageNet plays a second role here as well, as one
of the large public image pools from which an adversary can draw its queries.

### Knowledge distillation

[Knowledge distillation](../concepts/knowledge-distillation.md) trains a student
model to match a teacher's output distribution rather than ground-truth labels
alone (Hinton et al., 2015; Buciluǎ et al., 2006). Training a model on another
model's soft predictions over a set of inputs is equivalent, up to a constant, to
minimizing the [KL divergence](../concepts/kl-divergence.md) between the two.
Classic distillation assumes white-box access to the teacher and a shared task and
training distribution.

### Model extraction and black-box access

[Model extraction](../concepts/model-extraction.md) attacks reproduce some asset
of a deployed model from external access, typically the
[black-box](../concepts/white-box-black-box.md) query interface of a prediction
API: inputs in, outputs out, with no view of weights or gradients. Different
attacks target different assets: exact parameters, hyperparameters, the
architecture, or the model's functionality. A common distinction is fidelity
(matching the victim prediction for prediction) versus accuracy (performing the
underlying task well).

### Query selection: active and reinforcement learning

Choosing which inputs to query under a budget is the subject of active learning,
in particular pool-based active learning, where the learner picks queries from a
fixed pool of unlabeled data (Settles and Craven, 2008). When the available
feedback is an evaluative reward for chosen actions rather than a correct label,
the natural framing is
[reinforcement learning](../concepts/reinforcement-learning.md); its simplest
instance is the multi-armed bandit, which trades off exploring uncertain actions
against exploiting ones already known to pay well (Sutton and Barto, 1998).

<details>
<summary><h2>Paper Context</h2></summary>

By 2018, several attacks recovered information about a deployed model through its
query interface. One line recovered model parameters directly: for simple model
families such as logistic regression and shallow networks, the input-output
equations can be solved from enough confidence outputs, yielding a near-exact
copy (Tramèr et al., 2016). Other work recovered hyperparameters (Wang and Gong,
2018) or reverse-engineered the architecture and training details of a black-box
network (Oh et al., 2018). These attacks aimed to reproduce the model itself, and
the strongest of them leaned on assumptions about the model family or on access to
data resembling the victim's.

A related thread trained a substitute model not to steal the task but to enable
evasion: a local stand-in, trained on synthetic queries to the victim, supplied
the gradients for crafting adversarial examples that transferred back to the
target (Papernot et al., 2017). Separately, a family of inference attacks read
properties of the model or its data off the same interface: membership inference
decided whether a specific record was in the training set (Shokri et al., 2017;
Salem et al., 2019), and model inversion reconstructed a representative, often
fuzzy, view of a class (Fredrikson et al., 2015).

The machinery for copying a model's behavior already existed in cooperative form.
Knowledge distillation transferred a teacher's behavior into a student from the
teacher's soft outputs (Hinton et al., 2015), extending older model-compression
work (Buciluǎ et al., 2006), but assumed a white-box teacher and a shared task and
dataset. Pool-based active learning offered ways to choose informative queries
under a labeling budget (Settles and Craven, 2008). What had not been established
was how far a copy of a model's *function*, rather than its parameters, could be
pushed by an adversary holding neither the victim's data nor its architecture nor
the meaning of its outputs.

</details>

## Reading guidance

- Section 3 (Problem Statement): the victim-versus-adversary game and the formal
  threat model. Note exactly which quantities the adversary is denied (internals,
  train/test data, output-class semantics) and how that list differs from earlier
  stealing work.
- Section 3 (Remarks, comparison to knowledge distillation) and Figure 3: where
  the setup is placed against distillation. Attention anchor: note which
  distillation assumptions are dropped and which are kept.
- Section 4.1 (Transfer Set Construction): the two query strategies, random and
  adaptive, the latter cast as a policy over a coarse-to-fine label hierarchy.
- Section 4.1.2 (Adaptive Strategy) and Figure 4: the reward design. Attention
  anchor: the reward combines a certainty term, a diversity term, and a loss
  term; note the justification given for each and how they are combined.
- Section 5 and Table 1: the four victim black-boxes and the choices of adversary
  image pool (closed-world versus open-world), with the label-overlap measurement
  (Table 3) that defines those regimes.
- Section 6.1, Table 2 and Figure 5: knockoff accuracy across datasets and query
  budgets, with the distillation row (adversary querying the victim's own training
  images) as a reference point.
- Section 6.2 and Figure 10: how the knockoff's architecture, relative to the
  victim's, affects performance. Attention anchor: the conclusion runs opposite to
  distillation's usual aim of a smaller student; note what is claimed about model
  complexity.
- Section 6.3 and Figure 11: the attack against a commercial image-analysis API,
  including the dollar cost.
- Section 6 (defense discussion): the victim counter-strategy of truncating or
  rounding the returned probabilities. Attention anchor: note what the defender is
  assumed able to change, and what the paper reports it costs the attack.

## Motivating questions

1. What must the adversary know about the victim model and its training data for
   the attack to work, and what does it only need query access to?
2. The knockoff is trained on images the adversary chose, which may come from a
   different distribution than the victim's training data. What does that buy, and
   what does it cost in task accuracy?
3. How does the way the adversary selects its query images affect how many paid
   queries the attack needs?
4. How does the knockoff's architecture, relative to the victim's, change the
   outcome?
5. What can the victim change about its API responses to resist the attack, and at
   what cost to its own users?

[Home page](../README.md)

<details>
<summary><h2>References</h2></summary>

- Buciluǎ, C., Caruana, R., and Niculescu-Mizil, A. "Model Compression." ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), 2006.
- Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., and Fei-Fei, L. "ImageNet: A Large-Scale Hierarchical Image Database." IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2009.
- Fredrikson, M., Jha, S., and Ristenpart, T. "Model Inversion Attacks that Exploit Confidence Information and Basic Countermeasures." ACM Conference on Computer and Communications Security (CCS), 2015.
- He, K., Zhang, X., Ren, S., and Sun, J. "Deep Residual Learning for Image Recognition." IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016.
- Hinton, G., Vinyals, O., and Dean, J. "Distilling the Knowledge in a Neural Network." arXiv:1503.02531, 2015.
- Oh, S.J., Augustin, M., Schiele, B., and Fritz, M. "Towards Reverse-Engineering Black-Box Neural Networks." International Conference on Learning Representations (ICLR), 2018.
- Papernot, N., McDaniel, P., Goodfellow, I., Jha, S., Celik, Z.B., and Swami, A. "Practical Black-Box Attacks against Machine Learning." ACM Asia Conference on Computer and Communications Security (AsiaCCS), 2017.
- Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., Huang, Z., Karpathy, A., Khosla, A., Bernstein, M., et al. "ImageNet Large Scale Visual Recognition Challenge." International Journal of Computer Vision (IJCV), 2015.
- Salem, A., Zhang, Y., Humbert, M., Fritz, M., and Backes, M. "ML-Leaks: Model and Data Independent Membership Inference Attacks and Defenses on Machine Learning Models." Network and Distributed System Security Symposium (NDSS), 2019.
- Settles, B. and Craven, M. "An Analysis of Active Learning Strategies for Sequence Labeling Tasks." Conference on Empirical Methods in Natural Language Processing (EMNLP), 2008.
- Shokri, R., Stronati, M., Song, C., and Shmatikov, V. "Membership Inference Attacks against Machine Learning Models." IEEE Symposium on Security and Privacy (S&P), 2017.
- Simonyan, K. and Zisserman, A. "Very Deep Convolutional Networks for Large-Scale Image Recognition." arXiv:1409.1556, 2014.
- Sutton, R.S. and Barto, A.G. "Introduction to Reinforcement Learning." MIT Press, 1998.
- Tramèr, F., Zhang, F., Juels, A., Reiter, M.K., and Ristenpart, T. "Stealing Machine Learning Models via Prediction APIs." USENIX Security Symposium, 2016.
- Wang, B. and Gong, N.Z. "Stealing Hyperparameters in Machine Learning." IEEE Symposium on Security and Privacy (S&P), 2018.

</details>
