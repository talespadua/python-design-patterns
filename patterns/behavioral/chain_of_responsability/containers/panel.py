from .container import Container
from typing import Optional


class Panel(Container):
    def __init__(self) -> None:
        super().__init__()
        self.modal_help_text: Optional[str] = None

    def show_help(self) -> Optional[str]:
        if self.modal_help_text:
            return self.modal_help_text
        else:
            return super().show_help()
