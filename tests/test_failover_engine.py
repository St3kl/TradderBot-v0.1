from app.execution.failover_engine import FailoverEngine

from app.execution.brokers.mock_broker import MockBroker

primary = MockBroker()

backup = MockBroker()

backup.connect()

engine = FailoverEngine()

engine.configure(

    primary,

    [backup]

)

engine.print()

print()

selected = engine.get_available()

print(selected is backup)