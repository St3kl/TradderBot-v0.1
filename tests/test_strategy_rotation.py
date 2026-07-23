from app.portfolio.strategy_rotation import StrategyRotation

strategies = [

    {"name":"TREND","score":91},

    {"name":"BREAKOUT","score":82},

    {"name":"RANGE","score":68},

    {"name":"SCALPING","score":43}

]

engine = StrategyRotation()

report = engine.rotate(strategies)

engine.print(report)