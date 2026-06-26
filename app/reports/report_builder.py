def build_report(
    symbol,
    tf_report,
    score,
    breakdown,
    grade,
    alignment,
    confidence,
    pattern,
    sr,
    trade,
    indicators,
    volume
):
    """
    Builds the Telegram analysis report.
    """

    report = f"""
📊 {symbol}

==============================
📈 Multi-Timeframe Trend
==============================

{tf_report}

==============================
⭐ Signal Score
==============================

Overall Score:
{score}/100

Grade:
{grade}

Trend:
{breakdown['Trend']}/25

RSI:
{breakdown['RSI']}/20

Volume:
{breakdown['Volume']}/20

MTF:
{breakdown['MTF']}/25

Pattern:
{breakdown['Pattern']}/10

==============================
📊 Market Analysis
==============================

Alignment:
{alignment}/4

Confidence:
{confidence}%

Pattern:
{pattern}

Support:
{sr['support']:.5f}

Resistance:
{sr['resistance']:.5f}

==============================
💰 Trade Setup
==============================

Entry:
{trade['entry']:.5f}

Stop Loss:
{trade['stop_loss']:.5f}

Take Profit:
{trade['take_profit']:.5f}

Risk Reward:
{trade['risk_reward']}

==============================
📉 Volatility
==============================

ATR:
{indicators.get('atr', 0):.2f}

Volume:
{volume['strength']}
"""

    return report