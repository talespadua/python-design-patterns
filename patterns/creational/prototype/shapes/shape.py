from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Shape(ABC):
    def __init__(self, source: Optional[Shape] = None) -> None:
        if source:
            self.x: int = source.x
            self.y: int = source.y
            self.color: str = source.color

    @abstractmethod
    def clone(self) -> Shape:
        ...
