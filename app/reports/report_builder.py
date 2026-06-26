def build_report(
    symbol,
    tf_report,
    decision,
    alignment,
    pattern,
    sr,
    trade,
    indicators,
    volume
):
    """
    Build the Telegram report.
    """

    reasons_text = ""

    for reason in decision["reasons"]:
        reasons_text += f"• {reason}\n"

    report = f"""
📊 {symbol}

Decision:
{decision["action"]}

Signal Score:
{decision["score"]}/100

Grade:
{decision["grade"]}

Confidence:
{decision["confidence"]}%

Multi Timeframe

{tf_report}

Trend:
{decision["breakdown"]["Trend"]}/25

RSI:
{decision["breakdown"]["RSI"]}/20

Volume:
{decision["breakdown"]["Volume"]}/20

MTF:
{decision["breakdown"]["MTF"]}/25

Pattern:
{decision["breakdown"]["Pattern"]}/10

Pattern Detected:
{pattern}

Support:
{sr["support"]:.5f}

Resistance:
{sr["resistance"]:.5f}

Entry:
{trade["entry"]:.5f}

Stop Loss:
{trade["stop_loss"]:.5f}

Take Profit:
{trade["take_profit"]:.5f}

Risk Reward:
{trade["risk_reward"]}

ATR:
{indicators["atr"]:.2f}

Volume:
{volume["strength"]}

Reasons:

{reasons_text}
"""

    return report