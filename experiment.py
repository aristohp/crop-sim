# experiment.py

import yaml

from simulator import run_episode
from environment import CropEnvironment

with open("rule_config.yaml", "r") as f:
    config = yaml.safe_load(f)

    policy = config["policy"]
    episodes = config["episodes"]
    seed_range = config["seed_range"]


def run_experiment(policy, episodes):
    results = []

    for i in range(episodes):
        env = CropEnvironment(seed=i)
        reward = run_episode(env, policy)
        results.append(reward)

    return results


def summarize(results):
    return {
        "mean_reward": sum(results) / len(results),
        "best": max(results),
        "worst": min(results)
    }