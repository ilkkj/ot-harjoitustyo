from database_connection import get_database_connection


class HighScoresRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def add_score(self, name: str, score: int):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO highscores (name, score) VALUES (?, ?)",
            (name, score)
        )
        self._connection.commit()

    def get_top_scores(self, limit: int = 10):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT name, score FROM highscores ORDER BY score DESC LIMIT ?",
            (limit,)
        )
        rows = cursor.fetchall()
        return [(row["name"], row["score"]) for row in rows]
