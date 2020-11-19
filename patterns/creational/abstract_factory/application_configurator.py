from typing import Dict, Any

from patterns.creational.abstract_factory.application import Application
from patterns.creational.abstract_factory.factories.abstract_gui_factory import (
    GUIFactory,
)
from patterns.creational.abstract_factory.factories.mac_gui_factory import MacGUIFactory
from patterns.creational.abstract_factory.factories.win_gui_factory import (
    WindowsGUIFactory,
)


class ApplicationConfigurator:
    def __init__(self, config: Dict[str, Any]):
        operating_system = config.get("os")
        self.gui_factory: GUIFactory
        if operating_system == "windows":
            self.gui_factory = WindowsGUIFactory()
        elif operating_system == "mac":
            self.gui_factory = MacGUIFactory()
        else:
            raise NotImplementedError

        self.app = Application(self.gui_factory)
