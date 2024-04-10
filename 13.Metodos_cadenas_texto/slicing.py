# las cadenas de texto se consideran listas de caracteres
texto = 'bienvenidos al curso de Python'

# Mostrar solo la palabra bienvenidos
print(texto[0:11])
print(texto.index(' ')) # 11
print(texto[0:texto.index(' ') + 1]) # 11

# mostrar solo al palabra python
print(texto[-6:])
print(texto[texto.index('P'):])

# Mostrar solo la palabra curso
print(texto[15:-10])
print(texto[texto.index('c'): -10])
print(texto[texto.index('c'): texto.index(' ', texto.index('c'))])

# Mostrar todas las letras de la frase de izda a dcha
print(texto[:])

# Mostrar todas las letras de la frase de dcha a izda
print(texto[::-1])

# Mostrar todas las letras de 2 en 2
print(texto[::2])