import mysql.connector
from mysql.connector import Error

def dbConnection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='products_db'
        )
        return connection
    except Error as e:
        print(f"Error de conexión con la base de datos: {e}")
        return None