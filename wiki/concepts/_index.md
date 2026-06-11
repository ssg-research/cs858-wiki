# Concepts

Shared prerequisite concept pages. One concept per file, named for the concept
itself (`differential-privacy.md`, `membership-inference.md`). Each page is
single-tier reference material written for a graduate ML student new to this
specific subfield, and is linked from the Tier-1 Background of every paper page
that depends on it.

Concept pages are created on demand by `/generate-paper-summary`. When you add
one, list it here as `[slug](slug.md) — one-line description`.

- [adversarial-examples](adversarial-examples.md) — the evasion phenomenon: small input perturbations that flip a prediction.
- [adversarial-threat-model](adversarial-threat-model.md) — how an adversary's power is specified: perturbation set, knowledge, timing.
- [adversarial-training](adversarial-training.md) — training on adversarially perturbed inputs as a defense.
- [differential-privacy](differential-privacy.md) — the formal bound on any single example's influence; DP-SGD and the epsilon guarantee.
- [empirical-risk-minimization](empirical-risk-minimization.md) — average training loss as a proxy for expected loss; the baseline objective.
- [fgsm](fgsm.md) — the one-step gradient-sign attack and its role as a baseline.
- [gaussian-mechanism](gaussian-mechanism.md) — sensitivity and noise calibrated to it; the additive-noise recipe behind DP mechanisms.
- [gradient-clipping](gradient-clipping.md) — norm-rescaling gradients; a training stabilizer that, per example, becomes a sensitivity bound.
- [gradient-masking](gradient-masking.md) — the defense failure mode where gradients become useless but worst-case loss stays high.
- [likelihood-ratio-test](likelihood-ratio-test.md) — deciding between two hypotheses by their likelihood ratio; Neyman-Pearson optimality.
- [lp-norms](lp-norms.md) — ℓ0 / ℓ2 / ℓ-infinity balls as perturbation budgets and proxies for perceptual similarity.
- [membership-inference](membership-inference.md) — predicting whether a specific example was in a model's training set; the standard privacy audit.
- [memorization](memorization.md) — per-example fitting, random-label capacity, and the long-tail argument; the signal privacy attacks exploit.
- [privacy-budget](privacy-budget.md) — the (epsilon, delta) budget, composition theorems, accountants, and amplification by subsampling.
- [projected-gradient-descent](projected-gradient-descent.md) — gradient step plus projection; the constrained-optimization primitive behind the PGD attack.
- [robust-optimization](robust-optimization.md) — min-max / saddle-point optimization and Danskin's theorem.
- [roc-curves](roc-curves.md) — TPR/FPR trade-offs, AUC, balanced accuracy, and why security evaluates at low false-positive rates.
- [shadow-models](shadow-models.md) — adversary-trained imitations of the target model used to calibrate membership inference attacks.
- [stochastic-gradient-descent](stochastic-gradient-descent.md) — minibatch gradient descent; the default optimizer and the source of attack gradients.
- [transferability](transferability.md) — adversarial examples crafted on one model often fool another; the basis of black-box transfer attacks.
- [white-box-black-box](white-box-black-box.md) — adversary knowledge assumptions, from full weights to query-only access.
