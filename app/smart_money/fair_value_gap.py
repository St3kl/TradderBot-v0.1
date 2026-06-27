def detect_fair_value_gaps(
    highs,
    lows
):
    """
    Detect bullish and bearish
    Fair Value Gaps.
    """

    bullish = []

    bearish = []

    for i in range(1, len(highs)-1):

        # -----------------------
        # Bullish FVG
        # -----------------------

        if lows[i+1] > highs[i-1]:

            bullish.append({

                "index": i,

                "top": lows[i+1],

                "bottom": highs[i-1]

            })

        # -----------------------
        # Bearish FVG
        # -----------------------

        if highs[i+1] < lows[i-1]:

            bearish.append({

                "index": i,

                "top": lows[i-1],

                "bottom": highs[i+1]

            })

    return {

        "bullish": bullish,

        "bearish": bearish

    }