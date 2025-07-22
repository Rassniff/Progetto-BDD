from config import Config
import mysql.connector

# Funzione per aprire connessione al database
def get_db_connection():
    return mysql.connector.connect(**Config.DB_CONFIG)