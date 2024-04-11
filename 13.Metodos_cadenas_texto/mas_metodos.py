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
print('replace() ->', 'abracadabra'.replace('a', 'A', -1)) # no hace nada ni da error


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

texto = 'bienvenidos al curso de Python'
cadena= 'abracadabra'
# count()
print("# count() - Devuelve el número de apariciones de un substring en el string:")
print('Cuantas "o"?', texto.count('o'))
print('Cuantas "o" a partir del indice 20?', texto.count('o', 20))
print('Cuantas "o" a partir del indice 8 y 20?', texto.count('o', 8, 20))

# ord() => Devuelve el valor Unicode de un carácter:"
print('Valor Unicode de "a":', ord('a'))

# chr() => Devuelve el carácter representado por el valor Unicode:
print('Carácter representado por 97:', chr(97))



# find() => busca por la izquierda y rfind busca por la derecha y retorna la posicion (index)
print('find() ->', cadena.find('a'))
print('find() ->', cadena.find('a', 5))
print('find() ->', cadena.find('a', 5, 8))

print('rfind() ->', cadena.find('a'))
print('rfind() ->', cadena.find('a', -4, -1))


# join() => es útil cuando quieres unir una lista de cadenas con un delimitador específico:
palabras = ["Hola", "mundo", "desde", "Python"]
delimitador = " "
resultado = delimitador.join(palabras)
print(resultado)  # Esto imprimirá: "Hola mundo desde Python"

print('-'.join(['a', 'e', 'i', 'o', 'u'])) # a-e-i-o-u

#FORMATO DE FACTURA
formato_numero_factura = ("Nº 0000-0", "-0000 (ID: ", ")")   #es una tupla de strings
print("275".join(formato_numero_factura))                    #275 es el separador, lo utiliza para unir cada elemento de la tupla

for i  in range(200,209):                          #del 200 al 209 son separadores
    print(str(i).join(formato_numero_factura))

# isspace() => se utiliza para comprobar si una cadena contiene solo espacios en blanco.
# Devuelve True si la cadena contiene solo espacios en blanco y False en caso contrario.
cadena1 = " "
cadena2 = "Hola mundo"
cadena3 = "   "
cadena4 = ""

print(cadena1.isspace())  # Esto imprimirá: True
print(cadena2.isspace())  # Esto imprimirá: False
print(cadena3.isspace())  # Esto imprimirá: True
print(cadena4.isspace())  # Esto imprimirá: False

# center() => se utiliza para centrar una cadena dentro de un ancho especificado.
# La función toma dos argumentos: el ancho total deseado de la cadena y un carácter
# opcional de relleno (por defecto es un espacio).
cadena = "platano"
ancho_total = 10
# rellenara el texto con caracteres para que logre el ancho total
resultado = cadena.center(10, '1')
print(resultado)  # Esto imprimirá: "1platano11"