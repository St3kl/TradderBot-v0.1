from app.execution.brokers.mock_broker import MockBroker
from app.execution.brokers.binance_broker import BinanceBroker
from app.execution.brokers.mt5_broker import MT5Broker
from app.execution.brokers.oanda_broker import OandaBroker


class BrokerFactory:

    @staticmethod
    def create(name):

        brokers = {

            "mock": MockBroker,

            "binance": BinanceBroker,

            "mt5": MT5Broker,

            "oanda": OandaBroker

        }

        broker = brokers.get(name.lower())

        if broker is None:

            raise ValueError(

                f"Unsupported broker: {name}"

            )

        return broker()