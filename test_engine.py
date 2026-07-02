from app.core.registry import engine

session = engine.analyze("BTCUSDT")

print(session.symbol)

print(session.indicators.keys())
print(session.bullish)
print(session.sr)
print(session.trade)
print(session.structure)