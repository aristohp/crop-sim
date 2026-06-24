# policies.py

import random

class RandomPolicy:
    def act(self, state):
        return {
            "water": random.choice([0, 1]),
            "fertilizer": random.choice([0, 1])
        }


class RuleBasedPolicy:
    def act(self, state):
        action = {"water": 0, "fertilizer": 0}

        if state["soil_moisture"] < 40:
            action["water"] = 1

        if state["soil_nutrients"] < 40:
            action["fertilizer"] = 1

        return action