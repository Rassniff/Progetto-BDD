from . import get_db_connection

def get_planner_for_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT data, pasto, piatto_id, piatti.nome
        FROM planner
        JOIN piatti ON planner.piatto_id = piatti.id
        WHERE planner.utente_id = %s
    """, (user_id,))
    planner = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "data": str(row[0]),
            "pasto": row[1],
            "piatto_id": row[2],
            "nome": row[3]
        }
        for row in planner
    ]

def add_or_update_planner(user_id, data_giorno, pasto, piatto_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id FROM planner WHERE utente_id = %s AND data = %s AND pasto = %s
    """, (user_id, data_giorno, pasto))
    existing = cursor.fetchone()

    if existing:
        cursor.execute("""
            UPDATE planner SET piatto_id = %s WHERE id = %s
        """, (piatto_id, existing[0]))
        planner_id = existing[0]
    else:
        cursor.execute("""
            INSERT INTO planner (utente_id, data, pasto, piatto_id)
            VALUES (%s, %s, %s, %s)
        """, (user_id, data_giorno, pasto, piatto_id))
        planner_id = cursor.lastrowid

    conn.commit()
    cursor.close()
    conn.close()

    return planner_id 

def remove_from_planner(user_id, data_giorno, pasto, piatto_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM planner
        WHERE utente_id = %s AND data = %s AND pasto = %s AND piatto_id = %s
    """, (user_id, data_giorno, pasto, piatto_id))
    conn.commit()
    cursor.close()
    conn.close()

#somma ingredienti per statistica giornaliera
def get_stats_for_day(user_id, date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
          COALESCE (SUM(ingredienti.proteine * piatti_ingredienti.quantita / 100), 0) AS tot_proteine,
          COALESCE (SUM(ingredienti.carboidrati * piatti_ingredienti.quantita / 100), 0) AS tot_carboidrati,
          COALESCE (SUM(ingredienti.calorie * piatti_ingredienti.quantita / 100), 0) AS tot_calorie
        FROM planner
        JOIN piatti ON planner.piatto_id = piatti.id
        JOIN piatti_ingredienti ON piatti.id = piatti_ingredienti.piatto_id
        JOIN ingredienti ON piatti_ingredienti.ingrediente_id = ingredienti.id
        WHERE planner.utente_id = %s AND DATE(planner.data) = %s
    """, (user_id, date))
    stats = cursor.fetchone()
    cursor.close()
    conn.close()
    return stats

#somma ingredienti per statistica settimanale
def get_stats_for_week(user_id, start_date, end_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
          COALESCE (SUM(ingredienti.proteine * piatti_ingredienti.quantita / 100), 0) AS tot_proteine,
          COALESCE (SUM(ingredienti.carboidrati * piatti_ingredienti.quantita / 100), 0) AS tot_carboidrati,
          COALESCE (SUM(ingredienti.calorie * piatti_ingredienti.quantita / 100), 0) AS tot_calorie
        FROM planner
        JOIN piatti ON planner.piatto_id = piatti.id
        JOIN piatti_ingredienti ON piatti.id = piatti_ingredienti.piatto_id
        JOIN ingredienti ON piatti_ingredienti.ingrediente_id = ingredienti.id
        WHERE planner.utente_id = %s AND planner.data BETWEEN %s AND %s
    """, (user_id, start_date, end_date))
    stats = cursor.fetchone()
    cursor.close()
    conn.close()
    return stats