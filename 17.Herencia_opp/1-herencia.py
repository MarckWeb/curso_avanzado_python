class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarInfo(self):
        return f'mi nombre es: {self.nombre} tengo {self.edad} años'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # llamar al constructor de la superclase y le pasamos el nombre y la edad
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    # no lo vemos pero implicitamnete tenemos el metodo mostrarInfo que hemos heredado de persona
    # sobreescribir un metodo heredado
    def mostrarInfo(self):
        # vamos a llamar al metodo mostrarInfo de la superclase, para no tener que pasar muchos parametros
        return f'{super().mostrarInfo()}, mi sueldo es: {self.sueldo}'


p1 = Persona('Juan', 27)
print(p1.mostrarInfo())

empleado1 = Empleado('Carlos', 27, 57000)
print(empleado1.mostrarInfo())

# Mostrar si Empleado es subclase de Persona
print(issubclass(Empleado, Persona)) # True

# Mostrar una tupla con las superclases de empleado
print(Empleado.__bases__) # (<class '__main__.Persona'>,)
print(Persona.__subclasses__()) # [<class '__main__.Empleado'>]

# Mostrar una tupla con las superclases de persona
print(Persona.__bases__) # (<class 'object'>,)

# mostrar una lista con todos lso recurso de la clase
print(dir(Empleado))
print(dir(Persona))