import pygame
import settings


class Wall(pygame.sprite.Sprite):
    """Represents a single wall segment.

    Walls are static objects.
    """

    def __init__(self, x, y):
        """Initializes a new Wall object at a specific position.

        Args:
            x (int): The x-coordinate of the wall segment.
            y (int): The y-coordinate of the wall segment.
        """
        super().__init__()
        self.cell_size = settings.CELL_SIZE
        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(settings.WALL_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
