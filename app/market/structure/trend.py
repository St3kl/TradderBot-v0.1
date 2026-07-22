def detect_trend(
    swing_highs,
    swing_lows
):
    """
    Determine market trend
    using swing highs and lows.
    """

    if len(swing_highs) < 2 or len(swing_lows) < 2:

        return "Unknown"

    last_high = swing_highs[-1][1]
    prev_high = swing_highs[-2][1]

    last_low = swing_lows[-1][1]
    prev_low = swing_lows[-2][1]

    # -------------------------
    # Bullish
    # -------------------------

    if (
        last_high > prev_high and
        last_low > prev_low
    ):

        return "Bullish"

    # -------------------------
    # Bearish
    # -------------------------

    if (
        last_high < prev_high and
        last_low < prev_low
    ):

        return "Bearish"

    # -------------------------
    # Sideways
    # -------------------------

    return "Sideways"