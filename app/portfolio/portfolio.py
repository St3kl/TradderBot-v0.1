from dataclasses import dataclass


@dataclass
class PortfolioSummary:
    initial_balance: float
    balance: float
    equity: float
    peak_equity: float
    max_drawdown: float


class Portfolio:

    def __init__(self, initial_balance=10000):

        self.initial_balance = initial_balance

        self.balance = initial_balance

        self.equity = initial_balance

        self.peak_equity = initial_balance

        self.max_drawdown = 0.0

    # ----------------------------------------

    def apply_trade(self, trade):

        pnl = getattr(trade, "pnl", 0.0)

        self.balance += pnl

        self.equity = self.balance

        if self.equity > self.peak_equity:

            self.peak_equity = self.equity

        drawdown = self.peak_equity - self.equity

        if drawdown > self.max_drawdown:

            self.max_drawdown = drawdown

    # ----------------------------------------

    def summary(self):

        return PortfolioSummary(

            initial_balance=self.initial_balance,

            balance=round(self.balance, 2),

            equity=round(self.equity, 2),

            peak_equity=round(self.peak_equity, 2),

            max_drawdown=round(self.max_drawdown, 2)

        ).__dict__