from abc import ABC, abstractmethod


class Graphic(ABC):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @abstractmethod
    def move(self, x: int, y: int) -> None:
        ...

    @abstractmethod
    def draw(self) -> None:
        ...
