from typing import Optional
from abc import ABC
from .component_with_contextual_help import ComponentWithContextualHelp
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from patterns.behavioral.chain_of_responsability.containers.container import (
        Container,
    )


class Component(ComponentWithContextualHelp, ABC):
    def __init__(self) -> None:
        self.container: Optional[Container] = None
        self.tooltip_text: Optional[str] = None

    def show_help(self) -> Optional[str]:
        if self.tooltip_text:
            return self.tooltip_text
        else:
            if self.container:
                return self.container.show_help()
        return None
