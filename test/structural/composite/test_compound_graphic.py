from typing import List

import pytest

from patterns.structural.composite.circle import Circle
from patterns.structural.composite.compound_graphic import CompoundGraphic
from patterns.structural.composite.dot import Dot
from patterns.structural.composite.graphic import Graphic


class TestCompoundGraphic:
    @pytest.fixture()
    def leafs(self) -> List[Graphic]:
        return [
            Dot(1, 2),
            Circle(3, 5, 10),
            Dot(9, 9),
        ]

    @pytest.fixture()
    def nested_graphics(self, leafs: List[Graphic]) -> CompoundGraphic:
        inner_graphics = CompoundGraphic()
        inner_graphics.add(leafs[0])
        inner_graphics.add(leafs[1])

        outer_graphics = CompoundGraphic()
        outer_graphics.add(inner_graphics)
        outer_graphics.add(leafs[2])

        return outer_graphics

    def test_all_graphics_are_moved(
        self, nested_graphics: CompoundGraphic, leafs: List[Graphic]
    ) -> None:
        nested_graphics.move(100, 100)

        for leaf in leafs:
            assert leaf.x == 100
            assert leaf.y == 100
