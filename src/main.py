import sys
from game import Game


def launch_game():
    game = Game()
    game.run()
    sys.exit()


if __name__ == '__main__':
    launch_game()
