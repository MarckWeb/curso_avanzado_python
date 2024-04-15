# sintaxis: lambda parametros: cuerpo de la funcion

'''map'''

#Ejemplo
'''
numeros = [1,2,3,4,5]
def duplicar(numero):
    return numero * 2
numeros_dobles = list(map(duplicar, numeros))
print(numeros_dobles) # con list()  [2, 4, 6, 8, 10]
'''

numeros_dobles = list(map(lambda numero:numero * 2, [1,2,3,4,5]))
print(numeros_dobles)

# Ejemplo 2
alumnos = dict(Luis=8.9, Maria=6.3, Adolfo=3.8, Pedro=10)
nuevas_notas = dict(map(lambda item: (item[0], 10 if item[1] >= 9 else item[1] + 1), alumnos.items()))
#Hay otro formato de if comprimido: (valor_False,valor_True)[condición]
nuevas_notas = dict(map(lambda item: (item[0], (item[1] + 1, 10)[item[1] >= 9]), alumnos.items()))
print(nuevas_notas)

# Ejemplo 3
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

lista = [1, 2, 3, 4, 5, 6]
pares = filter(lambda x: x % 2 == 0, lista)
print(list(pares)) # Devuelve: [2, 4, 6]

persona_proces = list(map(lambda persona: Persona(persona.nombre.upper(), persona.edad + 1), personas))
print(persona_proces)


# ejemplo 4
'''Retornar la plabra abracadabra donde la letra a sea mayuscula'''

palabra1 = ''.join(list(map(lambda  letra:  letra.upper() if letra == 'a' else letra, 'abracadabra'  )))
print(palabra1)
# (valor_False, valor_True)[condicion]
palabra2 = ''.join((map(lambda  letra:  (letra, letra.upper() )[letra == 'a'], 'abracadabra'  )))
print(palabra2)