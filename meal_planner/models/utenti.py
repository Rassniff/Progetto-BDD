from . import get_db_connection

# Recupera un utente dal database tramite email
def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM utenti WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# Verifica se un utente con lo stesso username o email esiste già
def user_exists(username, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM utenti WHERE username = %s OR email = %s",
        (username, email)
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# Inserisce un nuovo utente nel database
def insert_user(username, email, hashed_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO utenti (username, email, password) VALUES (%s, %s, %s)",
        (username, email, hashed_password)
    )
    conn.commit()
    cursor.close()
    conn.close()