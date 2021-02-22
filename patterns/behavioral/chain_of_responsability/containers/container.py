from __future__ import annotations
from abc import ABC
from typing import List

from patterns.behavioral.chain_of_responsability.components.component import Component


class Container(Component, ABC):
    def __init__(self) -> None:
        super().__init__()
        self.childrens: List[Component] = []

    def add(self, child: Component) -> None:
        self.childrens.append(child)
        child.container = self
