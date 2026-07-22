from app.market.regime.regime_engine import MarketRegimeEngine

engine = MarketRegimeEngine()

result = engine.analyze(

    ema50=105,

    ema200=100,

    adx=34,

    atr=120,

    closes=[100] * 100

)

print(result)