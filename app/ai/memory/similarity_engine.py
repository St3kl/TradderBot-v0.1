from app.database.repositories.trade_repository import TradeRepository
from app.ai.memory.vector_engine import VectorEngine


class SimilarityEngine:

    def __init__(self):

        self.repo = TradeRepository()
        self.vector = VectorEngine()

    def similarity_score(self, current, historical):

        score = 0

        score += abs(current["entry"] - historical["entry"])
        score += abs(current["stop_loss"] - historical["stop_loss"])
        score += abs(current["take_profit"] - historical["take_profit"])

        return score

    def find_similar(self, symbol, current_vector):

        trades = self.repo.get_closed_trades()

        trades = [
            trade
            for trade in trades
            if trade["symbol"] == symbol
        ]

        if not trades:
            return None

        ranked = []

        for trade in trades:

            historical_vector = self.vector.from_trade(trade)

            score = self.similarity_score(
                current_vector,
                historical_vector
            )

            ranked.append(
                (score, trade)
            )

        ranked.sort(key=lambda item: item[0])

        return ranked[0][1]