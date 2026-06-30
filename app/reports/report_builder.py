print("LOADING REPORT BUILDER")


def build_report(
    symbol,
    tf_report,
    decision,
    alignment,
    pattern,
    sr,
    trade,
    indicators,
    volume,
    structure,
    smart_money,
    validation,
    checklist,
    story
):
    """
    Build the Telegram report.
    """

    # ----------------------------------
    # Confluence text
    # ----------------------------------

    signals_text = ""

    for signal in decision["signals"]:
        signals_text += f"✅ {signal}\n"

    missing_text = ""

    for item in decision["missing"]:
        missing_text += f"❌ {item}\n"

    if not missing_text:
        missing_text = "None"

    # ----------------------------------
    # Validation text
    # ----------------------------------

    reasons_text = ""

    for reason in validation["reasons"]:
        reasons_text += f"✅ {reason}\n"

    warnings_text = ""

    for warning in validation["warnings"]:
        warnings_text += f"⚠️ {warning}\n"

    if warnings_text == "":
        warnings_text = "None"

    # ----------------------------------
    # Summary
    # ----------------------------------

    summary = f"""
📊 {symbol}

🎯 Decision:
{decision["action"]}

Score:
{decision["score"]}/100

Confidence:
{decision["confidence"]}%

Risk:
{decision["risk"]}

Strength:
{decision["strength"]}

Entry:
{trade["entry"]:.5f}

Stop Loss:
{trade["stop_loss"]:.5f}

Take Profit:
{trade["take_profit"]:.5f}

Setup Quality:
{validation["quality"]}/100

Trade Valid:
{"YES ✅" if validation["valid"] else "NO ❌"}
"""

    # ----------------------------------
    # Technical
    # ----------------------------------

    technical = f"""
📈 TECHNICAL ANALYSIS

Trend:
{structure["trend"]}

Pattern:
{pattern}

Support:
{sr["support"]:.5f}

Resistance:
{sr["resistance"]:.5f}

ATR:
{indicators["atr"]:.2f}

Volume:
{volume["strength"]}

Multi-Timeframe

{tf_report}
"""

    # ----------------------------------
    # Smart Money
    # ----------------------------------

    smart = f"""
🧠 SMART MONEY

Equal Highs:
{smart_money["liquidity"]["equal_highs"]}

Equal Lows:
{smart_money["liquidity"]["equal_lows"]}

Bullish Order Blocks:
{smart_money["order_blocks"]["bullish"]}

Bearish Order Blocks:
{smart_money["order_blocks"]["bearish"]}

Bullish FVG:
{smart_money["fair_value_gaps"]["bullish"]}

Bearish FVG:
{smart_money["fair_value_gaps"]["bearish"]}

Premium / Discount:
{smart_money["premium_discount"]["zone"]}

Equilibrium:
{smart_money["premium_discount"]["equilibrium"]:.2f}
"""

    if "liquidity_sweep" in smart_money:

        smart += f"""

Liquidity Sweep:
{smart_money["liquidity_sweep"]["type"]}
"""

    # ----------------------------------
    # Confluence
    # ----------------------------------

    confluence = f"""
🎯 CONFLUENCE

Signals

{signals_text}

Missing

{missing_text}
"""

    # ----------------------------------
    # Validation
    # ----------------------------------

    validation_report = f"""
🛡 TRADE VALIDATION

Setup Quality:
{validation["quality"]}/100

Trade Valid:
{"YES ✅" if validation["valid"] else "NO ❌"}

Reasons:

{reasons_text}

Warnings:

{warnings_text}
"""

    # ----------------------------------
    # Institutional Checklist
    # ----------------------------------

    check = "📋 INSTITUTIONAL CHECKLIST\n\n"

    for item, passed in checklist.items():

        icon = "✅" if passed else "❌"

        check += f"{icon} {item}\n"

    # ----------------------------------
    # AI Narrator
    # ----------------------------------

    ai_report = f"""
🤖 AI MARKET ANALYSIS

{story}
"""

    return [
        summary,
        technical,
        smart,
        confluence,
        validation_report,
        check,
        ai_report
    ]