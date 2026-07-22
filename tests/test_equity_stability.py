from app.analytics.equity_stability import EquityStability

equity = [

    10000,
    10100,
    10200,
    10350,
    10450,
    10600

]

engine = EquityStability()

report = engine.analyze(equity)

engine.print(report)