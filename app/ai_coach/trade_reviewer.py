class TradeReviewer:

    def review(self, trades):

        if not trades:

            return []

        recommendations = []

        losses = [

            t for t in trades

            if t["result"] == "LOSS"

        ]

        if len(losses) > len(trades) * 0.60:

            recommendations.append(

                "Win rate is low. Reduce position size."

            )

        return recommendations