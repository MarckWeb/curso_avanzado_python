
'''Para utilizar reduce hay que importarlo'''
from functools import reduce

# Ejemplo 1
'''Con una lista de nuemros devolver la suma'''
numeros = [3, 8, 2, 1, 7]
resultado = reduce(lambda acu, num: acu + num, numeros)
print('Suma:', resultado)

# Ejemplo 2
'''Con una lista de nombres, retornar una cadena con los nombres en mayuscula y separador por -'''
nombres =['Juan', 'Pedro', 'Carlos']
print(reduce(lambda acum, nombre: acum.upper() + ' - ' + nombre.upper(), nombres))