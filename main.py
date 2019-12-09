from lionhyena.game.field import Field

from lionhyena.simulation.arena import Arena
from lionhyena.engine import Engine

engine = Engine()

arena = Arena()
field = Field(arena, engine)

engine.initialize_game(field)
engine.run()
