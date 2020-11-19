from abc import ABC, abstractmethod


class BaseTransport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        ...
