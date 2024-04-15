# la funcion filter se aplica sobre un elemento (coleccion y string)
# filtramso los elementos en vase a una funcion que retorna dos posibles valores
# si retorna True =>  nos quedamos con el elemento, pasa el filtro
# si retorna False => lo descartamos

# Sintaxis: filter(funcion, iterable)

# Ejemplo 1
'''Dada una lista de numeros y una funcion quedarnos solo con los pares'''
numeros = list(range(1, 101))


def filtrar_pares(numero):
    if numero % 2 == 0:
        return numero


numeros_pares = list(filter(filtrar_pares, numeros))
print(numeros_pares)

# ejemplo 2
'''Dado un diccionario con los nombres y notas de cada alumno, filtrar para quedarnos solo con los aprobados'''

alumnos = {'Juan': 6.4, 'Maria': 3.3, 'Luis': 6.4, 'Adolfo': 7.1, 'Pedro': 4.3}
'''
def aprobar(item):
    if item[1] > 5:
        return (item[0], item[1])
aprobados = list(filter(aprobar, alumnos.items()))
print(aprobados)
'''


def es_aprobado(item):
    nombre, calificacion = item
    return calificacion > 5


# Filtrar los alumnos aprobados
aprobados = list(filter(es_aprobado, alumnos.items()))

print(aprobados)

# Ejemplo 3
'''Partiendo de una lista de instancias de Persona, filtrar para quedarnos solo con los mayores de edad'''


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"


def personas_mayores(persona):
    print('..', persona)
    persona_mayor = persona.edad
    return persona_mayor >= 18


personas = [
    Persona("Juan", 25),
    Persona("Maria", 10),
    Persona("Carlos", 40),
    Persona("Pedro", 17)
]

personas_mayores = list(filter(personas_mayores, personas))
# personas_mayores = list(filter(lambda persona: persona.edad >= 18, personas))

for persona in personas_mayores:
    print(persona.nombre, persona.edad)

# Ejemplo 4
'''Con la palabra ayuntamiento devolver las letra que no tengan aeiuo'''


def consonantes(letras):
    return letras not in 'aeiou'


palabra = ''.join(list(filter(consonantes, 'ayuntamiento')))
print(palabra)
