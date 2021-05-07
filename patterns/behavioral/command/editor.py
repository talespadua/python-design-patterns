class Editor:
    def __init__(self) -> None:
        self.text = ""
        self.selection_range = 0, 0

    def get_selection(self) -> str:
        initial_range = self.selection_range[0]
        last_range = self.selection_range[1]
        return self.text[initial_range:last_range]

    def delete_selection(self) -> None:
        initial_range = self.selection_range[0]
        last_range = self.selection_range[1]
        self.text = self.text.replace(self.text[initial_range:last_range], "")

    def replace_selection(self, text: str) -> None:
        initial_range = self.selection_range[0]
        last_range = self.selection_range[1]
        self.text = self.text.replace(self.text[initial_range:last_range], text)
