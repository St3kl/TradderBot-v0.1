from app.execution.order_status_manager import OrderStatusManager

engine = OrderStatusManager()

order = {

    "id": "TB-000001"

}

engine.update(

    order,

    "CREATED"

)

engine.print(order)

engine.update(

    order,

    "SUBMITTED"

)

engine.print(order)

engine.update(

    order,

    "FILLED"

)

engine.print(order)

engine.update(

    order,

    "CLOSED"

)

engine.print(order)