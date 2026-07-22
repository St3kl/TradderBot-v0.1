class PortfolioListener:

    def __init__(self, portfolio):

        self.portfolio = portfolio

    def handle(self, trade):

        print("Portfolio Listener")

        self.portfolio.apply_trade(trade)