class Producto:
    # contador = 0 # publico
    __contador = 0  # Privado
    '''
      def __init__(self, id, descripcion, precio):
         # Variable de instancia: cada objeto mantiene una copia de estas variables
         self.id = id
         self.descripcion = descripcion
         self.precio = precio
         # cada objeto de instacia empieza con cero
         #   self.contador = 0
         Producto.contador += 1
         # contador += 1 # UnboundLocalError: cannot access local variable 'contador' where it is not associated with a value
    '''

    def __init__(self, descripcion, precio):
        # Variable de instancia: cada objeto mantiene una copia de estas variables
        # Incrementar el contador
        Producto.__contador += 1
        self.id = Producto.__contador
        self.descripcion = descripcion
        self.precio = precio

    # Metodo de clase: solo hay una copia y reside en una clase
    # Quitamos como argumento el puntero sefl
    def getContador():
        return Producto.__contador

    def __str__(self):
        return f'ID: {self.id}, Descripcion: {self.descripcion}, Precio: {self.precio}'


'''
p1 = Producto(1, 'Pantalla', 129.50)
p2 = Producto(2, 'Teclado', 58.95)
p3 = Producto(3, 'Mouse', 12.95)

'''

# Al ser conatdor publico puedo ca,biar su valor
Producto.__contador = 10

# Acceso a recurso de clase (estatico): Clase.recurso
# print('Contador:', Producto.contador)
print('Contador', Producto.getContador())

p1 = Producto('Pantalla', 129.50)
p2 = Producto('Teclado', 58.95)
p3 = Producto('Mouse', 10.95)

print(p1)
print(p2)
print(p3)
print('Contador', Producto.getContador())
# print('Cuantos productos tengo?', p1.contador)
# print('Cuantos productos tengo?', p2.contador)
