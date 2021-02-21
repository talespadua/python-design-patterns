from typing import List, Any
from .tree import Tree
from .tree_factory import TreeFactory


class Forest:
    def __init__(self, tree_factory: TreeFactory) -> None:
        self.trees: List[Tree] = []
        self.tree_factory = tree_factory

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        tree_type = self.tree_factory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas: Any) -> None:
        for tree in self.trees:
            tree.draw(canvas)
