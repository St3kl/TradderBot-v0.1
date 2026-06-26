def calculate_trade_levels(
    price,
    support,
    resistance,
    bullish=True,
    atr=0
):
    """
    Calculate Entry, Stop Loss and Take Profit.

    If ATR is available, use an ATR-based stop loss.
    Otherwise, fall back to Support/Resistance.
    """

    entry = price

    if bullish:

        if atr > 0:
            stop_loss = entry - (atr * 1.5)
        else:
            stop_loss = support

        risk = entry - stop_loss

        take_profit = entry + (risk * 2)

    else:

        if atr > 0:
            stop_loss = entry + (atr * 1.5)
        else:
            stop_loss = resistance

        risk = stop_loss - entry

        take_profit = entry - (risk * 2)

    return {
        "entry": round(entry, 5),
        "stop_loss": round(stop_loss, 5),
        "take_profit": round(take_profit, 5),
        "risk_reward": "1:2"
    }