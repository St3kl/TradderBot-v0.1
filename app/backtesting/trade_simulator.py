class TradeSimulator:
    """
    Simulates open trades using historical candles.
    """

    def update(self, trade, candle):

        direction = trade["direction"]

        high = candle["high"]
        low = candle["low"]

        sl = trade["stop_loss"]
        tp = trade["take_profit"]

        if direction == "SHORT":

            if low <= sl:

                return {

                    "closed": True,

                    "result": "LOSS",

                    "exit_price": sl

                }

            if high >= tp:

                return {

                    "closed": True,

                    "result": "WIN",

                    "exit_price": tp

                }

        else:

            if high >= sl:

                return {

                    "closed": True,

                    "result": "LOSS",

                    "exit_price": sl

                }

            if low <= tp:

                return {

                    "closed": True,

                    "result": "WIN",

                    "exit_price": tp

                }

        return {

            "closed": False

        }