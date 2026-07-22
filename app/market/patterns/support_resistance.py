def find_support_resistance(
    candles
):

    lows = candles[-50:]
    highs = candles[-50:]

    support = min(lows)

    resistance = max(highs)

    return {
        "support": support,
        "resistance": resistance
    }