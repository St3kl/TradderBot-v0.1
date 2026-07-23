from app.execution.broker_health_monitor import BrokerHealthMonitor

engine = BrokerHealthMonitor()

report = engine.evaluate(

    connected=True,

    latency_ms=120,

    slippage=8,

    retries=1

)

engine.print(report)

print()

report = engine.evaluate(

    connected=False,

    latency_ms=450,

    slippage=35,

    retries=3

)

engine.print(report)