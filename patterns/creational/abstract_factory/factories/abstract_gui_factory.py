from abc import ABC, abstractmethod
from patterns.creational.abstract_factory.gui_components.buttons import Button
from patterns.creational.abstract_factory.gui_components.checkboxes import Checkbox


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        ...

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        ...
