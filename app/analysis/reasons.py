def build_reasons(
    indicators,
    bullish,
    volume,
    alignment,
    pattern
):
    """
    Build a list explaining why
    the bot made its decision.
    """

    reasons = []

    # -----------------------
    # Trend
    # -----------------------

    if bullish:
        reasons.append(
            "Bullish EMA trend"
        )
    else:
        reasons.append(
            "Bearish EMA trend"
        )

    # -----------------------
    # RSI
    # -----------------------

    rsi = indicators["rsi"]

    if 55 <= rsi <= 65:

        reasons.append(
            "Healthy RSI"
        )

    elif rsi > 70:

        reasons.append(
            "RSI overbought"
        )

    elif rsi < 30:

        reasons.append(
            "RSI oversold"
        )

    else:

        reasons.append(
            "Neutral RSI"
        )

    # -----------------------
    # Volume
    # -----------------------

    reasons.append(
        f"Volume: {volume['strength']}"
    )

    # -----------------------
    # Multi Timeframe
    # -----------------------

    reasons.append(
        f"Alignment: {alignment}/4"
    )

    # -----------------------
    # Pattern
    # -----------------------

    if pattern != "No Pattern":

        reasons.append(
            f"Pattern: {pattern}"
        )

    return reasons