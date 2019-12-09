import pygame

from .config import CONFIG


class Engine:
    def __init__(self):
        self._clock = pygame.time.Clock()
        self._playtime = 0.0

        self._is_running = True
        self._game = None

        self.screen = None
        self.surface = None

        pygame.init()
    
    def initialize_game(self, game_instance=None):
        self._game = game_instance

        self.screen = pygame.display.set_mode(CONFIG.SCREEN_SIZE)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface.fill((125, 125, 125))
        self.surface = self.surface.convert()

    def run(self):
        while self._is_running:
            self.refresh()

    def refresh(self):
        self._playtime += self._clock.tick(CONFIG.MAX_FPS) / 1000

        self.surface.fill((125, 125, 125))
        self._game.step()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._is_running = False
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._is_running = False

                    if self._game is not None:
                        self._game.control_event(event.key, True)

                if event.type == pygame.KEYUP:
                    if self._game is not None:
                        self._game.control_event(event.key, False)

        if CONFIG.DEBUG:
            pygame.display.set_caption(
                "{} FPS:{:.2f} Playtime:{:.2f}".format(CONFIG.APP_NAME, self._clock.get_fps(), self._playtime)
            )
        else:
            pygame.display.set_caption(
                CONFIG.APP_NAME
            )

        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()