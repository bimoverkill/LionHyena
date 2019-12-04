class Arena {
    constructor(map_width, map_height, cell_size){
        this.map_size = {
            width: map_width,
            height: map_height
        };
        this.cell_size = cell_size;

        this.grid = new PF.Grid(24, 24);
    }
    
    drawGrid() {
        push();
        for(let y=0; y<this.map_size.height; y+=24){
            for(let x=0; x<this.map_size.width; x+=24){
                fill(255, 0);
                rect(x, y, 24, 24);
            }
        }
        pop();
    }
}