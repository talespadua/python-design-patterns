import pytest

from patterns.structural.flyweight.tree_factory import TreeFactory


class TestTreeFactory:
    @pytest.fixture()
    def tree_factory(self) -> TreeFactory:
        return TreeFactory()

    def test_factory(self, tree_factory: TreeFactory) -> None:
        green_pine = tree_factory.get_tree_type("pine", "green", "pine_texture")
        green_pine_2 = tree_factory.get_tree_type("pine", "green", "pine_texture")
        tree_factory.get_tree_type("pine", "blue", "pine_texture")

        assert id(green_pine) == id(green_pine_2)
        assert len(tree_factory.tree_types) == 2
