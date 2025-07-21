from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from flask_bcrypt import Bcrypt
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = app.config['SECRET_KEY']
bcrypt = Bcrypt(app)

# Funzione per aprire connessione al database
def get_db_connection():
    connection = mysql.connector.connect(**Config.DB_CONFIG)
    return connection

# --- ROUTE: Home page protetta ---
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, descrizione FROM piatti")
    piatti = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('index.html', user_id=session['user_id'], piatti=piatti)


# --- ROUTE: Registrazione ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = get_db_connection()
        cursor = conn.cursor()

        # Controlla se username o email esistono già
        cursor.execute("SELECT id FROM utenti WHERE username = %s OR email = %s", (username, email))
        user = cursor.fetchone()

        if user:
            flash('Username o email già esistente, scegli un altro!')
            cursor.close()
            conn.close()
            return redirect(url_for('register'))

        # Inserisci utente nel DB
        cursor.execute(
            "INSERT INTO utenti (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed_password)
        )
        conn.commit()

        cursor.close()
        conn.close()

        flash('Registrazione avvenuta con successo! Effettua il login.')
        return redirect(url_for('login'))

    return render_template('register.html')

# --- ROUTE: Login ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, password FROM utenti WHERE email = %s", (email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and bcrypt.check_password_hash(user[1], password):
            session['user_id'] = user[0]
            #flash('Login effettuato con successo!')
            return redirect(url_for('index'))
        else:
            flash('Email o password errati')
            return redirect(url_for('login'))

    return render_template('login.html')

# --- ROUTE: Logout ---
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    #flash('Logout effettuato')
    return redirect(url_for('login'))


# Esegui l'app
if __name__ == '__main__':
    app.run(debug=True)