from app.core.registry import engine

session = engine.analyze("BTCUSDT")

print(session.symbol)

print(session.indicators.keys())
print(session.bullish)
print(session.sr)
print(session.trade)
print(session.structure)
print(session.smart_money)
print(session.volume)
print(session.alignment)
print(session.tf_report)
print(session.confluence)
print(session.decision)
print(session.validation)