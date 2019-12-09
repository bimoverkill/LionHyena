from typing import List, Union
from random import randint

from ..config import CONFIG


class Object:
    def __init__(self, init_id: int, init_type: str, init_pos: tuple, init_arena):
        self.id = init_id
        self.type = init_type
        self.pos = init_pos
        self.parent_arena = init_arena

    def __repr__(self):
        return f"<{self.type}-{self.id}>"

    def __str__(self):
        return f"<{self.type}-{self.id}>"


class Entity(Object):
    def __init__(self, init_id: int, init_type: str, init_pos: tuple, parent_arena):
        super().__init__(init_id, init_type, init_pos, parent_arena)

        self.is_alive = True
        self.will_reproduce = False
        self.hunger = 0
        self.target_food = None

        self.simulation_config = CONFIG.SIMULATION.HAWK if self.type == "HWK" else CONFIG.SIMULATION.DOVE

    def wake_up(self):
        self.hunger = 0
        self.is_alive = True
        self.will_reproduce = False
        self.target_food = None

    def find_food(self):
        # check if there any food available
        # print(f"            {self} is hunting")
        if not (True in [i.is_available() for i in self.parent_arena.foods]):
            print(f"            {self} don't get anything to eat !")
            self.is_alive = False
            return

        # print(f"            {self} have chance to get food !")
        while True:
            for i in range(10):
                probability = 0 <= (randint(0, 10000) / 100) <= (100 / len(self.parent_arena.foods))
            for i in range(10):
                self.target_food = self.parent_arena.foods[randint(0, len(self.parent_arena.foods) - 1)]
            if probability:
                if self.target_food.is_available():
                    break
                else:
                    self.target_food = None
                    continue
        print(f"            {self} got {self.target_food}!")

        self.target_food.claim(self.id)

    def fight(self):
        pass        # NO FIGHTING SCENARIO
        # if self.target_food is None:
        #     self.hunger = 0
        #     self.is_alive = False
        #     return
        #
        # partner = self.parent_arena.order(self.target_food.get_eater_partner(self))
        # if partner is None:
        #     return
        #
        # if self.type == "DOV" and partner.type == "DOV":
        #     self.hunger = self.hunger
        # elif self.type == "DOV" and partner.type == "HWK":
        #     self.hunger = self.hunger
        # elif self.type == "HWK" and partner.type == "DOV":
        #     self.hunger = self.hunger
        # elif self.type == "HWK" and partner.type == "HWK":
        #     self.hunger = self.hunger

    def fill_hunger(self, food_points):
        self.hunger += food_points

    def sleep(self):  # All Next Day Calculation and Chances calculated here
        # check if there any chance to survive
        # if self.hunger <= self.simulation_config.SURVIVAL_HUNGER_THRESHOLD:
        #     print(f"            {self} is starving ! {self.hunger}")
        #     self.is_alive = False
        #     return
        # else:
        #     print(f"            {self} eaten {self.hunger} food today")

        print(f"            {self} eaten {self.hunger} food today")
        # calculate survivability
        if self.type == "HWK":
            chance = randint(1, 100000) / 1000
            roll = 100
            if 1.0 < self.hunger < 1.5:
                roll = 75
                self.is_alive = 0 < chance <= roll   # Chance 75%
            elif self.hunger < 1.0:
                self.is_alive = False
                print(f"            {self} has died from starvation !")
                return
            elif self.hunger >= 1.5:
                self.is_alive = True
            elif self.hunger == 1.0:
                roll = 50
                self.is_alive = 0 < chance <= roll   # Chance 50%
        elif self.type == "DOV":
            chance = randint(1, 100000) / 1000
            roll = 100
            if 0.5 < self.hunger < 1.0:
                roll = 75
                self.is_alive = 0 < chance <= roll   # Chance 75%
            if self.hunger < 0.5:
                self.is_alive = False
                print(f"            {self} has died from starvation !")
                return
            elif self.hunger >= 1.0:
                self.is_alive = True
            elif self.hunger == 0.5:
                roll = 50
                self.is_alive = 0 < chance <= roll   # Chance 50%

        if not self.is_alive:

            print(f"            {self} has died from {CONFIG.COMETICS.DIGESTIVE_PROBLEMS[randint(0, len(CONFIG.COMETICS.DIGESTIVE_PROBLEMS)-1)]}")
            return
        else:
            print(f"            {self} stomach is full and seems healty !")

        # surv_chance = self.hunger * self.simulation_config.SURVIVAL_CHANCES_PER_ONE_FOOD
        # surv_chance = round(surv_chance * 1000000) / 1000000  # pembulatan ke 6 decimal
        #
        # self.is_alive = 0 <= (randint(1, 100000000) / 1000000) <= surv_chance
        # if not self.is_alive:
        #     # if not alive, skip reproduce calculation
        #     print(f"            {self} is dying !")
        #     return

        # check if there any chance to reproduce
        if self.hunger < self.simulation_config.REPRODUCE_HUNGER_THRESHOLD:
            print(f"            {self} is hungry, and does not have enouh energy to reproduce !")
            self.will_reproduce = False
            return
        else:
            # calculate reproduce
            repr_chance = self.hunger * self.simulation_config.REPRODUCE_CHANCES_PER_ONE_FOOD
            repr_chance = round(repr_chance * 1000000) / 1000000  # pembulatan ke 6 decimal
            chance = (randint(1, 100000000) / 1000000)

            self.will_reproduce = 0 <= chance <= repr_chance
            if self.will_reproduce:
                print(f"            {self} just finished having fun ! and he got lucky to have a kid !")
            else:
                print(f"            {self} just finished having fun ! but failed to have any kid !")


class Food(Object):
    def __init__(self, init_id: int, init_pos: tuple, parent_arena):
        super().__init__(init_id, "FOD", init_pos, parent_arena)

        self._eater: List[int] = []
        self.food_points = CONFIG.SIMULATION.MEAT_FOOD_POINTS
        self.is_eaten = False

    def claim(self, claimant_id):
        claimant = self.parent_arena.get_object(claimant_id)
        if claimant.type not in ["DOV", "HWK"]:
            raise ValueError("Someting Not Dove or Hawk is trying to eat !")
        if len(self._eater) <= 2:
            self._eater.append(claimant_id)
        else:
            raise ValueError(
                "Food Claimed by more than 3 ! Claimed : {} | new Claimant : {}".format(self._eater, claimant)
            )

    def give_hunger_point(self):
        if len(self._eater) == 1:
            print(f"            {self.parent_arena.order(self._eater[0])} is eating {self} by itself :(")

            portion = 0
            if self.parent_arena.get_object(self._eater[0]).type == "HWK":
                portion = self.food_points * (CONFIG.SIMULATION.HAWK.SELF_PORTION / 100)
            elif self.parent_arena.get_object(self._eater[0]).type == "DOV":
                portion = self.food_points * (CONFIG.SIMULATION.DOVE.SELF_PORTION / 100)

            self.parent_arena.order(self._eater[0]).fill_hunger(portion)
            self.food_points -= self.food_points * (CONFIG.SIMULATION.HAWK.SELF_PORTION / 100)
            if self.food_points < 0 or \
                    self.food_points * (CONFIG.SIMULATION.HAWK.SELF_PORTION / 100) > CONFIG.SIMULATION.MEAT_FOOD_POINTS:
                raise ValueError(f"Hawk <-> Dove Portion Valuation Error ! {self} {self.food_points}")
        elif len(self._eater) < 1:
            return
        elif len(self._eater) > 1:
            print(f"            {self.parent_arena.order(self._eater[0])} is sharing {self} with {self.parent_arena.order(self._eater[1])}")
            fe: Entity = self.parent_arena.get_object(self._eater[0])  # first eater
            se: Entity = self.parent_arena.get_object(self._eater[1])  # second eater

            fe_portion: float = 0.0
            se_portion: float = 0.0

            if fe.type == "DOV" and se.type == "DOV":
                fe_portion = 1.0
                se_portion = 1.0
            elif fe.type == "DOV" and se.type == "HWK":
                fe_portion = 0.5
                se_portion = 1.5
            elif fe.type == "HWK" and se.type == "DOV":
                fe_portion = 1.5
                se_portion = 0.5
            elif fe.type == "HWK" and se.type == "HWK":
                fe_portion = 1.0
                se_portion = 1.0

            fe.fill_hunger(fe_portion)
            se.fill_hunger(se_portion)
            # fe: Entity = self.parent_arena.get_object(self._eater[0])  # first eater          # PORSI DEFAULT
            # se: Entity = self.parent_arena.get_object(self._eater[1])  # second eater
            #
            # fe_portion: float = 0.0
            # se_portion: float = 0.0
            # if fe.type == "DOV" and se.type == "DOV":
            #     fe_portion = self.food_points * (CONFIG.SIMULATION.DOVE.SELF_MEET_DOVE_PORTION / 100)
            #     se_portion = self.food_points * (CONFIG.SIMULATION.DOVE.SELF_MEET_DOVE_PORTION / 100)
            # elif fe.type == "DOV" and se.type == "HWK":
            #     fe_portion = self.food_points * (CONFIG.SIMULATION.DOVE.SELF_MEET_HAWK_PORTION / 100)
            #     se_portion = self.food_points * (CONFIG.SIMULATION.HAWK.SELF_MEET_DOVE_PORTION / 100)
            # elif fe.type == "HWK" and se.type == "DOV":
            #     fe_portion = self.food_points * (CONFIG.SIMULATION.HAWK.SELF_MEET_DOVE_PORTION / 100)
            #     se_portion = self.food_points * (CONFIG.SIMULATION.DOVE.SELF_MEET_HAWK_PORTION / 100)
            # elif fe.type == "HWK" and se.type == "HWK":
            #     fe_portion = self.food_points * (CONFIG.SIMULATION.HAWK.SELF_MEET_HAWK_PORTION / 100)
            #     se_portion = self.food_points * (CONFIG.SIMULATION.HAWK.SELF_MEET_HAWK_PORTION / 100)
            #
            # self.parent_arena.order(self._eater[0]).fill_hunger(fe_portion)
            # self.parent_arena.order(self._eater[1]).fill_hunger(se_portion)
            #
            # self.food_points -= fe_portion + se_portion
            # if self.food_points < 0 or (fe_portion + se_portion) > CONFIG.SIMULATION.MEAT_FOOD_POINTS:
            #     raise ValueError(f"Hawk <-> Dove Portion Valuation Error ! {self} {self.food_points}")

        self.is_eaten = True

    def get_eater_partner(self, eater):
        if len(self._eater) > 1:
            for i in self._eater:
                if i != eater:
                    return i

    def is_owned_by_anyone(self):
        return not len(self._eater) == 0

    def is_available(self):
        if self.is_eaten:
            return False
        else:
            return len(self._eater) < 2
