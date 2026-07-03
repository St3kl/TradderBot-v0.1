def build_reasoning(context):
    """
    Converts raw market data into structured
    institutional reasoning for the AI.
    """

    reasoning = []

    market = context["market"]
    technical = context["technical"]
    smc = context["smart_money"]
    validation = context["validation"]
    decision = context["decision"]

    # ---------------------------------
    # Trend
    # ---------------------------------

    if market["ema50"] > market["ema200"]:
        reasoning.append(
            "The long-term trend is bullish because EMA 50 is above EMA 200."
        )
    else:
        reasoning.append(
            "The long-term trend is bearish because EMA 50 is below EMA 200."
        )

    # ---------------------------------
    # RSI
    # ---------------------------------

    rsi = market["rsi"]

    if rsi < 30:
        reasoning.append(
            "RSI indicates oversold conditions."
        )

    elif rsi > 70:
        reasoning.append(
            "RSI indicates overbought conditions."
        )

    else:
        reasoning.append(
            "RSI is within a neutral range."
        )

    # ---------------------------------
    # Structure
    # ---------------------------------

    reasoning.append(
        f"Market structure is currently {technical['trend']}."
    )

    # ---------------------------------
    # Smart Money
    # ---------------------------------

    zone = smc["premium_discount"]["zone"]

    reasoning.append(
        f"Price is currently trading inside the {zone} zone."
    )

    sweep = smc["liquidity_sweep"]["type"]

    if sweep != "None":
        reasoning.append(
            f"A {sweep} has recently occurred."
        )

    # ---------------------------------
    # Order Blocks
    # ---------------------------------

    bullish_ob = smc["order_blocks"]["bullish"]
    bearish_ob = smc["order_blocks"]["bearish"]

    if bullish_ob > bearish_ob:
        reasoning.append(
            "Bullish Order Blocks dominate the market."
        )

    elif bearish_ob > bullish_ob:
        reasoning.append(
            "Bearish Order Blocks dominate the market."
        )

    # ---------------------------------
    # Fair Value Gaps
    # ---------------------------------

    bullish_fvg = smc["fair_value_gaps"]["bullish"]
    bearish_fvg = smc["fair_value_gaps"]["bearish"]

    if bullish_fvg > bearish_fvg:
        reasoning.append(
            "Bullish Fair Value Gaps are more prevalent."
        )

    elif bearish_fvg > bullish_fvg:
        reasoning.append(
            "Bearish Fair Value Gaps are more prevalent."
        )

    # ---------------------------------
    # Volume
    # ---------------------------------

    reasoning.append(
        f"Volume strength is {technical['volume']['strength']}."
    )

    # ---------------------------------
    # Validation
    # ---------------------------------

    if validation["valid"]:
        reasoning.append(
            "The trade setup passed all validation filters."
        )
    else:
        reasoning.append(
            "The trade setup failed one or more validation filters."
        )

    # ---------------------------------
    # Decision
    # ---------------------------------

    reasoning.append(
        f"The trading engine recommends a {decision['action']} decision."
    )

    return reasoning