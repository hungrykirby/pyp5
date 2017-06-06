const N = 20;

let p_x = [];
let p_y = [];
let p_pX = [];
let p_pY = [];

let p_distances = [];
let p_gap_theata = [];

let p_colors = [];

let p_frameCount;

function setup(){
  let canvas = createCanvas(windowWidth, windowHeight);
  //console.log(canvas);
  canvas.parent("p5Canvas");
  background(255);

  colorMode(HSB, 255, 100, 100);

  p_frameCount = 0;
  noStroke();

  for(var i = 0; i < N; i++){
    p_x.push(30);
    p_pX.push(30);
    p_y.push(30);
    p_pY.push(30);
    p_distances.push(random(15, 150));
    p_gap_theata.push(random(-PI, PI));

    p_colors.push(color(random(255), 100, 100));
  }
}
function draw(){
  colorMode(RGB, 255);
  background(255);
  colorMode(HSB, 255, 100, 100);
  for(var i = 0; i < N; i++){
    fill(p_colors[i]);
    var theata = radians(p_frameCount*5.0) + p_gap_theata[i];
    var dist =p_distances[i] + 90.0*noise(theata/1.0, p_frameCount/100.0)
    p_x[i] = (mouseX + dist*cos(theata) + p_pX[i])/2.0;
    p_y[i] = (mouseY + dist*sin(theata) + p_pY[i])/2.0;
    ellipse(p_x[i], p_y[i], 20, 20);
    p_pX[i] = p_x[i];
    p_pY[i] = p_y[i];
  }
  p_frameCount++;
}
