import pytest

from patterns.behavioral.memento.command import Command
from patterns.behavioral.memento.editor import Editor


class TestCaretakerCommand:
    @pytest.fixture()
    def editor(self) -> Editor:
        return Editor()

    def test_command_create_and_restores_snapshot(self, editor: Editor) -> None:
        command = Command(editor)

        editor.set_text("Sherolero")
        assert editor.text == "Sherolero"

        command.make_backup()

        editor.set_text("LeroShero")
        assert editor.text == "LeroShero"

        command.undo()
        assert editor.text == "Sherolero"
