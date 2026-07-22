from app.backtesting.replay_context import ReplayContext


class CandlePlayer:
    """
    Simulates live candle streaming.

    Instead of yielding a raw candle,
    it yields a ReplayContext object.
    """

    def __init__(self, replay):

        self.replay = replay

    def play(self):

        while self.replay.has_next():

            candle = self.replay.next()

            context = ReplayContext()

            context.index = self.replay.index - 1

            context.candle = candle

            context.previous = self.replay.previous()

            context.next = self.replay.next_candle()

            context.dataset = self.replay.candles

            context.history = self.replay.candles[: self.replay.index]

            context.symbol = self.replay.symbol

        yield context