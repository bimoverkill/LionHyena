from lionhyena.game.field import Field

from lionhyena.simulation.arena import Arena
from lionhyena.engine import Engine

from lionhyena.config import CONFIG

if CONFIG.GRAPHICS:
    engine = Engine()

    arena = Arena()
    field = Field(arena, engine)

    engine.initialize_game(field)
    engine.run()
else:
    arena = Arena()

    running = False
    while not running:
        running = arena.step()