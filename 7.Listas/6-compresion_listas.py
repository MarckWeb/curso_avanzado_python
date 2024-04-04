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
