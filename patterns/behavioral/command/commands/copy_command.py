from .command import Command


class CopyCommand(Command):
    def execute(self) -> bool:
        self.application.clipboard = self.editor.get_selection()
        return False
