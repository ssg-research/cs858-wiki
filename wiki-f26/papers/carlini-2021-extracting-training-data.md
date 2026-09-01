---
title: "Extracting Training Data from Large Language Models"
authors:
  - Carlini, Nicholas
  - Tramèr, Florian
  - Wallace, Eric
  - Jagielski, Matthew
  - Herbert-Voss, Ariel
  - Lee, Katherine
  - Roberts, Adam
  - Brown, Tom
  - Song, Dawn
  - Erlingsson, Úlfar
  - Oprea, Alina
  - Raffel, Colin
year: 2021
section: "Training-data Extraction from LLMs"
primary: true
arxiv: "2012.07805"
tags:
  - training-data-extraction
  - memorization
  - privacy
  - language-models
  - membership-inference
---

## [Wiki Home](../README.md)

# Extracting Training Data from Large Language Models

**Paper:** [arXiv:2012.07805](https://arxiv.org/abs/2012.07805)

## High-level overview

A language model trained by next-token prediction assigns high probability to
its training data, so some [memorization](../concepts/memorization.md) of that
data is intrinsic to the objective. This work asks whether a large model trained roughly once over a
massive, de-duplicated corpus, a regime with almost no gap between training and
test loss, still memorizes individual examples tightly enough that an outsider
can pull them back out word for word. It answers yes, with a training-data
extraction attack that pairs broad sampling of candidate continuations with a
[membership-inference](../concepts/membership-inference.md) ranking signal: a
sequence the target model finds far less
surprising than a reference model does is flagged as likely verbatim training
text.

Run against GPT-2, a model trained on text scraped from the public web, the
attack recovers hundreds of verbatim training sequences, including personally
identifiable information (names, phone and fax numbers, email and physical
addresses), source code, news headlines, and high-entropy strings such as
UUIDs, many present in only a single training document. The paper pins down its
target as k-eidetic memorization: a string the model reproduces that appears in
at most k of the training documents, with small k the dangerous regime, where
"eidetic" borrows the term for recall after a single exposure. It further
reports that within the GPT-2 family, larger models memorize more.

**Threat Model:** The adversary has black-box query access to a trained,
deployed language model. It can submit a prefix, sample continuations, and read
the probability the model assigns to any sequence, but cannot inspect weights,
gradients, or hidden states. It acts only at inference time on an already-trained
model and changes nothing about training. It does not target a particular person
or record; the goal is to extract memorized training data indiscriminately,
prioritizing verbatim sequences (distinct from the fuzzy, representative
reconstructions of model inversion) that appear in few training documents.
Because memorized content surfaces through ordinary, honest generation, the
"adversary" can be an algorithm or even a benign user, and the party at risk is
whoever trained the model on a corpus that may contain private text.

## Basic Background

### Language models and text generation

A neural [language model](../concepts/language-model-pretraining.md) is trained
by next-token prediction: it estimates the probability of each token given the
preceding ones, and the training loss is the average
[cross-entropy](../concepts/cross-entropy.md), equivalently the negative
log-likelihood, over the corpus. The same model generates text autoregressively, sampling one
token at a time and feeding it back; the
[decoding strategy](../concepts/decoding-strategies.md) (greedy selection,
[temperature](../concepts/temperature.md) scaling, or top-k sampling) controls
how each next token is drawn
from the predicted distribution. The standard intrinsic quality measure is
[perplexity](../concepts/perplexity.md), the exponential of the per-token average
negative log-likelihood, low when the model finds a sequence unsurprising. GPT-2
(Radford et al., 2019) is a [Transformer](../concepts/transformer.md) language
model of this kind (Vaswani et al., 2017), released in sizes from 124
million to 1.5 billion parameters and trained on text scraped from the public
web.

### Memorization and overfitting

A model [memorizes](../concepts/memorization.md) an example when its behavior on
that example depends strongly on the example being in the training set.
Memorization is often conflated with overfitting, the gap between low training
error and higher test error, but the two come apart: the generalization gap is
an average over the data, while memorization is per-example and can persist in a
model whose average training and test losses are nearly identical. Theory
contemporaneous with this paper argues that fitting the long tail of rare
examples may be necessary for accuracy, so well-generalizing models memorize
some data by design (Feldman, 2020; Feldman and Zhang, 2020).

### Training-data privacy attacks

Privacy attacks recover information about a model's training set from access to
the model. The least revealing is
[membership inference](../concepts/membership-inference.md), which decides
whether a given example was in the training set (Shokri et al., 2017); its
baseline thresholds the model's confidence, since models tend to be more
confident on training data, and its success was tied to overfitting (Yeom et
al., 2018). Model inversion instead reconstructs a representative, often fuzzy,
view of a class (Fredrikson et al., 2015). Training-data extraction is stronger
still: it aims to reproduce specific training examples verbatim. Sharper
membership tests compare the target model's score against a second reference
model, a [likelihood-ratio](../concepts/likelihood-ratio-test.md) style
calibration that down-weights sequences any model would rate as likely. Every
such attack assumes a particular access level, from
[white-box](../concepts/white-box-black-box.md) weights and gradients to
query-only black-box access.

### Differential privacy as a defense

The standard principled defense is to train with
[differential privacy](../concepts/differential-privacy.md), which bounds how
much any single training record can affect the model. [DP-SGD](abadi-2016-dp-sgd.md)
is its deep-learning instantiation (Abadi et al., 2016), and it has been applied
to recurrent language models (McMahan et al., 2018). The guarantee comes at a
cost in accuracy and training time, and that cost falls hardest on the long-tail
examples that contribute most to quality.

## Reading guidance

- Section 3, Definitions 1 and 2: what makes a string extractable, and k-eidetic
  memorization, defined by counting the training documents containing it.
  Definition 1 admits pathological cases; note what footnote 4 lists and how
  short prefixes sidestep them.
- Section 5.2, with the metric list in Section 6.1: candidates are ranked by
  five comparison signals (Small and Medium GPT-2, zlib entropy, lower-cased
  text, a 50-token sliding window) set against a plain-perplexity baseline. The
  comparison, not the perplexity, is the attack.
- Section 6.2 with Table 2: 604 of 1,800 candidates confirmed memorized, an
  aggregate true-positive rate of 33.5%, broken out by generation strategy and
  inference metric. Section 6.1 fixes what confirmation meant, one of four
  authors finding a non-trivial substring that returns an exact Google match;
  note what that makes the 604 a count of.

<details>
<summary><h2>Paper Context</h2></summary>

When this paper appeared, the prevailing intuition held that privacy leakage
tracks overfitting (Yeom et al., 2018). Large language models were trained once,
or for a few epochs, over massive de-duplicated corpora and showed almost no
train-test gap, so the common assumption was that they did not meaningfully
memorize particular examples. Membership inference (Shokri et al., 2017) and
model inversion (Fredrikson et al., 2015) had been established mainly against
smaller or more overfit models, and their reliance on a measurable confidence
gap seemed to leave large, well-generalizing models largely out of reach.

Evidence that generative text models can memorize already existed, in restricted
settings. The Secret Sharer measured unintended memorization by inserting canary
sequences and tracking their exposure, and could extract them, in models trained
on academic datasets, often for more epochs than usual, or when the secret's
format was known in advance (Carlini et al., 2019). Related work examined
memorization of updates to language models (Zanella-Béguelin et al., 2020) and
in [federated training](../concepts/federated-learning.md) (Thakkar et al.,
2020). These demonstrations relied on
planted canaries, atypical training regimes, or prior knowledge of the secret's
format.

Model scale was rising fast. GPT-2 reached 1.5 billion parameters (Radford et
al., 2019), GPT-3 reached 175 billion (Brown et al., 2020), and T5 trained on
near-terabyte corpora (Raffel et al., 2020), with scaling laws predicting
continued returns from size (Kaplan et al., 2020). Differentially private
training (Abadi et al., 2016; McMahan et al., 2018) was rarely used at this scale
because of its accuracy and compute costs, though production systems had begun
designing autocomplete models to avoid memorizing user data (Chen et al., 2019;
Ramaswamy et al., 2020). The framework of privacy as contextual integrity
(Nissenbaum, 2004) offered one way to say when reproducing public text is still
a violation: when it moves data out of the context for which it was shared.

</details>

<details>
<summary><h2>Essential Readings</h2></summary>

- [Scalable Extraction of Training Data from (Production) Language Models](https://arxiv.org/abs/2311.17035) — the follow-up that scales extraction to aligned production models and measures total memorization rather than confirming individual examples.
- [Extracting Training Data from Diffusion Models](https://arxiv.org/abs/2301.13188) — the same memorization question in image generation, where a training photograph is regenerated from its caption.

</details>

<details>
<summary><h4>References</h4></summary>

- Abadi, M., Chu, A., Goodfellow, I., McMahan, H.B., Mironov, I., Talwar, K., and
  Zhang, L. "Deep Learning with Differential Privacy." ACM Conference on Computer
  and Communications Security (CCS), 2016.
- Brown, T.B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P.,
  Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. "Language Models are
  Few-Shot Learners." arXiv:2005.14165, 2020.
- Carlini, N., Liu, C., Erlingsson, Ú., Kos, J., and Song, D. "The Secret Sharer:
  Evaluating and Testing Unintended Memorization in Neural Networks." USENIX
  Security Symposium, 2019.
- Chen, M.X., Lee, B.N., Bansal, G., Cao, Y., Zhang, S., Lu, J., Tsay, J., Wang,
  Y., Dai, A.M., Chen, Z., Sohn, T., and Wu, Y. "Gmail Smart Compose: Real-Time
  Assisted Writing." ACM SIGKDD (KDD), 2019.
- Feldman, V. "Does Learning Require Memorization? A Short Tale about a Long
  Tail." ACM Symposium on Theory of Computing (STOC), 2020.
- Feldman, V. and Zhang, C. "What Neural Networks Memorize and Why: Discovering
  the Long Tail via Influence Estimation." Advances in Neural Information
  Processing Systems (NeurIPS), 2020.
- Fredrikson, M., Jha, S., and Ristenpart, T. "Model Inversion Attacks that
  Exploit Confidence Information and Basic Countermeasures." ACM Conference on
  Computer and Communications Security (CCS), 2015.
- Kaplan, J., McCandlish, S., Henighan, T., Brown, T.B., Chess, B., Child, R.,
  Gray, S., Radford, A., Wu, J., and Amodei, D. "Scaling Laws for Neural Language
  Models." arXiv:2001.08361, 2020.
- McMahan, H.B., Ramage, D., Talwar, K., and Zhang, L. "Learning Differentially
  Private Recurrent Language Models." International Conference on Learning
  Representations (ICLR), 2018.
- Nissenbaum, H. "Privacy as Contextual Integrity." Washington Law Review, 2004.
- Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I.
  "Language Models are Unsupervised Multitask Learners." 2019.
- Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou,
  Y., Li, W., and Liu, P.J. "Exploring the Limits of Transfer Learning with a
  Unified Text-to-Text Transformer." Journal of Machine Learning Research (JMLR),
  2020.
- Ramaswamy, S., Thakkar, O., Mathews, R., Andrew, G., McMahan, H.B., and
  Beaufays, F. "Training Production Language Models without Memorizing User
  Data." arXiv:2009.10031, 2020.
- Shokri, R., Stronati, M., Song, C., and Shmatikov, V. "Membership Inference
  Attacks against Machine Learning Models." IEEE Symposium on Security and
  Privacy (S&P), 2017.
- Thakkar, O., Ramaswamy, S., Mathews, R., and Beaufays, F. "Understanding
  Unintended Memorization in Federated Learning." arXiv:2006.07490, 2020.
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N.,
  Kaiser, Ł., and Polosukhin, I. "Attention Is All You Need." Advances in Neural
  Information Processing Systems (NIPS), 2017.
- Yeom, S., Giacomelli, I., Fredrikson, M., and Jha, S. "Privacy Risk in Machine
  Learning: Analyzing the Connection to Overfitting." IEEE Computer Security
  Foundations Symposium (CSF), 2018.
- Zanella-Béguelin, S., Wutschitz, L., Tople, S., Rühle, V., Paverd, A.,
  Ohrimenko, O., Köpf, B., and Brockschmidt, M. "Analyzing Information Leakage of
  Updates to Natural Language Models." ACM Conference on Computer and
  Communications Security (CCS), 2020.

</details>
