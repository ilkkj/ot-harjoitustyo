import unittest
from sprites import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        player_start_x = 0
        player_start_y = 0
        self.player = Player(player_start_x, player_start_y)

    def test_calculate_new_pos(self):
        new_pos = self.player.calculate_new_pos(1)
        self.assertEqual(new_pos, 1)
