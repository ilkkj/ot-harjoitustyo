import pygame
import settings


class BaseBox(pygame.sprite.Sprite):
    """Base for two different types of boxes.

    Contains common logic for initialization
    and determining when a box should fall.
    """

    def __init__(self, x, y, color, level_delay=5000):
        """Initializes a new BaseBox object.

        Args:
            x (int): The x-coordinate (top-left corner) of the box.
            y (int): The y-coordinate (top-left corner) of the box.
            color (tuple): The RGB color tuple for the box.
            level_delay (int, optional): The delay in milliseconds before the
                                         box starts falling. Defaults to 5000.
        """
        super().__init__()
        self.cell_size = settings.CELL_SIZE
        self.image = pygame.Surface((self.cell_size, self.cell_size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.level_delay = level_delay
        self.initial_spawn_time = None
        self.previous_move_time = 0

    def should_fall(self, current_time):
        """Checks if the box should fall based on elapsed time and level delay.

        Args:
            current_time (int): The current game time in milliseconds.

        Returns:
            bool: True if the box should fall, False otherwise.
        """
        if not self.initial_spawn_time:
            self.initial_spawn_time = current_time

        if current_time - self.initial_spawn_time < self.level_delay:
            return False

        return current_time - self.previous_move_time >= 100


class Box(BaseBox):
    """Represents a breakable box"""

    def __init__(self, x, y, level_delay=5000):
        """See base class"""
        super().__init__(x, y, settings.BOX_COLOR, level_delay)


class SolidBox(BaseBox):
    """Represents an unbreakable box."""

    def __init__(self, x, y, level_delay=5000):
        """See base class"""
        super().__init__(x, y, settings.SOLID_BOX_COLOR, level_delay)
