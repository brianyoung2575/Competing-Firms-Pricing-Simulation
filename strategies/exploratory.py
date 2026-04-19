import random
from .base import BaseStrategy

class ExploratoryStrategy(BaseStrategy):
    def __init__(self):
        self.baseline = 10
        self.last_price = 10
        self.best_price = 10
        self.best_profit = float("-inf")

    def choose_price(self, state):
        last_profit = state.get("last_profit", 0)
        
        if last_profit > self.best_profit:
            self.best_profit = last_profit
            self.best_price = self.last_price
            
        self.baseline = 0.8 * self.baseline + 0.2 * self.best_price
        
        if random.random() < 0.3:
            price = random.uniform(1, 50)
        else:
            price = self.baseline + random.uniform(-3, 3)

        price = max(0.1, price)
        self.last_price = price

        return price
