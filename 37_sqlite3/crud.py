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

# Mostrar los productos que comienzan por la letra M
cursor.execute('select * from PRODUCTOS where description LIKE("M%")')
producto_m = cursor.fetchone()
print(producto_m)

# Ejecutar la consulta para buscar productos que contengan la letra 'e' y cuyo precio sea menor que 50 euros
cursor.execute(
    "SELECT * FROM PRODUCTOS WHERE description LIKE '%e%' AND precio < 50"
)
# Obtener los resultados
productos = cursor.fetchall()
print('-'*50)

# Imprimir los resultados
for producto in productos:
    print(producto)
print('-'*50)


''''----MODIFICAR DATOS---'''
# Subir un 10% el precio de la impresora
# Obtener el precio actual de la impresora
# cursor.execute('SELECT precio FROM PRODUCTOS WHERE description = "Impresora"')
# dato = cursor.fetchone()
# # Calcular el nuevo precio aumentado en un 10%
# precio = dato[0] * 1.1

# # Ejecutar la consulta para actualizar el precio de la impresora
# cursor.execute(
#     "UPDATE PRODUCTOS SET precio = ? WHERE description = 'Impresora'",
#     (precio,)
# )

# FORMA CORTA
cursor.execute(
    "UPDATE productos SET precio = precio*1.1 WHERE description = 'Impresora'")

# Poner las descripciones en mayuscula de todos los productos
cursor.execute("UPDATE PRODUCTOS SET description = UPPER(description)")
cursor.execute('select * from PRODUCTOS')
productos = cursor.fetchall()
for prod in productos:
    print(prod)
print('-'*50)


'''------ELIMINAR DATOS-----'''
# Eliminar los precios con precios superior a los 50
cursor.execute("DELETE FROM PRODUCTOS where precio > 50")
producto = cursor.fetchall()

cursor.execute('select * from PRODUCTOS')
productos = cursor.fetchall()
for prod in productos:
    print(prod)
print('-'*50)

# Importante el commit
conexion.commit()
