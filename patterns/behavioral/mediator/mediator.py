from abc import ABC, abstractmethod

from patterns.behavioral.mediator.components.components import Component


class AbstractMediator(ABC):
    @abstractmethod
    def notify(self, sender: Component, event: str):
        ...
