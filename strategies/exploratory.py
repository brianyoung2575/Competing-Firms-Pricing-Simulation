import random
from .base import BaseStrategy

class RandomHillClimberStrategy(BaseStrategy):
    def __init__(self, sigma=5, warmup=10, restart_every=20):
        self.prices = list(range(1, 101))
        self.scores = {p: 0.0 for p in self.prices}
        self.counts = {p: 0 for p in self.prices}
        self.sigma = sigma
        self.warmup = warmup
        self.restart_every = restart_every
        self.last_price = None
        self.step = 0
        self.best_price = random.choice(self.prices)

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)

        if self.last_price is not None:
            p = self.last_price
            self.counts[p] += 1
            self.scores[p] += (last_profit - self.scores[p]) / self.counts[p]
            if self.scores[p] > self.scores[self.best_price]:
                self.best_price = p

        self.step += 1

        if self.step <= self.warmup:
            price = random.choice(self.prices)  # uniform warm-up
        elif self.step % self.restart_every == 0:
            price = random.choice(self.prices)  # random restart
        else:
            noise = random.gauss(0, self.sigma)
            price = int(round(self.best_price + noise))
            price = max(1, min(100, price))  # clamp

        self.last_price = price
        return price
