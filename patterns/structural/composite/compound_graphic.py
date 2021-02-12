from typing import List

from .graphic import Graphic


class CompoundGraphic(Graphic):
    def __init__(self) -> None:
        self.childrens: List[Graphic] = []

    def add(self, child: Graphic) -> None:
        self.childrens.append(child)

    def remove(self, child: Graphic) -> None:
        self.childrens.remove(child)

    def move(self, x: int, y: int) -> None:
        for child in self.childrens:
            child.move(x, y)

    def draw(self) -> None:
        for child in self.childrens:
            child.draw()
