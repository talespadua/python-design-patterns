from typing import List
from .shapes import Rectangle, Circle, Shape


def main() -> None:
    shapes: List[Shape] = []
    circle = Circle()
    circle.x = 10
    circle.y = 20

    shapes.append(circle)

    another_circle = circle.clone()
    shapes.append(another_circle)

    rect = Rectangle()

    rect.width = 10
    rect.height = 20
    shapes.append(rect)

    cloned_shapes: List[Shape] = []

    for shape in shapes:
        cloned_shapes.append(shape.clone())


if __name__ == "__main__":
    main()
