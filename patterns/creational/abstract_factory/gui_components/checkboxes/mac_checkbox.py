from .abstract_checkbox import Checkbox


class MacCheckbox(Checkbox):
    def paint(self) -> str:
        return "render the checkbox in Mac style"
