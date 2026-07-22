from abc import ABC, abstractmethod


class BaseBroker(ABC):
    """
    Base interface for every broker.
    """

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_price(self, symbol):
        pass

    @abstractmethod
    def place_order(

        self,

        symbol,

        side,

        quantity,

        stop_loss,

        take_profit

    ):
        pass

    @abstractmethod
    def close_position(self, position_id):
        pass