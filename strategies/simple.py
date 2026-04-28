from .base import BaseStrategy

class SimpleStrategy(BaseStrategy):
    def choose_price(self, state):
        return 10
