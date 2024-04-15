# la funcion reduce le pasamos un elemento iterable y retorna un solo resultado
# la funcion pasada como argumento ha de recibir
#       - una variabe que actua como acumulador
#       - el item recibido
# syntaxis: reduce (funcion, iterable)
'''Para utilizar reduce hay que importarlo'''
from functools import reduce
# Ejemplo 1
'''Con una lista de nuemros devolver la suma'''
numeros = [3,8,2,1,7]
def sumar (acu, num):
    # la primera vez que se invoca a la funcion, el primer item se guarda como acumulador
    # al realizar la suma el resultado se almacena en acum para siguientes iteraciones
    return acu + num
print('Suma', reduce(sumar, numeros))

# Utilizando lambda

from functools import reduce

numeros = [3, 8, 2, 1, 7]

# Utilizar reduce con una función lambda para sumar los números
resultado = reduce(lambda acu, num: acu + num, numeros)

print('Suma:', resultado)


# Ejemplo 2

'''Con una lista de nombres, retornar una cadena con los nombres en mayuscula y separador por -'''
nombres =['Juan', 'Pedro', 'Carlos']
def concatenar(acum, nombre):
    return acum.upper() + ' - ' + nombre.upper()

print(reduce(concatenar, nombres))