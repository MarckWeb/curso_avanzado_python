class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarInfo(self):

        # return f"{self.nombre}, {self.edad}"
        # return self.nombre + ", " + str(self.edad)
        return "{}, {}".format(self.nombre, self.edad)


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # llamar al constructor de la superclase y le pasamos el nombre y la edad
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    # Impicitamente tenemos el metodo mostrarInfo que hemos heredado de Persona
    # Sobreescribir un metodo heredado
    # Ha de tener la misma definicion de metodo
    def mostrarInfo(self):
        # vamos a llamar al metodo mostrarInfo de la superclase
        # return "{}, {}".format(super().mostrarInfo(), self.sueldo)
        return f"{super().mostrarInfo()}, {self.sueldo}"


p1 = Persona("Juan", 27)
print(p1.mostrarInfo())

empleado1 = Empleado("Juan", 27, 57000)
print(empleado1.mostrarInfo())

# Mostrar si Empleado es subclase de Persona
print(issubclass(Empleado, Persona))  # True
print(Persona.__subclasses__())  # [<class '__main__.Empleado'>]

# Mostrar una tupla con las superclases de Empleado
print(Empleado.__bases__)  # (<class '__main__.Persona'>,)

# Mostrar una tupla con las superclases de Persona
print(Persona.__bases__)  # (<class 'object'>,)

# Mostrar una lista con todos los recursos de la clase
print(dir(Persona))
print(dir(Persona))
