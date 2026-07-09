from app.database.repositories.trade_repository import TradeRepository


class ConfidenceEngine:

    def __init__(self):

        self.repo = TradeRepository()

    def calibrate(self, confidence):

        trades = self.repo.get_closed_trades()

        if not trades:

            return confidence

        minimum = confidence - 5
        maximum = confidence + 5

        candidates = [

            trade

            for trade in trades

            if minimum <= trade["confidence"] <= maximum

        ]

        if not candidates:

            return confidence

        wins = [

            trade

            for trade in candidates

            if trade["result"] == "WIN"

        ]

        return round(

            len(wins) / len(candidates) * 100,

            2

        )