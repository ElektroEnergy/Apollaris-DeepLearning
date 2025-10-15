projetoMain = document.getElementById('projeto')
demandaMain = document.getElementById('demanda')
sistemaMain = document.getElementById('sistema')
var page = null

navProjeto = document.getElementById('navProjeto');
navDemanda = document.getElementById('navDemanda');
navSistema = document.getElementById('navSistema');

navProjeto.addEventListener('click', async () => { pageProjeto() });
navDemanda.addEventListener('click', async () => { pageDemanda() });
navSistema.addEventListener('click', async () => { pageSistema() });


function pageProjeto() {
    page = 1
    projetoMain.style.display = 'block';
    demandaMain.style.display = 'none';
    sistemaMain.style.display = 'none';

    navProjeto.classList.add('active'); 
    navDemanda.classList.remove('active');
    navSistema.classList.remove('active'); 
}

function pageDemanda() {
    page = 2
    projetoMain.style.display = 'none';
    demandaMain.style.display = 'block';
    sistemaMain.style.display = 'none';

    navProjeto.classList.remove('active'); 
    navDemanda.classList.add('active');
    navSistema.classList.remove('active'); 
}

function pageSistema() {
    if (demanda == null) {
        alert('Você precisa primeiro inserir a demanda antes de prosseguir com o projeto!')
        return 0;
    }

    page = 3
    projetoMain.style.display = 'none';
    demandaMain.style.display = 'none';
    sistemaMain.style.display = 'block';

    navProjeto.classList.remove('active'); 
    navDemanda.classList.remove('active');
    navSistema.classList.add('active'); 
}

pageProjeto()