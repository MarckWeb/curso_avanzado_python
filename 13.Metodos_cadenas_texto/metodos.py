'''
Para manejar cadenas de texto podemos hacer uso de las siguientes funciones:
• Función capitalize
• Función upper
• Función lower
• Función len
• Función isalnum
• Función isalpha
• Función isdigit
• Función islower
• Función isupper
• Funciónes lstrip, rstrip, strip
• Funciones max y min
• Funcion replace
• Función swapcase
• Función split
'''

cadena_de_texto = 'bienvenidos al curso de Python'
# Función capitalize() => Pone la primera letra, solo la primera, en mayúsculas.
print('Capitalize ->', cadena_de_texto.capitalize())

# poner la primera letra de cada palabra en mayuscula
print('title() ->', cadena_de_texto.title())

# Función upper() => Pone en mayúsculas toda la cadena de texto
print('upper() ->', cadena_de_texto.upper())

# Función lower() => Pone en minúsculas toda la cadena de texto.
print('lower() ->', cadena_de_texto.lower())

# Funcion len() => Permite saber el número de caracteres que componen la cadena de texto.
print('len()', len(cadena_de_texto))

# Función isalnum() => Comprueba si todos los caracteres que componen la cadena de texto
# son alfanuméricos o no. Devuelve un valor booleano.
'''
los caracteres del punto y del espacio en blanco que contienen las
cadenas primera y cuarta no son caracteres alfanuméricos.
'''
print('Alfanumerica:', cadena_de_texto.isalnum()) # false por que tiene espacio en blanco
print('Alfanumerica:', "caracola12345".isalnum()) # false por que tiene espacio en blanco


# Función isalpha() =>  Comprueba si todos los caracteres de la cadena de texto son caracteres alfabéticos.
#  Ni los números, ni los puntos ni los espacios en blanco son caracteres alfabéticos,
# únicamente las letras componen el conjunto de caracteres alfabéticos.
print('Alfanumerica:', cadena_de_texto.isalpha()) # false pro que tiene espacio en blanco
print('Alfanumerica:', "caracola".isalpha()) # true
print('Alfanumerica:', "caracola12345".isalpha()) # false
print('Alfanumerica:', "12345".isalpha()) # false


# Función isdigit() => Comprueba si todos los caracteres de la cadena de texto son caracteres numéricos.
print('Numerica:', cadena_de_texto.isdigit()) # false no tenemos ningun numero
print('Numerica:', "12345".isdigit()) # true
print('Numerica:', "12  345".isdigit()) # false
print('Numerica:', "12.345".isdigit()) # false


# Funcion isdecimal() => solo caracteres 0-9 y permite unicode
print("Numerica:", '12345'.isdecimal()) #true
print("Numerica:", '12.345'.isdecimal()) # false
print("Numerica:", '00011101'.isdecimal()) # true

# Función islower() => Comprueba si todos los caracteres que componen la cadena están en minúscula.
# retorna un valor  en booleano
print('islower():', cadena_de_texto.islower()) # false por la P de python
print('islower():', 'hola'.islower()) # true
print('islower():', 'hola12345'.islower()) # true
print('islower():', '12345hola'.islower()) # true

# Función isupper() => Comprueba si todos los caracteres que componen la cadena de texto están en mayúscula.
# retorna un valor  en booleano
print('isupper():', cadena_de_texto.isupper()) # false solo la P de python es mayuscula
print('isupper():', 'HOLA'.isupper()) # true
print('isupper():', 'HOLA12345'.isupper()) # true
print('isupper():', '12345HOLA'.isupper()) # true

