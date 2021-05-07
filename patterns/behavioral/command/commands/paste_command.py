from .command import Command


class PasteCommand(Command):
    def execute(self) -> bool:
        self.save_backup()
        self.editor.replace_selection(self.application.clipboard)
        return True
