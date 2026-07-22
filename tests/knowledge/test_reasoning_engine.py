from pprint import pprint

from app.knowledge.relationship_engine import RelationshipEngine
from app.knowledge.reasoning_engine import ReasoningEngine

relationships = RelationshipEngine()

relationships.update([

    ("TREND","market_regime","TRENDING"),

    ("TREND","market_regime","TRENDING"),

    ("TREND","market_regime","TRENDING"),

    ("TREND","volatility","NORMAL"),

    ("TREND","volatility","NORMAL"),

    ("TREND","session","LONDON")

])

reasoning = ReasoningEngine(

    relationships

)

result = reasoning.recommend(

    strategy="TREND",

    market_regime="TRENDING",

    volatility="NORMAL",

    session="LONDON"

)

print()

print("="*40)

print("REASONING ENGINE")

print("="*40)

print()

pprint(result)

print()

print("✓ TEST PASSED")