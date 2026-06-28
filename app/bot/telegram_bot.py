from telegram import Update
from telegram.ext import (
    CommandHandler,
    Application,
    ContextTypes
)

from app.services.analysis_service import (
    analyze_symbol
)


async def analyze(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if len(context.args) == 0:

        await update.message.reply_text(
            "Usage: /analyze BTCUSDT"
        )

        return

    symbol = context.args[0].upper()

    reports = analyze_symbol(symbol)

    # Send each report as a separate Telegram message
    for i, report in enumerate(reports):
        print("=" * 50)
    print(f"REPORT {i+1}")
    print(f"Length: {len(report)}")
    print(report[:500])  # Preview first 500 chars
    print("=" * 50)

    await update.message.reply_text(report)


def build_bot(token):

    app = (
        Application
        .builder()
        .token(token)
        .build()
    )

    app.add_handler(
        CommandHandler(
            "analyze",
            analyze
        )
    )

    return app