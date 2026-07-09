class ReplayEngine:
    """
    Replays historical candles one at a time.
    """

    def __init__(self):

        self.candles = []

        self.index = 0

    def load(self, candles):

        self.candles = candles

        self.index = 0

        print(f"Loaded {len(candles)} candles")

    def has_next(self):

        return self.index < len(self.candles)

    def next(self):

        if not self.has_next():

            return None

        candle = self.candles[self.index]

        self.index += 1

        return candle

    def reset(self):

        self.index = 0