import pytest

from patterns.structural.flyweight.forest import Forest
from patterns.structural.flyweight.tree_factory import TreeFactory


class TestForest:
    @pytest.fixture()
    def tree_factory(self) -> TreeFactory:
        return TreeFactory()

    @pytest.fixture()
    def forest(self, tree_factory: TreeFactory) -> Forest:
        return Forest(tree_factory)

    def test_add_tree(self, forest: Forest) -> None:
        forest.plant_tree(1, 1, "pine", "green", "pine_texture")
        forest.plant_tree(1, 1, "pine", "green", "pine_texture")
        forest.plant_tree(1, 1, "pine", "blue", "pine_texture")

        assert len(forest.trees) == 3
