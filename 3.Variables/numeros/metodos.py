import math  # archivo de python

# round()-. redondea un numero a su valor mas proximo
print(round(1.3))
print(round(1.5))
print(round(1.9))

# abd()-. devuleve un valor absoluto es decir -77 = 77
print(abs(-77))
print(abs(55))

# usando math

# muestra el numero mas cercano a su valor hacia arriba si el numero es 1.22 mostrar 2
print(math.ceil(1.22))

# muestra el numero mas cercano a su valor hacia abajo si el numero es 3.999 mostrar 3
print(math.floor(3.999))

# devuleve un valor boolean, si es numero mostra false y es string mostra error, isnan= no es un numero? false -- es un numero
print(math.isnan(23))
# print(math.isnan("23"))

# nos permite elevar un numero a la potencia
print(math.pow(2, 10))

# nos permite sacar la raiz cuadra
print(math.sqrt(36))

"""para mas funciones o metodos de python 
https://docs.python.org/es/3.10/library/math.html"""
