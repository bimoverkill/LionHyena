from random import randint
from typing import List, Union, Callable

from .entities import Entity, Food
from ..config import CONFIG


class Arena:
    def __init__(self):
        self.foods: List[Food] = []
        self.dov_population_log = []
        self.hwk_population_log = []
        self.entities: List[Entity] = []

        self._day = 0
        self._steps: List[Callable] = [
            self.generate_foods,
            self.wakeup,
            self.find_food,
            self.moving_to_food,
            self.eating,
            self.fighting,
            self.moving_to_home,
            self.sleep,
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

    def start_match(self):
        while self._day <= CONFIG.SIMULATION.MAX_DAYS:
            self.dov_population_log.append(len([i for i in self.entities if i.type=="DOV"]))
            self.hwk_population_log.append(len([i for i in self.entities if i.type=="HWK"]))

            print(f"Day : {self._day}")
            for i in self._steps:
                i()

            print(f"    Entities : ")
            print(f"        - Total Length : {len(self.entities)} Entities")
            print(f"        - Hyena Count  : {len([i for i in self.entities if i.type=='DOV'])} Entities")
            print(f"        - Lion Count   : {len([i for i in self.entities if i.type=='HWK'])} Entities")

            self._day += 1

        self.export_to_csv()

    def export_to_csv(self):
        print("Exporting to CSV...")
        with open("data.csv", "w+") as f:
            f.writelines(["Populasi Singa,", "Populasi Hyena\n"])
            for i in range(CONFIG.SIMULATION.MAX_DAYS):
                f.writelines([f"{self.hwk_population_log[i]},", f"{self.dov_population_log[i]}\n"])
        print("CSV export done")

    def wakeup(self):
        print(f"        Delivering all new born babies ! {len([i.will_reproduce for i in self.entities])}")
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

                    print(f"            {i} successfuly borned {new_entity} !")

        print(f"        Waking Up All Entities {len(self.entities)}")
        c = 0
        for i in self.entities:
            i.wake_up()
            c += 1


    def find_food(self):
        print(f"        Letting All Entities Finding Food {len(self.entities)}")
        c = 0
        for i in self.entities:
            food = i.find_food()
            c += 1


    def moving_to_food(self):
        ...

    def eating(self):
        print(f"        Ordering Entities to Eat {len(self.entities)}")
        c = 0
        for i in self.foods:
            if i.is_owned_by_anyone():
                i.give_hunger_point()
                c += 1


    def fighting(self):
        print(f"        Match each Entities to fight each other ! {len(self.entities)}")
        c = 0
        for i in self.entities:
            i.fight()
            c += 1


    def moving_to_home(self):
        ...

    def sleep(self):
        print(f"        letting Entities to sleep {len(self.entities)}")
        c = 0
        for i in self.entities:
            i.sleep()
            c += 1

        print("         Wiping all dead entities !", end="\r")
        while False in [i.is_alive for i in self.entities]:
            for i in range(len(self.entities)):
                if not self.entities[i].is_alive:
                    self.entities.pop(i)
                    break

    def generate_foods(self):
        print(f"        Generating food for day {self._day}")
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