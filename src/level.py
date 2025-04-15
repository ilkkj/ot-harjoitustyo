import pygame
from sprites import Player, Box, SolidBox, Wall, Laser
import settings


class Level:

    def __init__(self, initial_grid_data=None):
        self.cell_size = settings.CELL_SIZE

        self.grid_data = initial_grid_data

        if self.grid_data is None:
            self.create_default_grid()

        self.player = None
        self.all_sprites = pygame.sprite.Group()
        self.box_sprites = pygame.sprite.Group()
        self.solid_box_sprites = pygame.sprite.Group()
        self.all_box_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()
        self.laser_sprites = pygame.sprite.Group()

        self._initialize_sprites(self.grid_data)

    def _initialize_sprites(self, level_map):
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
                elif cell == 3:
                    self.wall_sprites.add(Wall(normalized_x, normalized_y))

        self.player = Player()

        self.all_box_sprites.add(
            self.box_sprites,
            self.solid_box_sprites
        )

        self.all_sprites.add(
            self.wall_sprites,
            self.box_sprites,
            self.solid_box_sprites,
            self.all_box_sprites,
            self.player
        )

    def _player_can_move(self, dx=0, dy=0):
        self.player.rect.move_ip(dx, dy)

        colliding_walls = pygame.sprite.spritecollide(
            self.player, self.wall_sprites, False)
        can_move = not colliding_walls
        self.player.rect.move_ip(-dx, -dy)

        return can_move

    def move_player(self, dx=0, dy=0):
        if not self._player_can_move(dx):
            return

        self.player.rect.move_ip(dx, dy)

    def move_boxes(self, current_time):
        for box in self.all_box_sprites:
            if box.should_fall(current_time):
                box.rect.move_ip(0, self.cell_size)
                box.previous_move_time = current_time

    def shoot_laser(self):
        laser = Laser(self.player.rect.midtop)
        self.all_sprites.add(laser)
        self.laser_sprites.add(laser)

    def _check_collision(self):
        pygame.sprite.groupcollide(
            self.laser_sprites, self.box_sprites, True, True)
        pygame.sprite.groupcollide(
            self.laser_sprites, self.solid_box_sprites, True, False)
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

    def update(self, current_time):
        self.move_boxes(current_time)
        self.all_sprites.update()
        self._check_collision()

    def create_default_grid(self):
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

        self.grid_data = grid_data
