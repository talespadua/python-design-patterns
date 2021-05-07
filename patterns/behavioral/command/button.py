from typing import Callable, Any, Optional

from patterns.behavioral.command.commands.command import Command


class Button:
    def __init__(self, command: Command) -> None:
        self.command = command
        self.wrapper: Optional[Callable[[Any], None]] = None

    def execute_action(self) -> None:
        if self.wrapper:
            self.wrapper(self.command)
        else:
            self.command.execute()

    def register_wrapper(self, wrapper: Callable[[Any], None]) -> None:
        self.wrapper = wrapper
