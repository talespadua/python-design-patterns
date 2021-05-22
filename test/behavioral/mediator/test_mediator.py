import pytest

from patterns.behavioral.mediator.auth_dialog import AuthenticationDialog


class TestAuthDialogMediator:
    @pytest.fixture()
    def mediator(self) -> AuthenticationDialog:
        return AuthenticationDialog()

    def test_title_changes_on_login_checkbox(
        self, mediator: AuthenticationDialog
    ) -> None:
        mediator.login_checkbox.check()
        assert mediator.title == "Register"
