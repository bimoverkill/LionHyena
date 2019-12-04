var pathfinding_algorithm = {
    astar: PF.AStarFinder,
    best_first: PF.BestFirstFinder,
    breadth_first: PF.BreadthFirstFinder,
    dijkstra: PF.DijkstraFinder,
    jumppoint: PF.JumpPointFinder,
    orthogonal: PF.OrthogonalJumpPointFinder,
    biastar: PF.BiAStarFinder,
    bibestfirst: PF.BiBestFirstFinder,
    bibreadthfirst: PF.BiBreadthFirstFinder,
    bidijkstra: PF.BiDijkstraFinder
}
var config = {
    food_generation: {
        meat_per_day: 8,
        meat_increase_per_day: 4,
        food_points_per_meat: 2
    },
    map: {
        // Available Pathfinding Algorithm
        // astar
        // best_first
        // breadth_first
        // dijkstra
        // jumppoint
        // orthogonal
        // biastar
        // bibestfirst
        // bibreadthfirst
        // bidijkstra
        // random
        default_pathfinding_algorithm: pathfinding_algorithm.astar, 
    },
    behavior: {
        lion: {
            icon: "assets/lion.png",
            view_distance: 3,
            minimum_food: 1,
            reproduction: {
                full: 1.5,
                half: 1
            }
        },
        hyena: {
            icon: "assets/hyena.png",
            view_distance: 3,
            minimum_food: 0.5,
            reproduction: {
                full: 1,
                half: 0.5
            }
        }
    }
}