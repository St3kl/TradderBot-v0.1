def find_swings(
    highs,
    lows,
    lookback=2
):
    """
    Detect swing highs and swing lows.

    A swing high is higher than the
    candles around it.

    A swing low is lower than the
    candles around it.
    """

    swing_highs = []
    swing_lows = []

    for i in range(
        lookback,
        len(highs) - lookback
    ):

        high = highs[i]

        if all(
            high > highs[j]
            for j in range(
                i - lookback,
                i + lookback + 1
            )
            if j != i
        ):
            swing_highs.append(
                (i, high)
            )

        low = lows[i]

        if all(
            low < lows[j]
            for j in range(
                i - lookback,
                i + lookback + 1
            )
            if j != i
        ):
            swing_lows.append(
                (i, low)
            )

    return {
        "highs": swing_highs,
        "lows": swing_lows
    }