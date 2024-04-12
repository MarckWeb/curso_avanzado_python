'''
Crear una clase Cliente que tenga como propiedades:
  - nombre, CIF, vip:boolean, direccion(calle, numero, poblacion)
  - por defecto todos los clientes seran NO vip
  - crear un metodo que me muestre la informacion
  - Crear 2 clientes
'''

# Composición: En Python, la composición es un concepto de programación orientada a objetos (POO)
# que se refiere a la capacidad de crear una clase utilizando objetos de otras clases en lugar de
# heredar directamente de ellas. Esto se logra mediante la creación de instancias de otras clases
# dentro de una clase principal.
#
# En lugar de usar la herencia, donde una clase hereda atributos y comportamientos de otra clase,
# la composición permite construir una clase utilizando objetos de otras clases como componentes.

class Direccion:
    def __init__(self, calle, numero, poblacion):
        self.calle = calle
        self.numero = numero
        self.poblacion = poblacion

    def mostrarDireccion(self):
        return (f"calle: {self.calle}/{self.numero} ({self.poblacion})")
class Cliente:
    def __init__(self, nombre, cif, direccion:Direccion, vip=False):
        self.nombre = nombre
        self.cif = cif
        self.vip = vip
        self.direccion = direccion

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, CIF: {self.cif}, Vip: {self.vip}, Direccion: {self.direccion.mostrarDireccion()}")


# Instancia de cliente 1
dir = Direccion('Gran via', 7, 'Bilbao')
print(type(dir))
cliente1 = Cliente(8, '7-253xx', dir, vip=True)
cliente1.mostrar_info()


# Instancia de cliente 2
cliente2 = Cliente('David', '8-54511xx', Direccion('Gran via', 7, 'Bilbao'))
cliente2.mostrar_info()


# comprobra si las variables apuntan al mismo objeto
print('Mismo objeto:', dir in cliente1.direccion)







