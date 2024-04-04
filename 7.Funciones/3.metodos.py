
# primer caso de importacion

# import modulo
# modulo.funcion(argumento)

from random import randint as rnd
from random import uniform
# import math
from math import pi, e

# print(math.sin(0))

# segundo caso de importacion

# from modulo import funcion
# funcion(argumento)


print(uniform(0, 1))
print(uniform(0, 10))

# tercer caso de importacion

# from modulo import funcion as mifun
# mifun(argumento)


print(rnd(5, 10))

# Ejeecicios

lanzamiento = rnd(1, 6)
if lanzamiento < 4:
    print(pi * lanzamiento)
else:
    print(e * lanzamiento)


# /*///
def funcion(x):
    n = 3
    return not bool(x % n)


print(funcion(9))
print(funcion(10))

d = funcion(2)


def funcion(n):
    a = n ** 3
    b = a ** 2
    c = b + 100
    d = 5 * c
    return print(d)


cantidad = 0


sumando = 10


def sumador(n):
    n += sumando
    return n


print(sumador(5))
print(sumando)
