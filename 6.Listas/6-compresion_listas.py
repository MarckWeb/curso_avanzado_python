# Se trata de comprimir, de hacer un codigo largo a una fila

row = []
for i in range(8):
    row.append(i)

print(row)

"""Lista Comprimida"""
fila = [i for i in range(8)]
print('comprimido', fila)

# Squares
squares = [x ** 2 for x in range(10)]
print('SQUARES', squares)

# Twos
twos = [2 ** i for i in range(8)]
print('twos', twos)

# Ejemplo 1
lista_palabras = ['casa', 'mesa', 'manzana', 'pijama']
longitud_palabras = []

for palabra in lista_palabras:
    longitud_palabras.append(len(palabra))

print(longitud_palabras)

"""Lista Comprimida"""
lista = [len(palabra) for palabra in lista_palabras]
print(lista)
print('----FIN---')


# Ejemplo 2
"""Lista Comprimida"""
num_pares = [num for num in range(0, 12) if num % 2 == 0]
print(num_pares)

"""Lista normal"""
pares = []
for n in range(0, 12):
    if n % 2 == 0:
        pares.append(n)

print(pares)
print('----FIN---')

# Ejemplo 3

# dado ese vector mostrar solo los numeros impares
'''BUCLE NORMAL'''
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vector_pares = []
for fila in vector:
   #  print(fila)
    for col in fila:
        if col % 2 != 0:
            vector_pares.append(col)
print('normal', vector_pares)
print('----FIN---')

'''BUCLE CON UNA COMPRESION'''
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vector_pares = []
for fila in vector:
    #  print(fila)
    row = [col for col in fila if col % 2 != 0]
    vector_pares.append(row)
print('mid compresion', vector_pares)
print('----FIN---')

'''BUCLE CON TOTAL COMPRESION'''
pares = [col for fila in vector for col in fila if col % 2 != 0]
print('compresion', pares)
print('----FIN---')


# devolver la lista de 2 dimenciones: [[1,3], [5], [7,9]]

pares_dos_dimeciones = [
    [num for num in fila if col % 2 != 0]for fila in vector
]
print(pares_dos_dimeciones)

# lista de 3 dimenciones

cubo = [[[0, 1], [2, 3], [4, 5]], [[6, 7], [8, 9], [10, 11]]]

cobo_dos = [num for fila in cubo for col in fila for num in col]
print(cobo_dos)
print('----FIN---')

# Ejemplo 4
# con esta matriz devolver una lista con 2 filas: [[1,3,5,7],[2,4,6,8]]

matriz = [[1, 2], [3, 4], [5, 6], [7, 8]]
matriz_par_impar = [[], []]
for fila in matriz:
    matriz_impar = []
    matriz_par = []
    for i in range(len(fila)):
      #   print(i)
        if i == 0:
            print(fila[i])
            matriz_par_impar[0].append(fila[i])
        elif i == 1:
            matriz_par_impar[1].append(fila[i])
print(matriz_par_impar)

# 2 solucion

nueva_matriz = []
for i in range(len(matriz[0])):
    nueva_fila = []
    for fila in matriz:
        nueva_fila.append(fila[i])
    nueva_matriz.append(nueva_fila)
print(nueva_matriz)

# solucion en comprension

matriz_nueva = [[fila[i] for fila in matriz] for i in range(2)]
print(matriz_nueva)
