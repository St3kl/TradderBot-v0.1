from app.risk.portfolio import calculate_portfolio_risk

portfolio = [

    {
        "symbol":"BTCUSDT",
        "risk":100
    },

    {
        "symbol":"ETHUSDT",
        "risk":75
    },

    {
        "symbol":"SOLUSDT",
        "risk":50
    }

]

report = calculate_portfolio_risk(portfolio)

print(report)