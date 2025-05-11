import pygame
import settings


class Laser(pygame.sprite.Sprite):
    """Represents a laser projectile fired by the player or an enemy."""

    def __init__(self, xy):
        """Initializes a new Laser object.

        Args:
            xy (tuple): A tuple containing the initial x and y coordinates.
        """
        super().__init__()
        laser_width = settings.CELL_SIZE // 10
        laser_height = settings.CELL_SIZE // 2
        self.image = pygame.Surface((laser_width, laser_height))
        self.image.fill(settings.LASER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.centerx = xy[0]
        self.rect.bottom = xy[1]
        self.speed_y = - settings.CELL_SIZE // 3

    def update(self):
        """Updates the laser's position and removes it if it goes off-screen."""
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
