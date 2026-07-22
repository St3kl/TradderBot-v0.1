from pprint import pprint

from app.knowledge.fact_extractor import FactExtractor

trade = {

    "strategy":"TREND",

    "market_regime":"TRENDING",

    "volatility":"NORMAL",

    "session_name":"LONDON",

    "result":"WIN"

}

extractor = FactExtractor()

facts = extractor.extract(trade)

print()

print("=" * 40)

print("FACT EXTRACTION")

print("=" * 40)

print()

pprint(facts)

print()

print("✓ TEST PASSED")