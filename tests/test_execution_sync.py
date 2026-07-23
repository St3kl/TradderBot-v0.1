from app.execution.execution_sync import ExecutionSync

engine = ExecutionSync()

order = {

    "status":"PENDING",

    "filled":1.0,

    "price":65000

}

broker = {

    "status":"FILLED",

    "filled":2.0,

    "price":65010

}

report = engine.sync(

    order,

    broker

)

engine.print(report)

print()

print(report["order"])