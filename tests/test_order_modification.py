from app.execution.order_modification import OrderModification

engine = OrderModification()

order = {

    "id": "TB-000001",

    "entry": 65000,

    "stop_loss": 64500,

    "take_profit": 66500,

    "quantity": 0.02,

    "status": "PENDING"

}

engine.modify(

    order,

    stop_loss=65000

)

engine.modify(

    order,

    take_profit=67000

)

engine.print(order)