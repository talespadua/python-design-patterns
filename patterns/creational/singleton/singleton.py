from __future__ import annotations

from typing import Dict, List, Any, Optional


class SingletonMeta(type):

    _instance: Optional[SingletonMeta] = None

    def __call__(cls, *args: List[Any], **kwargs: Dict[Any, Any]) -> SingletonMeta:
        if cls._instance is None:
            instance = super().__call__(*args, **kwargs)
            cls._instance = instance
        return cls._instance


class Database(metaclass=SingletonMeta):
    def query(self, query: str) -> None:
        pass
