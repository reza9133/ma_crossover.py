class AdvancedTradingBot:
def __init__(self):
self.short_window = 5
        self.long_window = 20
self.prices = []
self.current_position = None
self.balance = 1000
self.take_profit_pct = 0.05
self.stop_loss_pct = 0.02
def add_price(self, price):
self.prices.append(price)
if len(self.prices) > self.long_window + 5:
            self.prices.pop(0)
def get_sma(self, window):
        if len(self.prices) < window: return None
return sum(self.prices[-window:]) / window
