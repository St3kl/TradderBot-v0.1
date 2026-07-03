from app.ai.memory.market_memory import (
    save_market_snapshot,
    load_market_snapshot
)


class MemoryEngine:

    def save(self, session):

        save_market_snapshot(session)

    def load(self, symbol):

        return load_market_snapshot(symbol)