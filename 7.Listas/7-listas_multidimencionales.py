# lista de una dimencion es
numeros = [1, 2, 3, 4, 5]  # un solo indice -> un bucle para recorrer


# lista de 2 dimenciones
# 2 indices (fila, columna) -> 2 bucles
lista_multidimencion = [[2, 7, 4], [8, 1, 6], [3, 9, 5]]
'''
lista de dos dimenciones
      2  7  4
      8  1  6
      3  9  5
'''

for fila in lista_multidimencion:
    for num in fila:
        print(num, sep=' ', end='')
    print()  # es para hacer el salto y que no se muestre seguido la salida

# mostrar suma de la diagonal es decir 2, 1, 5
suma = 0
for fila in range(len(lista_multidimencion)):
    for col in range(len(lista_multidimencion[fila])):
        if fila == col:
            suma += lista_multidimencion[fila][col]
print('Suma de la diagonal:', suma)

# otra solucion
suma_diagonal = 0
print(lista_multidimencion)
lista_multidimencion.reverse()
print(lista_multidimencion)
for i in range(len(lista_multidimencion)):
    suma_diagonal += lista_multidimencion[i][i]

print('paso corto:', suma_diagonal)

# lista de 2 dimenciones no cuadrdas cada fila tiene diferente numero de columna
# 2 indices (fila, columna) -> 2 bucles
matriz = [[2, 7, 4, 1], [8, 1], [3, 9, 5, 6, 0]]

for fila in matriz:
    for num in fila:
        print(num, end=' ')
    print()

print('----FIN----')

# lista de  3 diemnciones -> cubo de rubik
cubo = [[[0, 1], [2, 3], [4, 5]], [[6, 7], [8, 9], [10, 11]]]
for x in cubo:
    for y in x:
        for z in y:
            print(z, end="  ")
