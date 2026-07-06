class VectorEngine:

    def build(self, context):

        market = context["market"]
        technical = context["technical"]
        trade = context["trade"]

        return {
            "rsi": market["rsi"],
            "adx": market["adx"],
            "atr": market["atr"],
            "entry": trade["entry"],
            "stop_loss": trade["stop_loss"],
            "take_profit": trade["take_profit"]
        }

    def from_trade(self, trade):

        return {
            "entry": trade["entry"],
            "stop_loss": trade["stop_loss"],
            "take_profit": trade["take_profit"]
        }