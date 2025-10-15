var demanda = null;

document.getElementById('submeterDemanda').addEventListener('click', async () => {
    demanda = document.getElementById('demandaInput').value;
    document.getElementById('sitedemanda').textContent = demanda + 'W';
});