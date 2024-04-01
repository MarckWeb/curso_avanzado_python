# las variables en python con sensibles en minuscula y mayuscula (nombre y NOMBRE ) no son iguales.

# 📌 FORMA CONVENCIONA
import math
nombre = 'david'
nombre_completo = 'David marck'

# 📌 OTRAS FORMAS NO CONVENCIONALES

Apellido = 'marck'
NombreYApellido = 'david marck'
enviarSaludo = 'hola mundo'

# 📌VARIABLES CON ENTRADA DE DATOS
# leer la entrada hecha desde el teclado
nombre = input('ingresa tu nombre: ')
print(nombre)

# También se puede llamar a la función input sin un parámetro:
print('Cual es tu nombre?')
mi_nombre = input()
print(mi_nombre)

# 📌 CONVERTIR STRING A ENTERO
# Lectura de números como entrada
n1 = input('Ingresa un número: ')
print(type(n1))  # valor de "5" mostraría <class 'str'>

# Para convertir el valor en una variable de entero verdadera, se usa la función int(),
"""
si el valor entero no es un numero:  ValueError: invalid literal for int() with base 10: 'tres'
   ValueError: invalid literal for int() with base 10: '1234tres'
   ValueError: invalid literal for int() with base 10: '12.56'
   ValueError: invalid literal for int() with base 10: 'True'
   Todo valor que no es entero se termina convirtiendo en un error.
"""
n2 = int(input('Ingresa un número: '))
print(type(n2))

# 📌 CONVERTIR STRING A REAL(FLOAT)
# si colocamos un entero, de forma nativa python entiende que tendra 75.0

radio = float(input("Introduce radio del circulo: "))
print("Area del circulo", math.pi * radio ** 2)

# 📌 REDONDEAR NUMEROS
# redondea con 2 decimales
print("Area del circulo", round(math.pi * radio ** 2, 2))

"""
Si el numero se coloca con una coma(,)  ValueError: could not convert string to float: '12,5'
"""

# 📌 CONVERTIR A TEXTO

print('34', type(str(34)))
print('34.12', type(str(34.12)))
print('True', type(str(True)))
