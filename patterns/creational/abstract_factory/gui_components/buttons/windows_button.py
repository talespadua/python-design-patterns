from .abstract_button import Button


class WindowsButton(Button):
    def paint(self) -> str:
        return "render the button windows style"
