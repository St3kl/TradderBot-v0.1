class LiveMarketStream:

    def __init__(

        self,

        data_manager,

        cache,

        aggregator,

        candle_builder

    ):

        self.data_manager = data_manager
        self.cache = cache
        self.aggregator = aggregator
        self.candle_builder = candle_builder

    def on_tick(

        self,

        symbol,

        price,

        volume=0

    ):

        self.data_manager.update_price(

            symbol,

            price

        )

        self.cache.update(

            symbol,

            price

        )

        self.aggregator.add_tick(

            price,

            volume

        )

        self.candle_builder.update(

            price,

            volume

        )

    def status(self):

        return {

            "symbols": self.data_manager.symbols(),

            "cached": self.cache.size("BTCUSDT"),

            "ticks": self.aggregator.count(),

            "latest_price": self.data_manager.get_price("BTCUSDT")

        }