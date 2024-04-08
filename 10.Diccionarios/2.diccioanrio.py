alumnos = {'Juan': 6.4, 'Maria': 8.3, 'Luis': 6.4, 'Adolfo': 7.1, 'Maria': 9.3}

# Ordenar el diccionario según los valores de forma descendente
# Crear una lista de tuplas a partir del diccionario
lista_alumnos = [(nombre, calificacion)
                 for nombre, calificacion in alumnos.items()]

# Ordenar la lista de tuplas según las calificaciones de forma descendente


def obtener_calificacion(item):
    return item[1]


lista_alumnos_ordenada = sorted(
    lista_alumnos, key=obtener_calificacion, reverse=True)

# Crear un nuevo diccionario ordenado a partir de la lista ordenada de tuplas
alumnos_ordenados = {nombre: calificacion for nombre,
                     calificacion in lista_alumnos_ordenada}

print(alumnos_ordenados)


# Funcion enumerate-. la funcion enumerate retorna el indice y el elemento de ese indice
lista = ['a', 'e', 'i', 'o', 'u']
resultado = {}
for clave, valor in enumerate(lista):
    print(clave)
    print(valor)
    resultado.update({clave: valor})
print(resultado)
