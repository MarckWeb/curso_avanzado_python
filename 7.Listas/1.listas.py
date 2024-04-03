# listas: colecciones ordenadas de elementos (tiene indice)
# en todas las colecciones podemos tener datos de distinto tipo
# permite tener elementos duplicados
# se crean con corchetes []

lista1 = ['Maria', 'Perez', 20, 'soltera', 'sin hijos']
lista2 = ['estudiante', 'medicina', 28010]

# motrar las listas por consola
print(lista1)
print(lista2)

# Crear una lista vacia

lista_vacia = []

# unir listas

lista_vacia = lista1 + lista2  # el orden es importante
print(lista_vacia)

lista_vacia = lista2 + lista1
print(lista_vacia)

# Longitud de la lista
print('Longitud de la lista:', len(lista_vacia))
