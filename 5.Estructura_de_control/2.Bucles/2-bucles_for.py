nombres = ['Luis', 'Jorge', 'Maria', 'Laura', 'Pedro']
print(nombres[2])  # muestra en nombre del indice

for indice in range(len(nombres)):
    print(nombres[indice], end=' - ')
print('\n-----FIN-----')

# mostrar los elementos de la lista empezando por el ultimo

for n in range(len(nombres) - 1, -1, -1):
    print(nombres[n], end=' -> ')
print('\n-----FIN-----')


"""mostrar las tablas de multiplicar"""

for a in range(1, 11):
    print('***Tabla del:', a, '***')
    for b in range(1, 11):
        print(str(a), 'X', str(b), '=', a*b)


"""
   crear una lista con 20 numero aleatorios
   mostrar por consola solo los numeros pares
"""

numeros = [8, 4, 100, 31, 5, 45, 7, 8, 9, 10,
           11, 12, 1, 14, 11, 300, 17, 18, 19, 20]

for num in numeros:
    if num % 2 == 0:
        print('par', num)
print('***fin')
