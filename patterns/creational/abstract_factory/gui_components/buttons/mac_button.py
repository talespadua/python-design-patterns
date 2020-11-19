from .abstract_button import Button


class MacButton(Button):
    def paint(self) -> str:
        return "render the button Mac style"
