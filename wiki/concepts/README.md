# Concepts

Background concepts the papers rely on. Each page is a short, self-contained
explanation you can read on its own or reach from a paper that uses it.

| Concept | Summary |
| --- | --- |
| [adversarial-examples](adversarial-examples.md) | The evasion phenomenon: small input perturbations that flip a prediction. |
| [adversarial-threat-model](adversarial-threat-model.md) | How an adversary's power is specified: perturbation set, knowledge, timing. |
| [adversarial-training](adversarial-training.md) | Training on adversarially perturbed inputs as a defense. |
| [backdoor-attacks](backdoor-attacks.md) | A trigger-fired hidden behavior trained into a model via data poisoning; the overcapacity that enables it and its reuse as the mechanism behind black-box model watermarking. |
| [convolutional-neural-network](convolutional-neural-network.md) | CNNs for image classification: learned convolutional filters, pooling, a softmax head, and the standard backbones (AlexNet, VGG, ResNet, DenseNet). |
| [cryptographic-commitment](cryptographic-commitment.md) | A binding, hiding token published for a value and opened later; with a time-stamped public log it gives proof of priority for ownership claims. |
| [data-poisoning](data-poisoning.md) | Corrupting training data to change what a model learns: availability vs targeted/integrity poisoning, backdoors as the trigger-conditioned subclass, and why training-set sanitization defenses presume data access. |
| [decoding-strategies](decoding-strategies.md) | How an LLM turns next-token distributions into text: greedy, temperature, top-k, top-p, and prefilling. |
| [differential-privacy](differential-privacy.md) | The formal bound on any single example's influence; DP-SGD and the epsilon guarantee. |
| [direct-preference-optimization](direct-preference-optimization.md) | Aligning an LM to pairwise preferences directly, without a separate reward model or RL loop; the DPO alternative to RLHF. |
| [empirical-risk-minimization](empirical-risk-minimization.md) | Average training loss as a proxy for expected loss; the baseline objective. |
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
| [llm-tool-use](llm-tool-use.md) | An LLM emitting calls to external tools and acting on their outputs; chaining calls toward a goal yields an agent. |
| [lp-norms](lp-norms.md) | ℓ0 / ℓ2 / ℓ-infinity balls as perturbation budgets and proxies for perceptual similarity. |
| [machine-unlearning](machine-unlearning.md) | Removing chosen training data's influence from a trained model without full retraining; exact vs approximate unlearning and the right-to-be-forgotten motivation. |
| [membership-inference](membership-inference.md) | Predicting whether a specific example was in a model's training set; the standard privacy audit. |
| [memorization](memorization.md) | Per-example fitting, random-label capacity, and the long-tail argument; the signal privacy attacks exploit. |
| [model-extraction](model-extraction.md) | Attacks that reproduce a deployed model's parameters, hyperparameters, architecture, or functionality from query access; the fidelity-versus-accuracy axes and the MLaaS setting. |
| [model-watermarking](model-watermarking.md) | Embedding an owner-verifiable marker in a trained model; white-box (in the weights) vs black-box (backdoor-based trigger set) verification, and the assumption that the owner controls training. |
| [perplexity](perplexity.md) | How well an LM predicts a sequence (exponentiated cross-entropy); the LM quality metric and the per-example membership signal in extraction attacks. |
| [privacy-budget](privacy-budget.md) | The (epsilon, delta) budget, composition theorems, accountants, and amplification by subsampling. |
| [projected-gradient-descent](projected-gradient-descent.md) | Gradient step plus projection; the constrained-optimization primitive behind the PGD attack. |
| [prompt-injection](prompt-injection.md) | Adversarial instructions in a prompt or ingested content that override the intended task; direct and indirect. |
| [red-teaming](red-teaming.md) | Probing a model for policy-violating outputs to inform safety training and as an evaluation benchmark. |
| [reinforcement-learning](reinforcement-learning.md) | Training an agent to maximize a reward from chosen actions; policy gradients, the multi-armed bandit, and the gradient-bandit update. |
| [retrieval-augmented-generation](retrieval-augmented-generation.md) | Conditioning generation on documents fetched at inference time; retrieved text shares the context window with the instructions. |
| [rlhf](rlhf.md) | Aligning an LM to human preferences via a reward model and policy optimization with a KL penalty to the base model. |
| [robust-optimization](robust-optimization.md) | Min-max / saddle-point optimization and Danskin's theorem. |
| [roc-curves](roc-curves.md) | TPR/FPR trade-offs, AUC, balanced accuracy, and why security evaluates at low false-positive rates. |
| [safety-training](safety-training.md) | Training a deployed LLM to refuse restricted behaviors; refusal, RLHF-for-harmlessness, Constitutional AI. |
| [shadow-models](shadow-models.md) | Adversary-trained imitations of the target model used to calibrate membership inference attacks. |
| [stochastic-gradient-descent](stochastic-gradient-descent.md) | Minibatch gradient descent; the default optimizer and the source of attack gradients. |
| [transfer-learning](transfer-learning.md) | Reusing representations across tasks; ImageNet pretraining then fine-tuning, for higher accuracy with less task-specific data. |
| [transferability](transferability.md) | Adversarial examples crafted on one model often fool another; the basis of black-box transfer attacks. |
| [white-box-black-box](white-box-black-box.md) | Adversary knowledge assumptions, from full weights to query-only access. |
