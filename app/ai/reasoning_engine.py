"""
Reasoning Engine

Transforms the analysis results into structured reasoning that
can later be consumed by any AI model (OpenAI, Ollama, DeepSeek,
Claude, etc.).
"""


def build_reasoning(context):
    """
    Generate structured reasoning from the complete AI context.

    Returns
    -------
    dict
        {
            bullish_arguments,
            bearish_arguments,
            missing_confirmations,
            institutional_view,
            trade_bias,
            confidence
        }
    """

    bullish_arguments = []
    bearish_arguments = []
    missing_confirmations = []

    market = context["market"]
    technical = context["technical"]
    smart_money = context["smart_money"]
    decision = context["decision"]
    validation = context["validation"]
    checklist = context["checklist"]

    # --------------------------------------------------
    # Trend
    # --------------------------------------------------

    if market["ema50"] > market["ema200"]:
        bullish_arguments.append(
            "The 50 EMA is above the 200 EMA, confirming a bullish long-term trend."
        )
    else:
        bearish_arguments.append(
            "The 50 EMA remains below the 200 EMA, indicating a bearish long-term trend."
        )
        missing_confirmations.append(
            "Bullish EMA crossover"
        )

    # --------------------------------------------------
    # Structure
    # --------------------------------------------------

    if technical["trend"] == "Bullish":
        bullish_arguments.append(
            "Market structure is bullish."
        )
    else:
        bearish_arguments.append(
            "Market structure is bearish."
        )
        missing_confirmations.append(
            "Bullish market structure"
        )

    # --------------------------------------------------
    # Pattern
    # --------------------------------------------------

    pattern = technical["pattern"]

    if pattern and pattern != "No Pattern":
        bullish_arguments.append(
            f"Detected chart pattern: {pattern}."
        )
    else:
        missing_confirmations.append(
            "High-confidence chart pattern"
        )

    # --------------------------------------------------
    # Volume
    # --------------------------------------------------

    volume = technical["volume"]

    if volume["score"] >= 15:
        bullish_arguments.append(
            "Volume supports the current move."
        )
    else:
        bearish_arguments.append(
            "Volume confirmation is weak."
        )

    # --------------------------------------------------
    # Order Blocks
    # --------------------------------------------------

    if smart_money["order_blocks"]["bullish"] > 0:
        bullish_arguments.append(
            "Bullish Order Blocks are present."
        )

    # --------------------------------------------------
    # Fair Value Gaps
    # --------------------------------------------------

    if smart_money["fair_value_gaps"]["bullish"] > 0:
        bullish_arguments.append(
            "Bullish Fair Value Gaps remain open."
        )

    # --------------------------------------------------
    # Liquidity Sweep
    # --------------------------------------------------

    sweep = smart_money.get("liquidity_sweep", {})

    if sweep.get("sell_side"):
        bullish_arguments.append(
            "A Sell-Side Liquidity Sweep suggests institutional accumulation."
        )

    if sweep.get("buy_side"):
        bearish_arguments.append(
            "A Buy-Side Liquidity Sweep suggests institutional distribution."
        )

    # --------------------------------------------------
    # Premium / Discount
    # --------------------------------------------------

    zone = smart_money["premium_discount"]["zone"]

    if zone == "Discount":
        bullish_arguments.append(
            "Price is trading in the Discount Zone."
        )

    elif zone == "Premium":
        bearish_arguments.append(
            "Price is trading in the Premium Zone."
        )

    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    if validation["valid"]:
        bullish_arguments.append(
            "The trade passed the validation process."
        )
    else:
        bearish_arguments.append(
            "The trade failed validation."
        )

    # --------------------------------------------------
    # Institutional Checklist
    # --------------------------------------------------

    failed = []

    for item, passed in checklist.items():

        if not passed:
            failed.append(item)

    missing_confirmations.extend(failed)

    # --------------------------------------------------
    # Institutional View
    # --------------------------------------------------

    if decision["action"] == "BUY":

        institutional_view = (
            "Institutional activity appears supportive of long positions."
        )

    elif decision["action"] == "SELL":

        institutional_view = (
            "Institutional activity appears supportive of short positions."
        )

    else:

        institutional_view = (
            "Institutional positioning remains neutral."
        )

    # --------------------------------------------------
    # Output
    # --------------------------------------------------

    return {

        "bullish_arguments": bullish_arguments,

        "bearish_arguments": bearish_arguments,

        "missing_confirmations": list(set(missing_confirmations)),

        "institutional_view": institutional_view,

        "trade_bias": decision["action"],

        "confidence": decision["confidence"]
    }