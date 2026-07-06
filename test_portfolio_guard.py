# from app.portfolio.portfolio_guard import PortfolioGuard

# guard = PortfolioGuard()

# print()

# print("Can Open Trade")

# print(guard.can_open_trade())

from app.portfolio.portfolio_guard import PortfolioGuard

guard = PortfolioGuard()

print(

    guard.can_open_trade("BTCUSDT")

)