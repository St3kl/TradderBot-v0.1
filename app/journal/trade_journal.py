class TradeJournal:
    """
    Stores executed trades.
    """

    def save(self, trade):

        print(f"Trade saved: {trade['symbol']}")