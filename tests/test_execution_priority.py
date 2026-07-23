from app.portfolio.execution_priority import ExecutionPriority

trades = [

    {

        "symbol":"BTCUSDT",

        "confidence":82,

        "quality":85,

        "expectancy":90,

        "market_health":80

    },

    {

        "symbol":"ETHUSDT",

        "confidence":91,

        "quality":70,

        "expectancy":75,

        "market_health":90

    },

    {

        "symbol":"EURUSD",

        "confidence":74,

        "quality":95,

        "expectancy":85,

        "market_health":88

    }

]

engine = ExecutionPriority()

ranked = engine.rank(trades)

engine.print(ranked)