# las variables en python con sensibles en minuscula y mayuscula (nombre y NOMBRE ) no son iguales.

# FORMA CONVENCIONAL
nombre = 'david'
nombre_completo = 'David marck'

# OTRAS FORMAS NO CONVENCIONALES

Apellido = 'marck'
NombreYApellido = 'david marck'
enviarSaludo = 'hola mundo'


# VARIABLES CON ENTRADA DE DATOS
# leer la entrada hecha desde el teclado
nombre = input('ingresa tu nombre:')
print(nombre)

# También se puede llamar a la función input sin un parámetro:

print('Cual es tu nombre?')
mi_nombre = input()
print(mi_nombre)


# Lectura de números como entrada
n1 = input('Ingresa un número: ')
print(type(n1))  # valor de "5" mostraría <class 'str'>

# Para convertir el valor en una variable de entero verdadera, se puede usar la función int()
n2 = int(input('Ingresa un número: '))
print(type(n2))
