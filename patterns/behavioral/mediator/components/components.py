from __future__ import annotations
import patterns.behavioral.mediator.mediator as mediator


class Component:
    def __init__(self, dialog: mediator.AbstractMediator):
        self.dialog = dialog

    def click(self):
        self.dialog.notify(self, "click")

    def keypress(self):
        self.dialog.notify(self, "keypress")


class Button(Component):
    pass


class Textbox(Component):
    pass


class Checkbox(Component):
    def __init__(self, dialog: mediator.AbstractMediator):
        super().__init__(dialog)
        self.checked = False

    def check(self):
        self.dialog.notify(self, "check")
        self.checked = False if self.checked else True