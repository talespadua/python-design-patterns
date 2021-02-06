from __future__ import annotations

from typing import Optional

from patterns.creational.prototype.shapes.shape import Shape


class Circle(Shape):
    def __init__(self, source: Optional[Circle] = None):
        super().__init__(source)
        if source:
            self.radius: int = source.radius

    def clone(self) -> Circle:
        return Circle(self)
