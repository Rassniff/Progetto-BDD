from . import get_db_connection

def get_ingredienti(user_id=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    if user_id:
        cursor.execute("""
            SELECT id, nome, unita_misura, proteine, carboidrati, calorie, validato, utente_id
            FROM ingredienti
            WHERE validato = 1 OR utente_id = %s
        """, (user_id,))
    else:
        cursor.execute("""
            SELECT id, nome, unita_misura, proteine, carboidrati, calorie, validato, utente_id
            FROM ingredienti
            WHERE validato = 1
        """)
    ingredienti = cursor.fetchall()
    cursor.close()
    conn.close()
    return ingredienti

def insert_ingrediente(nome, unita_misura, proteine, carboidrati, calorie, utente_id=None, validato=1):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ingredienti (nome, unita_misura, proteine, carboidrati, calorie, validato, utente_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (nome, unita_misura, proteine, carboidrati, calorie, validato, utente_id))
    conn.commit()
    cursor.close()
    conn.close()