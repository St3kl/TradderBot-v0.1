class ExecutionAgent:
    """
    Evaluates whether a trade can be
    executed safely.
    """

    def evaluate(

        self,

        market

    ):

        score = 100

        reasons = []

        # Spread

        if market["spread"] > 0.30:

            score -= 30

            reasons.append(

                "High spread"

            )

        # Slippage

        if market["slippage"] > 0.50:

            score -= 40

            reasons.append(

                "High slippage"

            )

        # Liquidity

        if market["liquidity"] == "LOW":

            score -= 30

            reasons.append(

                "Low liquidity"

            )

        return {

            "agent": "Execution",

            "score": max(score, 0),

            "reasons": reasons

        }