from .abstract_checkbox import Checkbox


class WindowsCheckbox(Checkbox):
    def paint(self) -> str:
        return "render the checkbox in Windows style"
