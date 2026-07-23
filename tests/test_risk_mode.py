from app.portfolio.risk_mode import RiskMode

engine = RiskMode()

for score in [95, 75, 60, 35]:

    report = engine.evaluate({

        "score": score

    })

    engine.print(report)