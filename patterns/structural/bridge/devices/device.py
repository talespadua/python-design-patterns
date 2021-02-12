from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        ...

    @abstractmethod
    def enable(self) -> None:
        ...

    @abstractmethod
    def disable(self) -> None:
        ...

    @abstractmethod
    def get_volume(self) -> int:
        ...

    @abstractmethod
    def set_volume(self, volume_level: int) -> None:
        ...

    @abstractmethod
    def get_channel(self) -> int:
        ...

    @abstractmethod
    def set_channel(self, channel: int) -> None:
        ...
