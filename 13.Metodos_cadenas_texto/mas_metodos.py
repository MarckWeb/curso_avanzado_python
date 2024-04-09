'''
        Funciónes lstrip, rstrip, strip
- Para eliminar los caracteres del comienzo de la cadena tienes que utilizar lstrip,
- para eliminar los caracteres del final de la cadena tienes que utilizar rstrip, y por último,
- para eliminar ambos a la vez tienes que utilizar strip, que hace lo mismo que los dos
  anteriores pero en una sola instrucción.
- dentro de los parentesis se puede colocar el caracter a eliminar
'''

ejemplo= '  hola  caracola  '
print('lstrip() ->', ejemplo.lstrip()) # elimina espacios por defecto
print('lstrip() ->', '******hola  caracola  '.lstrip('*')) # elimina *

print('rstrip() ->', ejemplo.rstrip())
print('rstrip() ->', '----hola  caracola******'.rstrip('*')) # elimina * al final de la cadena

print('strip() ->', ejemplo.strip()) # elimina espaciso de inicio y final


# Funciónes max() y min() =>  permiten conocer el carácter alfabético mayor y menor de la cadena de texto
'''
Cuando usas la función max() o min() con una cadena de texto, 
devuelve el carácter que tiene el mayor valor según su posición en la tabla ASCII. 
En la tabla ASCII, los caracteres numéricos tienen valores más bajos que las letras.
'''
print('Max() ->', max(ejemplo)) # r
print('Max() ->', max('12255Ma')) # a
print('Max() ->', max('012255Ma')) # a
print('Min() ->', min(ejemplo)) # espacio
print('min() ->', min('12255Ma')) # a

# Función replace() =>
# Va a permitir reemplazar caracteres de la cadena de texto por otros caracteres.
#  En el siguiente ejemplo se reemplaza la A por una E.
print('replace() ->', 'abracadabra'.replace('a', 'A')) # reemplaza todas
print('replace() ->', 'abracadabra'.replace('a', 'A', 1)) # reemplaza solo la primera
print('replace() ->', 'abracadabra'.replace('a', 'A', 2)) # reemplaza las dos primeras 'a'


# Función split() =>
# Va a permitir convertir una cadena de texto en una lista de elementos que se encuentran
# separados por espacios en la cadena de texto original.

print('split() ->', ejemplo.split())
print('split() ->', '9/10/2024'.split('/'))

# Función swapcase() =>
# Va a permitir invertir las mayúsculas y minúsculas de la cadena de texto, es decir, las
# mayúsculas pasarán a ser minúsculas y las minúsculas pasarán a ser mayúsculas.

print('swapcase() ->', ejemplo.swapcase())
print('swapcase() ->', 'HoLa MuNdoo'.swapcase()) # hOlA mUnDOO