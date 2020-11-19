from patterns.creational.abstract_factory.factories.abstract_gui_factory import (
    GUIFactory,
)
from patterns.creational.abstract_factory.gui_components.buttons import (
    Button,
    WindowsButton,
)
from patterns.creational.abstract_factory.gui_components.checkboxes import (
    Checkbox,
    WindowsCheckbox,
)


class WindowsGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()
