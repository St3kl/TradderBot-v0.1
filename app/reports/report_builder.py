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
    story=story
):
    """
    Build the Telegram report.
    """

    signals_text = ""

    for signal in decision["signals"]:
        signals_text += f"✅ {signal}\n"

    missing_text = ""

    for item in decision["missing"]:
        missing_text += f"❌ {item}\n"

    if not missing_text:
        missing_text = "None"

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

    # Only show Liquidity Sweep if it exists
    if "liquidity_sweep" in smart_money:
        smart += f"""

Liquidity Sweep:
{smart_money['liquidity_sweep']['type']}
"""

    confluence = f"""
🎯 CONFLUENCE

Signals

{signals_text}

Missing

{missing_text}
"""

    validation_report = f"""
🛡 TRADE VALIDATION

Setup Quality:
{validation["quality"]}/100

Trade Valid:
{"YES ✅" if validation["valid"] else "NO ❌"}

Reasons:

{"".join(f"✅ {r}\n" for r in validation["reasons"])}

Warnings:

{"".join(f"⚠️ {w}\n" for w in validation["warnings"])}
"""

    check = "📋 INSTITUTIONAL CHECKLIST\n\n"

    for item, passed in checklist.items():
        icon = "✅" if passed else "❌"
        check += f"{icon} {item}\n"
        
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