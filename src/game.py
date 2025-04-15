import pygame
import settings


class Game:
    def __init__(self, level, renderer, clock, event_queue):
        self._level = level
        self._renderer = renderer
        self._clock = clock
        self._event_queue = event_queue
        self._running = False
        self._restart_requested = False
        self._cell_size = settings.CELL_SIZE

    def start(self):
        self._running = True
        while self._running:
            if not self._handle_events():
                break
            self._update()
            self._render()
            self._clock.tick(settings.FPS)
        return self._restart_requested

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                self._running = False
                return False

            if event.type == settings.GAME_RESTART_EVENT:
                self._restart()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.move_player(dx=-settings.CELL_SIZE)
                elif event.key == pygame.K_RIGHT:
                    self._level.move_player(dx=settings.CELL_SIZE)
                elif event.key == pygame.K_SPACE:
                    self._level.shoot_laser()
                elif event.key == pygame.K_r:
                    self._restart()
                elif event.key == pygame.K_q:
                    self._running = False
                    return False
        return True

    def _update(self):
        current_time = self._clock.get_ticks()

        self._level.update(current_time)

    def _render(self):
        self._renderer.render()

    def _restart(self):
        self._running = False
        self._restart_requested = True
