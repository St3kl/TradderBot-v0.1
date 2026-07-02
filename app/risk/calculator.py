def calculate_trade_levels(
    price,
    support,
    resistance,
    bullish=True,
    atr=0
):
    """
    Calculate Entry, Stop Loss, Take Profit and Risk/Reward.
    """

    entry = price

    if bullish:

        stop_loss = entry - (atr * 1.5) if atr > 0 else support

        risk = entry - stop_loss
        reward = risk * 2
        take_profit = entry + reward

    else:

        stop_loss = entry + (atr * 1.5) if atr > 0 else resistance

        risk = stop_loss - entry
        reward = risk * 2
        take_profit = entry - reward

    risk_reward = 0

    if risk > 0:
        risk_reward = round(reward / risk, 2)

    return {
        "entry": round(entry, 5),
        "stop_loss": round(stop_loss, 5),
        "take_profit": round(take_profit, 5),
        "risk_reward": risk_reward
    }