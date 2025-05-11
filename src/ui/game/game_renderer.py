import pygame
import settings


class GameRenderer:
    """Responsible for drawing all game elements onto the display."""

    def __init__(self, display, level):
        """Initializes the Renderer.

        Args:
            display: The surface to draw onto.
            level: The game level object containing the sprites to render.
        """
        self._display = display
        self._level = level

    def render(self):
        """Clears the display and draws all sprites from the level."""
        self._display.fill(settings.BACKGROUND_COLOR)
        self._level.all_sprites.draw(self._display)
        self._level.laser_sprites.draw(self._display)
        pygame.display.flip()
