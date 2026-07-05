from datetime import datetime

from app.database.repositories.trade_repository import TradeRepository


class TradeMonitor:

    def __init__(self):

        self.repo = TradeRepository()

    def monitor(self, current_price):

        open_trades = self.repo.get_open_trades()

        print("OPEN TRADES:", open_trades)

        for trade in open_trades:

            self.check_trade(trade, current_price)

    def check_trade(self, trade, price):

        # LONG Trades
        if trade["direction"] == "LONG":

            if price >= trade["take_profit"]:

                self.close_trade(
                    trade,
                    price,
                    "WIN"
                )

            elif price <= trade["stop_loss"]:

                self.close_trade(
                    trade,
                    price,
                    "LOSS"
                )

        # SHORT Trades
        elif trade["direction"] == "SHORT":

            if price <= trade["take_profit"]:

                self.close_trade(
                    trade,
                    price,
                    "WIN"
                )

            elif price >= trade["stop_loss"]:

                self.close_trade(
                    trade,
                    price,
                    "LOSS"
                )

    def close_trade(self, trade, exit_price, result):

        print()
        print("================================")
        print("Closing Trade")
        print("================================")
        print(f"Symbol : {trade['symbol']}")
        print(f"Result : {result}")
        print(f"Exit   : {exit_price}")
        print(f"Opened : {trade['opened_at']}")
        print(f"Closed : {datetime.utcnow()}")
        print()