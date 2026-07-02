from app.core.registry import engine

session = engine.analyze("BTCUSDT")

print(session.symbol)

print(session.indicators.keys())
print(session.bullish)