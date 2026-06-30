def build_reasoning(context):
    """
    Converts market data into human reasoning.

    Returns a list of explanations that later become
    the AI market story.
    """

    reasoning = []

    market = context["market"]
    technical = context["technical"]
    smart = context["smart_money"]
    validation = context["validation"]
    decision = context["decision"]

    # ----------------------------------
    # Trend
    # ----------------------------------

    if technical["trend"] == "Bullish":
        reasoning.append(
            "Market structure remains bullish."
        )
    else:
        reasoning.append(
            "Market structure remains bearish."
        )

    # ----------------------------------
    # EMA
    # ----------------------------------

    if market["ema50"] > market["ema200"]:
        reasoning.append(
            "The 50 EMA is above the 200 EMA, confirming trend continuation."
        )
    else:
        reasoning.append(
            "The 50 EMA is below the 200 EMA, suggesting bearish pressure."
        )

    # ----------------------------------
    # RSI
    # ----------------------------------

    if market["rsi"] < 30:
        reasoning.append(
            "RSI indicates oversold conditions."
        )

    elif market["rsi"] > 70:
        reasoning.append(
            "RSI indicates overbought conditions."
        )

    else:
        reasoning.append(
            "RSI remains neutral."
        )

    # ----------------------------------
    # Volume
    # ----------------------------------

    if technical["volume"]["score"] >= 15:
        reasoning.append(
            "Volume confirms participation."
        )
    else:
        reasoning.append(
            "Volume remains below institutional levels."
        )

    # ----------------------------------
    # Smart Money
    # ----------------------------------

    if smart["order_blocks"]["bullish"] > 0:
        reasoning.append(
            "Bullish Order Blocks are present."
        )

    if smart["fair_value_gaps"]["bullish"] > 0:
        reasoning.append(
            "Bullish Fair Value Gaps remain open."
        )

    if smart["liquidity_sweep"]["sell_side"]:
        reasoning.append(
            "Sell-side liquidity has been swept."
        )

    if smart["premium_discount"]["zone"] == "Discount":
        reasoning.append(
            "Price is trading inside the institutional discount zone."
        )

    # ----------------------------------
    # Validation
    # ----------------------------------

    if validation["valid"]:
        reasoning.append(
            "Trade validation passed institutional filters."
        )
    else:
        reasoning.append(
            "Trade validation failed institutional filters."
        )

    # ----------------------------------
    # Final Decision
    # ----------------------------------

    reasoning.append(
        f"Final decision: {decision['action']}."
    )

    return reasoning