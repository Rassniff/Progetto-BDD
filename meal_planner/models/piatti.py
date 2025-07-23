from . import get_db_connection

def get_piatti(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nome, descrizione
        FROM piatti
        WHERE validato = 1 OR utente_id = %s
    """, (user_id,))
    piatti = cursor.fetchall()
    cursor.close()
    conn.close()
    return piatti

from . import get_db_connection
from .ingredienti import get_ingredienti

def insert_piatto(nome, descrizione, utente_id=None, validato=1):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO piatti (nome, descrizione, validato, utente_id)
        VALUES (%s, %s, %s, %s)
    """, (nome, descrizione, validato, utente_id))
    piatto_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return piatto_id

def associa_ingredienti_al_piatto(piatto_id, ingredienti_quantita):
    # ingredienti_quantita: lista di tuple (ingrediente_id, quantita)
    conn = get_db_connection()
    cursor = conn.cursor()
    for ingrediente_id, quantita in ingredienti_quantita:
        cursor.execute("""
            INSERT INTO piatti_ingredienti (piatto_id, ingrediente_id, quantita)
            VALUES (%s, %s, %s)
        """, (piatto_id, ingrediente_id, quantita))
    conn.commit()
    cursor.close()
    conn.close()