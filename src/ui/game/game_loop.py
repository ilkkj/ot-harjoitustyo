
import pygame
import settings
from level_logic.level_logic import LevelLogic
from ui.game.game import Game
from infra.clock import Clock
from ui.game.game_renderer import GameRenderer
from infra.event_queue import EventQueue
from repositories.level_repository import LevelRepository
from ui.menu.main_menu import MainMenu
from ui.menu.how_to_play_menu import HowToPlayMenu
from ui.menu.high_scores_menu import HighScoresMenu
from ui.menu.game_cleared_menu import GameClearedMenu


class GameLoop:
    """Manages the overall game execution flow."""

    def __init__(self):
        self.display = pygame.display.set_mode(
            (settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption("Game")
        self.clock = Clock()
        self.event_queue = EventQueue()

    def run(self):
        """Starts the main application loop."""
        menu = MainMenu(self.display, self.event_queue)
        while True:
            choice = menu.run()

            if choice == "Start":
                self._run_game()
            elif choice == "High scores":
                self._open_high_scores()
            elif choice == "How to play":
                self._open_how_to_play()
            elif choice == "Quit":
                break

    def _run_game(self):
        """Starts the gameplay loop."""
        level_loader = LevelRepository()
        level_data = level_loader.get()

        while True:
            level = LevelLogic(level_data)
            renderer = GameRenderer(self.display, level)
            game_loop = Game(level, renderer, self.clock, self.event_queue)

            restart = game_loop.start()
            if game_loop.is_game_cleared():
                score = game_loop.get_score()
                self._handle_game_cleared(score)
            if not restart:
                break

    def _open_high_scores(self):
        highscores_page = HighScoresMenu(self.display, self.event_queue)
        highscores_page.run()

    def _open_how_to_play(self):
        how_to_play_page = HowToPlayMenu(self.display, self.event_queue)
        how_to_play_page.run()

    def _handle_game_cleared(self, score):
        game_cleared_page = GameClearedMenu(
            self.display, self.event_queue, score)
        game_cleared_page.run()
