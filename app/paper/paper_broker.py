from copy import deepcopy


class PaperBroker:
    """
    Simulates order execution without using a real exchange.
    """

    def open_trade(self, session, execution):

        if session.decision["action"] != "BUY":
            return None

        trade = deepcopy(session.trade_plan)

        trade.direction = "LONG"

        trade.status = "OPEN"

        trade.entry_time = session.replay.candle["time"]

        trade.exit_time = None

        trade.exit_price = None

        trade.result = None

        trade.pnl = 0.0

        return trade

    # -------------------------------------------------

    def close_trade(
        self,
        trade,
        exit_price,
        result,
    ):

        trade.exit_price = exit_price

        trade.status = "CLOSED"

        trade.result = result

        trade.exit_time = None

        if trade.direction == "LONG":

            trade.pnl = (
                exit_price
                - trade.entry
            ) * trade.position_size

        else:

            trade.pnl = (
                trade.entry
                - exit_price
            ) * trade.position_size

        return trade