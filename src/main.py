import pygame
from level import Level
from sprites import Player, Box

pygame.init()

CELL_SIZE = 50
ROWS, COLS = 10, 15
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
background_color = (0, 0, 0)

#this gets refactored later

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

level = Level(ROWS, COLS, CELL_SIZE)
grid = level.generate_grid()

all_sprites = pygame.sprite.Group()
box_sprites = pygame.sprite.Group()

player_x, player_y = COLS//2, ROWS-1
player = Player(player_x, player_y, CELL_SIZE)
all_sprites.add(player)


for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == 1:
            box = Box(col, row, CELL_SIZE)
            all_sprites.add(box)
            box_sprites.add(box)

running = True
while running:
    screen.fill(background_color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(-1, grid)
            elif event.key == pygame.K_RIGHT:
                player.move(1, grid)
    
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

