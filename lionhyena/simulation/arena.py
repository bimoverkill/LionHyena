from random import randint
from typing import List, Union, Callable

from .entities import Entity, Food
from ..config import CONFIG
from .utilities import debug


class Arena:
    def __init__(self):
        self.foods: List[Food] = []
        self.dov_population_log = []
        self.hwk_population_log = []
        self.entities: List[Entity] = []

        self._day = 0
        self._current_steps = 0
        self._steps: List[Callable] = [
            self.log,
            self.generate_foods,
            self.wakeup,
            self.find_food,
            self.moving_to_food,
            self.eating,
            self.fighting,
            self.moving_to_home,
            self.sleep
        ]

        self.spawn_initial_entities()

    def spawn_initial_entities(self):
        for i in range(CONFIG.SIMULATION.INITIAL_HAWK):
            self.entities.append(
                Entity(
                    self.get_available_id(),
                    "HWK",
                    (randint(0, CONFIG.SIMULATION.ARENA_SIZE[0]), randint(0, CONFIG.SIMULATION.ARENA_SIZE[1])),
                    self
                )
            )

        for i in range(CONFIG.SIMULATION.INITIAL_DOVE):
            self.entities.append(
                Entity(
                    self.get_available_id(),
                    "DOV",
                    (randint(0, CONFIG.SIMULATION.ARENA_SIZE[0]), randint(0, CONFIG.SIMULATION.ARENA_SIZE[1])),
                    self
                )
            )

    def step(self):
        if self._day <= CONFIG.SIMULATION.MAX_DAYS:
            self._steps[self._current_steps]()

            self._current_steps += 1
            if self._current_steps > len(self._steps) - 1:
                self._current_steps = 0
                self._day += 1

            return False

        self.export_to_csv()
        return True

    def log(self):
        debug(f"Day {self._day} Started !")
        self.dov_population_log.append(len([i for i in self.entities if i.type == "DOV"]))
        self.hwk_population_log.append(len([i for i in self.entities if i.type == "HWK"]))

    def export_to_csv(self):
        debug("Exporting to CSV...")
        with open("data.csv", "w+") as f:
            f.writelines(["Populasi Singa,", "Populasi Hyena\n"])
            for i in range(CONFIG.SIMULATION.MAX_DAYS):
                f.writelines([f"{self.hwk_population_log[i]},", f"{self.dov_population_log[i]}\n"])
        debug("CSV export done")

    def wakeup(self):
        debug(f"        Delivering all new born babies ! {len([i.will_reproduce for i in self.entities])}")
        # let all entities reproduce
        while True in [i.will_reproduce for i in self.entities]:
            for i in self.entities:
                if i.will_reproduce:
                    new_entity = Entity(
                        self.get_available_id(),
                        i.type,
                        (randint(0, CONFIG.SIMULATION.ARENA_SIZE[0]), randint(0, CONFIG.SIMULATION.ARENA_SIZE[1])),
                        self
                    )
                    self.entities.append(new_entity)
                    i.will_reproduce = False

                    debug(f"            {i} successfuly borned {new_entity} !", is_verbose=True)

        debug(f"        Waking Up All Entities {len(self.entities)}")
        c = 0
        for i in self.entities:
            i.wake_up()
            c += 1

    def find_food(self):
        debug(f"        Letting All Entities Finding Food {len(self.entities)}")
        c = 0
        for i in self.entities:
            food = i.find_food()
            c += 1

    def moving_to_food(self):
        debug(f"        telling entities to go to food ! {len(self.entities)}")
        c = 0
        for i in self.entities:
            i.goto_food()
            c += 1

    def eating(self):
        debug(f"        Ordering Entities to Eat {len(self.entities)}")
        c = 0
        for i in self.foods:
            if i.is_owned_by_anyone():
                i.give_hunger_point()
                c += 1

    def fighting(self):
        debug(f"        Match each Entities to fight each other ! {len(self.entities)}")
        c = 0
        for i in self.entities:
            i.fight()
            c += 1

    def moving_to_home(self):
        debug(f"        telling entities to go home ! {len(self.entities)}")
        c = 0
        for i in self.entities:
            i.goto_home()
            c += 1

    def sleep(self):
        debug(f"        letting Entities to sleep {len(self.entities)}")
        c = 0
        for i in self.entities:
            i.sleep()
            c += 1

        debug("         Wiping all dead entities !", end="\r")
        while False in [i.is_alive for i in self.entities]:
            for i in range(len(self.entities)):
                if not self.entities[i].is_alive:
                    self.entities.pop(i)
                    break

    def generate_foods(self):
        debug(f"        Generating food for day {self._day}")
        self.foods = []
        for i in range(CONFIG.SIMULATION.INITIAL_MEATS + (self._day * CONFIG.SIMULATION.MEAT_CHANGE_PER_DAY)):
            self.foods.append(
                Food(
                    self.get_available_id(),
                    (randint(0, CONFIG.SIMULATION.ARENA_SIZE[0]), randint(0, CONFIG.SIMULATION.ARENA_SIZE[1])),
                    self
                )
            )

    def get_available_id(self):
        all_id = self.get_all_id()
        if len(all_id) <= 0:
            return 1
        else:
            return max(all_id) + 1

    def check_id_exist(self, target_id):
        return target_id in [i.id for i in self.foods] + [i.id for i in self.entities]

    def get_all_id(self):
        all_id = []
        for i in self.foods:
            all_id.append(i.id)

        for i in self.entities:
            all_id.append(i.id)

        return all_id

    def get_object(self, target_id):
        for i in self.foods:
            if i.id == target_id:
                return i

        for i in self.entities:
            if i.id == target_id:
                return i

    def order(self, target_id):
        return self.get_object(target_id)