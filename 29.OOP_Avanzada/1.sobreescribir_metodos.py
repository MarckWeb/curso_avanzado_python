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

   # __hash__ => devuleve un valor numerico, es impresindible para comparar elementos del conjunto
    def __hash__(self):
        return int(self.id + len(self.descripcion) + self.precio)

   # __add__ => devuleve un numero que sera el resultado de aplicar una suma
    def __add__(self, otra):
        return self.precio + otra.precio


p1 = Producto(1, 'Pantalla', 129.50)
# print(p1) # <__main__.Producto object at 0x00000185C4EF0410> sin metodo
print(p1)  # ID: 1, descripcion: Pantalla, Precio: 129.5

'''
En Metodo.__eq__ => self seria el objeto a comparar p1 y otra el objeto comparador que es p2
'''

p2 = Producto(1, 'Pantalla', 129.50)
# print("Son iguales?", p1 == p2)  #sin _eq_ False => compara direccion memoria

print("Son iguales con __eq_?", p1 == p2)  # con _eq_ True => Son iguales? True
print("Son iguales con __eq_?", p1.__eq__(p2))  # otra forma no tradicional

'''
En Metodo.__add__
'''
p3 = Producto(1, 'Teclado', 37.95)
p4 = Producto(1, 'Mouse', 19.80)

# sin __add_ => TypeError: unsupported operand type(s) for +: 'Producto' and 'Producto'
print(p3 + p4)
print(p3 + p4)  # con __add__ => 57.75


'''
__hash__ y __eq__ van juntos siempres para operar
En Metodo.__hash__
'''
'''
Los conjuntos son colecciones que no permiten elementos duplicados
'''
# p1 y p2 al tener el mismo id, entiende que son iguales
conjunto = {p1, p2, p3, p4}
print(conjunto)
'''
{<__main__.Producto object at 0x000001EC82B718B0>, 
<__main__.Producto object at 0x000001EC82B71700>, 
<__main__.Producto object at 0x000001EC82B71730>}
'''

for p in conjunto:
    print(p)
'''
ID: 1, descripcion: Mouse, Precio: 19.8
ID: 1, descripcion: Pantalla, Precio: 129.5
ID: 1, descripcion: Teclado, Precio: 37.95
'''
