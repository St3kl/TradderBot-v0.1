from datetime import datetime

from app.portfolio.trade_reservation import TradeReservation

engine = TradeReservation()

now = datetime.utcnow()

print(engine.available("BTCUSDT"))

engine.reserve(

    "BTCUSDT",

    minutes=2,

    now=now

)

print(engine.available("BTCUSDT"))

engine.release("BTCUSDT")

print(engine.available("BTCUSDT"))

engine.print()