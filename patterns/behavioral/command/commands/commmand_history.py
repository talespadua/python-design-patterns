from .command import Command
from typing import List


class CommandHistory:
    def __init__(self) -> None:
        self.history: List[Command] = []

    def push(self, command: Command) -> None:
        self.history.append(command)

    def pop(self) -> Command:
        return self.history.pop()
