from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
from config import Config

# Importo funzioni dai modelli
from models.utenti import get_user_by_email, user_exists, insert_user
from models.piatti import get_piatti
from models.planner import get_planner_for_user, add_or_update_planner, remove_from_planner

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = app.config['SECRET_KEY']
bcrypt = Bcrypt(app)

# --- ROUTE: Home page protetta ---
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    piatti = get_piatti(session['user_id'])
    planner = get_planner_for_user(session['user_id'])
    
    return render_template(
        'index.html', 
        user_id=session['user_id'], 
        piatti=piatti,
        planner=planner)

# --- ROUTE: Registrazione ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        if user_exists(username, email):
            flash('Username o email già esistente, scegli un altro!')
            return redirect(url_for('register'))

        insert_user(username, email, hashed_password)

        flash('Registrazione avvenuta con successo! Effettua il login.')
        return redirect(url_for('login'))

    return render_template('register.html')

# --- ROUTE: Login ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = get_user_by_email(email)

        if user and bcrypt.check_password_hash(user[1], password):
            session['user_id'] = user[0]
            return redirect(url_for('index'))
        else:
            flash('Email o password errati')
            return redirect(url_for('login'))

    return render_template('login.html')

# --- ROUTE: Logout ---
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# --- ROUTE: Aggiungi piatto al planner ---
@app.route('/add-to-planner', methods=['POST'])
def add_to_planner():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Utente non autenticato"}), 401

    data = request.get_json()
    giorno = data.get('giorno')   # es. 'Lun'
    pasto = data.get('pasto')     # es. 'pranzo'
    piatto_id = data.get('piatto_id')

    if not (giorno and pasto and piatto_id):
        return jsonify({"success": False, "message": "Dati incompleti"}), 400

    # Controlla che pasto sia valido per l'ENUM
    valid_pasti = ['colazione', 'pranzo', 'merenda', 'cena']
    if pasto not in valid_pasti:
        return jsonify({"success": False, "message": "Pasto non valido"}), 400

    # Mappa giorno della settimana
    weekday_map = {"Lun": 0, "Mar": 1, "Mer": 2, "Gio": 3, "Ven": 4, "Sab": 5, "Dom": 6}
    if giorno not in weekday_map:
        return jsonify({"success": False, "message": "Giorno non valido"}), 400

    # Calcola la data del giorno corrente della settimana
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())  # Lunedì corrente
    data_giorno = start_of_week + timedelta(days=weekday_map[giorno])

    planner_id = add_or_update_planner(session['user_id'], data_giorno.date(), pasto, piatto_id)

    return jsonify({
        "success": True, 
        "message": "Piatto aggiunto al planner", 
        "data_giorno": str(data_giorno.date()),
        "planner_id": planner_id,
        "piatto_id": piatto_id
    })

# --- ROUTE: Rimuovi piatto dal planner ---
@app.route('/remove-from-planner', methods=['POST'])
def remove_from_planner_r():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Utente non autenticato"}), 401

    data = request.get_json()
    data_giorno = data['data']      # formato 'YYYY-MM-DD'
    pasto = data['pasto']
    piatto_id = data['piatto_id']

    remove_from_planner(session['user_id'], data_giorno, pasto, piatto_id)

    return jsonify({'success': True})

# Esegui l'app
if __name__ == '__main__':
    app.run(debug=True)