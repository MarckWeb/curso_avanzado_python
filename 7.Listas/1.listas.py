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

# acceso a los elementos de la lista
# indice positivo comienza por el primero

print(lista_vacia[2])

# indice negativo comienza pro el ultimo, por la derecha
print(lista_vacia[-2])
print(lista_vacia[len(lista_vacia) - 2])

# agregar elementos al final -> append
lista_vacia.append('morena')
print(lista_vacia)

# agregar elementos en una determinada posicion -> insert
lista_vacia.insert(0, 1.70)
print(lista_vacia)

# agregar varios elementos a la vez -> extend
lista_vacia.extend([1, 2, 3])
print(lista_vacia)

# Eliminar un elemento de la lista
del lista_vacia[0]
print(lista_vacia)

# Modificar un elemento
lista_vacia[-5] = '1 hijo'
print(lista_vacia)


"""Ejercicios
    Crear una lista llamada colores con los valores rojo, verde y azul
    Mostrrar el tipo de la variable colores
    Mostrar el contenido de la lista
    Recorrer la lista con for in
    Recorrer la lista con for in a traves de indice
    Mostrar en la consola el color verde (posicion)
    Borra el color azul
    Crear nueva lista mas_colores
    en la nueva lista concatenar colores y otra lista con estos: blanco, negro, rosa, azul,
    Añadir el color naranja al final
    Añadir el color marron al principio
    mostrar la longitud de la lista mas_colores
    Mostrar el antepenultimo elemento
"""

colores = ['rojo', 'verde', 'azul']
print('El tipo de la variable colores es: ', type(colores))
print('Contenido de la lista:', colores)

for item in colores:
    print(item, end=', ')
print('\n---FINAL---')

for indice in range(len(colores)):
    print(colores[indice])
print('\n---FINAL---')

print('Posicion del color verde es:', colores[1])
print('\n---FINAL---')

# Borra por posicion
del colores[2]
print(colores)

# Borra por posicion
# colores.remove('azul')
# print(colores)
print('\n---FINAL---')

mas_colores = []
mas_colores = colores + ['blanco', 'negro', 'rosa', 'azul']
print(mas_colores)
print('\n---FINAL---')

mas_colores.append('naranja')
print(mas_colores)
print('\n---FINAL---')

mas_colores.insert(0, 'marron')
print(mas_colores)
print('\n---FINAL---')


print('La longitud de mas colores es: ', len(mas_colores))
print('\n---FINAL---')

print('El antepenultimo de la lista colores es: ',
      mas_colores[len(mas_colores) - 3])
print('El antepenultimo de la lista colores es: ', mas_colores[- 3])
print('\n---FINAL---')


# mostrar el indice donde se encuentra el color azul
print(mas_colores.index('azul'))
# print(mas_colores.index('amarillo')) #ValueError: 'amarillo' is not in list
mas_colores.extend(['azul'])
print(mas_colores.index('azul', 7))

# Mostrar cuantos elementos azul tenemos
print('cuantos azules tenemos', mas_colores.count('azul'))

# Mostrar la lista invertida
print('Lista original', mas_colores)

mas_colores.reverse()
print('lista invertida', mas_colores)

# Ordenar lalista por el metodo short-. modifica el original
mas_colores.sort()  # orden ascendente
print(mas_colores)
# sorted es otra funcion que se pasa un parametro pero hace una copia, fijar como que le psas un array y devuleve otro array, pero no modifica al original
print(sorted(mas_colores))

mas_colores.sort(reverse=True)  # orden descendente
print(mas_colores)
print(sorted(mas_colores, reverse=True))  # sorted es otra funcion

# eliminar todos los elementos de la lista
mas_colores = []
mas_colores.clear()
print(mas_colores)


"""SLICES [start:stop:step] [donde_empieza : donde_termine - 1]"""

# Mostrar todos los elemento de la lista
print('Todos', lista_vacia[:])

# Mostrar los ultimos 4 de la lista
print('Ultimos 4', lista_vacia[-4:])


# Mostrar desde el tercero al sexto
print('Tercero al sexto:', lista_vacia[3:7])

# Mostrar desde el sexto al tercero
print('Sexto al tercero:', lista_vacia[7:3])  # sale vacio
print('Sexto al tercero:', lista_vacia[7:3:-1])  # asi si que funciona

# Siempre se recorre de izquierda a derecha
# Mostrar desde el sexto al tercero
print('Sexto al tercero:', lista_vacia[-6:2:-1])
print('Penultimo al quinto pro derecha:', lista_vacia[-2:-6:-1])


# Mostrar todo los elementos de la lista en orden inverso
print('todos en inverso', lista_vacia[::-1])

# Mostrar todo los elementos de la lista de 2 en dos
print('todos en inverso', lista_vacia[::2])

# Mostrar todo los elementos de la lista en orden inverso de 2 en 2
print('todos en inverso', lista_vacia[::-2])
