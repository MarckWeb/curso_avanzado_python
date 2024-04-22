'''se utilizaria delf, pero en este caso usamos Contabilidad'''


class Contabilidad:
    contabilidad = None

    @staticmethod
    def crearContabilidad():
        if Contabilidad.contabilidad is None:
            Contabilidad.contabilidad = Contabilidad()
        return Contabilidad.contabilidad

    @staticmethod
    def getContabilidad():
        return Contabilidad.contabilidad


libro = Contabilidad.crearContabilidad()
print(libro)

# OTRO EJEMPLO


class Producto:
    __contador = 0

    def __init__(self, descripcion, precio):
        Producto.__contador += 1
        self.id = Producto.__contador
        self.descripcion = descripcion
        self.precio = precio

    @staticmethod
    def getContador():
        return Producto.__contador

    @classmethod
    def verContador():
        return Producto('xxx', 100)

    def __str__(self):
        return f'ID: {self.id}, Descripcion: {self.descripcion}, precio: {self.precio}'


print('conatdor:', Producto.getContador())

p1 = Producto('Pantalla', 129.50)
print(p1)

# Probar el metodo estatico
print('conatdor:', Producto.getContador())
print('conatdor:', p1.getContador())

# Probar el metodo de la clase
print('metodo clase:', Producto.getContador())
print('metodo clase:', p1.verContador())

# El metodo de la clase puede actuar como constructor
p3 = Producto.verContador()
print(p3)
