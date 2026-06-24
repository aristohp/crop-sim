# main.py

from policies import RandomPolicy, RuleBasedPolicy
from experiment import run_experiment, summarize

print("=== RANDOM POLICY ===")
random_results = run_experiment(RandomPolicy(), episodes=20)
print(summarize(random_results))

print("\n=== RULE-BASED POLICY ===")
rule_results = run_experiment(RuleBasedPolicy(), episodes=20)
print(summarize(rule_results))