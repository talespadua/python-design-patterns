from typing import Dict, Any

import pytest

from patterns.creational.abstract_factory.application_configurator import (
    ApplicationConfigurator,
)
from patterns.creational.abstract_factory.factories.abstract_gui_factory import (
    GUIFactory,
)
from patterns.creational.abstract_factory.factories.mac_gui_factory import MacGUIFactory
from patterns.creational.abstract_factory.factories.win_gui_factory import (
    WindowsGUIFactory,
)


class TestApplicationConfigurator:
    class TestZGivenValidConfig:
        @pytest.fixture()
        def application_configurator(
            self, config: Dict[str, Any]
        ) -> ApplicationConfigurator:
            return ApplicationConfigurator(config)

        @pytest.mark.parametrize(
            "config, expected_factory",
            [
                ({"os": "windows"}, WindowsGUIFactory),
                ({"os": "mac"}, MacGUIFactory),
            ],
        )
        def test_should_return_correct_factory(
            self,
            application_configurator: ApplicationConfigurator,
            config: Dict[str, Any],
            expected_factory: GUIFactory,
        ) -> None:
            assert isinstance(
                application_configurator.gui_factory, expected_factory  # type: ignore
            )
