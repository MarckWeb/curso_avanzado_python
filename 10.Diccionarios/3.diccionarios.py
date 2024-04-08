alumnos = {'Juan': 6.4, 'Maria': 8.3, 'Luis': 6.4, 'Adolfo': 7.1, 'Maria': 9.3}

# Recorrer un diccionario

for alumno in alumnos:  # solo me devuelve las claves
    print(alumno, alumnos[alumno])


for item in alumnos.items():
    print(item)  # Cada item es una tupla (clave, valor)

for clave, valor in alumnos.items():
    print(clave, ':', valor)


# Otras formas de crear diccionarios
alumnos = dict()
alumnos = {}
# alumnos = dict([('Juan', 6.4), ('Maria', 9.3), ('Luis', 6.4), ('Adolfo', 7.1)])
alumnos = dict(Juan=6.4, Maria=9.3, Luis=6.4, Adolfo=7.1)
print(alumnos)

# Eliminar todos los elemntos
alumnos.clear()
print(alumnos)


'''
   -Crear una lista con las vocales
   - Utilizar compresion, crear el diccionario donde:
   --> la clave es el indice de la lista
   --> el valor es la letra
'''

vocale = ['a', 'e', 'i', 'o', 'u']
vocales_dic = {}
for i in range(len(vocale)):
    vocales_dic.update({i: vocale[i]})
    # vocales_dic[i] = vocale[i]
print(vocales_dic)

# Compresion
rsultado = {i: vocale[i] for i in range(len(vocale))}
print(rsultado)


# alumnos['Pepito'] = 3.5
# print(alumnos)
# 2da solucion:
lista_vocales = ["a", "e", "i", "o", "u"]
dict_vocales = {vocal: lista_vocales.index(vocal) for vocal in lista_vocales}
print("dict_vocales", dict_vocales, type(dict_vocales))

# 3da solucion:
vocales = "aeiou"
list_vocales = [vocal for vocal in vocales]
diccionario_vocales = {list_vocales.index(item): item for item in list_vocales}
print(diccionario_vocales)

# 4da solucion:
VOCALES = ['a', 'e', 'i', 'o', 'u']
diccionario = {letra[0]: letra[1] for letra in enumerate(VOCALES)}
print(diccionario)


'''
Obtener un diccionario a partir de utilizar la funcion zip
   - ziperar un alista con lenguajes de programacion
   - una lista con las versiones
'''
lenguaje = ['JS', 'TS', 'PY', 'C#']
version = [2.2, 1.01, 1.2, 5.02]
resultado = {}
for lenguaje, version in zip(lenguaje, version):
    resultado.update({lenguaje: version})
print(resultado)

# COMPRIMIDO
rsdo = {lenguaje: version for lenguaje, version in zip(lenguaje, version)}
print(rsdo)

# lista_lenguajes = ['JS', 'TS', 'PY', 'C#']
# lista_version = [2.2, 1.01, 1.2, 5.02]
lista_zip = dict(zip(lenguaje, version))
print(lista_zip)
