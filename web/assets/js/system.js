let model, scalers, encoders;

buttonRunPrediction = document.getElementById('runPrediction');
buttonRunPrediction.addEventListener('click', async () => { runPrediction() });

async function loadAll() {
    model = await tf.loadLayersModel("web_model/model.json");
    scalers = await fetch("web_model/scalers.json").then(r => r.json());
    encoders = await fetch("web_model/encoders.json").then(r => r.json());
    console.log("Modelo e normalizadores carregados.");
}

function normalizeX(x) {
    return x.map((v, i) => {
        console.log(scalers.x);
        const mean = Number(scalers.x.mean[i]);
        const scale = Number(scalers.x.scale[i]);

        return scale !== 0 ? (v - mean) / scale : 0;
    });
}

function denormalizeY(y_norm_array) {
    return y_norm_array.map(row => {
        const denorm = [];

        console.log(row[0]);
        denorm.push(row[0] * (scalers.y.power.max[0] - scalers.y.power.min[0]) + scalers.y.power.min[0]);
        denorm.push(row[1] * (scalers.y.nmod.max[0] - scalers.y.nmod.min[0]) + scalers.y.nmod.min[0]);
        denorm.push(row[2] * (scalers.y.ninv.max[0] - scalers.y.ninv.min[0]) + scalers.y.ninv.min[0]);
        denorm.push(row[3] * (scalers.y.total_ipmd.max[0] - scalers.y.total_ipmd.min[0]) + scalers.y.total_ipmd.min[0]);
        denorm.push(row[4] * (scalers.y.total_ipinv.max[0] - scalers.y.total_ipinv.min[0]) + scalers.y.total_ipinv.min[0]);
        denorm.push(row[5] * (scalers.y.ipsys.max[0] - scalers.y.ipsys.min[0]) + scalers.y.ipsys.min[0]);

        console.log(denorm);
        return denorm;
    });
}

async function runPrediction() {
    const modules = await fetch("data/modules.json").then(r => r.json());
    const inverters = await fetch("data/inverters.json").then(r => r.json()); 

    if (siteParams == null) {
        updateParams(latGlobal, lngGlobal)
    }

    const f0 = parseFloat(demanda);
    const f1 = parseFloat(siteParams.irr.mean);
    const f2 = parseFloat(siteParams.temp.mean);
    const f3 = parseFloat(siteParams.wind.mean);
    const x = [f0, f1, f2, f3];
    console.log(x)

    const x_norm = normalizeX(x);
    const inputTensor = tf.tensor2d([x_norm]);

    const y_preds = await model.predict(inputTensor);
    // y_preds é array de tensors para cada saída

    // Classificação: módulo e inversor
    const moduleTensor = y_preds[0];
    const inverterTensor = y_preds[1];

    const moduleIdx = moduleTensor.argMax(-1).dataSync()[0];
    const inverterIdx = inverterTensor.argMax(-1).dataSync()[0];

    // Regressões normais: power, nmod, ninv, ipmd, ipin, ipsys
    const otherTensors = y_preds.slice(2);
    const otherNorm = await Promise.all(otherTensors.map(t => t.data()));
    // otherNorm será um array de arrays: e.g. [ [power_norm], [nmod_norm], ... ]

    // Organizar como filas por amostra
    const numOutputs = otherNorm.length;
    const rowNorm = [];
    for (let i = 0; i < numOutputs; i++) {
        rowNorm.push(otherNorm[i][0]);
    }
    const y_norm_array = [rowNorm];
    const y_denorm = denormalizeY(y_norm_array)[0];

    // Montar texto
    const moduleId = encoders.module[moduleIdx];
    const inverterId = encoders.inverter[inverterIdx];

    const module = modules.modules.find(m => m.id === moduleId);
    const inverter = inverters.inverters.find(i => i.id === inverterId);

    outputModule = document.getElementById("outputModule");
    outputInverter = document.getElementById("outputInverter");
    outputModule.textContent = `${module.name}`;
    outputInverter.textContent = `${inverter.name}`;

    outputPower = document.getElementById("outputPower");
    outputPower.textContent = `${y_denorm[0].toFixed(2)}W`;

    outputNmod = document.getElementById("outputNmod");
    outputNmod.textContent = `${y_denorm[1].toFixed(0)} Módulos`;

    outputNinv = document.getElementById("outputNinv");
    outputNinv.textContent = `${y_denorm[2].toFixed(0)} Inversores`;

    outputIpmd = document.getElementById("outputIpmd");
    outputIpmd.textContent = `${y_denorm[3].toFixed(6)}`;

    outputIpinv = document.getElementById("outputIpinv");
    outputIpinv.textContent = `${y_denorm[4].toFixed(6)}`;

    outputIpsys = document.getElementById("outputIpsys");
    outputIpsys.textContent = `${y_denorm[5].toFixed(6)}`;

    // Modules and others
    moduleName = document.getElementById("moduleName");
    moduleName.textContent = module.name;

    modulePmp = document.getElementById("modulePmp");
    modulePmp.textContent = `${module.pmp}W`;

    moduleVmp = document.getElementById("moduleVmp");
    moduleVmp.textContent = `${module.vmp}V`;

    moduleImp = document.getElementById("moduleImp");
    moduleImp.textContent = `${module.imp}A`;
    
    moduleVoc = document.getElementById("moduleVoc");
    moduleVoc.textContent = `${module.voc}V`;

    moduleIsc = document.getElementById("moduleIsc");
    moduleIsc.textContent = `${module.isc}A`;

    moduleDur = document.getElementById("moduleDur");
    moduleDur.textContent = `${module.dur} anos`;

    moduleEf = document.getElementById("moduleEf");
    moduleEf.textContent = `${module.ef}%`;

    inverterName = document.getElementById("inverterName");
    inverterName.textContent = inverter.name;

    inverterPot = document.getElementById("inverterPot");
    inverterPot.textContent = `${inverter.pdc}W`;

    inverterNmppts = document.getElementById("inverterNmmpts");
    inverterNmppts.textContent = `${inverter.nmmpts}`;

    inverterIsc = document.getElementById("inverterIsc");
    inverterIsc.textContent = `${inverter.isc}A`;

    inverterVmpdelta = document.getElementById("inverterVmpdelta");
    inverterVmpdelta.textContent = `${inverter.vmpmin}V - ${inverter.vmpmax}V`;

    inverterEf = document.getElementById("inverterEf");
    inverterEf.textContent = `${inverter.ef}%`;
}

loadAll();