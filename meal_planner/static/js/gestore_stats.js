// Statistiche giorno selezionato
document.getElementById('stats-day-btn').onclick = function() {
  if (!giornoSelezionato) {
    alert('Seleziona un giorno dalla intestazione della griglia!');
    return;
  }
  fetch(`/stats-day?date=${giornoDataSelezionata}`)
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        document.getElementById('stats-result').innerHTML =
          `<b>Giorno ${giornoSelezionato} (${giornoDataSelezionata})</b><br>
          Proteine: ${data.proteine.toFixed(2)} g<br>
          Carboidrati: ${data.carboidrati.toFixed(2)} g<br>
          Calorie: ${data.calorie.toFixed(2)} kcal`;
      } else {
        document.getElementById('stats-result').innerHTML = 'Nessun dato.';
      }
    });
};

document.getElementById('stats-week-btn').onclick = function() {
  const start = document.getElementById('stats-week-start').value;
  const end = document.getElementById('stats-week-end').value;
  if (!start || !end) {
    alert('Seleziona le date di inizio e fine settimana!');
    return;
  }
  fetch(`/stats-week?start=${start}&end=${end}`)
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        document.getElementById('stats-result').innerHTML =
          `<b>Settimana ${start} - ${end}</b><br>
          Proteine: ${data.proteine.toFixed(2)} g<br>
          Carboidrati: ${data.carboidrati.toFixed(2)} g<br>
          Calorie: ${data.calorie.toFixed(2)} kcal`;
      } else {
        document.getElementById('stats-result').innerHTML = 'Nessun dato.';
      }
    });
};
// --- Selezione giorno dalla griglia ---
let giornoSelezionato = null;
let giornoDataSelezionata = null;

const weekdayMap = {
  'Lunedì': 0,
  'Martedì': 1,
  'Mercoledì': 2,
  'Giovedì': 3,
  'Venerdì': 4,
  'Sabato': 5,
  'Domenica': 6
};

function getDateForWeekday(weekday) {
  const today = new Date();
  const startOfWeek = new Date(today);
  startOfWeek.setDate(today.getDate() - today.getDay() + 1); // Lunedì
  const giornoIndex = weekdayMap[weekday];
  const giornoDate = new Date(startOfWeek);
  giornoDate.setDate(startOfWeek.getDate() + giornoIndex);
  return giornoDate.toISOString().slice(0, 10);
}

// Evidenzia la cella selezionata e salva il giorno
document.querySelectorAll('.giorno-header').forEach(cell => {
  cell.addEventListener('click', function() {
    if (this.classList.contains('selected-cell')) {
      // Se già selezionata, deseleziona e azzera variabili
      this.classList.remove('selected-cell');
      giornoSelezionato = null;
      giornoDataSelezionata = null;
    } else {
      // Deseleziona tutte e seleziona questa
      document.querySelectorAll('.giorno-header').forEach(c => c.classList.remove('selected-cell'));
      this.classList.add('selected-cell');
      giornoSelezionato = this.getAttribute('data-giorno');
      giornoDataSelezionata = getDateForWeekday(giornoSelezionato);
    }
  });
});

// Statistiche giorno selezionato
document.getElementById('stats-day-btn').onclick = function() {
  if (!giornoSelezionato || !giornoDataSelezionata) {
    alert('Seleziona un giorno dalla intestazione della griglia!');
    return;
  }
  fetch(`/stats-day?date=${giornoDataSelezionata}`)
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        document.getElementById('stats-result').innerHTML =
          `<b>Giorno ${giornoSelezionato} (${giornoDataSelezionata})</b><br>
          Proteine: ${data.proteine.toFixed(2)} g<br>
          Carboidrati: ${data.carboidrati.toFixed(2)} g<br>
          Calorie: ${data.calorie.toFixed(2)} kcal`;
      } else {
        document.getElementById('stats-result').innerHTML = 'Nessun dato.';
      }
    });
};

