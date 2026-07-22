class TradeLifecycle:

    def __init__(

        self,

        simulator,

        paper,

        trade_manager,

        portfolio,

        learning,

        equity_curve

    ):

        self.simulator = simulator

        self.paper = paper

        self.trade_manager = trade_manager

        self.portfolio = portfolio

        self.learning = learning

        self.equity_curve = equity_curve

    def process(self, candle):

        for trade in self.trade_manager.get_open().copy():

            result = self.simulator.update(

                trade,

                candle

            )

            if not result["closed"]:

                continue

            closed_trade = self.paper.close_trade(

                trade,

                result["exit_price"],

                result["result"]

            )

            self.trade_manager.close(

                closed_trade

            )

            self.portfolio.apply_trade(

                closed_trade

            )

            self.equity_curve.add(

                self.portfolio.balance

            )

            self.learning.learn(

                closed_trade

            )