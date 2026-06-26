import os

from dotenv import load_dotenv

from app.bot.telegram_bot import (
    build_bot
)

load_dotenv()

token = os.getenv(
    "TELEGRAM_TOKEN"
)

app = build_bot(token)

app.run_polling()