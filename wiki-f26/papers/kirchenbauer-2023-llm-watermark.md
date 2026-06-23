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
  - language-models
  - threat-model
  - statistics
---

# A Watermark for Large Language Models

## High-level overview

Text produced by a large language model can be hard to tell apart from text
written by a person, which complicates tracing the provenance of online content
and excluding machine text from web-scale training corpora. This work embeds a
watermark into generated text at decoding time so that the source of a passage
can later be established from the text alone. The watermark is a hidden
statistical pattern, imperceptible to a human reader yet detectable by an
algorithm that holds the right key. Before each token is sampled, the method
seeds a pseudo-random generator from a hash of the preceding token, uses that
seed to split the vocabulary into a "green list" and a "red list," and then
softly promotes the green-list tokens by adding a constant to their logits.
Across a span of tokens, watermarked text carries far more green-list tokens
than a human writer would produce by chance.

Detection needs neither the model nor its parameters nor its API, only the text
and the hashing scheme. A detector recomputes the green list at each position,
counts green-list tokens, and applies a one-proportion z-test against the null
hypothesis that the text was written with no knowledge of the green-list rule,
which yields an interpretable p-value and a controllable false-positive rate.
How strongly a passage can be watermarked depends on its entropy: high-entropy
spans, where the model has many plausible next tokens, absorb the green-list
bias with little change to the text, while low-entropy spans, where one
continuation is nearly forced, carry almost no signal and resist watermarking.
The authors derive an information-theoretic analysis relating watermark strength
to a measure of next-token-distribution entropy, report that the watermark is
detectable from short spans with negligible cost to text quality measured by
[perplexity](../concepts/perplexity.md), and study how it degrades under attacks
that edit, paraphrase, or otherwise rewrite the text. Experiments use a
multi-billion-parameter model from the Open Pre-trained Transformer (OPT) family
(Zhang et al., 2022). Decoded terminology: the watermark marks the output text
rather than the model's weights, and serves provenance (telling machine text
from human text) rather than ownership; the green list and red list are a
per-position pseudo-random partition of the token vocabulary, not fixed word
sets.

**Threat Model:** The watermark is embedded by the model provider, the party
that controls decoding and can modify the model's output logits before a token
is drawn; embedding needs no retraining and can be retrofitted to any model that
generates by sampling from a next-token distribution. The detector is any third
party holding the hash function and key, for example a platform screening
uploaded text; it needs only the candidate text, not the model's parameters or
API, so the detection algorithm can be open-sourced even when the model is
closed, or kept private behind an API. The adversary is a user who obtains
watermarked text and wants it to pass as un-watermarked: it edits tokens by
insertion, deletion, or substitution, paraphrases the text by hand or with a
weaker public language model, or applies generative tricks such as emoji,
homoglyph, or tokenization manipulations that scramble the green-list
computation; with knowledge of a public scheme it could instead try to forge the
watermark onto text the provider never generated. The paper analyzes both a
worst-case adversary with complete knowledge of the watermark and a setting
where the scheme is kept secret, and it assumes the adversary lacks a language
model as strong as the watermarked one, since an equally strong model would
remove any need to use the watermarked API. The provider's claim is that false
positives are statistically improbable regardless of a human author's writing
style, and that removing the watermark from a long passage requires changing a
large fraction of its tokens.

## Why read this

<!-- instructor: confirm -->

Decoding-time watermarking of language-model output became practical and
analyzable here: the watermark needs no model retraining, the detector needs
neither the model nor its API, and detection reports an interpretable p-value
rather than a trained classifier's score. The information-theoretic tie between a
passage's entropy and how strongly it can be marked sets the method apart from
earlier rule-based text watermarking and explains why some text resists marking.
The paper rewards attention to both what the test guarantees and where the
authors place the watermark's limits.

## Basic Background

### Language models, tokens, and decoding

A [language model](../concepts/language-model-pretraining.md) for next-token
prediction reads a sequence of tokens, the units of text drawn from a fixed
vocabulary of tens of thousands of entries, and outputs a vector of logits, one
score per vocabulary token. A softmax turns those logits into a probability
distribution over the next token.
[Decoding](../concepts/decoding-strategies.md) is the procedure that turns these
distributions into text: greedy decoding takes the most probable token,
multinomial sampling draws from the distribution, and beam search keeps several
high-scoring candidate continuations. The provider that runs the model sees and
can alter the logits before a token is drawn, which is the hook the watermark
uses.

### Entropy of the next-token distribution

The entropy of a next-token distribution measures how spread out it is. A
high-entropy position has many tokens of comparable probability, so several
continuations are about equally good; a low-entropy position concentrates almost
all mass on one token, so the next token is nearly determined by what came
before. Code and stock phrases sit at the low-entropy end, where "Barack" is
almost always followed by "Obama." This quantity governs how much a
sampling-time intervention can change which token is chosen without making the
text worse.

### Perplexity and generation quality

[Perplexity](../concepts/perplexity.md) is the standard intrinsic measure of how
well a language model predicts a sequence, the exponential of the average
per-token negative log-likelihood. Lower perplexity under a reference model
indicates text the model finds more fluent and predictable. It serves here as
the yardstick for whether biasing the output toward green-list tokens degrades
quality.

### Detecting a statistical signal

Casting watermark detection as a hypothesis test treats the count of green-list
tokens as a test statistic under the null hypothesis that the writer had no
knowledge of the green-list rule. A one-proportion z-test compares the observed
green-token fraction against the fraction expected by chance and reports a
p-value, the probability of seeing so many green tokens if the null held. The
trade-off between true-positive and false-positive rates as the decision
threshold moves is summarized by an
[ROC curve and its AUC](../concepts/roc-curves.md); security applications demand
very low false-positive rates, since flagging human text as machine-generated is
costly.

### Watermarking and provenance

Digital watermarking hides an identifying signal inside a media object so its
source can be recovered later; embedding hidden information into data more
generally is steganography.
[Model watermarking](../concepts/model-watermarking.md) marks a trained model's
weights or behavior to prove ownership of a copy.
[Text or output watermarking](../concepts/llm-watermarking.md) instead marks the
content a model generates, so a passage can be attributed to a machine source,
which is the provenance setting the green-list method targets. Watermarking
discrete text has historically been harder than watermarking continuous media
such as images or audio, because small edits to wording are conspicuous.

## Paper Context

By late 2022 the public release of capable chat models had sharpened concern
about machine-generated text at scale: automated misinformation and bot content,
academic and professional dishonesty, and the contamination of future training
corpora by synthetic text scraped from the web. The ability to detect and audit
machine-generated text was argued to be a basic instrument of harm reduction for
language models (Bender et al., 2021; Crothers et al., 2022), and an explicit
ethical case was made for watermarking such text (Grinbaum and Adomaitis, 2022).

Watermarking natural language had a long history before neural models. Marking
discrete text was considered hard relative to continuous media (Katzenbeisser
and Petitcolas, 2000), and early schemes embedded a mark by editing syntactic
structure or substituting synonyms in a given text (Atallah et al., 2001;
Topkara et al., 2006; Venugopal et al., 2011), though the limited flexibility of
pre-neural methods meant that strong marks tended to degrade quality (Jalil and
Mirza, 2009). Neural language models improved linguistic steganography and
watermarking, encoding hidden bits by partitioning the vocabulary or by editing
already-generated text (Fang et al., 2017; Ziegler et al., 2019; Ueoka et al.,
2021), and an end-to-end system trained encoder and decoder networks together to
trace text provenance (Abdelnabi and Fritz, 2021); related schemes watermarked
the outputs of text-generation APIs to protect them against imitation (He et
al., 2022). A separate line marks the model's parameters rather than its output,
to defend against model stealing rather than to establish provenance (Adi et
al., 2018; Boenisch, 2021; Gu et al., 2022).

An alternative to embedding any signal is post-hoc detection: training a
classifier to separate machine from human text using language-model features or
fine-tuned detectors (Zellers et al., 2019; Jawahar et al., 2020). Such
detectors exploit statistical residue that models leave in their output, but
they lose ground as models improve, with detectors built for one generation of
model struggling on the next (Gambini et al., 2022), and they can be evaded by
adversarial edits (Wolff and Wolff, 2022); deployed tools of this kind, such as
GPTZero, drew scrutiny over false positives on atypical human writing (Tian,
2023). Concurrently, a cryptographic approach to watermarking language-model
output was announced as work in progress (Aaronson, 2022).

## Reading guidance

- Section 1.1: notation and language-model basics; the vocabulary and the
  logit-to-distribution pipeline the method intervenes on.
- Section 1.2, with the "quick brown fox" sentence and the for-loop: the two
  example sequences carry the difficulty argument; note what property of a
  sequence the method needs to leave a signal.
- Section 2, Algorithm 1: the hard red-list proof of concept, its z-test, and
  the argument for how many tokens an attacker must change to scrub it.
- Section 3, Algorithm 2: the soft red-list rule that adds a constant to
  green-list logits and adapts its effect to entropy.
- Section 4, Definition 4.1 and Theorem 4.2: the spike-entropy analysis
  predicting the green-token count. Attention anchor: the analysis assumes the
  red list is sampled uniformly at random rather than pseudo-randomly as in the
  deployed method; note where the text says this gap is taken up.
- Section 4.1 and Table 1: detection sensitivity and the failure cases,
  including memorized text the model reproduces verbatim.
- Section 5: keeping the watermark secret behind an API versus open-sourcing the
  detector.
- Section 6, Figures 2 to 4 with the error tables: the strength-versus-quality
  trade-off, swept over the green-list fraction and the logit bias.
- Section 7, Figures 5 and 6: the catalog of removal attacks (insertion,
  deletion, substitution, paraphrase, homoglyph, the emoji generative attack,
  and the T5 span-replacement attack) and what each costs the attacker.
  Attention anchor: Section 7 states the assumption about which models the
  attacker has access to; note what the security argument rests on.
- Section 8: where the authors place the scheme relative to steganography and to
  post-hoc detection.
- Section 9: the open questions left for future work, including robust hashing
  and detection over a streaming or partially watermarked span.

## Motivating questions

1. What does detecting the watermark require, and what access to the model or
   its API does it assume?
2. What does adding the watermark cost in the quality of the generated text?
3. How does the predictability of a passage, its entropy, affect whether it can
   be watermarked at all?
4. What kinds of editing or rewriting could remove the watermark, and what does
   each cost the party attempting it?
5. What can the model provider keep secret or tune per context, and what must a
   detector know to run the test?

## Supplementary readings

- [Tree-Ring Watermarks: Fingerprints for Diffusion Images that are Invisible and Robust](https://arxiv.org/abs/2305.20030) — the analogue for diffusion-image provenance, a contrast in modality.
- [Media Forensics and DeepFakes: An Overview](https://arxiv.org/abs/2001.06564) — the detection-after-the-fact tradition this proactive approach departs from.

## References

Entries read off the paper's bibliography (arXiv 2301.10226v4, pages 13-17).

- Aaronson, S. "My AI Safety Lecture for UT Effective Altruism." 2022.
- Abdelnabi, S. and Fritz, M. "Adversarial Watermarking Transformer: Towards Tracing Text Provenance with Data Hiding." IEEE Symposium on Security and Privacy (SP), 2021.
- Adi, Y., Baum, C., Cisse, M., Pinkas, B., and Keshet, J. "Turning Your Weakness Into a Strength: Watermarking Deep Neural Networks by Backdooring." USENIX Security Symposium, 2018.
- Atallah, M. J., Raskin, V., Crogan, M., Hempelmann, C., Kerschbaum, F., Mohamed, D., and Naik, S. "Natural Language Watermarking: Design, Analysis, and a Proof-of-Concept Implementation." Information Hiding (Lecture Notes in Computer Science), 2001.
- Bender, E. M., Gebru, T., McMillan-Major, A., and Shmitchell, S. "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" ACM Conference on Fairness, Accountability, and Transparency (FAccT), 2021.
- Boenisch, F. "A Systematic Review on Model Watermarking for Neural Networks." Frontiers in Big Data, 4, 2021.
- Crothers, E., Japkowicz, N., and Viktor, H. "Machine Generated Text: A Comprehensive Survey of Threat Models and Detection Methods." arXiv:2210.07321, 2022.
- Fang, T., Jaggi, M., and Argyraki, K. "Generating Steganographic Text with LSTMs." Annual Meeting of the Association for Computational Linguistics (ACL), Student Research Workshop, 2017.
- Gambini, M., Fagni, T., Falchi, F., and Tesconi, M. "On Pushing DeepFake Tweet Detection Capabilities to the Limits." ACM Web Science Conference (WebSci), 2022.
- Grinbaum, A. and Adomaitis, L. "The Ethical Need for Watermarks in Machine-Generated Language." arXiv:2209.03118, 2022.
- Gu, C., Huang, C., Zheng, X., Chang, K.-W., and Hsieh, C.-J. "Watermarking Pre-trained Language Models with Backdooring." arXiv:2210.07543, 2022.
- He, X., Xu, Q., Lyu, L., Wu, F., and Wang, C. "Protecting Intellectual Property of Language Generation APIs with Lexical Watermark." AAAI Conference on Artificial Intelligence, 2022.
- Jalil, Z. and Mirza, A. M. "A Review of Digital Watermarking Techniques for Text Documents." International Conference on Information and Multimedia Technology (ICIMT), 2009.
- Jawahar, G., Abdul-Mageed, M., and Lakshmanan, L. V. S. "Automatic Detection of Machine Generated Text: A Critical Survey." International Conference on Computational Linguistics (COLING), 2020.
- Katzenbeisser, S. and Petitcolas, F. A. P. "Information Hiding Techniques for Steganography and Digital Watermarking." Artech House, 2000.
- Tian, E. "GPTZero Update v1." 2023.
- Topkara, U., Topkara, M., and Atallah, M. J. "The Hiding Virtues of Ambiguity: Quantifiably Resilient Watermarking of Natural Language Text through Synonym Substitutions." ACM Workshop on Multimedia and Security (MM&Sec), 2006.
- Ueoka, H., Murawaki, Y., and Kurohashi, S. "Frustratingly Easy Edit-based Linguistic Steganography with a Masked Language Model." Conference of the North American Chapter of the Association for Computational Linguistics (NAACL), 2021.
- Venugopal, A., Uszkoreit, J., Talbot, D., Och, F., and Ganitkevitch, J. "Watermarking the Outputs of Structured Prediction with an Application in Statistical Machine Translation." Conference on Empirical Methods in Natural Language Processing (EMNLP), 2011.
- Wolff, M. and Wolff, S. "Attacking Neural Text Detectors." arXiv:2002.11768, 2022.
- Zellers, R., Holtzman, A., Rashkin, H., Bisk, Y., Farhadi, A., Roesner, F., and Choi, Y. "Defending Against Neural Fake News." Advances in Neural Information Processing Systems (NeurIPS), 2019.
- Zhang, S., Roller, S., Goyal, N., Artetxe, M., Chen, M., Chen, S., Dewan, C., Diab, M., Li, X., Lin, X. V., Mihaylov, T., Ott, M., Shleifer, S., Shuster, K., Simig, D., Koura, P. S., Sridhar, A., Wang, T., and Zettlemoyer, L. "OPT: Open Pre-trained Transformer Language Models." 2022.
- Ziegler, Z., Deng, Y., and Rush, A. "Neural Linguistic Steganography." Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), 2019.
