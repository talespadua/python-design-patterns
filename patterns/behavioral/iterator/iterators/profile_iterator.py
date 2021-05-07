from abc import ABC, abstractmethod
from typing import Optional

from patterns.behavioral.iterator.profile import Profile


class ProfileIterator(ABC):
    @abstractmethod
    def get_next(self) -> Optional[Profile]:
        ...

    @abstractmethod
    def has_more(self) -> bool:
        ...
