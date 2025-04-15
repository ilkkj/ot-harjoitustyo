import pygame
import settings


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.cell_size = settings.CELL_SIZE

        sprite_width = 3 * self.cell_size
        sprite_height = 2 * self.cell_size
        self.image = pygame.Surface(
            (sprite_width, sprite_height), pygame.SRCALPHA)
        color = settings.PLAYER_COLOR
        pygame.draw.rect(self.image, color, (0, self.cell_size,
                         self.cell_size, self.cell_size))
        pygame.draw.rect(self.image, color, (self.cell_size,
                         self.cell_size, self.cell_size, self.cell_size))
        pygame.draw.rect(self.image, color, (2 * self.cell_size,
                         self.cell_size, self.cell_size, self.cell_size))
        pygame.draw.rect(self.image, color, (self.cell_size,
                         0, self.cell_size, self.cell_size))

        self.rect = self.image.get_rect()
        self.rect.topleft = (
            settings.COLS//2 * self.cell_size - self.cell_size,
            (settings.ROWS-2) * self.cell_size - self.cell_size
        )


class Box(pygame.sprite.Sprite):

    def __init__(self, x, y, level_delay=5000):
        super().__init__()
        self.cell_size = settings.CELL_SIZE
        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(settings.BOX_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.level_delay = level_delay
        self.initial_spawn_time = None
        self.previous_move_time = 0

    def should_fall(self, current_time):
        if not self.initial_spawn_time:
            self.initial_spawn_time = current_time
        if current_time - self.initial_spawn_time < self.level_delay:
            return False

        return current_time - self.previous_move_time >= 100


class SolidBox(pygame.sprite.Sprite):

    def __init__(self, x, y, level_delay=5000):
        super().__init__()
        self.cell_size = settings.CELL_SIZE
        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(settings.SOLID_BOX_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.level_delay = level_delay
        self.initial_spawn_time = None
        self.previous_move_time = 0

    def should_fall(self, current_time):
        if not self.initial_spawn_time:
            self.initial_spawn_time = current_time
        if current_time - self.initial_spawn_time < self.level_delay:
            return False

        return current_time - self.previous_move_time >= 100


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.cell_size = settings.CELL_SIZE
        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(settings.WALL_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Laser(pygame.sprite.Sprite):
    def __init__(self, xy):
        super().__init__()
        laser_width = settings.CELL_SIZE // 10
        laser_height = settings.CELL_SIZE
        self.image = pygame.Surface((laser_width, laser_height))
        self.image.fill(settings.LASER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = xy[0]
        self.rect.bottom = xy[1]
        self.speed_y = -15

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
