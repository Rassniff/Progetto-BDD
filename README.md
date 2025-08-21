# Progetto Meal Planner 2024–2025

Questo progetto consiste in una web application full-stack che consente di pianificare i pasti settimanali e calcolare i valori nutrizionali giornalieri e settimanali.  
L’applicazione è sviluppata con **Python (Flask)** per il backend e **HTML, CSS e JavaScript** per il frontend, utilizzando **MySQL** come database relazionale.

---

## Funzionalità principali

- Registrazione e login utente con gestione sessioni (bcrypt per password hashing).
- Visualizzazione dei piatti disponibili (propri o validati).
- Pianificazione settimanale tramite **drag & drop** dei piatti nel planner.
- Creazione di nuovi piatti e associazione ingredienti.
- Inserimento di nuovi ingredienti personalizzati.
- Calcolo automatico delle **statistiche nutrizionali**:
  - valori giornalieri
  - valori settimanali
- Backend strutturato in moduli (`models/`) con query SQL parametrizzate.
- Utilizzo di una **view SQL** (`planner_nutritional_view`) per ottimizzare i calcoli nutrizionali.

---

## Struttura del progetto

    Meal-Planner/
    ├── app.py                            # Entry point Flask (route principali)
    ├── config.py                         # Configurazione applicazione e DB
    ├── requirements.txt                  # Dipendezne utilizzate
    ├── db/
    │ ├── init_db.sql
    │ ├── planner_nutritional_view.sql
    ├── models/                           # Moduli Python con le query per ciascuna tabella
    │ ├── utenti.py
    │ ├── ingredienti.py
    │ ├── piatti.py
    │ └── planner.py
    ├── static/
    │ ├── css/
    │ │ └── style_index.css               # Stili principali index
    │ │ └── style.css                     # Stili principali pagina di login
    │ └── js/
    │ | └── planner.js                    # Logica frontend per drag&drop e API
    │ | └── gestore_stats.js              # Logica stats
    │ | └── set_week_dates.js             # Logica date
    │ | └── gestore_new_piatti.js         # Logica piatti
    ├── templates/
    │ | ├── index.html                    # Homepage con planner settimanale
    │ | ├── login.html                    # Pagina di login
    │ | └── register.html                 # Pagina di registrazione
    ├── relazione/
    │ └── relazione.pdf                   # Relazione tecnica del progetto
    └── README.md                         # Documentazione del progetto

---

## Avvio del progetto

### Requisiti

- **[Python 3.10+](https://www.python.org/)**  
- **[MySQL](https://www.mysql.com/)** installato e attivo  
- Un **browser moderno** (Chrome, Firefox, Edge)

### Installazione

1. Clona il repository o scaricalo in locale.
2. Crea un ambiente virtuale ed installa i pacchetti:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # su Linux/Mac
   .venv\Scripts\activate      # su Windows
   pip install -r requirements.txt
   
3.Configura il database in config.py:

    DB_CONFIG = {
        'host': 'localhost',
        'user': 'root',
        'password': 'password',
        'database': 'meal_planner'
    }

---

### Avvia l’app:

python app.py
Apri il browser su http://localhost:5000

Principali route Flask

    Metodo	Endpoint	Descrizione
    GET	/login	Login utente
    POST	/login	Autenticazione utente
    GET	/register	Pagina di registrazione
    POST	/register	Creazione nuovo account
    GET	/	Homepage con planner settimanale
    POST	/add-to-planner	Aggiunge un piatto al planner
    POST	/remove-from-planner	Rimuove un piatto dal planner
    POST	/crea-piatto	Crea un nuovo piatto con ingredienti
    POST	/aggiungi-ingrediente	Inserisce un nuovo ingrediente
    GET	/stats-day	Restituisce le statistiche nutrizionali giornaliere
    GET	/stats-week	Restituisce le statistiche nutrizionali settimanali

---

## Autori

Andrii Ursu
Diego Chiodi

Corso di Basi di Dati 
A.A. 2024/2025

---
## Licenza
Questo progetto è realizzato a scopo didattico per uso universitario.
