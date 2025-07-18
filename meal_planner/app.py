from flask import Flask, render_template
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

# Funzione per aprire connessione al database
def get_db_connection():
    connection = mysql.connector.connect(**DB_CONFIG)
    return connection

# Rotta principale
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM piatti")
    piatti = cursor.fetchall()
    cursor.close()
    conn.close()

    # Mostra i piatti come lista HTML
    html = "<h1>Piatti disponibili:</h1><ul>"
    for p in piatti:
        html += f"<li>{p[0]} - {p[1]} - {p[2]} - {p[3]} kcal</li>"
    html += "</ul>"
    return html


# Esegui l'app
if __name__ == '__main__':
    app.run(debug=True)