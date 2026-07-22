def detect_liquidity(
    highs,
    lows,
    tolerance=0.001
):
    """
    Detect Equal Highs and Equal Lows.

    These areas often contain liquidity.
    """

    equal_highs = []

    equal_lows = []

    # -------------------------
    # Equal Highs
    # -------------------------

    for i in range(len(highs)-1):

        for j in range(i+1, len(highs)):

            diff = abs(highs[i]-highs[j])

            if diff <= highs[i] * tolerance:

                equal_highs.append(
                    (
                        i,
                        j,
                        highs[i]
                    )
                )

    # -------------------------
    # Equal Lows
    # -------------------------

    for i in range(len(lows)-1):

        for j in range(i+1, len(lows)):

            diff = abs(lows[i]-lows[j])

            if diff <= lows[i] * tolerance:

                equal_lows.append(
                    (
                        i,
                        j,
                        lows[i]
                    )
                )

    return {

        "equal_highs": equal_highs,

        "equal_lows": equal_lows

    }