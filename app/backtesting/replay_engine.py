class ReplayEngine:
    """
    Replays historical candles one at a time.
    """

    def __init__(self):
        
        self.symbol = ""

        self.candles = []

        self.index = 0

    # --------------------------------

    def load(self, candles, symbol):

        self.symbol = symbol

        self.candles = candles

        self.index = 0

        print(f"Loaded {len(candles)} candles")

    # --------------------------------

    def has_next(self):

        return self.index < len(self.candles)

    # --------------------------------

    def next(self):

        if not self.has_next():

            return None

        candle = self.candles[self.index]

        self.index += 1

        return candle

    # --------------------------------

    def current(self):

        if self.index == 0:

            return None

        return self.candles[self.index - 1]

    # --------------------------------

    def previous(self):

        if self.index <= 1:

            return None

        return self.candles[self.index - 2]

    # --------------------------------

    def next_candle(self):

        if self.index >= len(self.candles):

            return None

        return self.candles[self.index]

    # --------------------------------

    def reset(self):

        self.index = 0