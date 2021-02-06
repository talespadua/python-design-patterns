import pytest
from patterns.creational.prototype.shapes import Circle, Rectangle


class TestRectangle:
    @pytest.fixture()
    def rectangle(self) -> Rectangle:
        rect = Rectangle()
        rect.width = 20
        rect.height = 10
        rect.x = 1
        rect.y = 2
        rect.color = "red"

        return rect

    def test_clone_rectangle(self, rectangle: Rectangle) -> None:
        cloned_rectangle = rectangle.clone()
        assert cloned_rectangle.width == rectangle.width
        assert cloned_rectangle.height == rectangle.height
        assert cloned_rectangle.x == rectangle.x
        assert cloned_rectangle.y == rectangle.y
        assert cloned_rectangle.color == rectangle.color


class TestCircle:
    @pytest.fixture()
    def circle(self) -> Circle:
        circle = Circle()
        circle.radius = 10
        circle.x = 1
        circle.y = 2
        circle.color = "yellow"

        return circle

    def test_clone_circle(self, circle: Circle) -> None:
        cloned_circle = circle.clone()

        assert cloned_circle.radius == circle.radius
        assert cloned_circle.x == circle.x
        assert cloned_circle.y == circle.y
        assert cloned_circle.color == circle.color
