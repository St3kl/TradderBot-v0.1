class TradingWindowGuard:
    """
    Blocks trading during poor market conditions.
    """

    def evaluate(self, session):

        reasons = []

        allowed = True

        market = getattr(session, "market_health", {})

        volatility = getattr(session, "volatility", {})

        correlation = getattr(session, "correlation", {})

        # -----------------------------
        # Market Health
        # -----------------------------

        if market.get("score", 100) < 40:

            allowed = False

            reasons.append("Poor Market Health")

        # -----------------------------
        # Volatility
        # -----------------------------

        if volatility.get("level") == "EXTREME":

            allowed = False

            reasons.append("Extreme Volatility")

        # -----------------------------
        # Correlation
        # -----------------------------

        if correlation.get("score", 100) < 40:

            allowed = False

            reasons.append("Weak Correlation")

        return {

            "allowed": allowed,

            "reasons": reasons

        }