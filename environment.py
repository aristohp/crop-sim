import random

class CropEnvironment:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)
        self.reset()

    def reset(self):
        self.day = 0
        self.crop_stage = 0          # 0 = seed, 1 = growing, 2 = mature
        self.soil_moisture = 50
        self.soil_nutrients = 50
        self.water = 50
        self.yield_accumulated = 0

        return self._get_state()

    def _get_state(self):
        return {
            "day": self.day,
            "crop_stage": self.crop_stage,
            "soil_moisture": self.soil_moisture,
            "soil_nutrients": self.soil_nutrients,
            "water": self.water
        }

    def step(self, action):
        """
        action = {
            "water": 0/1,
            "fertilizer": 0/1
        }
        """

        # --- apply action ---
        if action["water"] == 1:
            self.soil_moisture += 10
            self.water -= 5

        if action["fertilizer"] == 1:
            self.soil_nutrients += 10

        # --- natural processes ---
        rain = self.rng.randint(0, 10)
        self.soil_moisture += rain

        # evaporation
        self.soil_moisture -= 5
        self.soil_nutrients -= 1

        # --- crop growth logic (very simplified) ---
        growth_signal = (self.soil_moisture + self.soil_nutrients) / 2

        if growth_signal > 60:
            self.crop_stage += 1

        # cap values
        self.soil_moisture = max(0, min(100, self.soil_moisture))
        self.soil_nutrients = max(0, min(100, self.soil_nutrients))
        self.water = max(0, min(100, self.water))

        # --- reward ---
        reward = 0
        if self.crop_stage == 2:
            reward += 100  # harvest value

        reward -= (action["water"] + action["fertilizer"]) * 2  # cost

        self.day += 1

        done = self.day >= 30 or self.crop_stage == 2

        return self._get_state(), reward, done