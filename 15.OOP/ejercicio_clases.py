'''
Crear una clase Cliente que tenga como propiedades:
  - nombre, CIF, vip:boolean, direccion(calle, numero, poblacion)
  - por defecto todos los clientes seran NO vip
  - crear un metodo que me muestre la informacion
  - Crear 2 clientes
'''

# Composición: Clases como atributos de otras clases
'''
Consiste en dividir el software en diferentes componentes, resolver cada uno por
separado y por último unirlos en una solución única.
• Ante un problema complejo es más fácil resolverlo cuando se divide en piezas
manejables.
'''
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







