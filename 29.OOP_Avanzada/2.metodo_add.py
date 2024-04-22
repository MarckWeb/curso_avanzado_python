class Producto:
    def __init__(self, id, descripcion, precio):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio

   # Cuando mostresmos el objeto, represente su estado (contenido, valores)
    def __str__(self):
        return f'ID: {self.id}, descripcion: {self.descripcion}, Precio: {self.precio}'

   # __eq__ => devuleve valor booleano si la instancia es igual a la recibida como argumento
    def __eq__(self, otra):
        return self.id == otra.id and self.descripcion == otra.descripcion and self.precio == otra.precio

   # __add__ => devuleve un numero que sera el resultado de aplicar una suma
    def __add__(self, otra):
        return self.precio + otra.precio


p3 = Producto(1, 'Teclado', 37.95)
p4 = Producto(1, 'Mouse', 19.80)


# sin __add_ => TypeError: unsupported operand type(s) for +: 'Producto' and 'Producto'
print(p3 + p4)
print(p3 + p4)  # con __add__ => 57.75
