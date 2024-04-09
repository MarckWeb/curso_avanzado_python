import random

# para generar numeros aleatorios entre 9 y 1 pero sin llegar a 1
# modulo.recurso
print(random.random())
print(random.random())
print(random.random())

# Para generar numeros aleatorios cambiando la semilla
random.seed()
print(random.random())
random.seed(3)
print(random.random())
random.seed(3)
print(random.random())

random.seed(10)
for id in range(4):
    print(random.random())
random.seed()
print("Numeros entre 0 y 50", random.randrange(50))
print("Numeros entre 10 y 50", random.randrange(10,50))
print("Numeros entre 10 y 50 solo pares", random.randrange(10,50, 2))

# randint si que lo incluye
print('Numeros del 20 al 30: ', random.randint(20,30)) # coge el valor 30 tambien

# randint no tiene estep
# print('Numeros 20 al 30 solo pares', random.randint(20, 30, 2))

# Quiero obtener 5 numero aleatorios
for i in range(5):
    print('Numero aleatorio:', random.randint(20,30))

    '''Impotante los metodos randrange y randint pueden devolver numeros repetidos'''

# Generar numeros aleatorios sin duplicados
'''
El choice()método devuelve un elemento seleccionado aleatoriamente de la secuencia especificada.

La secuencia puede ser una cadena, un rango, una lista, una tupla o cualquier otro tipo de secuencia.
'''
# Choise-. retorna un elemento aleatorio de la secuencia
print('Choise', random.choice((1,2,3,4,5,6,7,8,9)))


# Sample: retorna el numero de elemntos especificados aleatorios
# de la secuencia pasada como argumentos
# no recibe un conjunto
print('Sample', random.sample((1,2,3,4,5,6,7,8,9), 2))
print('Sample', random.sample([1,2,3,4,5,6,7,8,9], 3))
print('Sample', random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], 1))
print('Sample', random.sample(range(10), 1))
