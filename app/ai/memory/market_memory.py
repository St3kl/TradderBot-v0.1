from datetime import datetime

from app.ai.memory.storage import (
    load_json,
    save_json
)

FILE = "market_memory.json"


def save_market_snapshot(session):

    memory = load_json(FILE)

    symbol = session.symbol

    snapshot = {

        "timestamp": datetime.utcnow().isoformat(),

        "trend": session.trend,

        "bullish": session.bullish,

        "price": session.indicators.get("price"),

        "confidence": session.validation.get(
            "confidence",
            0
        ),

        "decision": session.decision,

        "trade": session.trade

    }

    if symbol not in memory:

        memory[symbol] = []

    memory[symbol].append(snapshot)

    save_json(FILE, memory)

def load_market_snapshot(symbol):

    memory = load_json(FILE)

    return memory.get(symbol, [])