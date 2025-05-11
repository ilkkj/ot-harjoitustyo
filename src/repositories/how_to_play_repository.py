import os


class HowToPlayRepository:
    def __init__(self, filename: str = "instructions.txt"):
        base_dir = os.path.dirname(__file__)
        self.filepath = os.path.join(base_dir, "..", "data", filename)

    def get(self):
        error_msg = "Unable to load instructions."
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return [error_msg]
