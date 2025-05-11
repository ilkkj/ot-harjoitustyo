import unittest
from repositories.how_to_play_repository import HowToPlayRepository

class TestHowToPlayRepository(unittest.TestCase):
    def setUp(self):
        self.repository = HowToPlayRepository()
        self.test_text = [
            "Use LEFT and RIGHT arrows or (A) and (D) to move.",
            "Press SPACE to shoot a laser.",
            "",
            "Lasers destroy brown boxes; gray boxes are indestructible.",
            "You gain score by destroying brown boxes.",
            "Do not get hit by falling boxes from above.",
            "If hit, the game restarts.",
            "",
            "Press (R) to restart the game.",
            "Press (Q) or ESC to return to menu."
        ]

    def test_get_returns_correct_text(self):
        text = self.repository.get()
        self.assertEqual(text, self.test_text)

    def test_get_displays_error_msg(self):
        repository = HowToPlayRepository("incorrect.txt")
        text = repository.get()
        test_text = ["Unable to load instructions."]
        self.assertEqual(text, test_text)

    def test_get_handles_incorrect_files(self):
        repository = HowToPlayRepository("incorrect.yaml")
        text = repository.get()
        test_text = ["Unable to load instructions."]
        self.assertEqual(text, test_text)

    
