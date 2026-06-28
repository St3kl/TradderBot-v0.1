def detect_liquidity_sweep(highs, lows, closes):
    """
    Detect buy-side and sell-side liquidity sweeps.
    """

    if len(closes) < 5:
        return {
            "buy_side": False,
            "sell_side": False,
            "type": "None"
        }

    last_close = closes[-1]

    previous_high = max(highs[-5:-1])
    previous_low = min(lows[-5:-1])

    last_high = highs[-1]
    last_low = lows[-1]

    buy_side = (
        last_high > previous_high
        and last_close < previous_high
    )

    sell_side = (
        last_low < previous_low
        and last_close > previous_low
    )

    sweep = "None"

    if buy_side:
        sweep = "Buy Side Sweep"

    elif sell_side:
        sweep = "Sell Side Sweep"

    return {
        "buy_side": buy_side,
        "sell_side": sell_side,
        "type": sweep
    }