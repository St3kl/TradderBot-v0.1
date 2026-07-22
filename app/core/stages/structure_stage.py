from app.market.structure.structure_engine import StructureEngine


class StructureStage:

    def __init__(self):

        self.engine = StructureEngine()

    def run(self, session):

        print("Running Structure Stage")

        dataset = session.replay.history

        highs = [c["high"] for c in dataset]
        lows = [c["low"] for c in dataset]
        closes = [c["close"] for c in dataset]

        session.structure = self.engine.analyze(
            highs=highs,
            lows=lows,
            closes=closes
        )

        return session