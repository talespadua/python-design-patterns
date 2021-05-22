from typing import Optional

from .editor import Editor
from .snapshot import Snapshot


class Command:
    def __init__(self, editor: Editor) -> None:
        self.backup: Optional[Snapshot] = None
        self.editor = editor

    def make_backup(self) -> None:
        self.backup = self.editor.create_snapshot()

    def undo(self) -> None:
        if self.backup:
            self.backup.restore()
