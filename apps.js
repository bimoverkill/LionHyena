let arena;

function setup() {
    createCanvas(windowWidth, windowHeight);
    frameRate(60);

    arena = new Arena(windowWidth, windowHeight, 24);
}

function draw() {
    background(255);
    arena.drawGrid();
}