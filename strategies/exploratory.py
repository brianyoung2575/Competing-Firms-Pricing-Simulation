import random
from .base import BaseStrategy

class ExploratoryStrategy(BaseStrategy):
    def __init__(self):
        self.history = []  # (price, profit)
        self.last_price = 10

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)

        # store last result
        if self.history:
            self.history[-1] = (self.last_price, last_profit)
        else:
            self.history.append((self.last_price, last_profit))
            
        if len(self.history) < 10 or random.random() < 0.3:
            price = random.uniform(1, 50)
        else:
            best_price = max(self.history, key=lambda x: x[1])[0]
            price = best_price + random.uniform(-2, 2)

        price = max(0.1, price)

        self.history.append((price, 0))  # placeholder for next step
        self.last_price = price

        return price
