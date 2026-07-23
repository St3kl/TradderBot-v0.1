from app.execution.broker_reconciliation import BrokerReconciliation

engine = BrokerReconciliation()

internal = {

    "status":"PENDING",

    "filled":1.0,

    "quantity":2.0

}

broker = {

    "status":"FILLED",

    "filled":2.0,

    "quantity":2.0

}

report = engine.reconcile(

    internal,

    broker

)

engine.print(report)

print()

print(report["updated"])