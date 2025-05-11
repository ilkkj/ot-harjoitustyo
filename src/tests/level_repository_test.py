import unittest
from repositories.level_repository import LevelRepository

class TestLevelRepository(unittest.TestCase):
    def setUp(self):
        self.repository = LevelRepository()

    def test_get_handles_incorrect_files(self):
        repository = LevelRepository("incorrect.txt")
        data = repository.get()
        self.assertEqual(data, None)

    def test_get_returns_a_list(self):
        data = self.repository.get()
        self.assertIsInstance(data, list)
