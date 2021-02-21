from .tree_type import TreeType
from typing import Any


class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.type = tree_type

    def draw(self, canvas: Any) -> None:
        self.type.draw(canvas, self.x, self.y)
