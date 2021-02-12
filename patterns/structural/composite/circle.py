from .dot import Dot


class Circle(Dot):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self) -> None:
        pass  # draw a circle
