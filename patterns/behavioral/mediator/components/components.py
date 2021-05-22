from __future__ import annotations
import patterns.behavioral.mediator.mediator as mediator


class Component:
    def __init__(self, dialog: mediator.AbstractMediator):
        self.dialog = dialog

    def click(self) -> None:
        self.dialog.notify(self, "click")

    def keypress(self) -> None:
        self.dialog.notify(self, "keypress")


class Button(Component):
    pass


class Textbox(Component):
    pass


class Checkbox(Component):
    def __init__(self, dialog: mediator.AbstractMediator) -> None:
        super().__init__(dialog)
        self.checked = False

    def check(self) -> None:
        self.dialog.notify(self, "check")
        self.checked = False if self.checked else True
