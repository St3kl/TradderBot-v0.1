from app.analytics.strategy_health import StrategyHealth

engine = StrategyHealth()

strategy = {

    "score": 85,

    "expectancy": 120,

    "recovery_factor": 5

}

report = engine.evaluate(strategy)

engine.print(report)
