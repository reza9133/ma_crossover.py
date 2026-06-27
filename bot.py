import time
class AdvancedTradingBot:
def __init__(self):
self.short_window = 5
        self.long_window = 20
self.prices = []
self.current_position = None
self.balance = 1000
self.take_profit_pct = 0.05
self.stop_loss_pct = 0.02
self.entry_price = 0
self.total_trades = 0
        self.win_trades = 0
self.total_pnl = 0
self.trade_history = []
def add_price(self, price):
self.prices.append(price)
if len(self.prices) > self.long_window + 5:
            self.prices.pop(0)
def get_sma(self, window):
        if len(self.prices) < window: return None
return sum(self.prices[-window:]) / window
def analyze_market(self):
        short_sma = self.get_sma(self.short_window)
        long_sma = self.get_sma(self.long_window)
if not short_sma or not long_sma:
            return
        self.check_risk_management(self.prices[-1])
if short_sma > long_sma and self.current_position != 'BUY':
        self.entry_price = short_sma
            print(f"BUY Signal! SMA: {short_sma}")
            self.current_position = 'BUY'
elif short_sma < long_sma and self.current_position == 'BUY':
            print(f"SELL Signal! SMA: {short_sma}")
            self.current_position = None
if __name__ == "__main__":
    bot = AdvancedTradingBot()
market_data = [100, 101, 102, 105, 108, 110, 112, 115, 110, 105, 95, 90]
for price in market_data:
        bot.add_price(price)
        bot.analyze_market()
def check_risk_management(self, current_price):
        if self.current_position != 'BUY': return
price_change = (current_price - self.entry_price) / self.entry_price
if price_change >= self.take_profit_pct:
            print(f"💰 TAKE PROFIT HIT! Closed at {current_price}")
        self.log_trade(current_price, "Take Profit")
            self.current_position = None
elif price_change <= -self.stop_loss_pct:
            print(f"🛡️ STOP LOSS HIT! Closed at {current_price}")
self.log_trade(current_price, "Stop Loss")
            self.current_position = None
def log_trade(self, exit_price, reason):
        self.total_trades += 1
trade_pnl = ((exit_price - self.entry_price) / self.entry_price) * self.balance
        self.total_pnl += trade_pnl
self.balance += trade_pnl
if trade_pnl > 0:
            self.win_trades += 1
        self.trade_history.append({"price": exit_price, "reason": reason})
def print_summary(self):
        win_rate = (self.win_trades / self.total_trades) * 100 if self.total_trades > 0 else 0
        print(f"\n📊 --- FINAL REPORT ---")
        print(f"Total Trades: {self.total_trades} | Win Rate: {win_rate:.1f}%")
        print(f"Final Balance: ${self.balance:.2f} | Net Profit/Loss: ${self.total_pnl:.2f}")
bot.print_summary()
def export_history(self):
        filename = "trades.txt"
