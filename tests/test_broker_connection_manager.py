from app.execution.brokers.mock_broker import MockBroker
from app.execution.broker_connection_manager import BrokerConnectionManager

broker = MockBroker()

manager = BrokerConnectionManager(broker)

manager.print()

manager.connect()

manager.print()

manager.disconnect()

manager.print()

manager.ensure_connection()

manager.print()