import settings
from ui.menu.menu_base import MenuBase
from repositories.high_scores_repository import HighScoresRepository


class GameClearedMenu(MenuBase):
    """Menu screen shown when the game is successfully completed."""

    def __init__(self, display, event_queue, score):
        """See base class"""
        super().__init__(display, event_queue)
        self.title = "Game cleared!"
        self.options = ["Back"]
        self.content_font = settings.HIGH_SCORE_FONT
        self.score = score
        self.repository = HighScoresRepository()
        self.content = ["Your score has been saved.",
                        f"Your score: {self.score}"]
        self._save_high_scores()

    def _save_high_scores(self):
        """Stores the player's score in the high scores database."""
        username = "Local user"
        self.repository.add_score(username, self.score)
