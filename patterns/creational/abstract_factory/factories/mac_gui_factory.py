from patterns.creational.abstract_factory.factories.abstract_gui_factory import (
    GUIFactory,
)
from patterns.creational.abstract_factory.gui_components.buttons import (
    Button,
    MacButton,
)
from patterns.creational.abstract_factory.gui_components.checkboxes import (
    Checkbox,
    MacCheckbox,
)


class MacGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()
