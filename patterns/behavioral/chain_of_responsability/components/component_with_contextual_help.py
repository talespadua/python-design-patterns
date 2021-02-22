from abc import ABC, abstractmethod
from typing import Optional


class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def show_help(self) -> Optional[str]:
        ...
