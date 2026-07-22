class ReplayContext:

    def __init__(self):

        # Symbol
        self.symbol = ""

        # Current replay index
        self.index = 0

        # Current candle
        self.candle = None

        # Previous candle
        self.previous = None

        # Next candle
        self.next = None

        # Entire dataset (kept only for debugging)
        self.dataset = None

        # Historical candles available at this point
        self.history = []