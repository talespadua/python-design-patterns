from __future__ import annotations

from abc import abstractmethod

import patterns.behavioral.command.application as app
from patterns.behavioral.command.editor import Editor


class Command:
    def __init__(
        self,
        application: app.Application,
        editor: Editor,
    ) -> None:
        self.application = application
        self.editor = editor
        self.backup = ""

    def save_backup(self) -> None:
        self.backup = self.editor.text

    def undo(self) -> None:
        self.editor.text = self.backup

    @abstractmethod
    def execute(self) -> bool:
        ...
