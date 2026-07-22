from app.database.repositories.trade_repository import TradeRepository


class EquityCurve:

    def __init__(self):

        self.repo = TradeRepository()

    def build(self, starting_balance=10000):

        trades = self.repo.get_closed_trades()

        balance = starting_balance

        curve = []

        for trade in trades:

            pnl = trade["pnl"] or 0

            balance += pnl

            curve.append({

                "trade_id": trade["id"],

                "balance": round(balance, 2),

                "pnl": pnl,

                "result": trade["result"]

            })

        return curve