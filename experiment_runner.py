import yaml
from policies import *
from experiment import run_experiment, summarize

POLICIY_MAP = {
    "RandomPolicy": RandomPolicy(),
    "RuleBasedPolicy": RuleBasedPolicy()
}


def run_from_config(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

        policies = config["policy"]
        episodes = config["episodes"]

    for policy_name in policies:
        policy_class = POLICIY_MAP[policy_name]
        policy = policy_class

        print(f"\n=== {policy_name.upper()} ===")
        results = run_experiment(policy, episodes=episodes)
        print(summarize(results))