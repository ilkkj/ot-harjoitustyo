import pygame

CELL_SIZE = 50
ROWS, COLS = 12, 17
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
FPS = 60

MENU_BACKGROUND_COLOR = (30, 30, 30)
MENU_TITLE_COLOR = (255, 255, 255)
MENU_TEXT_COLOR = (155, 155, 155)
MENU_TEXT_HIGHLIGHT_COLOR = (255, 0, 0)

pygame.font.init()
MENU_FONT = pygame.font.SysFont(None, 60)
TITLE_FONT = pygame.font.SysFont(None, 80)
CONTENT_FONT = pygame.font.SysFont(None, 32)
HIGH_SCORE_FONT = pygame.font.SysFont(None, 45)

BACKGROUND_COLOR = (0, 0, 0)
PLAYER_COLOR = (255, 0, 0)
BOX_COLOR = (150, 80, 0)
SOLID_BOX_COLOR = (150, 150, 150)
WALL_COLOR = (80, 80, 80)
LASER_COLOR = (0, 255, 0)

GAME_RESTART_EVENT = pygame.USEREVENT + 1
GAME_WON_EVENT = pygame.USEREVENT + 2
