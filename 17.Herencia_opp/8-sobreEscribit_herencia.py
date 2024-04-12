'''La clase persona esta heredando de la clase object'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad
    '''En la clase objetc el motodo __str__ devulve al informacion del objeto en modo texto'''
    def __str__(self):
        return f'mi nombre es: {self.nombre} tengo {self.edad} años'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    '''
        -Impliciatamnete tenemos al metodo __str__ que hemos heredado de persona
        -Sobreescribimos un metodo heredado
    '''
    def __str__(self):
        # acceder a un recurso publico de la superclase
        print('Nombre:', self.nombre)
        # Acceder al recurso privado de la superclase
        return f'{super().__str__()}, mi sueldo es: {self.sueldo}'


p1 = Persona('Juan', 27)

'''Cuando muestro el objeto de froma implicita se invoca al metodo __str__'''
print(p1) # <__main__.Persona object at 0x00000212FC0BDA60>
#print(p1.__str__()) # <__main__.Persona object at 0x00000140955EDAF0>
'''mostrar el hash o hashcode o identificador del objeto'''
print(p1.__hash__()) # 133400251814

empleado1 = Empleado('Carlos', 27, 57000)
print(empleado1)

'''al sobreescribir metodos con el objetod __srt__, ya no colocamos un nombre al metodo tanto 
del padfre y del hijo que herada solo colocamos __srt__,'''

