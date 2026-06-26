def decide_action(
    score,
    bullish
):
    """
    Decide the trading action based on
    the overall score and trend.
    """

    if score >= 90:
        return "BUY" if bullish else "SELL"

    elif score >= 75:
        return (
            "BUY (Moderate)"
            if bullish
            else "SELL (Moderate)"
        )

    elif score >= 60:
        return "WAIT"

    else:
        return "NO TRADE"