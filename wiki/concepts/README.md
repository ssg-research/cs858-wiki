# Concepts

Shared prerequisite concept pages. One concept per file, named for the concept
itself (`differential-privacy.md`, `membership-inference.md`). Each page is
single-tier reference material written for a graduate ML student new to this
specific subfield, and is linked from the Tier-1 Background of every paper page
that depends on it.

Concept pages are created on demand by `/generate-paper-summary`. When you add
one, add a row to the table below, keeping it alphabetical by slug:
`| [slug](slug.md) | one-line description |`.

| Concept | Summary |
| --- | --- |
| [adversarial-examples](adversarial-examples.md) | The evasion phenomenon: small input perturbations that flip a prediction. |
| [adversarial-threat-model](adversarial-threat-model.md) | How an adversary's power is specified: perturbation set, knowledge, timing. |
| [adversarial-training](adversarial-training.md) | Training on adversarially perturbed inputs as a defense. |
| [differential-privacy](differential-privacy.md) | The formal bound on any single example's influence; DP-SGD and the epsilon guarantee. |
| [empirical-risk-minimization](empirical-risk-minimization.md) | Average training loss as a proxy for expected loss; the baseline objective. |
| [fgsm](fgsm.md) | The one-step gradient-sign attack and its role as a baseline. |
| [gaussian-mechanism](gaussian-mechanism.md) | Sensitivity and noise calibrated to it; the additive-noise recipe behind DP mechanisms. |
| [gradient-clipping](gradient-clipping.md) | Norm-rescaling gradients; a training stabilizer that, per example, becomes a sensitivity bound. |
| [gradient-masking](gradient-masking.md) | The defense failure mode where gradients become useless but worst-case loss stays high. |
| [likelihood-ratio-test](likelihood-ratio-test.md) | Deciding between two hypotheses by their likelihood ratio; Neyman-Pearson optimality. |
| [lp-norms](lp-norms.md) | ℓ0 / ℓ2 / ℓ-infinity balls as perturbation budgets and proxies for perceptual similarity. |
| [membership-inference](membership-inference.md) | Predicting whether a specific example was in a model's training set; the standard privacy audit. |
| [memorization](memorization.md) | Per-example fitting, random-label capacity, and the long-tail argument; the signal privacy attacks exploit. |
| [privacy-budget](privacy-budget.md) | The (epsilon, delta) budget, composition theorems, accountants, and amplification by subsampling. |
| [projected-gradient-descent](projected-gradient-descent.md) | Gradient step plus projection; the constrained-optimization primitive behind the PGD attack. |
| [robust-optimization](robust-optimization.md) | Min-max / saddle-point optimization and Danskin's theorem. |
| [roc-curves](roc-curves.md) | TPR/FPR trade-offs, AUC, balanced accuracy, and why security evaluates at low false-positive rates. |
| [shadow-models](shadow-models.md) | Adversary-trained imitations of the target model used to calibrate membership inference attacks. |
| [stochastic-gradient-descent](stochastic-gradient-descent.md) | Minibatch gradient descent; the default optimizer and the source of attack gradients. |
| [transferability](transferability.md) | Adversarial examples crafted on one model often fool another; the basis of black-box transfer attacks. |
| [white-box-black-box](white-box-black-box.md) | Adversary knowledge assumptions, from full weights to query-only access. |
