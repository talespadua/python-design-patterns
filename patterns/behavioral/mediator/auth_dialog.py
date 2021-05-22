from .mediator import AbstractMediator
from .components.components import Checkbox, Textbox, Button, Component


class AuthenticationDialog(AbstractMediator):
    def __init__(self):
        self.title = "Log In"
        self.login_checkbox = Checkbox(self)
        self.login_username = Textbox(self)
        self.login_password = Textbox(self)
        self.registration_username = Textbox(self)
        self.registration_password = Textbox(self)
        self.ok_button = Button(self)
        self.cancel_button = Button(self)

    def notify(self, sender: Component, event: str) -> None:
        if sender is self.login_checkbox and event == "check":
            if self.login_checkbox.checked:
                self.title = "Log In"
            else:
                self.title = "Register"

        if sender is self.ok_button and event == "click":
            if self.login_checkbox.checked:
                # try to find user with credentials
                pass
            else:
                # register user with register data
                pass
