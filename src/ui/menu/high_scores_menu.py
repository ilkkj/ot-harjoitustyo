import settings
from ui.menu.menu_base import MenuBase
from repositories.high_scores_repository import HighScoresRepository


class HighScoresMenu(MenuBase):
    """Menu screen for displaying the top high scores."""

    def __init__(self, display, event_queue):
        """See base class"""
        super().__init__(display, event_queue)
        self.title = "High scores"
        self.options = ["Back"]
        self.content_font = settings.HIGH_SCORE_FONT
        self.repository = HighScoresRepository()
        self.content = self._get_high_scores()

    def _get_high_scores(self):
        """Fetches and formats the top high scores.

        Returns:
            list[str]: Formatted list of top scores, or a message if none exist.
        """
        scores = self.repository.get_top_scores(limit=5)
        if len(scores) == 0:
            return ["No high scores yet."]
        formatted_scores = [
            f"{index + 1}. {name} - {score}" for index, (name, score) in enumerate(scores)
        ]
        return formatted_scores
