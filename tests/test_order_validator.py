from app.execution.order_validator import OrderValidator

engine = OrderValidator()

order = {

    "symbol":"BTCUSDT",

    "direction":"BUY",

    "entry":65000,

    "stop_loss":64500,

    "take_profit":66500,

    "lot_size":0.02,

    "risk_percent":1

}

report = engine.validate(order)

engine.print(report)

print()

bad_order = {}

report = engine.validate(bad_order)

engine.print(report)