import os
import mysql.connector

# Establece la conexión a la base de datos utilizando variables de entorno
db = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "perez"),
    password=os.getenv("DB_PASSWORD", ""),
    database=os.getenv("DB_NAME", "mercaflask"),
    port=os.getenv("DB_PORT", 3306)
)

def get_db_cursor():
    return db.cursor(dictionary=True)

# Segunda conexión a la base de datos utilizando las mismas variables de entorno
database = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "perez"),
    password=os.getenv("DB_PASSWORD", ""),
    database=os.getenv("DB_NAME", "mercaflask"),
    port=os.getenv("DB_PORT", 3306)
)
