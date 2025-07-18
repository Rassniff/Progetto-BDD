# Progetto-BDD

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


# Frontend 

Flask genera pagine HTML dal server.
Tu crei file .html in una cartella templates/.
Dentro i file .html puoi usare Jinja2, che ti permette di inserire variabili Python nel codice HTML.
