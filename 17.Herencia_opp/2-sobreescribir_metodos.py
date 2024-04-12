''' Ejemplo de sobreescritura de metodos heredados de object'''
# La clase Persona esta heredando de la clase object


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad
        # agregar el sexo

    # En la clase object el metodo __str__ devuelve la informacion del objeto en modo texto
    def __str__(self):
        # return f"{self.nombre}, {self.edad}"
        # return self.nombre + ", " + str(self.edad)
        return "{}, {}".format(self.nombre, self.__edad)


class Empleado(Persona):
    '''
        docstring de Empleado
    '''
    # Heredamos los recursos publicos de Persona

    def __init__(self, nombre, edad, sueldo):
        # llamar al constructor de la superclase y le pasamos el nombre y edad
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    # Impicitamente tenemos el metodo __str__ que hemos heredado de Persona
    # Sobreescribir un metodo heredado
    # Ha de tener la misma definicion de metodo
    def __str__(self):
        # Acceder a un recurso publico de la superclase
        print("Nombre:", self.nombre)

        # Acceder a un recurso privado de la superclase
        # print("Edad:", self.__edad) # AttributeError: 'Persona' object has no attribute 'edad'
        # print("Edad:", super().__edad) # AttributeError: 'super' object has no attribute '_Empleado__edad'

        # name mangling
        print("Edad:", self._Persona__edad)   # 27

        # vamos a llamar al metodo __str__ de la superclase
        return f"{super().__str__()}, {self.sueldo}"


p1 = Persona("Juan", 27)

# Cuando muestro el objeto de forma implicita se invoca al metodo __str__()
print(p1)  # <__main__.Persona object at 0x1044a3640>
# print(p1.__str__())  # <__main__.Persona object at 0x109336770>

# mostrar el hash o hascode o identificador del objeto
print(p1.__hash__())  # 270679908

empleado1 = Empleado("Juan", 27, 57000)
print(empleado1)

# name mangling
# Accedemos a un recurso privado
print("Edad:", empleado1._Persona__edad)

print(empleado1.__doc__)  # docstring de Empleado
print(__doc__)  # Ejemplo de sobreescritura de metodos heredados de object


'''al sobreescribir metodos con el objetod __srt__, ya no colocamos un nombre al metodo tanto 
del padfre y del hijo que herada solo colocamos __srt__,'''
