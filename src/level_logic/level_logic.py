import pygame
from sprites.player import Player
from sprites.box import Box, SolidBox
from sprites.wall import Wall
from sprites.laser import Laser
import settings


class LevelLogic:
    """Manages the game level structure and sprite interactions"""

    def __init__(self, initial_grid_data=None):
        """Initializes the Level object.

        Creates a default grid if `initial_grid_data` is not provided.
        Initializes sprite groups and loads the sprites for the first level.

        Args:
            initial_grid_data (list, optional): A list containing levels as 2D lists.
                                                Defaults to None.
        """
        self.cell_size = settings.CELL_SIZE

        self.grid_data = initial_grid_data

        if self.grid_data is None:
            self._create_default_grid()

        self.next_level_index = 0
        self.hits = 0

        self.player = None
        self.all_sprites = pygame.sprite.Group()
        self.box_sprites = pygame.sprite.Group()
        self.solid_box_sprites = pygame.sprite.Group()
        self.all_box_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()
        self.laser_sprites = pygame.sprite.Group()

        self._initialize_sprites(self.grid_data[self.next_level_index])

    def _initialize_sprites(self, level_map):
        """Initializes sprite objects based on the provided level map.

        Calls `_start_new_level` to load the map data and creates the player object.
        Adds walls and the player to the `all_sprites` group.

        Args:
            level_map (list): A 2D list representing the level to load.
        """
        self._start_new_level(level_map)

        self.player = Player()

        self.all_sprites.add(
            self.wall_sprites,
            self.player
        )

    def _read_level_map(self, level_map):
        """Reads the level map and creates corresponding sprite objects.

        Iterates through the given 2D list and creates Box, SolidBox,
        or Wall objects based on the values in the map

        Args:
            level_map (list): A list representing the level to load.
                            1: Box, 2: SolidBox, 3: Wall.
        """
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 1:
                    self.box_sprites.add(Box(normalized_x, normalized_y))
                elif cell == 2:
                    self.solid_box_sprites.add(
                        SolidBox(normalized_x, normalized_y))
                elif self.next_level_index == 1 and cell == 3:
                    self.wall_sprites.add(Wall(normalized_x, normalized_y))

    def _player_can_move(self, dx=0, dy=0):
        """Checks if the player can move in the specified direction without hitting walls.

        Temporarily moves the player, checks for collisions with walls, and then
        moves the player back to its original position.

        Args:
            dx (int, optional): The change in the x-coordinate in pixels. Defaults to 0.
            dy (int, optional): The change in the y-coordinate in pixels. Defaults to 0.

        Returns:
            bool: True if the player can move in the specified direction, False otherwise.
        """
        self.player.rect.move_ip(dx, dy)

        colliding_walls = pygame.sprite.spritecollide(
            self.player, self.wall_sprites, False)
        can_move = not colliding_walls
        self.player.rect.move_ip(-dx, -dy)

        return can_move

    def move_player(self, dx=0, dy=0):
        """Moves the player in the specified direction if the movement is possible.

        Calls `_player_can_move` to check if the movement is allowed

        Args:
            dx (int, optional): The change in the x-coordinate in pixels. Defaults to 0.
            dy (int, optional): The change in the y-coordinate in pixels. Defaults to 0.
        """
        if not self._player_can_move(dx):
            return

        self.player.rect.move_ip(dx, dy)

    def _move_boxes(self, current_time):
        """Moves all boxes downwards if they are supposed to fall.

        If a box should fall, it is
        moved down by one cell size.

        Args:
            current_time (int): The current game time used
                                for timing the fall.
        """
        for box in self.all_box_sprites:
            if box.should_fall(current_time):
                box.rect.move_ip(0, self.cell_size)
                box.previous_move_time = current_time

    def _move_laser(self):
        """Updates the position of all active lasers."""
        for laser in self.laser_sprites:
            laser.update()

    def shoot_laser(self):
        """Creates a new laser projectile originating from the player."""
        laser = Laser(self.player.rect.midtop)
        self.laser_sprites.add(laser)

    def _check_collision(self):
        """Checks and handles collisions between sprite objects.

        Checks for the following collisions:
        - Lasers vs. Solid Boxes (laser is destroyed)
        - Lasers vs. Regular Boxes (both are destroyed)
        - Lasers vs. Walls (laser is destroyed)
        - Regular Boxes vs. Walls (box is destroyed)
        - Solid Boxes vs. Walls (box is destroyed)
        - Player vs. Any Box (game gets restarted)
        """
        pygame.sprite.groupcollide(
            self.laser_sprites, self.solid_box_sprites, True, False)
        if pygame.sprite.groupcollide(
                self.laser_sprites, self.box_sprites, True, True):
            self.hits += 1
        pygame.sprite.groupcollide(
            self.laser_sprites, self.wall_sprites, True, False)
        pygame.sprite.groupcollide(
            self.box_sprites, self.wall_sprites, True, False)
        pygame.sprite.groupcollide(
            self.solid_box_sprites, self.wall_sprites, True, False)

        if pygame.sprite.spritecollide(self.player, self.all_box_sprites, False):
            if pygame.sprite.spritecollide(self.player, self.all_box_sprites, True,
                                           pygame.sprite.collide_mask):
                pygame.event.post(pygame.event.Event(
                    settings.GAME_RESTART_EVENT))

    def _check_level_status(self):
        """Checks if the current level is completed and loads the next one if necessary.

        If all boxes have been removed and there is a next level
        available in the `grid_data` list, loads the next level by calling `_start_new_level`.
        """

        if not self.all_box_sprites:
            if self.next_level_index == len(self.grid_data):
                pygame.event.post(pygame.event.Event(
                    settings.GAME_WON_EVENT))
                return
            self._start_new_level(self.grid_data[self.next_level_index])

    def _start_new_level(self, level_map):
        """Initializes and loads a new level using the provided map.

        Clears old lasers, increments the level index, reads the new map to create
        new boxes.

        Args:
            level_map (list): A 2D list representing the level to load.
        """
        self.laser_sprites.empty()
        self.next_level_index += 1
        self._read_level_map(level_map)

        self.all_box_sprites.add(
            self.box_sprites,
            self.solid_box_sprites
        )

        self.all_sprites.add(
            self.box_sprites,
            self.solid_box_sprites,
            self.all_box_sprites,
        )

    def update(self, current_time):
        """Updates the entire level state.

        Calls methods to move boxes and lasers, check for collisions,
        and check the level status.

        Args:
            current_time (int): The current game time, passed to `_move_boxes` which
                                need it for timing.
        """
        self._move_boxes(current_time)
        self._move_laser()
        self._check_collision()
        self._check_level_status()

    def _create_default_grid(self):
        """Creates a default grid if no `initial_grid_data` is provided to the constructor."""
        rows = settings.ROWS
        cols = settings.COLS
        grid_data = []

        for r in range(rows):
            row_data = []
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    row_data.append(3)
                elif r < 3:
                    row_data.append(1)
                elif r == 3 and c < 4:
                    row_data.append(2)
                else:
                    row_data.append(0)
            grid_data.append(row_data)

        self.grid_data = [grid_data]

    def get_score(self):
        """Calculates the score

        Returns:
            int: Number of times the player has destroyed a box.
        """
        score = self.hits
        return score
