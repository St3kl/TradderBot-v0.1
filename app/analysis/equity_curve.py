from app.database.repositories.trade_repository import TradeRepository


class EquityCurveEngine:

    def __init__(self):

        self.repo = TradeRepository()

    def build_curve(self, starting_balance=10000):

        balance = starting_balance

        curve = [balance]

        trades = self.repo.get_closed_trades()

        for trade in trades:

            balance += trade["pnl"]

            curve.append(round(balance, 2))

        return curve
    