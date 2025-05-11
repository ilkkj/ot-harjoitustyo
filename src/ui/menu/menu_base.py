import pygame
import sys
import settings


class MenuBase:
    """Base class for game menu screens."""

    def __init__(self, display, event_queue):
        self.display = display
        self.event_queue = event_queue
        self.title_font = settings.TITLE_FONT
        self.option_font = settings.MENU_FONT
        self.content_font = settings.CONTENT_FONT
        self.title = None
        self.options = []
        self.selected = 0
        self.content = []

    def _render_title(self):
        """Renders the menu title at the top of the screen."""
        if self.title:
            title_text = self.title_font.render(
                self.title, True, settings.MENU_TITLE_COLOR)
            title_rect = title_text.get_rect(center=(settings.WIDTH // 2, 60))
            self.display.blit(title_text, title_rect)

    def _render_content(self, start_y):
        """Renders content text.

        Args:
            start_y (int): The vertical position to begin rendering content.

        Returns:
            int: The new vertical position after rendering all content lines.
        """
        for line in self.content:
            text = self.content_font.render(
                line, True, settings.MENU_TEXT_COLOR)
            rect = text.get_rect(center=(settings.WIDTH // 2, start_y))
            self.display.blit(text, rect)
            start_y += 40
        return start_y

    def _render_options(self, start_y):
        """Renders menu options, highlighting the currently selected one.

        Args:
            start_y (int): The vertical position to begin rendering options.
        """
        for i, option in enumerate(self.options):
            color = settings.MENU_TEXT_HIGHLIGHT_COLOR if i == self.selected else settings.MENU_TEXT_COLOR
            text = self.option_font.render(option, True, color)
            rect = text.get_rect(
                center=(settings.WIDTH // 2, start_y + i * 60))
            self.display.blit(text, rect)

    def _render(self):
        """Clears the screen and renders title, content, and options."""
        self.display.fill(settings.MENU_BACKGROUND_COLOR)
        self._render_title()
        y_offset = self._render_content(start_y=120)
        self._render_options(start_y=y_offset + 40)
        pygame.display.flip()

    def _handle_events(self):
        """Processes user input for navigating and selecting menu options.

        Returns:
            str or None: The selected option as a string, or None if quitting.
        """
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    self.selected = (self.selected - 1) % len(self.options)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.selected = (self.selected + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    return self.options[self.selected]
                elif event.key in (pygame.K_q, pygame.K_ESCAPE) and __name__ != "main_menu":
                    return

    def run(self):
        """Runs the menu loop until an option is selected or quit.

        Returns:
            str or None: The selected option, or None if user exits menu.
        """
        while True:
            self._render()
            choice = self._handle_events()
            if choice:
                return choice
