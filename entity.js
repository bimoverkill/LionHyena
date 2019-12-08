class Entity {
    constructor(pos_x, pos_y) {
        // Basic Property
        this.icon = "assets/default_entity.png";
        this.hue = {
            r: random(255),
            g: random(255),
            b: random(255)
        }
        this.pos = {
            x: pos_x,
            y: pos_y
        }
        
        // Behavior
        this.finder = null;
        this.icon_path = config.behavior.default.icon;
        this.view_distance = 0;
        this.minimum_food = 0;
        this.reproduction = {
            full: 0,
            half: 0
        }

        // Initialize Path finding
        if(config.map.pathfinding_algorithm == 'random') {
            algo = [
                pathfinding_algorithm.astar,
                pathfinding_algorithm.best_first,
                pathfinding_algorithm.breadth_first,
                pathfinding_algorithm.dijkstra,
                pathfinding_algorithm.jumppoint,
                pathfinding_algorithm.orthogonal,
                pathfinding_algorithm.biastar,
                pathfinding_algorithm.bibestfirst,
                pathfinding_algorithm.bibreadthfirst,
                pathfinding_algorithm.bidijkstra
            ]
            this.pathfinder = new (random(algo))();
        } else {
            this.pathfinder = (config.map.default_pathfinding_algorithm)();
        }
    }

    load_image() {
        console.log("Loading : " + this.icon_path);
        try {
            this.icon = loadImage(this.icon_path);
        } catch (Exception) {
            console.log("Failed to load file : " + this.icon_path)
        }
    }

    draw() {
        push();
        
        strokeWeight(1);
        rect(this.pos.x, this.pos.y, 24, 24);
        if(this.icon !== null){
            image(this.icon, this.pos.x, this.pos.y, this.icon.width, this.icon.height);
        }
        fill(this.hue.r, this.hue.g, this.hue.b, 0.2);

        pop();
    }
}