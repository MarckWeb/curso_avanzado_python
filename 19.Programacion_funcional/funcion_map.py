# la funcion ma se aplica sobre un elemento iterable, (coleccion y cademnas de texto)
# a cada elemnto le aplicamos una funcion y el resultado sera el nuevo elemneto modificado
# sintaxis: map(funcion, iterable)

'''
     la función map(). La función map() toma cada elemento del diccionario
     alumnos.items() (que es una lista de tuplas clave-valor) y aplica la función
     sumar_punto a cada elemento.

     La función map() en Python aplica la función especificada a cada elemento del iterable
     (como una lista, tupla, diccionario, etc.) que se le pasa como argumento.
'''

# ejemplo 1
numeros = [1,2,3,4,5]
def duplicar(numero):
    return numero * 2
numeros_dobles = list(map(duplicar, numeros))
print(type(numeros_dobles))
#print(numeros_dobles) # sin list() <map object at 0x00000173613A7130>
print(numeros_dobles) # con list()  [2, 4, 6, 8, 10]

# ejemplo 2
alumnos= dict(Luis=8.9, Maria=6.3, Adolfo=3.8, Pedro=10)

def sumar_punto(item):
    if item[1] >= 9:
        nota = 10
    else:
        nota = item[1] + 1

    return item[0], nota

nuevas_notas = dict(map(sumar_punto, alumnos.items()))
print(nuevas_notas)

# Ejemplo 3
'''
    Crear la clase Persona con nombre y edad y sobreescribir __srt__
    Crear una lista de personas
    Crear una funcion que recibe el objeto de Persona y retorne el nombre en mayuscula y edad +1
    Crear una lista con la funcion map
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

def procesar_persona(persona):
    nombre_mayuscula = persona.nombre.upper()
    edad_mas_uno = persona.edad + 1
    return nombre_mayuscula, edad_mas_uno

# Crear una lista de personas
personas = [
    Persona("Juan", 25),
    Persona("Maria", 30),
    Persona("Carlos", 40)
]

# Usar map para aplicar la función procesar_persona a cada objeto Persona en la lista personas
personas_procesadas = list(map(procesar_persona, personas))
print(personas_procesadas)

# ejemplo 4
'''Retornar la plabra abracadabra donde la letra a sea mayuscula'''
def convertir_upper(letra):
    if letra == 'a':
        letra = letra.upper()
    return letra
palabra = list(map(convertir_upper, 'abracadabra'))
palabra = ''.join(palabra)
print(palabra)