from typing import Dict
from .tree_type import TreeType


class TreeFactory:
    tree_types: Dict[str, TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        tree_type = cls.tree_types.get(f"{name}{color}{texture}")
        if not tree_type:
            tree_type = TreeType(name, color, texture)
            cls.tree_types[f"{name}{color}{texture}"] = tree_type
        return tree_type
