import os
import yaml


class LevelRepository:
    """Responsible for loading level configuration data from a YAML file.

    Expected data structure is a list of levels, where each
    level is represented as a list of rows, and each row is a list of integers
    mapping to game elements.
    """

    def __init__(self, filename: str = "level_data.yaml"):
        """Sets up the path to the level data file for loading.

        Args:
            filename (str, optional): The name of the YAML file containing
                                      level data. Defaults to 'level_data.yaml'.
        """
        base_dir = os.path.dirname(__file__)
        self.filepath = os.path.join(base_dir, "..", "data", filename)

    def get(self):
        """Loads and returns the level data from the YAML file.

        Returns:
            list or None: Level data as list of [level [row [cell]]] integers, or None on failure.
        """
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
        except (yaml.YAMLError, OSError):
            return None

        if not isinstance(data, list):
            return None

        return data
