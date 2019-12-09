class CONFIG:
    APP_NAME = "Lion Hyena"
    SCREEN_SIZE = (1024, 1024)                          # w640 x h640 Pixel
    MAX_FPS = 120
    DEBUG = True

    class GAME:
        CELL_SIZE = (24, 24)                            # PIXEL -> w24 x h24 Pixel

    class COMETICS:
        DIGESTIVE_PROBLEMS = [
            "Marasmus",
            "Rickets",
            "Tetany",
            "Goiter",
            "Anemia",
            "Beriberi",
            "Pellagra",
            "Scurvy",
            "Malnutritions"
        ]
    class SIMULATION:
        ARENA_SIZE = (1024, 1024)                       # PIXEL -> xw100 x h100 Pixel
        MAX_DAYS = 50                                  # DAY -> Number of iteration to simulate

        INITIAL_MEATS = 8                              # PIECE -> Number Of Meats that will spawn initially at day 0
        MEAT_CHANGE_PER_DAY = +1                         # PIECE -> Number of food to add or
                                                        #          remove each day / iteration
        MEAT_FOOD_POINTS = 2                            # UNIT -> Food Points per Meat

        INITIAL_DOVE = 5
        INITIAL_HAWK = 5

        class ENTITY:
            SELF_MEET_HAWK_PORTION = 0                  # PERCENT -> My Portion if i meet another hawk >:(
            SELF_MEET_DOVE_PORTION = 0                  # PERCENT -> My Portion if i meet dove >:(
            SELF_PORTION = 0                            # PERCENT -> My Portion if i eat alone :(

            SURVIVAL_CHANCES_PER_ONE_FOOD = 0           # PERCENT
            REPRODUCE_CHANCES_PER_ONE_FOOD = 0          # PERCENT

            SURVIVAL_HUNGER_THRESHOLD = 0               # Unit -> Survival will not be calculated if hunger is
                                                        #         not past this point. or simply die
            REPRODUCE_HUNGER_THRESHOLD = 0              # Unit -> Reproduction Chances will not be calculated if
                                                        #         hunger is not past this point.
                                                        #         or simply wont have baby

        class DOVE:     # Hyena
            SELF_MEET_DOVE_PORTION = 50                 # PERCENT -> My Portion if i meet another dove :)
            SELF_MEET_HAWK_PORTION = 25                 # PERCENT -> My Portion if i meet hawk >:(
            SELF_PORTION = 100                          # PERCENT -> My Portion if i eat alone :(

            SURVIVAL_CHANCES_PER_ONE_FOOD = 100         # PERCENT -> Chances of Survivability per one point of food
            REPRODUCE_CHANCES_PER_ONE_FOOD = 50         # PERCENT -> Chances to reproduce per one point of food

            # SURVIVAL_HUNGER_THRESHOLD = 0.5           # UNIT -> Survival will not be calculated if hunger is
                                                        #         not past this point. or simply die
            REPRODUCE_HUNGER_THRESHOLD = 1.0            # UNIT -> Reproduction Chances will not be calculated if
                                                        #         hunger is not past this point.
                                                        #         or simply wont have baby

        class HAWK:     # Lion
            SELF_MEET_HAWK_PORTION = 50                 # PERCENT -> My Portion if i meet another hawk >:(
            SELF_MEET_DOVE_PORTION = 75                 # PERCENT -> My Portion if i meet dove >:(
            SELF_PORTION = 100                          # PERCENT -> My Portion if i eat alone :(

            SURVIVAL_CHANCES_PER_ONE_FOOD = 50          # PERCENT
            REPRODUCE_CHANCES_PER_ONE_FOOD = 50         # PERCENT 33.333334

            # SURVIVAL_HUNGER_THRESHOLD = 1.0           # Unit -> Survival will not be calculated if hunger is
                                                        #         not past this point. or simply die
            REPRODUCE_HUNGER_THRESHOLD = 1.0            # Unit -> Reproduction Chances will not be calculated if
                                                        #         hunger is not past this point.
                                                        #         or simply wont have baby
