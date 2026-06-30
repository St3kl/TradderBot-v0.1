from app.ai.reasoning import build_reasoning


def build_ai_context(
    symbol,
    indicators,
    decision,
    trade,
    structure,
    smart_money,
    pattern,
    volume,
    validation,
    checklist,
    tf_report,
    alignment,
    confluence,
):
    """
    Builds a complete context object for the AI.

    Every AI model will consume this object instead of
    dozens of individual variables.
    """

    context = {

        # -------------------------
        # Symbol
        # -------------------------

        "symbol": symbol,

        # -------------------------
        # Current Market
        # -------------------------

        "market": {

            "price": indicators["price"],
            "ema50": indicators["ema50"],
            "ema200": indicators["ema200"],
            "rsi": indicators["rsi"],
            "atr": indicators["atr"]

        },

        # -------------------------
        # Technical Analysis
        # -------------------------

        "technical": {

            "trend": structure["trend"],
            "pattern": pattern,
            "volume": volume,
            "alignment": alignment,
            "multi_timeframe": tf_report

        },

        # -------------------------
        # Smart Money
        # -------------------------

        "smart_money": smart_money,

        # -------------------------
        # Trade
        # -------------------------

        "trade": trade,

        # -------------------------
        # Decision Engine
        # -------------------------

        "decision": decision,

        # -------------------------
        # Confluence
        # -------------------------

        "confluence": confluence,

        # -------------------------
        # Validation
        # -------------------------

        "validation": validation,

        # -------------------------
        # Institutional Checklist
        # -------------------------

        "checklist": checklist

    }

    # -------------------------
    # AI Reasoning
    # -------------------------

    context["reasoning"] = build_reasoning(context)

    return context