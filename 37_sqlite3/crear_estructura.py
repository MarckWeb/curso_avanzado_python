'''Crear la base de datos y la tabla'''
import sqlite3

# Crear la base de datos
# Abrir una conexion, si no existe la creara
conexion = sqlite3.connect('tienda.db')

# Obtener el cursor
cursor = conexion.cursor()

# Crear la tabla de productos
cursor.execute(
    'CREATE IF NOT EXISTS PRODUCTOS PRODUCTOS(codigo INTEGER PRIMARY KEY, description TEXT, precio REAL)'
)

# Importante el commit
conexion.commit()

# Cerra la conexion
# conexion.close()
