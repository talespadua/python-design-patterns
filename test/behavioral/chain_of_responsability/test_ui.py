import pytest

from patterns.behavioral.chain_of_responsability.components.button import Button
from patterns.behavioral.chain_of_responsability.containers.dialog import Dialog
from patterns.behavioral.chain_of_responsability.containers.panel import Panel


class TestUI:
    @pytest.fixture()
    def ok_button(self) -> Button:
        ok = Button()
        ok.tooltip_text = "This is an OK Button that does....."
        return ok

    @pytest.fixture()
    def cancel_button(self) -> Button:
        cancel = Button()
        return cancel

    @pytest.fixture()
    def ui(self, ok_button: Button, cancel_button: Button) -> Dialog:
        dialog = Dialog()
        dialog.wikipage_url = "http://www.wikipedia......"

        panel = Panel()

        panel.add(ok_button)
        panel.add(cancel_button)
        dialog.add(panel)

        return dialog

    def test_help_functions(
        self, ui: Dialog, ok_button: Button, cancel_button: Button
    ) -> None:
        ok_button_msg = ok_button.show_help()
        assert ok_button_msg == ok_button.tooltip_text

        cancel_button_msg = cancel_button.show_help()
        assert cancel_button_msg == ui.wikipage_url
