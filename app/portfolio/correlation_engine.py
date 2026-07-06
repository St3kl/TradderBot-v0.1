class CorrelationEngine:

    """
    Simple correlation groups.

    Later this will be replaced with
    live statistical correlation.
    """

    GROUPS = {

        "CRYPTO": [
            "BTCUSDT",
            "ETHUSDT",
            "SOLUSDT",
            "BNBUSDT"
        ],

        "NASDAQ": [
            "NAS100",
            "US100",
            "QQQ"
        ],

        "GOLD": [
            "XAUUSD"
        ],

        "FOREX_USD": [
            "EURUSD",
            "GBPUSD",
            "AUDUSD"
        ]

    }

    def group(self, symbol):

        symbol = symbol.upper()

        for group, assets in self.GROUPS.items():

            if symbol in assets:

                return group

        return "UNKNOWN"