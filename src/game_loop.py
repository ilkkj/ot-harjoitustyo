
import pygame
import settings
from level import Level
from game import Game
from clock import Clock
from renderer import Renderer
from event_queue import EventQueue


class GameLoop:

    def run(self):
        display = pygame.display.set_mode(
            (settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption("Game")

        while True:
            level = Level()
            renderer = Renderer(display, level)
            clock = Clock()
            event_queue = EventQueue()
            game_loop = Game(level, renderer, clock, event_queue)

            restart = game_loop.start()
            if not restart:
                break
