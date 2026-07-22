class ConfirmationEngine:
    """
    Multi-factor confirmation engine.

    Confirms LONG and SHORT setups using:

    - Trend
    - Market Structure
    - Smart Money Concepts
    - Volume
    - Confluence

    Produces:

        score
        confirmations
        confirmed
    """

    def evaluate(self, session):

        confirmations = []

        bullish = session.decision["action"] == "BUY"
        bearish = session.decision["action"] == "SELL"

        # ===================================================
        # TREND
        # ===================================================

        if bullish and session.bullish:

            confirmations.append("Bullish Trend")

        if bearish and not session.bullish:

            confirmations.append("Bearish Trend")

        # ===================================================
        # MARKET STRUCTURE
        # ===================================================

        if session.structure.get("bos"):

            confirmations.append("Break Of Structure")

        if session.structure.get("choch"):

            confirmations.append("CHOCH")

        # ===================================================
        # SMART MONEY
        # ===================================================

        smc = session.smart_money

        # Order Blocks

        if bullish:

            if smc["order_blocks"]["bullish"] > 0:

                confirmations.append("Bullish Order Block")

        if bearish:

            if smc["order_blocks"]["bearish"] > 0:

                confirmations.append("Bearish Order Block")

        # Fair Value Gaps

        if bullish:

            if smc["fair_value_gaps"]["bullish"] > 0:

                confirmations.append("Bullish FVG")

        if bearish:

            if smc["fair_value_gaps"]["bearish"] > 0:

                confirmations.append("Bearish FVG")

        # Liquidity Sweep

        if bullish:

            if smc["liquidity_sweep"]["buy_side"]:

                confirmations.append("Buy Side Liquidity")

        if bearish:

            if smc["liquidity_sweep"]["sell_side"]:

                confirmations.append("Sell Side Liquidity")

        # ===================================================
        # VOLUME
        # ===================================================

        volume_score = session.volume.get("score", 0)

        if volume_score >= 15:

            confirmations.append("Strong Volume")

        # ===================================================
        # CONFLUENCE
        # ===================================================

        if session.confluence["score"] >= 3:

            confirmations.append("High Confluence")

        # ===================================================
        # FINAL SCORE
        # ===================================================

        score = len(confirmations)

        confirmed = score >= 4

        return {

            "score": score,

            "confirmations": confirmations,

            "confirmed": confirmed

        }