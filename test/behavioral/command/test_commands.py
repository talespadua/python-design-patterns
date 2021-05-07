import pytest

from patterns.behavioral.command.application import Application
from patterns.behavioral.command.commands.copy_command import CopyCommand
from patterns.behavioral.command.commands.cut_command import CutCommand
from patterns.behavioral.command.commands.paste_command import PasteCommand
from patterns.behavioral.command.editor import Editor


@pytest.fixture
def editor() -> Editor:
    editor = Editor()
    return editor


@pytest.fixture
def application(editor: Editor) -> Application:
    return Application(editor)


def test_copy_command(application: Application, editor: Editor) -> None:
    copy_command = CopyCommand(application, editor)
    editor.text = "Hello World"
    editor.selection_range = 0, 5

    copy_command.execute()
    assert application.clipboard == "Hello"
    assert editor.text == "Hello World"


def test_cut_command(application: Application, editor: Editor) -> None:
    cut_command = CutCommand(application, editor)
    editor.text = "Hello World"
    editor.selection_range = 0, 5

    cut_command.execute()
    assert application.clipboard == "Hello"
    assert editor.text == " World"


def test_paste_command(application: Application, editor: Editor) -> None:
    copy_command = CopyCommand(application, editor)
    paste_command = PasteCommand(application, editor)
    editor.text = "Hello World"
    editor.selection_range = 0, 5

    copy_command.execute()

    editor.selection_range = 0, 1

    paste_command.execute()
    assert editor.text == "Helloello World"
