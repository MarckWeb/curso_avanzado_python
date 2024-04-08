mesestraducidos = {
    "Enero": "January",
    "Febrero": "February",
    "Marzo": "March",
    "Abril": "April",
    "Mayo": "May",
    "Junio": "June",
    "Julio": "July",
    "Agosto": "August",
    "Septiembre": "September",
    "Octubre": "October",
    "Noviembre": "November",
    "Diciembre": "December",
}
print(mesestraducidos["Noviembre"])
print(mesestraducidos["Mayo"])


# diccionarios: tiene los elementos como 'clase':'valor'
# No tiene indices y se accede a los elementos a traves de si clave entre corchetes
# A partir de 3.7 se garantiza el orden de entrada
# las claves nose pueden repetir, se sobreescribe el valor
# los valores si se pueden repetir
# se crean con {}
# si se repite la clave, se sobreescribe el valor

alumnos = {'Juan': 6.4, 'Maria': 8.3, 'Luis': 6.4, 'Adolfo': 7.1, 'Maria': 9.3}

# ver el tipo de dato
print(type(alumnos))  # <class 'dict'>

# Mostrar solo los nombres de los alumnos (claves)
print(alumnos.keys())  # dict_keys(['Juan', 'Maria', 'Luis', 'Adolfo']


# Mostrar solo las notas de los alumnos(valores)
print(alumnos.values())  # dict_values([6.4, 9.3, 6.4, 7.1])

# Mostrar los elementos que tengo en el diccionario
# retornar una lista de tuplas
# dict_items([('Juan', 6.4), ('Maria', 9.3), ('Luis', 6.4), ('Adolfo', 7.1)])
print(alumnos.items())

# Operadores de pertenencia in y not in
print('Maria' in alumnos)
print('Paco' not in alumnos)

'''
Accedemos a los elementos pro su clave al no tener indice
Buscamos a luis
'''
print(alumnos['Luis'])
# print(alumnos['Luisss']) # Error si no lo encuentra KeyError: 'Luisss'
# print(alumnos.get('Luisss'))  # si no lo encuentra devuelve None
print(alumnos.get('Luis'))

# Borra un elemento
# del alumnos['Adolfoss']  # Error si no lo encuentra KeyError: 'Adolfoss'
# 1ra forma
print(alumnos.__delitem__('Adolfo'))
# 2da forma
# del alumnos['Adolfo']
print(alumnos)


# Agregar nuevos elemento
alumnos['Pepito'] = 3.5
print(alumnos)

# Otra forma de agregar elemntos
alumnos.update({'David': 10})

# Modificar el valor de un elemento
alumnos['Pepito'] = 5
print(alumnos)

# Eliminar el ultimo elemento
alumnos.popitem()
print(alumnos)

# Eliminar un elemento por su clave y retorna su valor, (verificar guardando en una variable)
# si no existe devuleve KeyError: 'clave'
alumnos.pop('Juan')
print(alumnos)


# Ordenar el diccioanario
# Ordena segun el alfabeto de la primera letra da la palabra
# print(sorted(alumnos))  # ascendente
print(sorted(alumnos.keys()))  # ascendente
print(sorted(alumnos, reverse=True))  # descendente

# Ordena segun los valores del diccionario
print(sorted(alumnos.values()))  # ascendente
print(sorted(alumnos.values(), reverse=True))  # descendente
