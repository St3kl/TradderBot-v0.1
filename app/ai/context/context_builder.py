from app.ai.memory.memory_engine import MemoryEngine
from app.ai.memory.similarity_engine import SimilarityEngine
from app.ai.memory.vector_engine import VectorEngine


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

        "evolution": evolution,
        
        "market_regime": session.market_regime,
    }

    # ---------------------------------
    # Feature Vector
    # ---------------------------------

    vector_engine = VectorEngine()

    current_vector = vector_engine.build(context)

    context["vector"] = current_vector
    
    from app.ai.memory.performance_engine import PerformanceEngine

    performance = PerformanceEngine()

    context["performance"] = performance.build()
    
    from app.ai.memory.confidence_engine import ConfidenceEngine

    confidence_engine = ConfidenceEngine()

    context["confidence_calibration"] = confidence_engine.calibrate(

    session.decision["confidence"]

)

    # ---------------------------------
    # Similar Historical Trade
    # ---------------------------------

    similarity = SimilarityEngine()

    similar_trade = similarity.find_similar(
        session.symbol,
        current_vector
    )

    context["similar_trade"] = similar_trade

    return context

