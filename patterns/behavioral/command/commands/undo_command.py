from .command import Command


class UndoCommand(Command):
    def execute(self) -> bool:
        self.application.undo()
        return False
