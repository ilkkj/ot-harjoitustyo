from ui.menu.menu_base import MenuBase
from repositories.how_to_play_repository import HowToPlayRepository


class HowToPlayMenu(MenuBase):
    """Menu screen for displaying game instructions."""

    def __init__(self, display, event_queue):
        """See base class"""
        super().__init__(display, event_queue)
        self.title = "How to play"
        self.options = ["Back"]
        self.repository = HowToPlayRepository()
        self.content = self._get_instructions()

    def _get_instructions(self):
        """Retrieves instructional lines from the repository.

        Returns:
            list[str]: A list of instruction lines to be displayed in the menu.
        """
        instructions = self.repository.get()
        return instructions
