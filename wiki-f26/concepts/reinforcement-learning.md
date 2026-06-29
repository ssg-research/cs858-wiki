---
title: "Reinforcement learning"
type: concept
description: "Training an agent to maximize a reward signal from chosen actions rather than from labeled targets; policy-gradient methods, the multi-armed bandit special case, and the gradient-bandit update with a baseline."
tags:
  - reinforcement-learning
  - machine-learning
---

## [Wiki Home](../README.md)

# Reinforcement learning

## Definition

Reinforcement learning (RL) trains an agent to choose actions that maximize a
cumulative reward returned by an environment, rather than learning from labeled
examples. The learning signal is evaluative (how good was the action taken)
instead of instructive (what the correct output was). Policy-gradient methods
parameterize a stochastic policy, a distribution over actions, and adjust its
parameters in the direction that increases expected reward (Sutton and Barto,
1998).

The multi-armed bandit is the simplest case: a single decision with no state,
where the agent balances exploiting actions known to pay well against exploring
uncertain ones. The gradient-bandit algorithm maintains a numerical preference
per action, converts preferences to sampling probabilities with a softmax, and
nudges each preference by the received reward measured relative to a running
baseline. RL is the natural framing whenever the available feedback is a reward
for actions the learner chooses, not a target it is told to reproduce.

## Papers that use this concept

- [Knockoff Nets: Stealing Functionality of Black-Box Models](../papers/orekondy-2019-knockoff-nets.md) — its adaptive query strategy is a policy, learned with a gradient-bandit update, that selects which images to send to the victim to improve query sample-efficiency.

## See also

- [Stochastic gradient descent](stochastic-gradient-descent.md)

## References

- Sutton, R.S. and Barto, A.G. "Introduction to Reinforcement Learning." MIT Press, 1998.
