# experiment.py

from simulator import run_episode
from environment import CropEnvironment

def run_experiment(policy, episodes=10):
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