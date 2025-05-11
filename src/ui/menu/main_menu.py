from ui.menu.menu_base import MenuBase


class MainMenu(MenuBase):
    """Main menu screen for the game."""

    def __init__(self, display, event_queue):
        """See base class"""
        super().__init__(display, event_queue)
        self.title = "Box Breaker"
        self.options = ["Start", "High scores", "How to play", "Quit"]
