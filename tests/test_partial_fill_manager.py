from app.execution.partial_fill_manager import PartialFillManager

engine = PartialFillManager()

order = {

    "quantity":2.0,

    "filled":0.0,

    "status":"SUBMITTED"

}

engine.update(order,0.8)

engine.print(order)

engine.update(order,0.7)

engine.print(order)

engine.update(order,0.5)

engine.print(order)