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
