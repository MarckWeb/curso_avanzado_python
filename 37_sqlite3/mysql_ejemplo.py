import mysql.connector

# Datos de conexion
mydb = mysql.connector.connect(
    host="colocar un hos en la nube o local",
    user="nombre de usuario",
    password="cuando es local no tiene password",
    database="normalmente en local suele ser root"
)


# Obtener el cursor
cursor = mydb.cursor()

# Mostrar las tablas que tengo en esa BBDD
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)
print('-'*50)

# Ejecutar una consulta para seleccionar datos de la tabla
# cursor.execute("SELECT * FROM user LIMIT 1")

# # Obtener información sobre las columnas de la tabla
# columnas = cursor.description

# # Imprimir la información sobre las columnas
# for columna in columnas:
#     print(columna[0], columna[1])
# print('-'*50)

# Consultar todos los usuarios
cursor.execute("SELECT id, name, lastname, email FROM user")
usuarios = cursor.fetchall()
for user in usuarios:
    print(user)
print("-------------")

# Cerrar la conexión
mydb.close()
