class TradeRankingEngine:

    def rank(self, sessions):

        ranked = []

        for session in sessions:

            score = 0

            score += session.trade_quality.get("score", 0)

            score += session.confluence.get("confidence", 0)

            score += session.validation.get("confidence", 0)

            score += session.trend.get("confidence", 0)

            ranked.append({
                "symbol": session.symbol,
                "score": round(score / 4, 2),
                "session": session
            })

        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranked