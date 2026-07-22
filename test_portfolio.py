from app.portfolio.portfolio import Portfolio

class Trade:
    pnl = 250

portfolio = Portfolio()

print(portfolio.summary())

portfolio.apply_trade(Trade())

print(portfolio.summary())