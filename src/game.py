import pygame
from level import Level
from sprites import Player, Box, Laser
import settings


class Game:
    """Manages the game loop and sprites"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.running = False
        self.player = None
        self.grid = None

        self.level = Level()
        self._load_level()

    def _load_level(self):
        """Creates an empty grid, adds boxes and creates the sprites"""
        self.grid = self.level.generate_grid()
        self.grid = self.level.generate_new_boxes(self.grid)

        self.all_sprites = pygame.sprite.Group()
        self.box_sprites = pygame.sprite.Group()
        self.laser_sprites = pygame.sprite.Group()

        self._create_player()

        for r in range(settings.ROWS):
            for c in range(settings.COLS):
                if self.grid[r][c] == settings.BOX:
                    self._create_box(c, r)

        self.running = True

    def _create_player(self):
        """Creates a Player sprite at the default coordinates"""
        player_start_x = settings.COLS // 2
        player_start_y = settings.ROWS - 1

        player_model_cells = []
        self.player = Player(player_start_x, player_start_y)
        shape_offsets = self.player.shape_offsets

        for dx, dy in shape_offsets:
            grid_c, grid_r = player_start_x + dx, player_start_y + dy
            player_model_cells.append((grid_c, grid_r))

        for c, r in player_model_cells:
            self.grid[r][c] = settings.PLAYER
        self.all_sprites.add(self.player)

    def _create_box(self, grid_x, grid_y):
        """Creates a Box sprite at the grid coordinates"""
        box = Box(grid_x, grid_y)
        self.all_sprites.add(box)
        self.box_sprites.add(box)

    def _handle_events(self):
        """Handles user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._move_player(-1)
                elif event.key == pygame.K_RIGHT:
                    self._move_player(1)
                elif event.key == pygame.K_SPACE:
                    self._shoot_laser()
                elif event.key == pygame.K_q:
                    self.running = False

    def _move_player(self, dx):
        """Handles the movement logic for the player"""
        if not self.player:
            return

        new_center_x = self.player.calculate_new_pos(dx)
        current_center_x = self.player.grid_x
        center_y = self.player.grid_y

        can_move = True
        new_player_xy = []
        for offset_x, offset_y in self.player.shape_offsets:
            new_x = new_center_x + offset_x
            new_y = center_y + offset_y
            new_player_xy.append((new_x, new_y))

            if not (0 <= new_x < settings.COLS and 0 <= new_y < settings.ROWS):
                can_move = False
                break

            grid_value = self.grid[new_y][new_x]
            if grid_value not in (settings.EMPTY, settings.PLAYER):
                can_move = False
                break

        if can_move:
            for offset_x, offset_y in self.player.shape_offsets:
                old_x = current_center_x + offset_x
                old_y = center_y + offset_y
                if 0 <= old_x < settings.COLS and 0 <= old_y < settings.ROWS:
                    self.grid[old_y][old_x] = settings.EMPTY

            for new_x, new_y in new_player_xy:
                self.grid[new_y][new_x] = settings.PLAYER
            self.player.update_position(new_center_x)

    def _shoot_laser(self):
        """Creates a Laser sprite"""
        top_center_offset_x, top_center_offset_y = 0, -1
        laser_origin_grid_x = self.player.grid_x + top_center_offset_x
        laser_origin_grid_y = self.player.grid_y + top_center_offset_y
        laser_centerx_pixel = (laser_origin_grid_x *
                               settings.CELL_SIZE) + (settings.CELL_SIZE // 2)
        laser_bottom_y_pixel = laser_origin_grid_y * settings.CELL_SIZE

        laser = Laser(laser_centerx_pixel, laser_bottom_y_pixel)
        self.all_sprites.add(laser)
        self.laser_sprites.add(laser)

    def _update(self):
        """Updates the state of game sprites"""
        self.all_sprites.update()
        pygame.sprite.groupcollide(
            self.laser_sprites, self.box_sprites, True, True)

    def _draw(self):
        """Draws all game elements to the screen"""
        self.screen.fill(settings.BACKGROUND_COLOR)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def run(self):
        """Starts the main game loop"""
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(settings.FPS)

        pygame.quit()
