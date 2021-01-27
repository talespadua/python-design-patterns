from abc import ABC, abstractmethod


class AbstractBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        ...

    @abstractmethod
    def set_seats(self, seats: int) -> None:
        ...

    @abstractmethod
    def set_engine(self, engine: str) -> None:
        ...

    @abstractmethod
    def set_trip_computer(self) -> None:
        ...

    @abstractmethod
    def set_gps(self) -> None:
        ...
