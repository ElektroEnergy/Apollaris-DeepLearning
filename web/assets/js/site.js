var siteParams = null;

async function getNasaPowerData(lat, lon) {
  const baseUrl = "https://power.larc.nasa.gov/api/temporal/climatology/point";
  const parameters = ["ALLSKY_SFC_SW_DWN", "WS10M", "T2M"];
  const url = `${baseUrl}?latitude=${lat}&longitude=${lon}&parameters=${parameters.join(",")}&community=RE&format=JSON`;

  const response = await fetch(url);
  if (!response.ok) throw new Error("Erro ao consultar API da NASA POWER");
  const json = await response.json();

  const params = json.properties.parameter;
  const months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"];

  function calcAnnualMean(obj) {
    const values = months.map(m => obj[m]).filter(v => typeof v === "number");
    return values.reduce((a, b) => a + b, 0) / values.length;
  }

  const results = {
    latitude: lat,
    longitude: lon,
    irr: {
      unit: "W/m² (média mensal de radiação solar incidente na superfície)",
      montly: months.reduce((acc, m) => { acc[m] = ((params.ALLSKY_SFC_SW_DWN[m] * 1000) / 24) + 850; return acc; }, {}),
      mean: ((calcAnnualMean(params.ALLSKY_SFC_SW_DWN) * 1000) / 24) + 850
    },
    wind: {
      unit: "m/s (média montly da velocidade do vento a 10 m)",
      montly: months.reduce((acc, m) => { acc[m] = params.WS10M[m]; return acc; }, {}),
      mean: calcAnnualMean(params.WS10M)
    },
    temp: {
      unit: "°C (média montly da temperatura a 2 m)",
      montly: months.reduce((acc, m) => { acc[m] = params.T2M[m]; return acc; }, {}),
      mean: calcAnnualMean(params.T2M)
    }
  };

  console.log('Resultados obtidos!');
  siteParams = results;
}

async function updateParams(lat, lon) {
  results = await getNasaPowerData(lat, lon);

  document.getElementById('siteirr').textContent = siteParams.irr.mean.toFixed(2) + 'Wh/m²';
  document.getElementById('sitewind').textContent = siteParams.wind.mean.toFixed(2) + 'm/s';
  document.getElementById('sitetemp').textContent = siteParams.temp.mean.toFixed(2) + 'ºC';

  traceTemp(siteParams.temp.montly)
  
}

document.getElementById('obtersite').addEventListener('click', async () => { updateParams(latGlobal, lngGlobal) });


function traceIrr(irrMontly) {
  var trace1 = {
  x: ["JAN","FEV","MAR","ABR","MAI","JUN","JUL","AGO","SET","OUT","NOV","DEZ"],
  y: Object.values(irrMontly),
  type: 'scatter'
  };

  var data = [trace1];
  document.getElementById('graph1controls').style.display = 'block';
  document.getElementById('graph1title').textContent = 'Gráfico de Irradiação Solar';


  Plotly.newPlot('graph1', data);
}

function traceWind(windMontly) {
  var trace1 = {
  x: ["JAN","FEV","MAR","ABR","MAI","JUN","JUL","AGO","SET","OUT","NOV","DEZ"],
  y: Object.values(windMontly),
  type: 'scatter'
  };

  var data = [trace1];
  document.getElementById('graph1controls').style.display = 'block';
  document.getElementById('graph1title').textContent = 'Gráfico de Velocidade do Vento';

  Plotly.newPlot('graph1', data);
}

function traceTemp(tempMontly) {
  var trace1 = {
  x: ["JAN","FEV","MAR","ABR","MAI","JUN","JUL","AGO","SET","OUT","NOV","DEZ"],
  y: Object.values(tempMontly),
  type: 'scatter'
  };

  var data = [trace1];
  document.getElementById('graph1controls').style.display = 'block';
  document.getElementById('graph1title').textContent = 'Gráfico de Temperatura';

  Plotly.newPlot('graph1', data);
}

document.getElementById('traceirr').addEventListener('click', async () => { traceIrr(siteParams.irr.montly) });
document.getElementById('tracewind').addEventListener('click', async () => { traceWind(siteParams.wind.montly) });
document.getElementById('tracetemp').addEventListener('click', async () => { traceTemp(siteParams.temp.montly) });
