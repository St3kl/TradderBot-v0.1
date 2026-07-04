from app.risk.exposure import analyze_exposure

portfolio = [

    {
        "symbol":"BTC",
        "direction":"LONG",
        "risk":100
    },

    {
        "symbol":"ETH",
        "direction":"LONG",
        "risk":75
    },

    {
        "symbol":"SOL",
        "direction":"SHORT",
        "risk":50
    }

]

print(analyze_exposure(portfolio))