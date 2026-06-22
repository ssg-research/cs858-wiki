# Concepts

Background concepts the papers rely on. Each page is a short, self-contained
explanation you can read on its own or reach from a paper that uses it.

| Concept | Summary |
| --- | --- |
| [activation-steering](activation-steering.md) | Steering a frozen model at inference by adding a vector to its hidden activations; difference-of-activation steering vectors, ActAdd, and ITI. |
| [adversarial-examples](adversarial-examples.md) | The evasion phenomenon: small input perturbations that flip a prediction. |
| [adversarial-threat-model](adversarial-threat-model.md) | How an adversary's power is specified: perturbation set, knowledge, timing. |
| [adversarial-training](adversarial-training.md) | Training on adversarially perturbed inputs as a defense. |
| [algorithmic-fairness](algorithmic-fairness.md) | Group fairness across sensitive subgroups under metrics like demographic parity and equalized odds; discriminatory behavior as the risk and group-fairness constraints as the defense. |
| [attribute-inference](attribute-inference.md) | Inferring a record's hidden sensitive attribute value from a model's observables; distinct from membership and property inference, and the "just imputation?" debate. |
| [backdoor-attacks](backdoor-attacks.md) | A trigger-fired hidden behavior trained into a model via data poisoning; the overcapacity that enables it and its reuse as the mechanism behind black-box model watermarking. |
| [convolutional-neural-network](convolutional-neural-network.md) | CNNs for image classification: learned convolutional filters, pooling, a softmax head, and the standard backbones (AlexNet, VGG, ResNet, DenseNet). |
| [cryptographic-commitment](cryptographic-commitment.md) | A binding, hiding token published for a value and opened later; with a time-stamped public log it gives proof of priority for ownership claims. |
| [data-poisoning](data-poisoning.md) | Corrupting training data to change what a model learns: availability vs targeted/integrity poisoning, backdoors as the trigger-conditioned subclass, and why training-set sanitization defenses presume data access. |
| [data-reconstruction](data-reconstruction.md) | Privacy attacks that recover whole training records or their content: model inversion, gradient inversion, and verbatim extraction; recovers content where membership inference recovers a bit. |
| [decoding-strategies](decoding-strategies.md) | How an LLM turns next-token distributions into text: greedy, temperature, top-k, top-p, and prefilling. |
| [dense-retrieval](dense-retrieval.md) | Retrieving documents by embedding the query and passages and ranking by vector similarity (top-k); the neural alternative to BM25 and the retriever inside RAG. |
| [differential-privacy](differential-privacy.md) | The formal bound on any single example's influence; DP-SGD and the epsilon guarantee. |
| [direct-preference-optimization](direct-preference-optimization.md) | Aligning an LM to pairwise preferences directly, without a separate reward model or RL loop; the DPO alternative to RLHF. |
| [distributed-representations](distributed-representations.md) | Information spread across activation patterns rather than single neurons; transformer hidden states and their emergent, often linear, semantic structure. |
| [empirical-risk-minimization](empirical-risk-minimization.md) | Average training loss as a proxy for expected loss; the baseline objective. |
| [entropy](entropy.md) | Shannon entropy: how spread out or uncertain a discrete distribution is; the per-position uncertainty of a language model's next-token distribution. |
| [feature-attribution](feature-attribution.md) | Post-hoc explanations attributing a prediction to inputs or training data: saliency/attribution methods, influence functions, and counterfactual recourse; transparency tools that also widen the attack surface. |
| [fgsm](fgsm.md) | The one-step gradient-sign attack and its role as a baseline. |
| [gaussian-mechanism](gaussian-mechanism.md) | Sensitivity and noise calibrated to it; the additive-noise recipe behind DP mechanisms. |
| [gradient-clipping](gradient-clipping.md) | Norm-rescaling gradients; a training stabilizer that, per example, becomes a sensitivity bound. |
| [gradient-masking](gradient-masking.md) | The defense failure mode where gradients become useless but worst-case loss stays high. |
| [instruction-tuning](instruction-tuning.md) | Fine-tuning a base LM to follow natural-language instructions; the instruction-following objective. |
| [jailbreak](jailbreak.md) | A prompt that elicits behavior a safety-trained LLM was trained to refuse; distinct from adversarial examples. |
| [kl-divergence](kl-divergence.md) | Asymmetric measure of how far one distribution is from a reference; the per-token unit of how much alignment moved the base model. |
| [knowledge-distillation](knowledge-distillation.md) | Training a student to match a teacher's output distribution (soft labels); its equivalence to minimizing KL and its link to model extraction. |
| [language-model-pretraining](language-model-pretraining.md) | Autoregressive next-token pretraining; the pretraining objective, distribution, and base model. |
| [likelihood-ratio-test](likelihood-ratio-test.md) | Deciding between two hypotheses by their likelihood ratio; Neyman-Pearson optimality. |
| [linear-probing](linear-probing.md) | Training a simple classifier on a layer's activations to test what it encodes; locating concept directions, and the decodable-versus-used caveat. |
| [llm-tool-use](llm-tool-use.md) | An LLM emitting calls to external tools and acting on their outputs; chaining calls toward a goal yields an agent. |
| [lp-norms](lp-norms.md) | ℓ0 / ℓ2 / ℓ-infinity balls as perturbation budgets and proxies for perceptual similarity. |
| [machine-unlearning](machine-unlearning.md) | Removing chosen training data's influence from a trained model without full retraining; exact vs approximate unlearning and the right-to-be-forgotten motivation. |
| [mechanistic-interpretability](mechanistic-interpretability.md) | The bottom-up program of reverse-engineering a network into circuits of neurons and features; its identified circuits, labor cost, and the top-down contrast. |
| [membership-inference](membership-inference.md) | Predicting whether a specific example was in a model's training set; the standard privacy audit. |
| [memorization](memorization.md) | Per-example fitting, random-label capacity, and the long-tail argument; the signal privacy attacks exploit. |
| [model-extraction](model-extraction.md) | Attacks that reproduce a deployed model's parameters, hyperparameters, architecture, or functionality from query access; the fidelity-versus-accuracy axes and the MLaaS setting. |
| [model-watermarking](model-watermarking.md) | Embedding an owner-verifiable marker in a trained model; white-box (in the weights) vs black-box (backdoor-based trigger set) verification, and the assumption that the owner controls training. |
| [overfitting](overfitting.md) | The train-test generalization gap, the bias-variance picture, and dataset size and model capacity as the levers; the aggregate signal privacy and robustness attacks both interact with. |
| [perplexity](perplexity.md) | How well an LM predicts a sequence (exponentiated cross-entropy); the LM quality metric and the per-example membership signal in extraction attacks. |
| [principal-component-analysis](principal-component-analysis.md) | The orthogonal directions of greatest variance in a dataset; a low-dimensional summary used to recover salient directions in neural activations. |
| [privacy-budget](privacy-budget.md) | The (epsilon, delta) budget, composition theorems, accountants, and amplification by subsampling. |
| [projected-gradient-descent](projected-gradient-descent.md) | Gradient step plus projection; the constrained-optimization primitive behind the PGD attack. |
| [prompt-injection](prompt-injection.md) | Adversarial instructions in a prompt or ingested content that override the intended task; direct and indirect. |
| [property-inference](property-inference.md) | Inferring a global property of a model's training distribution (e.g., a subgroup's fraction) rather than anything about one record; distribution inference and its distinction from attribute and membership inference. |
| [pseudorandom-function](pseudorandom-function.md) | A keyed function whose outputs look random without the key but are reproducible with it; block ciphers (AES) and keyed cryptographic hashes (SHA-3) as instances. |
| [red-teaming](red-teaming.md) | Probing a model for policy-violating outputs to inform safety training and as an evaluation benchmark. |
| [reinforcement-learning](reinforcement-learning.md) | Training an agent to maximize a reward from chosen actions; policy gradients, the multi-armed bandit, and the gradient-bandit update. |
| [retrieval-augmented-generation](retrieval-augmented-generation.md) | Conditioning generation on documents fetched at inference time; retrieved text shares the context window with the instructions. |
| [rlhf](rlhf.md) | Aligning an LM to human preferences via a reward model and policy optimization with a KL penalty to the base model. |
| [robust-optimization](robust-optimization.md) | Min-max / saddle-point optimization and Danskin's theorem. |
| [roc-curves](roc-curves.md) | TPR/FPR trade-offs, AUC, balanced accuracy, and why security evaluates at low false-positive rates. |
| [safety-training](safety-training.md) | Training a deployed LLM to refuse restricted behaviors; refusal, RLHF-for-harmlessness, Constitutional AI. |
| [shadow-models](shadow-models.md) | Adversary-trained imitations of the target model used to calibrate membership inference attacks. |
| [statistical-hypothesis-testing](statistical-hypothesis-testing.md) | Deciding between a null hypothesis and its alternative from a test statistic and threshold; p-values, type I and type II errors, and the one-proportion z-test. |
| [steganography](steganography.md) | Hiding information inside ordinary-looking content so its presence is undetectable; its relation to cryptography and to digital watermarking. |
| [stochastic-gradient-descent](stochastic-gradient-descent.md) | Minibatch gradient descent; the default optimizer and the source of attack gradients. |
| [tokenization](tokenization.md) | Splitting text into a fixed vocabulary of subword tokens (BPE); tokens as the unit of generation, and the brittleness behind whitespace and homoglyph edits. |
| [transfer-learning](transfer-learning.md) | Reusing representations across tasks; ImageNet pretraining then fine-tuning, for higher accuracy with less task-specific data. |
| [transferability](transferability.md) | Adversarial examples crafted on one model often fool another; the basis of black-box transfer attacks. |
| [white-box-black-box](white-box-black-box.md) | Adversary knowledge assumptions, from full weights to query-only access. |
