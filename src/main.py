import sys
import pygame
from ui.game_loop import GameLoop


def launch_game():
    pygame.init()
    game = GameLoop()
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    launch_game()
