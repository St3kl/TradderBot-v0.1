from abc import ABC, abstractmethod


class BaseStrategy(ABC):

    name = "BASE"

    @abstractmethod
    def evaluate(self, session):
        """
        Receives the trading session.

        Returns the updated session.
        """
        pass