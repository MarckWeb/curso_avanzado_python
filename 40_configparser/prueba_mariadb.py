# pip install mariadb
import mariadb
import configparser

# Obtener el objeto config
config = configparser.ConfigParser()

# leer el archivo
config.read(filenames="config.ini")

con = mariadb.connect(
    user=config['mariadb']['user'],
    password=config['mariadb']['password'],
    host=config['mariadb']['host'],
    port=config['mariadb']['port'],
    database=config['mariadb']['database']
)

# Obtenemos el cursor
cursor = con.cursor()

# Lanzamos la query
cursor.execute("select * from PRODUCTOS")
productos = cursor.fetchall()
for prod in productos:
    print(prod)
print("-------------")

# Cerrar la conexion
con.close()
