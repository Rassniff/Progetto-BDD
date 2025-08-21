# Progetto-BDD INFO PROGETTO

# Ambiente virtuale python
venv\Scripts\activate --> oppure deactivate
python app.py --> per runnare il backend

# Funzionamento Flask (framework backend)
Gestisce richieste HTTP - Parla con il db
Browser ⟶ GET /piatti ⟶ Flask ⟶ SELECT * FROM piatti ⟶ MySQL
Risposta: MySQL → Flask → HTML/JSON → Browser

# Funzionamento MySql Workbench (DBSM)
Db in locale --> modifica del file init_db.sql --> run script sql su MySql Workbench
In seguito creazione dello schema...

# Funzionamento Frontend (flask + html + css + js)
Flask genera pagine HTML dal server.
Tu crei file .html in una cartella templates/.
Dentro i file .html puoi usare Jinja2, che ti permette di inserire variabili Python nel codice HTML.
Funzionalità come drag and drop / logica bottoni ecc in JavaScript (come nel progetto dell'API)

-----------------------------------------------------------------------------------------
# INIZIO PROGETTO

# Progettazione db

--Ingrediente(nome/unità di misura) #
--Piatti # sia pubblici che privati (per utente) 1 di default per piatti pubblici con utende_id NULL, 0 per piatto privato con utente_id settato
--Piatti_Ingredienti #
--Utenti # 
--Planner #

# Frontend + Backend

--Gestione utenza 
# route backend + file python /models/utenti.py con le query + html e css

--Aggiungere cambio password e recupera password e validazione email 

--Pagina principale (sx lista di tutti i piatti disponibili) (dx calendario) 
# html e css responsive (2 div centrali) 

--Aggiunta piatto globale al planner(griglia) con drag and drop 
# route backend per l'aggiunta + file python /models/planner.py con le query + file js per il drag and drop + html e css(tabella/griglia)

--Rimozione di un piatto dal planner(griglia) con bottone 
# route backend per la rimozione + file python /models/planner.py con le query + file js per bottone di rimozione + html e css(bottone)

--Aggiunta piatto privato (se non c'è l'ingrediente giusto lo aggiungo (globale)) 
# sia il piatto che ingrediente privati o pubblici in base a a una flag

--Gestione indici in fase di inserimento e rimozione(opzionale)(intendo l'ordine dell'id)

--Pagina stats con filtri su proteine/carbo giornalieri o settimanali (calcolo quantità x percentuale di proteine/carbo)
# fatta giornaliera e settimanale

--Migliorare estetica , progettarlo in orrizzontale non in verticale

--bottone che toglie tutti i piatti nella griglia




//LEGGENDA
# Completato
-- Da fare







// Evidenzia la cella selezionata e salva il giorno
document.querySelectorAll('.giorno-header').forEach(cell => {
  cell.addEventListener('click', function() {
    document.querySelectorAll('.giorno-header').forEach(c => c.classList.remove('selected-cell'));
    this.classList.add('selected-cell');
    giornoSelezionato = this.getAttribute('data-giorno');
    // Trova la prima cella del giorno selezionato e prendi la data reale
    const primaCella = document.querySelector(`.cell[data-giorno="${giornoSelezionato}"]`);
    giornoDataSelezionata = getDateForWeekday(giornoSelezionato);
  });
});