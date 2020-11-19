from patterns.creational.abstract_factory.factories.abstract_gui_factory import (
    GUIFactory,
)
from patterns.creational.abstract_factory.gui_components.buttons import Button
from patterns.creational.abstract_factory.gui_components.checkboxes import Checkbox


class Application:
    def __init__(self, gui_factory: GUIFactory):
        self._gui_factory = gui_factory
        self._button: Button = self._gui_factory.create_button()
        self._checkbox: Checkbox = self._gui_factory.create_checkbox()

    def paint(self) -> None:
        self._button.paint()
        self._checkbox.paint()
