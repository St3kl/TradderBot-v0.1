from app.execution.brokers.mock_broker import MockBroker

from app.execution.broker_heartbeat import BrokerHeartbeat

broker = MockBroker()

heartbeat = BrokerHeartbeat(broker)

report = heartbeat.check()

heartbeat.print(report)

broker.connect()

report = heartbeat.check()

heartbeat.print(report)