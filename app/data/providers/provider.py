class DataProvider:
    """
    Base interface for all market data providers.
    """

    def get_indicators(self, symbol):

        raise NotImplementedError()

    def get_price(self, symbol):

        raise NotImplementedError()

    def get_candles(

        self,

        symbol,

        timeframe,

        limit=500

    ):

        raise NotImplementedError()