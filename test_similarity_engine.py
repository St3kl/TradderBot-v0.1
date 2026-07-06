from pprint import pprint

from app.core.registry import engine
from app.ai.context.context_builder import build_ai_context

session = engine.analyze("BTCUSDT")

context = build_ai_context(session)

print()

print("VECTOR")

pprint(context["vector"])

print()

print("MOST SIMILAR TRADE")

pprint(context["similar_trade"])