import unittest
import pygame
from level_logic.level_logic import LevelLogic
from unittest.mock import MagicMock
import settings

class MockBox(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((settings.CELL_SIZE, settings.CELL_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.previous_move_time = 0
        self.should_fall = MagicMock(return_value=True)


class TestLevelLogic(unittest.TestCase):
    def setUp(self):
        self.level = LevelLogic()

    def test_create_default_grid(self):
        test_grid = [[
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]]

        grid = self.level.grid_data
        self.assertEqual(grid, test_grid)

    def test_initial_grid_data(self):
        test_grid = [[
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
            [3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]]

        level = LevelLogic(test_grid)
        grid = level.grid_data
        self.assertEqual(grid, test_grid)

    def test__player_can_move(self):
        self.assertTrue(self.level._player_can_move(settings.CELL_SIZE))

    def test_shoot_laser(self):
        self.level.shoot_laser()
        self.assertEqual(len(self.level.laser_sprites), 1)

    def test__move_boxes(self):
        box1 = MockBox(0,0)
        box2 = MockBox(0, settings.CELL_SIZE)
        self.level.all_box_sprites.add(box1, box2)

        box1.should_fall.return_value = True
        box2.should_fall.return_value = False

        current_time = 1000
        self.level._move_boxes(current_time)

        self.assertEqual(box1.rect.y, settings.CELL_SIZE)
        self.assertEqual(box1.previous_move_time, current_time)
        self.assertEqual(box2.rect.y, settings.CELL_SIZE)

    def test_get_score(self):
        score = self.level.get_score()
        self.assertEqual(score, 0)

