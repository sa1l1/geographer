let chart;



const xy = [document.getElementById("userInputx").value, document.getElementById("userInputy").value];

function setup() {
  createCanvas(400, 400);

  dataX = [x[0]]
  dataY = [x[1]]
  data = []

  colors = ['#ff0000', '#5649ff']

  lineLabels = ["Infected", "Healthy"]

  for(let i = 0; i < dataX.length; i++) {
    data.push([])
    for(let j = 0; j < dataX[i].length; j++) {
      data[i].push(createVector(dataX[i][j], dataY[i][j]))
    }
  }

  chart = new LineChart(data, colors, lineLabels, 250, 250, 5, 5, [min(dataX.flat()), max(dataX.flat())], [0, 200]);
  //[min(dataY.flat()), max(dataY.flat())]
}

function draw() {
  background(220);
  chart.show()
}