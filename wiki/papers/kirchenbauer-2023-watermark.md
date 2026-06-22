---
title: "A Watermark for Large Language Models"
authors:
  - Kirchenbauer, John
  - Geiping, Jonas
  - Wen, Yuxin
  - Katz, Jonathan
  - Miers, Ian
  - Goldstein, Tom
year: 2023
section: "Media Forensics and Proactive Provenance"
primary: true
arxiv: "2301.10226"
tags:
  - watermarking
  - provenance
  - llm
  - language-models
---

# A Watermark for Large Language Models

## High-level overview

Machine-generated text has become hard to distinguish from human writing, which
complicates flagging automated disinformation, detecting academic dishonesty, and
filtering synthetic data that would otherwise contaminate future training
corpora. This paper makes text produced by a large language model algorithmically
detectable by embedding a statistical **watermark** as the text is generated. The
scheme is a small change to the model's sampling step and needs no retraining.
Before each token is produced, a hash of the preceding token seeds a pseudorandom
partition of the vocabulary into a "green list" of fraction `gamma` and a
complementary "red list". A soft rule adds a constant bias `delta` to the logits
of the green-list tokens, nudging the model toward green tokens at positions where
many continuations are about equally good, while leaving near-deterministic
positions essentially unchanged. Watermarked text therefore contains many more
green tokens than ordinary text would.

Detection needs no access to the model, its parameters, or its API. A party who
knows the hash rule (and, in the private variant, the secret key) recomputes the
green list at each position and counts green tokens. That count feeds a
one-proportion z-test against the null hypothesis that the text was written with
no knowledge of the green-list rule, which yields an interpretable p-value.
Because a natural writer lands on the green list only with probability `gamma`
per token, a watermarked passage produces a count far above chance, and the rate
at which human text is falsely flagged can be driven very low. The watermark is
detectable from short spans (as few as roughly 25 tokens), costs little in text
quality as measured by perplexity, and an accompanying information-theoretic
analysis ties detectability to the entropy of the generated text. The paper
evaluates the watermark on a multi-billion-parameter model from the Open
Pretrained Transformer (OPT) family, describes a keyed private-detection mode,
and surveys attacks that try to scrub the mark.

**Threat Model:** The defender is the operator of a language model, who embeds the
watermark at generation time by biasing the sampling distribution; this is an
inference-time intervention that leaves the model weights unchanged. Detection is
run by a third party such as a platform, using either a public, open-sourced
detector or a private detector that holds a secret key behind an API. The
adversary is a user who obtains watermarked output and wants to launder it into
text that reads as un-watermarked while preserving its meaning and fluency. In the
public setting the adversary knows the watermarking rule, though each position's
green list is content-dependent through the hash; in the private setting the key,
and therefore the partition, is hidden. The adversary may edit the text within a
budget (inserting, deleting, or substituting a limited fraction of tokens),
paraphrase it with a separate and weaker language model, or apply tokenization
tricks such as whitespace, homoglyph, or prompted "emoji" edits. The paper assumes
the adversary's own models are weaker than the watermarked one, since an equally
strong model would remove the need to launder text at all. The defender claims
detection with a controllable, statistically small false-positive rate that does
not depend on the human writer's style, and graceful degradation under editing:
removing the mark from a long passage requires modifying a large fraction of its
tokens.

## Why read this

As AI-generated content becomes more popular, provenance has become even more
important. This paper introduces content watermarking to that end.

## Basic Background

### Language models, tokens, and decoding

A large language model generates text autoregressively: at each step it produces
a probability distribution over a fixed vocabulary of
[tokens](../concepts/tokenization.md), conditioned on the prompt and the tokens so
far, and the next token is drawn from it. The distribution comes from passing the
model's output logits through a softmax; how a token is then chosen is the
[decoding strategy](../concepts/decoding-strategies.md), such as greedy decoding,
multinomial sampling, or beam search. The model itself is the product of
[language-model pretraining](../concepts/language-model-pretraining.md) on a large
corpus. [Perplexity](../concepts/perplexity.md), the exponentiated average
negative log-likelihood under a reference model, is the standard measure of how
fluent a passage is and is used here as the proxy for text quality.

### Entropy of the next-token distribution

At some positions the model is nearly certain of the next token; at others many
continuations are about equally likely. [Shannon
entropy](../concepts/entropy.md) quantifies this spread: low entropy means a
single dominant token, high entropy means many comparable candidates. The
distinction is central background here, because a scheme that perturbs token
choice can act freely only where the distribution is spread out.

### Detecting a signal with a hypothesis test

The watermark is read out with a [statistical hypothesis
test](../concepts/statistical-hypothesis-testing.md). The relevant instance is the
one-proportion z-test: given a count of green tokens out of `T`, it standardizes
the count against what a null model (text written with no knowledge of the rule)
would produce and converts the result into a p-value and a false-positive (type I
error) rate. Detector performance across thresholds is summarized by [ROC curves
and AUC](../concepts/roc-curves.md), read at low false-positive rates as is
standard for detection tasks.

### Hiding information in text: steganography and watermarking

[Steganography](../concepts/steganography.md) hides information inside
ordinary-looking content so its presence is undetectable, and digital
watermarking is the narrower task of embedding a source-identifying marker that
resists removal. Watermarking the *content* a model emits is distinct from
[watermarking the model's parameters](../concepts/model-watermarking.md), which
marks the model itself to support ownership claims. The detector here needs no
model access, a [black-box](../concepts/white-box-black-box.md) setting relative
to the generator.

### Keyed pseudorandomness

The green/red partition at each position is produced by seeding a pseudorandom
generator with a hash of preceding tokens. In the private mode this becomes a
[pseudorandom function](../concepts/pseudorandom-function.md) keyed by a secret (a
block cipher such as AES, or a keyed cryptographic hash), so the partition is
reproducible for detection with the key but unpredictable without it.

## Paper Context

As large language models grew fluent enough to produce text indistinguishable
from human writing, detecting machine-generated text became a recognized
harm-reduction problem. Two families of approaches predate this work: post-hoc
detection, which inspects text after the fact, and watermarking and
steganography, which plant a signal at generation time.

Post-hoc detection trains a classifier to separate machine text from human text
using model features or fine-tuned detectors (Zellers et al., 2019; Jawahar et
al., 2020), or measures statistical regularities such as low variation in
per-token perplexity (Tian, 2023). These detectors weaken as models improve:
strategies that separate one generation of model output already struggle on the
next (Gambini et al., 2022), and the detectors are themselves vulnerable to
adversarial edits (Wolff and Wolff, 2022). They also risk false positives on
atypical human writers.

The other family hides a signal in the text itself, a problem long considered
hard for discrete media because edits to text are perceptible (Katzenbeisser and
Petitcolas, 2000). Early natural-language watermarking edited syntactic parse
trees or substituted synonyms under rule-based models of language (Atallah et al.,
2001), which constrained the output and degraded quality. Neural methods improved
fluency: recurrent and transformer-based steganography embeds bits by restricting
or biasing token choice (Fang et al., 2017; Ziegler et al., 2019), end-to-end
systems learn both to embed and to recover a watermark (Abdelnabi and Fritz,
2021), and cryptographic steganography was adapted to realistic generative-text
channels (Kaptchuk et al., 2021).

A separate line watermarks a model's parameters rather than its output, to claim
ownership of a stolen copy, often by training in a backdoor trigger (Adi et al.,
2018; Gu et al., 2022); there the goal is provenance of the model, not of the
text. Concurrently, a cryptographic approach to watermarking language-model
output was announced in collaboration with OpenAI, biasing token choice through
hashed n-grams (Aaronson, 2022).

## Reading guidance

- Sections 1.2 and 2 (the "hard" red list): the difficulty of watermarking
  low-entropy text, then the simplest scheme, which bars red-list tokens outright;
  the proof of concept the soft rule later replaces.
- Algorithm 2 and Section 3: the soft watermark, where `gamma` sets the green-list
  fraction and `delta` the logit bias. This is the mechanism used throughout.
- Section 4 and Theorem 4.2: the information-theoretic analysis, which defines
  "spike entropy" to bound the expected green-token count. Note that the section
  reports both a theoretical sensitivity bound and an empirical sensitivity; note
  which is larger and which the text foregrounds.
- Section 4.2 and Theorem 4.3: the bound on the watermark's impact on perplexity.
- Figures 2 to 4 and Table 2: the strength-versus-quality tradeoff across `gamma`
  and `delta`, the role of beam search, and the detection error rates.
- Section 5 and Algorithm 3: the private, keyed watermark, the "attack
  amplification" effect, and the window-size parameter `h`. Note the tradeoff the
  choice of `h` sets up.
- Sections 7 and 7.1 with Figure 6: the catalog of removal attacks and the single
  one evaluated quantitatively (span replacement with a separate T5 model).
  Re-read the threat model stated at the start of Section 7, and note which
  attacks are measured with numbers and which are discussed qualitatively.
- Section 8: where the scheme sits relative to post-hoc detection and earlier
  steganography.

## Motivating questions

1. What does the detector need to know about the model to run, and what guarantee
   does it give about falsely flagging human-written text?
2. How does the strength of the watermark depend on the entropy of the text being
   generated?
3. What does embedding the watermark cost in the quality of the generated text?
4. What must an adversary do to remove the watermark, and how does detection
   degrade as the text is edited?
5. What changes between the public watermark and the private, keyed version?

## Supplementary readings

- [Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust](https://arxiv.org/abs/2305.20030) — the analogous problem for image generators: a watermark planted in a diffusion model's initial noise that survives common image transformations.
- [Media Forensics and DeepFakes: An Overview](https://arxiv.org/abs/2001.06564) — the broader provenance landscape, surveying how synthetic media is produced and the forensic methods used to detect it.

## References

- Aaronson, S. "My AI Safety Lecture for UT Effective Altruism." Blog post, November 2022. <https://scottaaronson.blog/?p=6823>.
- Abdelnabi, S. and Fritz, M. "Adversarial Watermarking Transformer: Towards Tracing Text Provenance with Data Hiding." IEEE Symposium on Security and Privacy (S&P), 2021.
- Adi, Y., Baum, C., Cisse, M., Pinkas, B., and Keshet, J. "Turning Your Weakness Into a Strength: Watermarking Deep Neural Networks by Backdooring." USENIX Security Symposium, 2018.
- Atallah, M. J., Raskin, V., Crogan, M., Hempelmann, C., Kerschbaum, F., Mohamed, D., and Naik, S. "Natural Language Watermarking: Design, Analysis, and a Proof-of-Concept Implementation." Information Hiding (Lecture Notes in Computer Science), pp. 185-200, 2001.
- Fang, T., Jaggi, M., and Argyraki, K. "Generating Steganographic Text with LSTMs." ACL Student Research Workshop, pp. 100-106, 2017.
- Gambini, M., Fagni, T., Falchi, F., and Tesconi, M. "On Pushing DeepFake Tweet Detection Capabilities to the Limits." ACM Web Science Conference (WebSci), pp. 154-163, 2022.
- Gu, C., Huang, C., Zheng, X., Chang, K.-W., and Hsieh, C.-J. "Watermarking Pre-trained Language Models with Backdooring." arXiv:2210.07543, 2022.
- Jawahar, G., Abdul-Mageed, M., and Lakshmanan, V. S. "Automatic Detection of Machine Generated Text: A Critical Survey." International Conference on Computational Linguistics (COLING), pp. 2296-2309, 2020.
- Kaptchuk, G., Jois, T. M., Green, M., and Rubin, A. D. "Meteor: Cryptographically Secure Steganography for Realistic Distributions." ACM SIGSAC Conference on Computer and Communications Security (CCS), pp. 1529-1548, 2021.
- Katzenbeisser, S. and Petitcolas, F. A. P. "Information Hiding Techniques for Steganography and Digital Watermarking." Artech House, 2000.
- Tian, E. "GPTZero Update v1." January 2023. <https://gptzero.substack.com/p/gptzero-update-v1>.
- Wolff, M. and Wolff, S. "Attacking Neural Text Detectors." arXiv:2002.11768, 2022.
- Zellers, R., Holtzman, A., Rashkin, H., Bisk, Y., Farhadi, A., Roesner, F., and Choi, Y. "Defending Against Neural Fake News." Advances in Neural Information Processing Systems (NeurIPS), 2019.
- Ziegler, Z., Deng, Y., and Rush, A. "Neural Linguistic Steganography." Conference on Empirical Methods in Natural Language Processing (EMNLP-IJCNLP), pp. 1210-1215, 2019.
