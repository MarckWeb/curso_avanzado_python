'''
Crear una lista de objetos de tipo producto
a partir del fichero productos.txt
    - el id debe ser numero entero
    - la descripcion debe tener solo la primera letra mayuscula
    - el precio ha de ser numero real(float)
    -mostrar la lista con los productos
'''
class Producto:
    def __init__(self, id, descripcion, precio):
        self.id = int(id)
        # eliminamso espacios y el primer caracter convierte en mayuscula
        self.descripcion = descripcion.strip().capitalize()
        self.precio = float(precio)

    def __str__(self):
        return (f"ID: {producto.id}, Descripción: {producto.descripcion}, Precio: ${producto.precio}")

# Lista para almacenar los objetos Producto
lista_productos = []

# Leer el archivo y crear los objetos Producto
fichero_producto =  open('productos.txt', 'r', encoding='utf-8')
# print(fichero_producto.read())
for linea in fichero_producto:
    print(linea)
    # por cada linea de productos.txt elimina espacio de inicio a final
    # y con split convierte en una lista por cada separacion de |
    id, descripcion, precio = linea.split('|')
    producto = Producto(id, descripcion, precio)
    lista_productos.append(producto)

# Cerramos el fichero
fichero_producto.close()
# Mostrar la lista de productos
for producto in lista_productos:
    print(producto)

