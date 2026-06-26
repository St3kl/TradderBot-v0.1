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

    report = analyze_symbol(
        symbol
    )

    await update.message.reply_text(
        report
    )


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