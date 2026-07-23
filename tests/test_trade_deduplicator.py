from app.portfolio.trade_deduplicator import TradeDeduplicator

trades = [

    {

        "symbol":"BTCUSDT",

        "strategy":"TREND",

        "direction":"LONG"

    },

    {

        "symbol":"BTCUSDT",

        "strategy":"TREND",

        "direction":"LONG"

    },

    {

        "symbol":"ETHUSDT",

        "strategy":"BREAKOUT",

        "direction":"LONG"

    },

    {

        "symbol":"BTCUSDT",

        "strategy":"TREND",

        "direction":"SHORT"

    }

]

engine = TradeDeduplicator()

report = engine.deduplicate(trades)

engine.print(report)