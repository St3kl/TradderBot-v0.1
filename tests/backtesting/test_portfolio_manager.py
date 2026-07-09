from pprint import pprint

from app.backtesting.portfolio_manager import PortfolioManager


portfolio = PortfolioManager(initial_balance=10000)

portfolio.apply_trade({

    "pnl": 250

})

portfolio.apply_trade({

    "pnl": -100

})

portfolio.apply_trade({

    "pnl": 500

})

pprint(portfolio.summary())