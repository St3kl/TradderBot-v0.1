from app.execution.order_cancellation import OrderCancellation

engine = OrderCancellation()

order = {

    "id":"TB-000001",

    "status":"PENDING"

}

engine.cancel(

    order,

    reason="Signal Expired"

)

engine.print(order)