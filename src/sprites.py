import pygame
import settings


class Player(pygame.sprite.Sprite):
    """Represents the player character"""

    def __init__(self, grid_x, grid_y):
        super().__init__()
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.cell_size = settings.CELL_SIZE
        self.shape_offsets = [(-1, 0), (0, 0), (1, 0), (0, -1)]

        sprite_width_pixels = 3 * self.cell_size
        sprite_height_pixels = 2 * self.cell_size

        self.image = pygame.Surface(
            (sprite_width_pixels, sprite_height_pixels), pygame.SRCALPHA)

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
            self.grid_x * self.cell_size - self.cell_size,
            self.grid_y * self.cell_size - self.cell_size
        )

    def calculate_new_pos(self, dx):
        """Calculates the new grid x-coordinate"""
        return self.grid_x + dx

    def update_position(self, new_grid_x):
        """Updates the player's position"""
        old_grid_x = self.grid_x
        self.grid_x = new_grid_x
        self.rect.x += (new_grid_x - old_grid_x) * self.cell_size


class Box(pygame.sprite.Sprite):
    """Represents a destructible box"""

    def __init__(self, grid_x, grid_y):
        super().__init__()
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.cell_size = settings.CELL_SIZE
        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(settings.BOX_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.grid_x * self.cell_size,
                             self.grid_y * self.cell_size)


class Laser(pygame.sprite.Sprite):
    """Represents a laser fired by the player"""

    def __init__(self, centerx_pixel, bottom_y_pixel):
        super().__init__()
        laser_width = settings.CELL_SIZE // 10
        laser_height = settings.CELL_SIZE * 2
        self.image = pygame.Surface((laser_width, laser_height))
        self.image.fill(settings.LASER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx_pixel
        self.rect.bottom = bottom_y_pixel
        self.speed_y = -10

    def update(self):
        """Updates the laser projectile"""
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
