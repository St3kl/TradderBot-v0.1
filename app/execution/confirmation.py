class ConfirmationEngine:

    def evaluate(self, session):

        confirmations = []

        # -------------------------
        # Trend
        # -------------------------

        if session.bullish:

            confirmations.append(
                "Bullish Trend"
            )

        # -------------------------
        # Structure
        # -------------------------

        if session.structure.get("bos"):

            confirmations.append(
                "Bullish BOS"
            )

        # -------------------------
        # Smart Money
        # -------------------------

        if session.smart_money["order_blocks"]["bullish"] > 0:

            confirmations.append(
                "Bullish Order Block"
            )

        if session.smart_money["fair_value_gaps"]["bullish"] > 0:

            confirmations.append(
                "Bullish Fair Value Gap"
            )

        if session.smart_money["liquidity_sweep"]["buy_side"]:

            confirmations.append(
                "Buy-side Liquidity Sweep"
            )

        # -------------------------
        # Volume
        # -------------------------

        if session.volume["score"] >= 15:

            confirmations.append(
                "Strong Volume"
            )

        return {

            "score": len(confirmations),

            "confirmations": confirmations,

            "confirmed": len(confirmations) >= 4

        }