document.getElementById('open-create-piatto-modal').onclick = function() {
  document.getElementById('create-piatto-modal').style.display = 'block';
  fetch('/ingredienti-list')
    .then(res => res.json())
    .then(data => {
      const listDiv = document.getElementById('ingredienti-list');
      listDiv.innerHTML = '';
      data.forEach(ing => {
        listDiv.innerHTML += `
          <label>
            <input type="checkbox" name="ingredienti" value="${ing.id}">
            ${ing.nome} (${ing.unita_misura})
            <input type="number" name="quantita_${ing.id}" min="0" placeholder="Quantità">
          </label><br>
        `;
      });
    });
};

//gestore apertura chiusura modal della creazione piatto
document.getElementById('close-create-piatto-modal').onclick = function() {
  document.getElementById('create-piatto-modal').style.display = 'none';
};

document.getElementById('create-piatto-form').onsubmit = function(e) {
  e.preventDefault();
  const form = e.target;
  const nome = form.nome.value;
  const descrizione = form.descrizione.value;
  const ingredienti = [];
  form.querySelectorAll('input[type="checkbox"][name="ingredienti"]:checked').forEach(cb => {
    const quantita = form[`quantita_${cb.value}`].value;
    ingredienti.push({ id: cb.value, quantita: quantita });
  });
  fetch('/crea-piatto', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nome, descrizione, ingredienti })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      alert('Piatto creato!');
      document.getElementById('create-piatto-modal').style.display = 'none';
      location.reload();
    } else {
      alert('Errore: ' + data.message);
    }
  });
};

//gestione apertura e chiusura modal crea nuovo ingrediente
document.getElementById('open-add-ingrediente-modal').onclick = function() {
  document.getElementById('add-ingrediente-modal').style.display = 'block';
};
document.getElementById('close-add-ingrediente-modal').onclick = function() {
  document.getElementById('add-ingrediente-modal').style.display = 'none';
};
document.getElementById('add-ingrediente-form').onsubmit = function(e) {

  e.preventDefault();
  e.stopPropagation(); // Previene bubbling verso altri form
  console.log('Submit ingrediente');
  const form = e.target;
  const data = {
    nome: form.nome.value.trim(),
    unita_misura: form.unita_misura.value.trim(),
    proteine: form.proteine.value !== '' ? parseFloat(form.proteine.value) : 0,
    carboidrati: form.carboidrati.value !== '' ? parseFloat(form.carboidrati.value) : 0,
    calorie: form.calorie.value !== '' ? parseFloat(form.calorie.value) : 0
  };
  if (!data.nome || !data.unita_misura) {
    alert('Compila tutti i campi obbligatori!');
    return;
  }
  fetch('/aggiungi-ingrediente', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(result => {
    if (result.success) {
      document.getElementById('add-ingrediente-modal').style.display = 'none';
      // Aggiorna la lista ingredienti nel modal piatto SENZA riaprire il modal
      fetch('/ingredienti-list')
        .then(res => res.json())
        .then(data => {
          const listDiv = document.getElementById('ingredienti-list');
          listDiv.innerHTML = '';
          data.forEach(ing => {
            listDiv.innerHTML += `
              <label>
                <input type="checkbox" name="ingredienti" value="${ing.id}">
                ${ing.nome} (${ing.unita_misura})
                <input type="number" name="quantita_${ing.id}" min="0" placeholder="Quantità">
              </label><br>
            `;
          });
        });
      alert('Ingrediente aggiunto!');
    } else {
      alert('Errore: ' + result.message);
    }
  });
};