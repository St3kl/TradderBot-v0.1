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

    # Create symbol if it doesn't exist
    if symbol not in memory:
        memory[symbol] = []

    # Automatic migration from old format
    elif isinstance(memory[symbol], dict):
        memory[symbol] = [memory[symbol]]

    memory[symbol].append(snapshot)

    save_json(FILE, memory)


def load_market_snapshot(symbol):

    memory = load_json(FILE)

    data = memory.get(symbol, [])

    # Automatic migration when loading
    if isinstance(data, dict):
        data = [data]

    return data