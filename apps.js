function setup() {
    createCanvas(windowWidth, windowHeight);
    frameRate(60);
}

function draw() {
    background(255);

    
    fill(0, 0, 255);
    noStroke();
    ellipse(mouseX, mouseY, 50, 50);
}