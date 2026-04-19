import random
from .base import BaseStrategy

class RegimeExploratoryStrategy(BaseStrategy):
    def __init__(self):
        self.price = 10
        self.direction = None
        self.lock_steps = 0
        self.min_hold = 5

        self.last_profit = 0
        self.prev_profit = 0

    def choose_price(self, state):
        self.prev_profit = self.last_profit
        self.last_profit = state.get("last_profit", 0)

        if self.lock_steps > 0:
            self.lock_steps -= 1

            if self.last_profit < self.prev_profit * 0.8:
                self.lock_steps = 0

            return self.price

        if self.direction is None:
            self.direction = random.choice([-1, 1])
            shock = random.uniform(5, 20)

            self.price = max(0.1, self.price + self.direction * shock)

            return self.price

        new_price = self.price * (1 + 0.8 * self.direction * 0.1)

        if self.last_profit > self.prev_profit:
            self.price = new_price
        else:
            self.direction *= -1
            self.price = self.price * (1 + 0.8 * self.direction * 0.1)

        self.lock_steps = self.min_hold

        return self.price
