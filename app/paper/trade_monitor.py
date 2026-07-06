from datetime import datetime

from app.database.repositories.trade_repository import TradeRepository

from app.core.events import dispatcher
from app.events.trade_events import TRADE_CLOSED


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

        risk = trade["risk_amount"]

        if result == "WIN":

            pnl = risk * 2

        else:

            pnl = -risk

        self.repo.close_trade(

            trade["id"],

            exit_price,

            pnl,

            result

        )
        
        dispatcher.dispatch(
            TRADE_CLOSED,
            trade
        )

        print()

        print("=========================")

        print("TRADE CLOSED")

        print("=========================")

        print("Trade :", trade["id"])

        print("Symbol:", trade["symbol"])

        print("Result:", result)

        print("Exit  :", exit_price)

        print("PnL   :", pnl)

        print("Closed:", datetime.utcnow())

        print()