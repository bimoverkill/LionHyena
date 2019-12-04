class Entity {
    constructor(pos_x, pos_y) {
        // Basic Property
        this.icon = null;
        this.pos = {
            x: pos_x,
            y: pos_y
        }
        
        // Behavior
        this.icon_path = config.behavior.default.icon;
        this.draw_color = {
            r: 255,
            g: 0,
            b: 255
        }
        this.view_distance = 0;
        this.minimum_food = 0;
        this.reproduction = {
            full: 0,
            half: 0
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
        fill(this.draw_color.r, this.draw_color.g, this.draw_color.b);
        rect(this.pos.x, this.pos.y, 24, 24);
        if(this.icon !== null){
            image(this.icon, this.pos.x, this.pos.y, this.icon.width, this.icon.height);
        }

        pop();
    }
}

class Lion extends Entity {
    constructor(pos_x, pos_y){
        super();
        this.icon = null;
        super.pos = {
            x: pos_x,
            y: pos_y
        }

        // Behavior
        this.icon_path = config.behavior.lion.icon;
        super.draw_color = config.behavior.lion.draw_color;
        super.view_distance = config.behavior.lion.view_distance;
        super.minimum_food = config.behavior.lion.minimum_food;
        super.reproduction = config.behavior.lion.reproduction;
    }
}