from pprint import pprint

from app.knowledge.relationship_engine import RelationshipEngine
from app.knowledge.reasoning_engine import ReasoningEngine
from app.knowledge.strategy_reasoner import StrategyReasoner

relationships = RelationshipEngine()

relationships.update([

    ("TREND","market_regime","TRENDING"),
    ("TREND","market_regime","TRENDING"),
    ("TREND","market_regime","TRENDING"),

    ("TREND","volatility","NORMAL"),
    ("TREND","volatility","NORMAL"),

    ("TREND","session","LONDON"),

    ("BREAKOUT","market_regime","TRENDING"),
    ("BREAKOUT","volatility","NORMAL"),

    ("RANGE","market_regime","RANGING")

])

reasoning = ReasoningEngine(

    relationships

)

selector = StrategyReasoner(

    reasoning

)

results = selector.select(

    strategies=[

        "TREND",

        "BREAKOUT",

        "RANGE"

    ],

    market_regime="TRENDING",

    volatility="NORMAL",

    session="LONDON"

)

print()

print("="*40)

print("STRATEGY REASONER")

print("="*40)

print()

for r in results:

    pprint(r)

print()

print("✓ TEST PASSED")