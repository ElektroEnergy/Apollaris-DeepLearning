searchByAddress();

var latGlobal = null
var lngGlobal = null

// Cria o mapa centralizado (exemplo: São Paulo)
const map = L.map('map').setView([-23.5505, -46.6333], 13);
let marker = L.marker([-23.5505, -46.6333]).addTo(map);

// Adiciona o mapa base do OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contribuidores'
}).addTo(map);

// Elemento de texto para mostrar as coordenadas
const latlng = document.querySelector('#latlng');

map.on('click', async (e) => {
  const { lat, lng } = e.latlng;
  const url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}&addressdetails=1`;

  try {
    const res = await fetch(url, { headers: { 'User-Agent': 'LeafletExampleApp' } });
    const data = await res.json();

    const address = document.getElementById('address');
    address.value = data.display_name;

    marker.setLatLng([lat, lng]);
    map.flyTo([lat, lng], 15, { animate: true, duration: 1.2 });

    latGlobal = lat
    lngGlobal = lng

    latlng.textContent = `${lat.toFixed(4)}, ${lng.toFixed(4)}`
  } catch (err) {
    console.error(err);
    alert('Erro!');
  }
});

// Busca endereço ao clicar no botão
async function searchByAddress() {
  const address = document.getElementById('address').value.trim();
  if (!address) return alert("Digite um endereço!");

  const url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(address)}&addressdetails=1&limit=1`;

  try {
    const res = await fetch(url, { headers: { 'User-Agent': 'LeafletExampleApp' } });
    const data = await res.json();

    if (data.length === 0) {
      infoBox.textContent = "Endereço não encontrado.";
      return;
    }

    const loc = data[0];
    const lat = parseFloat(loc.lat);
    const lng = parseFloat(loc.lon);

    marker.setLatLng([lat, lng]);
    map.flyTo([lat, lng], 15, { animate: true, duration: 1.2 });

    latGlobal = lat
    lngGlobal = lng

    latlng.textContent = `${lat.toFixed(4)}, ${lng.toFixed(4)}`

  } catch (err) {
    console.error(err);
    infoBox.textContent = "Erro ao buscar endereço.";
  }
};

document.getElementById('search').addEventListener('click', async () => { searchByAddress() });
