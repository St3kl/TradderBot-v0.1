from app.portfolio.diversification import DiversificationEngine
from app.portfolio.concentration_risk import ConcentrationRisk

positions = [

    {"symbol":"BTCUSDT","strategy":"TREND"},
    {"symbol":"BTCUSDT","strategy":"BREAKOUT"},
    {"symbol":"BTCUSDT","strategy":"TREND"},
    {"symbol":"BTCUSDT","strategy":"TREND"},
    {"symbol":"ETHUSDT","strategy":"RANGE"}

]

div = DiversificationEngine()

portfolio = div.analyze(positions)

engine = ConcentrationRisk()

report = engine.evaluate(

    portfolio,

    limit=40

)

engine.print(report)