from __future__ import annotations

from typing import Optional

from patterns.creational.prototype.shapes.shape import Shape


class Rectangle(Shape):
    def __init__(self, source: Optional[Rectangle] = None) -> None:
        super().__init__(source)
        if source:
            self.width: int = source.width
            self.height: int = source.height

    def clone(self) -> Rectangle:
        return Rectangle(self)
