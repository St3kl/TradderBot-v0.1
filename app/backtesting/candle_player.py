class CandlePlayer:
    """
    Simulates live candle streaming.
    """

    def __init__(self, replay):

        self.replay = replay

    def play(self):

        while self.replay.has_next():

            candle = self.replay.next()

            yield candle