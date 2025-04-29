
import pygame
import settings
from level.level import Level
from ui.game import Game
from clock import Clock
from ui.renderer import Renderer
from event_queue import EventQueue
from level.level_data import LevelData


class GameLoop:
    """Manages the overall game execution flow."""

    def run(self):
        """Starts the main application loop."""
        display = pygame.display.set_mode(
            (settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption("Game")

        while True:
            level_data = LevelData().get()
            level = Level(level_data)
            renderer = Renderer(display, level)
            clock = Clock()
            event_queue = EventQueue()
            game_loop = Game(level, renderer, clock, event_queue)

            restart = game_loop.start()
            if not restart:
                break
