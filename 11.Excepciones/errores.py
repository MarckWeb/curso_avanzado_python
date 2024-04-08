#
# # se paso un texto ValueError: invalid literal for int() with base 10: 'texto'
# print(numero1)

# try-except-else-finally
numero1 = 0
try:
    # las sentencia que podrias causar error
    numero1 = int(input('Introduce un numero entero: '))
except:
    # capturar el error para que el programa no termine
    print('Error: debe ser un numero entero')
else:
    # solo se ejecuta si no ha habido errores
    print('Correcto, has introducido un numero entero')
finally:
    # siempres se va a ejecutar este bloque haya errores o no
    print('Numero: ', numero1)
