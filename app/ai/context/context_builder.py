from app.ai.memory.memory_engine import MemoryEngine


def build_ai_context(session):
    """
    Builds the complete AI context from the TradingSession.

    Every AI component receives this context instead
    of accessing the TradingSession directly.
    """

    # ---------------------------------
    # Memory
    # ---------------------------------

    memory = MemoryEngine()

    comparison = memory.compare(session.symbol)

    evolution = memory.evolution(session.symbol)

    # ---------------------------------
    # Context
    # ---------------------------------

    context = {

        # Symbol
        "symbol": session.symbol,

        # Market
        "market": {
            "price": session.indicators["price"],
            "ema50": session.indicators["ema50"],
            "ema200": session.indicators["ema200"],
            "rsi": session.indicators["rsi"],
            "adx": session.indicators["adx"],
            "atr": session.indicators["atr"]
        },

        # Technical
        "technical": {
            "trend": session.structure["trend"],
            "pattern": session.pattern,
            "volume": session.volume,
            "alignment": session.alignment,
            "multi_timeframe": session.mtf
        },

        # Structure
        "structure": session.structure,

        # Smart Money
        "smart_money": session.smart_money,

        # Trade
        "trade": session.trade,

        # Decision
        "decision": session.decision,

        # Confluence
        "confluence": session.confluence,

        # Validation
        "validation": session.validation,

        # Checklist
        "checklist": session.checklist,

        # Historical Memory
        "comparison": comparison,

        "evolution": evolution

    }

    return context