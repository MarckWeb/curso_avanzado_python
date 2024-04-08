# Para mostrar la pila de llamadas nesecitamos el modulo traceback (mensaje de error que sale en la terminal)
import traceback
try:
    dividendo = int(input('Introduce el dividendo: '))
    divisor = int(input('Introduce el divisor: '))
    resto = dividendo // divisor

except ValueError as error:
    # si es un error value, es decir texto enves de numero
    print('Error: debe ser un valor numerico')
    print(error)
    print(type(error))
    traceback.print_exc()
except ZeroDivisionError as e:
    # si el numero ingresado es cero
    print('Error: el divisor no puede ser cero')
    print(e)

except BaseException as ex:
    # si existe otro tipo de error
    print('otro tipo de error')
    print(type(ex))
    print(ex)
else:
    # si no hay errores
    print('Resultado', resto)

finally:
    # se ejecuta siempres haya error o no
    print('------FIN-----')
