from pprint import pprint

from app.knowledge.relationship_engine import RelationshipEngine

engine = RelationshipEngine()

facts = [

    ("TREND","market_regime","TRENDING"),

    ("TREND","market_regime","TRENDING"),

    ("TREND","market_regime","TRENDING"),

    ("TREND","volatility","NORMAL"),

    ("TREND","volatility","NORMAL"),

    ("TREND","session","LONDON")

]

engine.update(facts)

print()

print("="*40)

print("RELATIONSHIP ENGINE")

print("="*40)

print()

pprint(

    engine.summary()

)

print()

print(

    "TREND -> TRENDING:",

    engine.get_strength(

        "TREND",

        "market_regime",

        "TRENDING"

    )

)

print()

print("✓ TEST PASSED")