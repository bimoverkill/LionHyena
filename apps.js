let lion1;
function setup() {
    createCanvas(windowWidth, windowHeight);
    frameRate(60);

    lion1 = new Lion(100, 100);
    lion1.load_image();
}

function draw() {
    background(255);
    lion1.draw();
}