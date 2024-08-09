import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="perez",
    password="",
    database="mercaflask",
    port="3306"

)

def get_db_cursor():
    return db.cursor(dictionary=True)



database = mysql.connector.connect(
    host="localhost",
    user="perez",
    password="",
    database="mercaflask",
    port="3306"
)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "perez"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "mercaflask"),
        port=os.getenv("DB_PORT", 3306)
    )

def get_db_cursor():
    connection = get_db_connection()
    return connection.cursor(dictionary=True)





