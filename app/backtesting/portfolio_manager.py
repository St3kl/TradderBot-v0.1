class PortfolioManager:
    """
    Tracks account balance and performance during a backtest.
    """

    def __init__(self, initial_balance=10000):

        self.initial_balance = initial_balance

        self.balance = initial_balance

        self.equity = initial_balance

        self.peak_equity = initial_balance

        self.max_drawdown = 0.0

    # --------------------------
    # Apply Closed Trade
    # --------------------------

    def apply_trade(self, trade):

        pnl = trade.get("pnl", 0)

        self.balance += pnl

        self.equity = self.balance

        if self.equity > self.peak_equity:

            self.peak_equity = self.equity

        drawdown = self.peak_equity - self.equity

        if drawdown > self.max_drawdown:

            self.max_drawdown = drawdown

    # --------------------------
    # Get Summary
    # --------------------------

    def summary(self):

        return {

            "initial_balance": self.initial_balance,

            "balance": round(self.balance, 2),

            "equity": round(self.equity, 2),

            "peak_equity": round(self.peak_equity, 2),

            "max_drawdown": round(self.max_drawdown, 2)

        }