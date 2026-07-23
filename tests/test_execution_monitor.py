from app.execution.execution_monitor import ExecutionMonitor

engine = ExecutionMonitor()

orders = [

    {"id":"1","status":"PENDING"},

    {"id":"2","status":"PARTIAL"},

    {"id":"3","status":"FILLED"},

    {"id":"4","status":"FILLED"},

    {"id":"5","status":"CANCELLED"},

    {"id":"6","status":"REJECTED"}

]

report = engine.inspect(orders)

engine.print(report)