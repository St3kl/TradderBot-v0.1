from app.analytics.market_regime_analyzer import MarketRegimeAnalyzer

trades = [

    {"market_regime": "TRENDING", "result": "WIN"},

    {"market_regime": "TRENDING", "result": "LOSS"},

    {"market_regime": "RANGING", "result": "WIN"},

    {"market_regime": "RANGING", "result": "WIN"},

    {"market_regime": "VOLATILE", "result": "LOSS"}

]

engine = MarketRegimeAnalyzer()

result = engine.analyze(trades)

engine.print(result)