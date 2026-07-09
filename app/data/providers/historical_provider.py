class HistoricalDataProvider:

    def __init__(self):

        self.current_candle = None

    def update(self, candle):

        self.current_candle = candle

    def get_indicators(self, symbol):

        #
        # Temporary
        #
        # Later this will compute indicators
        # from historical candles.
        #

        return {

            "close": self.current_candle["close"]

        }