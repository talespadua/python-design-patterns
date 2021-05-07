from .command import Command


class CutCommand(Command):
    def execute(self) -> bool:
        self.save_backup()
        self.application.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True
