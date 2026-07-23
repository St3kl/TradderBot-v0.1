from abc import ABC, abstractmethod


class BaseBroker(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass

    @abstractmethod
    def place_order(self, order):
        pass

    @abstractmethod
    def modify_order(self, order):
        pass

    @abstractmethod
    def cancel_order(self, broker_order_id):
        pass

    @abstractmethod
    def get_order(self, broker_order_id):
        pass

    @abstractmethod
    def get_positions(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass