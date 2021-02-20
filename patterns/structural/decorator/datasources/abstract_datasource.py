from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def write_data(self, data: str) -> None:
        ...

    @abstractmethod
    def read_data(self, data: str) -> None:
        ...
