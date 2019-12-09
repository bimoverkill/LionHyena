from typing import List

from pathfinding.core.grid import Grid
import pygame

from ..config import CONFIG
from ..simulation.arena import Arena
from ..engine import Engine


class Field:
    def __init__(self, arena: Arena, engine: Engine):
        self.arena = arena
        self.engine = engine
        self.grid = Grid(
            matrix=[
                [0 for _ in range(CONFIG.SIMULATION.ARENA_SIZE[0])]
                for __ in range(CONFIG.SIMULATION.ARENA_SIZE[1])
            ]
        )
        self._mini_steps = 0
        self._current_steps = 0
        self._steps: List[bool] = [
            False,      # nil
            False,      # generate_foods
            False,      # wakeup
            False,      # find_food
            False,      # moving_to_food
            False,      # eating
            False,      # fighting
            False,      # moving_to_home
            False       # sleep
        ]
        self.current_session = {
            "foods": [],
            "entities": []
        }

    def step(self):
        self.draw()
        if self._mini_steps <= 240:
            self._mini_steps += 1
        else:
            self._steps[self._current_steps] = True

            self._current_steps += 1
            self.arena.step()
            self.update_session()

            if self._current_steps >= len(self._steps) - 1:
                self._steps = [False for _ in range(8)]
                self._current_steps = 0

            self._mini_steps = 0

    def update_session(self):
        self.current_session["foods"] = [i.pos for i in self.arena.foods]
        self.current_session["entities"] = [i.pos for i in self.arena.entities]

    def draw(self):
        if self._steps[0]:  # nil
            ...  # Draw Text "Day N"

        if self._steps[1]:  # generate_foods
            for i in self.current_session["foods"]:
                pygame.draw.circle(self.engine.surface, (255, 0, 0), i, 5)

        if self._steps[2]:  # wakeup
            for i in self.current_session["entities"]:
                pygame.draw.circle(self.engine.surface, (255, 255, 0), i, 5)
            ...

        if self._steps[3]:  # find_food
            ...

        if self._steps[4]:  # moving_to_food
            ...

        if self._steps[5]:  # eating
            ...

        if self._steps[6]:  # fighting
            ...

        if self._steps[7]:  # moving_to_home
            ...

        if self._steps[8]:  # sleep
            ...

