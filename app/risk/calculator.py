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
        reward = risk * 2
        take_profit = entry + reward

    else:

        if atr > 0:
            stop_loss = entry + (atr * 1.5)
        else:
            stop_loss = resistance

        risk = stop_loss - entry
        reward = risk * 2
        take_profit = entry - reward

    # Prevent division by zero
    if risk > 0:
        risk_reward = reward / risk
    else:
        risk_reward = 0

    return {
        "entry": round(entry, 5),
        "stop_loss": round(stop_loss, 5),
        "take_profit": round(take_profit, 5),
        "risk_reward": round(risk_reward, 2)
    }