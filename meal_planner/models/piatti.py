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