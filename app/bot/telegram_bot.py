from telegram import Update
from telegram.ext import CommandHandler, Application, ContextTypes

<<<<<<< HEAD
from app.services.analysis_service import (
    analyze_symbol
)

=======
from app.market.indicators import get_market_indicators

from app.patterns.detector import detect_pattern

from app.market.forex_indicators import get_forex_indicators
>>>>>>> 4440390 (Tradderbot_v01-- trading actions)

from app.patterns.support_resistance import find_support_resistance

from app.risk.calculator import calculate_trade_levels




async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:

        await update.message.reply_text("Usage: /analyze BTCUSDT")

        return

    symbol = context.args[0].upper()

<<<<<<< HEAD
    report = analyze_symbol(
        symbol
    )

    await update.message.reply_text(
        report
    )
=======

    if symbol.endswith("USDT"):

        indicators = get_market_indicators(symbol)

    else:

        forex_symbol = symbol[:3] + "/" + symbol[3:]

        indicators = get_forex_indicators(forex_symbol)

    pattern = detect_pattern(indicators)


    
    bullish = (
    indicators["ema50"] >
    indicators["ema200"]
)
    sr = find_support_resistance(
    indicators["closes"]
)
    trade = calculate_trade_levels(
    indicators["price"],
    sr["support"],
    sr["resistance"],
    bullish
)
    confidence = 75

    report = f"""
📊 {symbol}

Price:
{indicators['price']:.5f}

Trend:
{'Bullish' if bullish else 'Bearish'}

Pattern:
{pattern}

Support:
{sr['support']:.5f}

Resistance:
{sr['resistance']:.5f}

Entry:
{trade['entry']:.5f}

Stop Loss:
{trade['stop_loss']:.5f}

Take Profit:
{trade['take_profit']:.5f}

Risk Reward:
{trade['risk_reward']}

Confidence:
{confidence}%
"""

    await update.message.reply_text(report)
>>>>>>> 4440390 (Tradderbot_v01-- trading actions)


def build_bot(token):

<<<<<<< HEAD
    app = (
        Application
        .builder()
        .token(token)
        .build()
    )
=======
    app = Application.builder().token(token).build()
>>>>>>> 4440390 (Tradderbot_v01-- trading actions)

    app.add_handler(CommandHandler("analyze", analyze))

    return app
