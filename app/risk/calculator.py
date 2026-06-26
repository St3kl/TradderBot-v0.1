def calculate_trade_levels(
    price,
    support,
    resistance,
<<<<<<< HEAD
    bullish=True,
    atr=0
=======
    bullish=True
>>>>>>> 4440390 (Tradderbot_v01-- trading actions)
):

    if bullish:

        entry = price
<<<<<<< HEAD

        stop_loss = (
            entry -
            atr * 1.5
        )

        risk = (
            entry -
            stop_loss
        )
=======
        stop_loss = support

        risk = entry - stop_loss
>>>>>>> 4440390 (Tradderbot_v01-- trading actions)

        take_profit = (
            entry +
            risk * 2
        )

    else:

        entry = price
<<<<<<< HEAD

        stop_loss = (
            entry +
            atr * 1.5
        )

        risk = (
            stop_loss -
            entry
        )
=======
        stop_loss = resistance

        risk = stop_loss - entry
>>>>>>> 4440390 (Tradderbot_v01-- trading actions)

        take_profit = (
            entry -
            risk * 2
        )

    return {
<<<<<<< HEAD
        "entry": round(entry, 5),
        "stop_loss": round(stop_loss, 5),
        "take_profit": round(take_profit, 5),
=======
        "entry": entry,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
>>>>>>> 4440390 (Tradderbot_v01-- trading actions)
        "risk_reward": "1:2"
    }