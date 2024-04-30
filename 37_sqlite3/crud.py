'''
CRUD
C => Create ->Insert
R => Read -> Select
U => Update -> Update
D => Delete ->  Delete
'''

import sqlite3

# Crear la base de datos
# Abrir una conexion, si no existe la creara
conexion = sqlite3.connect('tienda.db')

# Obtener el cursor
cursor = conexion.cursor()

'''-------INSERTAR_DATOS----------'''
#  Insertar un registro
# cursor.execute('insert into PRODUCTOS values(1, "Pantalla", 89.95)')

# Insertar varios registros a la vez
productos = [(2, 'Teclado', 29.50), (3, 'Mouse', 15), (4, 'Impresora', 67.50)]

sql = 'insert into PRODUCTOS values(?, ?, ?)'
# cursor.executemany(sql, productos)

''''--------CONSULTAR DATOS-----'''
# Consultar los campos de la tabla
cursor.execute("SELECT name FROM PRAGMA_TABLE_INFO('PRODUCTOS')")
datos = cursor.fetchall()
for item in datos:
    print(item)
print('-'*50)

cursor.execute('select * from PRODUCTOS')

# Recojo los resultados obtenidos

productos = cursor.fetchall()
for prod in productos:
    print(prod)
print('-'*50)

# Consultar los prodcutos con precio inferior a 50

cursor.execute('select * from PRODUCTOS where precio <50 ')
productos_precio = cursor.fetchall()
print(productos_precio)
print('-'*50)


# Buscar productos cuya descripcion sea Impresora
cursor.execute('select * from PRODUCTOS where description = "Impresora" ')
impresora = cursor.fetchall()
print(impresora)
print('-'*50)
# Otra forma

parametro = ('Impresora',)
cursor.execute('select * from PRODUCTOS where description = ?', parametro)
prod_impr = cursor.fetchall()
for prod in prod_impr:
    print(prod)
print('-'*50)

# Mostrar todos los productos ordenados por precio ascendente
cursor.execute('select * from PRODUCTOS ORDER BY precio asc')
precios = cursor.fetchall()
for precio in precios:
    print(precio)
print('-'*50)

# Mostrar todos lso productos ordenados por precio descendente
cursor.execute('select * from PRODUCTOS ORDER BY precio desc')
precios = cursor.fetchall()
for precio in precios:
    print(precio)
print('-'*50)

# Importante el commit
conexion.commit()
