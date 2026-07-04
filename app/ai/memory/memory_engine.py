from app.ai.memory.market_memory import (
    save_market_snapshot,
    load_market_snapshot
)
from app.ai.memory.comparator import compare_sessions


class MemoryEngine:

    def save(self, session):

        save_market_snapshot(session)

    def load(self, symbol):

        return load_market_snapshot(symbol)
    
    def compare(self, symbol):

        history = self.load(symbol)

        if len(history) < 2:

            return None

        previous = history[-2]
        current = history[-1]

        return compare_sessions(
            previous,
            current
        )
        
        
    