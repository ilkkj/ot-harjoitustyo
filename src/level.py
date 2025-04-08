import settings


class Level:
    """Manages the game level structure"""

    def __init__(self):
        pass

    def generate_grid(self):
        """Creates an empty grid"""
        grid = [[settings.EMPTY for _ in range(
            settings.COLS)] for _ in range(settings.ROWS)]
        return grid

    def generate_new_boxes(self, grid, num_rows_to_fill=3):
        """Adds boxes to the grid"""
        rows_to_fill = min(num_rows_to_fill, settings.ROWS)

        for r in range(rows_to_fill):
            for c in range(settings.COLS):
                if grid[r][c] == settings.EMPTY:
                    grid[r][c] = settings.BOX
        return grid
