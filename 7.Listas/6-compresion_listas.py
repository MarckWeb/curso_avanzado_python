# Se trata de comprimir, de hacer un codigo largo a una fila

row = []
for i in range(8):
    row.append(i)

print(row)

"""Lista Comprimida"""
fila = [i for i in range(8)]
print('comprimido', fila)


# Ejemplo 1
lista_palabras = ['casa', 'mesa', 'manzana', 'pijama']
longitud_palabras = []

for palabra in lista_palabras:
    longitud_palabras.append(len(palabra))

print(longitud_palabras)

print('----FIN---')
"""Lista Comprimida"""
lista = [len(palabra) for palabra in lista_palabras]
print(lista)
