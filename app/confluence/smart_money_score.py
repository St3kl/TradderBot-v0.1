from app.confluence.weights import WEIGHTS


def calculate_smart_money_score(
    smart_money
):
    """
    Scores Smart Money Concepts.
    """

    score = 0

    signals = []

    missing = []

    # ----------------------------------
    # Bullish Order Block
    # ----------------------------------

    if smart_money["order_blocks"]["bullish"] > 0:

        score += WEIGHTS["order_block"]

        signals.append("Bullish Order Block")

    else:

        missing.append("Bullish Order Block")

    # ----------------------------------
    # Bullish Fair Value Gap
    # ----------------------------------

    if smart_money["fair_value_gaps"]["bullish"] > 0:

        score += WEIGHTS["fair_value_gap"]

        signals.append("Bullish Fair Value Gap")

    else:

        missing.append("Bullish Fair Value Gap")

    # ----------------------------------
    # Sell Side Liquidity Sweep
    # ----------------------------------

    if smart_money["liquidity_sweep"]["sell_side"]:

        score += WEIGHTS["liquidity_sweep"]

        signals.append("Sell Side Liquidity Sweep")

    else:

        missing.append("Sell Side Liquidity Sweep")

    # ----------------------------------
    # Discount Zone
    # ----------------------------------

    if smart_money["premium_discount"]["zone"] == "Discount":

        score += WEIGHTS["premium_discount"]

        signals.append("Discount Zone")

    else:

        missing.append("Discount Zone")

    return {

        "score": score,

        "signals": signals,

        "missing": missing

    }