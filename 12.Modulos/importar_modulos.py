'''Diferentes formas de utilizar modulos'''

# Primera forma
import  math

# Sintaxis: modulo.recurso

print('PI: ', math.pi)

# Segunda forma

from math import pi
print('PI:', pi)

# Tercera forma

from math import pi as num_pi
print('PI:', num_pi)


"""Si queremos importar mas de un recurso"""

from math import pi as n_pi, e as n_e
print('PI:', n_pi)
print('E', n_e)

'''Otra opcion para importar todo el modulo'''
# No nesecitamso poner por delante el nombre del modulo
from math import *
print('pi', pi)
print('e', e)


# mostrar el contenido de un modulo
import math

print(dir(math))
for recurso in dir(math):
    print(recurso)