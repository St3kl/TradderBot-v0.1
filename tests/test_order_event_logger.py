from app.execution.order_event_logger import OrderEventLogger

logger = OrderEventLogger()

logger.log(

    "TB-000001",

    "CREATED"

)

logger.log(

    "TB-000001",

    "VALIDATED"

)

logger.log(

    "TB-000001",

    "SUBMITTED"

)

logger.log(

    "TB-000001",

    "FILLED",

    {

        "price":65000,

        "volume":0.02

    }

)

logger.log(

    "TB-000001",

    "CLOSED",

    {

        "profit":125

    }

)

logger.print()