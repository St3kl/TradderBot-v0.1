def detect_choch(
    closes,
    swing_highs,
    swing_lows,
    bullish
):
    """
    Detect Change of Character (CHoCH).

    If the market is bullish,
    a break below the last swing low
    signals a bearish CHoCH.

    If the market is bearish,
    a break above the last swing high
    signals a bullish CHoCH.
    """

    latest_close = closes[-1]

    if bullish:

        if swing_lows:

            last_low = swing_lows[-1][1]

            if latest_close < last_low:

                return {
                    "type": "Bearish CHoCH",
                    "level": last_low
                }

    else:

        if swing_highs:

            last_high = swing_highs[-1][1]

            if latest_close > last_high:

                return {
                    "type": "Bullish CHoCH",
                    "level": last_high
                }

    return {
        "type": "No CHoCH",
        "level": None
    }