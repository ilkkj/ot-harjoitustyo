import pygame
import settings


class Player(pygame.sprite.Sprite):
    """Represents the player character.

    The player is drawn as a simple block
    shape composed of multiple cells.
    """

    def __init__(self):
        """Initializes a new Player object.

        Sets up the player's appearance and initial position
        based on game settings.
        """
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
