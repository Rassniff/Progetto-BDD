console.log('planner.js caricato.');

const plannerDiv = document.getElementById('planner-data');
const plannerData = JSON.parse(plannerDiv.dataset.planner);
const userId = JSON.parse(plannerDiv.dataset.userId);

const giorni = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica'];
const giorniAbbrev = ['Lun', 'Mar', 'Mer', 'Gio', 'Ven', 'Sab', 'Dom'];
const pasti = ['colazione', 'pranzo', 'merenda', 'cena'];

const cells = document.querySelectorAll('.cell');

// Attiva drag & drop sulle celle
cells.forEach(cell => {
  cell.addEventListener('dragover', e => {
    e.preventDefault();
    cell.classList.add('dragover');
  });
  cell.addEventListener('dragleave', () => cell.classList.remove('dragover'));
  cell.addEventListener('drop', handleDrop);
});

// Piatti trascinabili
const piatti = document.querySelectorAll('#piatti-list li');
piatti.forEach(piatto => {
  piatto.setAttribute('draggable', true);
  piatto.addEventListener('dragstart', handleDragStart);
});

// Popola celle esistenti dal plannerData (array di dati dal backend)
// plannerData = [[data, pasto, piatto_id, nome_piatto], ...]
plannerData.forEach(entry => {
  const data = new Date(entry.data);
  const dayIndex = data.getDay(); //conversione 0=Dom, 1=Lun,... a indice 0=Lun per giorni array
  
  const giorno = giorni[(dayIndex + 6) % 7];
  const pasto = entry.pasto;
  const piatto = entry.nome;

  const cell = document.querySelector(`.cell[data-giorno="${giorno}"][data-pasto="${pasto}"]`);
  if (cell) {
  cell.setAttribute('data-data', entry.data); // salva la data nella cella
  const p = document.createElement('p');
  p.textContent = piatto;

  const btn = document.createElement('button');
  btn.textContent = '✖';
  btn.className = 'remove-btn';
  btn.style.marginLeft = '8px';
  btn.onclick = function(e) {
    e.stopPropagation();
    p.remove();
    btn.remove();
    fetch('/remove-from-planner', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        data: entry.data,
        pasto: entry.pasto,
        piatto_id: entry.piatto_id
      })
    });
  };

  p.appendChild(btn);
  cell.appendChild(p);
}
});

let draggedPiattoId = null;
let draggedPiattoName = '';

// Funzioni drag & drop
function handleDragStart(e) {
  draggedPiattoId = this.dataset.id;
  draggedPiattoName = this.textContent;
}

// Gestione drop
function handleDrop(e) {
  e.preventDefault();
  this.classList.remove('dragover');

  const giornoLungo = this.dataset.giorno;
  const pasto = this.dataset.pasto;
  const giornoIndex = giorni.indexOf(giornoLungo);
  const giorno = giorniAbbrev[giornoIndex];

  const today = new Date();
  const startOfWeek = new Date(today);
  startOfWeek.setDate(today.getDate() - today.getDay() + 1); // Lunedì
  const dataDate = new Date(startOfWeek);
  dataDate.setDate(startOfWeek.getDate() + giornoIndex);
  const dataStr = dataDate.toISOString().slice(0, 10);

  this.setAttribute('data-data', dataStr);

  // Fai la chiamata fetch per salvare nel DB
  fetch('/add-to-planner', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      giorno: giorno,
      pasto: pasto,
      piatto_id: draggedPiattoId
    })
  })
  .then(response => response.json())
  .then(data => {
    if (data.success) {
      this.setAttribute('data-data', data.data_giorno);

      const p = document.createElement('p');
      p.textContent = draggedPiattoName;

      const btn = document.createElement('button');
      btn.textContent = '✖';
      btn.className = 'remove-btn';
      btn.style.marginLeft = '8px';

      btn.onclick = () => {
        p.remove();
        btn.remove();
        fetch('/remove-from-planner', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            data: data.data_giorno,  // la data corretta dal backend
            pasto: pasto,
            piatto_id: data.piatto_id  // usa ID corretto
          })
        });
      };

      p.appendChild(btn);
      this.appendChild(p);

      console.log('Piatto aggiunto con successo');
    } else {
      alert('Errore: ' + data.message);
    }
  })
  .catch(err => {
    alert('Errore di connessione');
    console.error(err);
  });
}



