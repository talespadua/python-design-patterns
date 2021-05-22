from __future__ import annotations
from patterns.behavioral.memento.snapshot import Snapshot


class Editor:
    def __init__(self) -> None:
        self.text = ""
        self.selection_width = 0
        self.cur_x = 0
        self.cur_y = 0

    def set_text(self, text: str) -> None:
        self.text = text

    def set_cursor(self, x: int, y: int) -> None:
        self.cur_x = x
        self.cur_y = y

    def set_selection_width(self, width: int) -> None:
        self.selection_width = width

    def create_snapshot(self) -> Snapshot:
        return Snapshot(self, self.text, self.cur_x, self.cur_y, self.selection_width)
