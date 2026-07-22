from app.risk.portfolio_heat import PortfolioHeat

engine = PortfolioHeat()

positions = [

    {"risk_percent": 1},

    {"risk_percent": 1.5},

    {"risk_percent": 2},

]

print(engine.evaluate(positions))

positions.append({"risk_percent": 2})

print(engine.evaluate(positions))