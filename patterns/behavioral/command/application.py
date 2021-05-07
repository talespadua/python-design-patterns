from __future__ import annotations

from typing import List, Dict, Callable, Tuple, Any

from patterns.behavioral.command.button import Button
from patterns.behavioral.command.commands.command import Command
from patterns.behavioral.command.commands.commmand_history import CommandHistory
from patterns.behavioral.command.commands.copy_command import CopyCommand
from patterns.behavioral.command.commands.cut_command import CutCommand
from patterns.behavioral.command.commands.paste_command import PasteCommand
from patterns.behavioral.command.editor import Editor


class Application:
    def __init__(self, editor: Editor) -> None:
        self.clipboard = ""
        self.editors: List[Editor] = [editor]
        self.active_editor: Editor = editor
        self.history = CommandHistory()
        self.shortcuts: Dict[str, Tuple[Callable[[Any], None], Command]]

    def create_ui(self) -> None:
        copy_command = CopyCommand(self, self.active_editor)
        cut_command = CutCommand(self, self.active_editor)
        paste_command = PasteCommand(self, self.active_editor)

        copy_button = Button(copy_command)
        copy_button.register_wrapper(self.execute_command)

        cut_button = Button(cut_command)
        cut_button.register_wrapper(self.execute_command)

        paste_button = Button(paste_command)
        paste_button.register_wrapper(self.execute_command)

        self.shortcuts["Ctrl+C"] = (self.execute_command, copy_command)
        self.shortcuts["Ctrl+X"] = (self.execute_command, cut_command)
        self.shortcuts["Ctrl+V"] = (self.execute_command, paste_command)

    def execute_command(self, command: Command) -> None:
        if command.execute():
            self.history.push(command)

    def undo(self) -> None:
        command = self.history.pop()
        if command is not None:
            command.undo()
