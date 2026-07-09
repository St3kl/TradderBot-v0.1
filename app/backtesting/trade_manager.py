class TradeManager:
    """
    Manages the lifecycle of simulated trades.
    """

    def __init__(self):

        self.open_trades = []
        self.closed_trades = []

    # ------------------------
    # Open
    # ------------------------

    def add(self, trade):

        self.open_trades.append(trade)

    # ------------------------
    # Close
    # ------------------------

    def close(self, trade):

        if trade in self.open_trades:
            self.open_trades.remove(trade)

        self.closed_trades.append(trade)

    # ------------------------
    # Queries
    # ------------------------

    def get_open(self):

        return self.open_trades

    def get_closed(self):

        return self.closed_trades

    def total_open(self):

        return len(self.open_trades)

    def total_closed(self):

        return len(self.closed_trades)

    def reset(self):

        self.open_trades.clear()
        self.closed_trades.clear()