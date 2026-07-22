from abc import ABC, abstractmethod


class Broker(ABC):
    """
    Generic Broker Interface.

    Every broker must implement the same API.
    """

    @abstractmethod
    def open_trade(self, session, execution):
        pass

    @abstractmethod
    def close_trade(self, trade, exit_price, result):
        pass

    @abstractmethod
    def cancel_trade(self, trade):
        pass

    @abstractmethod
    def account(self):
        pass

    @abstractmethod
    def positions(self):
        pass