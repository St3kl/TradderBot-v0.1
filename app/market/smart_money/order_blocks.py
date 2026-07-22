def detect_order_blocks(
    opens,
    highs,
    lows,
    closes
):
    """
    Detect simple bullish and bearish
    order blocks.
    """

    bullish_blocks = []

    bearish_blocks = []

    for i in range(1, len(closes)):

        previous_bearish = closes[i-1] < opens[i-1]

        current_bullish = closes[i] > opens[i]

        if previous_bearish and current_bullish:

            bullish_blocks.append({

                "index": i-1,

                "high": highs[i-1],

                "low": lows[i-1]

            })

        previous_bullish = closes[i-1] > opens[i-1]

        current_bearish = closes[i] < opens[i]

        if previous_bullish and current_bearish:

            bearish_blocks.append({

                "index": i-1,

                "high": highs[i-1],

                "low": lows[i-1]

            })

    return {

        "bullish": bullish_blocks,

        "bearish": bearish_blocks

    }