from typing import Any


class TreeType:
    def __init__(self, name: str, color: str, texture: str) -> None:
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas: Any, x: int, y: int) -> None:
        pass
