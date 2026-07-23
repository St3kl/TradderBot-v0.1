from app.portfolio.correlated_exposure import CorrelatedExposure

positions = [

    {"symbol":"BTCUSDT"},

    {"symbol":"ETHUSDT"},

    {"symbol":"EURUSD"}

]

correlations = {

    ("BTCUSDT","ETHUSDT"):0.91,

    ("BTCUSDT","EURUSD"):0.20,

    ("ETHUSDT","EURUSD"):0.18

}

engine = CorrelatedExposure()

report = engine.evaluate(

    positions,

    correlations

)

engine.print(report)