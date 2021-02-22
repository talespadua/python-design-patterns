from .container import Container
from typing import Optional


class Dialog(Container):
    def __init__(self) -> None:
        super().__init__()
        self.wikipage_url: Optional[str] = None

    def show_help(self) -> Optional[str]:
        if self.wikipage_url:
            return self.wikipage_url
        else:
            return super().show_help()
