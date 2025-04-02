import mysql.connector
from mysql.connector import Error

def dbConnection():
    try:
        # Configuración para XAMPP (valores por defecto)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',          # Usuario por defecto de XAMPP
            password='',          # Contraseña por defecto (vacía)
            database='products_app', # Nombre de tu base de datos
            port='3306'           # Puerto por defecto de MySQL en XAMPP
        )
        
        # Crear la base de datos si no existe
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS products_app")
        connection.database = 'products_app'  # Nos aseguramos de usar esta DB
        
        # Crear la tabla si no existe
        create_table_query = """
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL,
            quantity INT NOT NULL
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        
        return connection
        
    except Error as e:
        print(f'Error de conexión con la base de datos: {e}')
        raise