import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_size):
        super().__init__()
        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * cell_size, y * cell_size)
        self.x = x
        self.y = y
        self.cell_size = cell_size
    
    def move(self, dx, grid):
        new_x = self.x + dx
        if 0 <= new_x < len(grid[0]) and grid[self.y][new_x] == 0:
            grid[self.y][self.x] = 0
            self.x = new_x
            grid[self.y][self.x] = 2
            self.rect.x = self.x * self.cell_size

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_size):
        super().__init__()
        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill((80, 80, 80))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x * cell_size, y * cell_size)
