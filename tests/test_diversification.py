from app.portfolio.diversification import DiversificationEngine

positions = [

    {"symbol":"BTCUSDT","strategy":"TREND"},
    {"symbol":"BTCUSDT","strategy":"TREND"},
    {"symbol":"ETHUSDT","strategy":"BREAKOUT"},
    {"symbol":"EURUSD","strategy":"RANGE"},
    {"symbol":"XAUUSD","strategy":"TREND"}

]

engine = DiversificationEngine()

report = engine.analyze(positions)

engine.print(report)