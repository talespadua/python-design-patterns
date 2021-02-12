from .graphic import Graphic


class Dot(Graphic):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def draw(self) -> None:
        pass  # draw a dot
