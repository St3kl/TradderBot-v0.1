def build_explanation(context):
    """
    Convert AI reasoning into a human explanation.
    """

    reasoning = context["reasoning"]

    explanation = []

    # --------------------------------------------------
    # Market Trend
    # --------------------------------------------------

    if reasoning["trend_bias"] == "Bullish":

        explanation.append(
            "The market is maintaining a bullish structure."
        )

    elif reasoning["trend_bias"] == "Bearish":

        explanation.append(
            "The market remains under bearish control."
        )

    else:

        explanation.append(
            "The market is currently neutral."
        )

    # --------------------------------------------------
    # Smart Money
    # --------------------------------------------------

    if reasoning["institutional_bias"] == "Bullish":

        explanation.append(
            "Institutional activity favors buyers."
        )

    elif reasoning["institutional_bias"] == "Bearish":

        explanation.append(
            "Institutional activity favors sellers."
        )

    # --------------------------------------------------
    # Liquidity
    # --------------------------------------------------

    if reasoning["liquidity"] != "None":

        explanation.append(
            f"Recent liquidity event detected: {reasoning['liquidity']}."
        )

    # --------------------------------------------------
    # Momentum
    # --------------------------------------------------

    explanation.append(
        reasoning["momentum"]
    )

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    if reasoning["trade_quality"] >= 80:

        explanation.append(
            "The setup satisfies most institutional conditions."
        )

    elif reasoning["trade_quality"] >= 60:

        explanation.append(
            "The setup is acceptable but requires caution."
        )

    else:

        explanation.append(
            "The setup is weak and should be traded carefully."
        )

    return explanation