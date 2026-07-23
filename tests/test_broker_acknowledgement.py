from app.execution.broker_acknowledgement import BrokerAcknowledgement

engine = BrokerAcknowledgement()

order = {

    "id": "TB-000001"

}

engine.acknowledge(

    order,

    broker_order_id="BN-987654",

    broker_name="Binance"

)

engine.print(order)