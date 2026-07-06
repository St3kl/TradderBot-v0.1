from pprint import pprint

from app.core.registry import engine


session = engine.analyze("BTCUSDT")

pprint(session.ai_report)