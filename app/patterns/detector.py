def detect_pattern(indicators):

    if (
        indicators["price"]
        > indicators["ema50"]
        and indicators["ema50"]
        > indicators["ema200"]
    ):
        return "Trend Continuation"

    if indicators["rsi"] > 70:
        return "Overbought"

    if indicators["rsi"] < 30:
        return "Oversold"

    return "No Strong Pattern"