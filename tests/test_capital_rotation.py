from app.portfolio.capital_rotation import CapitalRotation

strategies = [

    {"name":"TREND","score":95},

    {"name":"BREAKOUT","score":85},

    {"name":"RANGE","score":70},

    {"name":"SCALPING","score":50}

]

engine = CapitalRotation()

report = engine.allocate(

    strategies,

    capital=100000

)

engine.print(report)