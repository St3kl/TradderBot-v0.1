from app.portfolio.trade_conflict_resolver import TradeConflictResolver

trades = [

    {

        "symbol":"BTCUSDT",

        "strategy":"TREND",

        "priority":90

    },

    {

        "symbol":"BTCUSDT",

        "strategy":"RANGE",

        "priority":82

    },

    {

        "symbol":"ETHUSDT",

        "strategy":"BREAKOUT",

        "priority":88

    },

]

engine = TradeConflictResolver()

report = engine.resolve(trades)

engine.print(report)