from app.market.regime_engine import RegimeEngine

engine = RegimeEngine()

result = engine.classify({

    "adx": 34,

    "atr": 1250

})

print(result)