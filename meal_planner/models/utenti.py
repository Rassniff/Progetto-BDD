from . import get_db_connection

def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM utenti WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

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