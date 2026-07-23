from datetime import datetime, timedelta

from app.portfolio.trade_expiration import TradeExpiration

engine = TradeExpiration()

now = datetime.utcnow()

trades = [

    {

        "symbol":"BTCUSDT",

        "strategy":"TREND",

        "created_at":now - timedelta(minutes=10),

        "ttl_minutes":30

    },

    {

        "symbol":"ETHUSDT",

        "strategy":"BREAKOUT",

        "created_at":now - timedelta(minutes=45),

        "ttl_minutes":30

    }

]

report = engine.filter(

    trades,

    now

)

engine.print(report)