from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Base class for every AI provider.

    Every provider must implement generate().
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Sends a prompt to the model
        and returns the response.
        """
        pass