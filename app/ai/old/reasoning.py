def build_reasoning(context):

    observations = []

    technical = context["technical"]
    smart = context["smart_money"]

    if technical["trend"] == "Bullish":
        observations.append(
            "Market structure is bullish."
        )
    else:
        observations.append(
            "Market structure is bearish."
        )

    if smart["premium_discount"]["zone"] == "Discount":
        observations.append(
            "Price is trading in Discount."
        )
    else:
        observations.append(
            "Price is trading in Premium."
        )

    if smart["liquidity_sweep"]["buy_side"]:
        observations.append(
            "Buy-side liquidity has been swept."
        )

    if smart["liquidity_sweep"]["sell_side"]:
        observations.append(
            "Sell-side liquidity has been swept."
        )

    if smart["order_blocks"]["bullish"] > 0:
        observations.append(
            "Bullish Order Blocks are present."
        )

    if smart["order_blocks"]["bearish"] > 0:
        observations.append(
            "Bearish Order Blocks are present."
        )

    if technical["volume"]["score"] >= 15:
        observations.append(
            "Volume confirms the move."
        )
    else:
        observations.append(
            "Volume is weak."
        )

    if technical["alignment"] >= 3:
        observations.append(
            "Higher timeframes are aligned."
        )
    else:
        observations.append(
            "Higher timeframes disagree."
        )

    return observations