# Ejercicios Strings

# 1 - Printa por pantalla el string "Hello World!"
saludo = 'hello world'
print(saludo)

# 2 - Printa por pantalla el string "La mente no es un vaso que llenar sino una lámpara que encender"

frase = 'La mente no es un vaso que llenar sino una lámpara que encender'
print(frase)

# 3 - Printa por pantalla la primera letra del string "The Bridge"
texto = 'The Bridge'
print(texto[0])

# 4 - Printa el string "Hello World!" desde atrás hacia adelante

print(saludo[::-1])

# 5 - Printa desde el carácter dos hasta el carácter seis (incluido) del string "Be water my friend"
persona = 'Be water my friend'
print(persona[2:])

# 6 - Crea una variable con el string "No puedes bañarte dos veces en el mismo río" y muéstralo por pantalla con todas sus letras en mayúsculas

frase2 = 'No puedes bañarte dos veces en el mismo río'
print(frase2.upper())

# 7 - Pasa el string "HELLO WORLD!" a minúsculas
print(saludo.upper())
print(saludo.lower())

# 8 - Printa el string " Tengo espacios " sin los espacios al principio y al final
texto_espacio = ' Tengo espacios '
print(texto_espacio)
print(texto_espacio.strip())
# 9 - Printa el string "Tengo varios espacios" en forma de lista separado por los espacios, donde cada elemento de la lista es una palabra

convertir_texto_en_lista = "Tengo varios espacios"
print(convertir_texto_en_lista.split())

# 10 - Crea una variable con el string "The Bridge". Tras esto cambia el primer carácter de esta variable por una "Q"
cambio_de_caracter = texto.replace('T', 'Q')

# 11 - Muestra por pantalla el tipo de la variable que has creado en el punto 10 de este ejercicio

print(cambio_de_caracter)