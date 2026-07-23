import time

from app.execution.latency_monitor import LatencyMonitor

engine = LatencyMonitor()


def simulated_order():

    time.sleep(0.1)

    return "Order Submitted"


report = engine.measure(simulated_order)

engine.print(report)