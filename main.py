# main.py

import yaml

from policies import RandomPolicy, RuleBasedPolicy
from experiment import run_experiment, summarize

with open("rule_config.yaml", "r") as f:
    config = yaml.safe_load(f)

    policy = config["policy"]
    episodes = config["episodes"]
    

print("=== RANDOM POLICY ===")
random_results = run_experiment(RandomPolicy(), episodes=20)
print(summarize(random_results))

if policy == "RuleBasedPolicy":
    print("\n=== RULE-BASED POLICY ===")
    rule_results = run_experiment(RuleBasedPolicy(), episodes=episodes)
    print(summarize(rule_results), policy, episodes)
