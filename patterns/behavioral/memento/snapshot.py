from __future__ import annotations
import patterns.behavioral.memento.editor as ed


class Snapshot:
    def __init__(
        self, editor: ed.Editor, text: str, cur_x: int, cur_y: int, selection_width: int
    ):
        self.editor = editor
        self.text = text
        self.cur_x = cur_x
        self.cur_y = cur_y
        self.selection_width = selection_width

    def restore(self) -> None:
        self.editor.set_text(self.text)
        self.editor.set_cursor(self.cur_x, self.cur_y)
        self.editor.set_selection_width(self.selection_width)
