from app.analytics.strategy_score import StrategyScore

engine = StrategyScore()

report = engine.calculate(

    winrate=76,

    expectancy=85,

    recovery=90,

    quality=88,

    stability=84

)

engine.print(report)