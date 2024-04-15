'''Filter en lambda'''
# Ejemplo 1
lista = [1, 2, 3, 4, 5, 6, 8]
pares = filter(lambda x: x % 2 == 0, lista)
print(list(pares)) # Devuelve: [2, 4, 6, 8]

# ejemplo 2
'''Dado un diccionario con los nombres y notas de cada alumno, filtrar para quedarnos solo con los aprobados'''

alumnos = {'Juan': 6.4, 'Maria': 3.3, 'Luis': 6.4, 'Adolfo': 7.1, 'Pedro': 4.3}
aprobados = dict(filter(lambda item: item[1] >= 5, alumnos.items()))
print(aprobados)

#Ejemplo 3
'''Partiendo de una lista de instancias de Persona, filtrar para quedarnos solo con los mayores de edad'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

personas = [
    Persona("Juan", 25),
    Persona("Maria", 10),
    Persona("Carlos", 40),
    Persona("Pedro", 17)
]


personas_mayores = list(filter(lambda persona: persona.edad >= 18, personas))

for persona in personas_mayores:
    print(persona.nombre, persona.edad)

#Ejemplo 4
'''Con la palabra ayuntamiento devolver las letra que no tengan aeiuo'''

palabra = ''.join(list(lambda letra: letra not in 'aeiuo', 'ayuntamiento'))
print(palabra)