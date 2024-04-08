try:
    dividendo = int(input('Introduce el dividendo: '))
    divisor = int(input('Introduce el divisor: '))
    resto = dividendo // divisor
except ValueError:
   # si es un error value, es decir texto enves de numero
    print('Error: debe ser un valor numerico')

except ZeroDivisionError:
   # si el numero ingresado es cero
    print('Error: el divisor no puede ser cero')
except:
   # si existe otro tipo de error
    print('otro tipo de error')
else:
   # si no hay errores
    print('Resultado', resto)

finally:
    print('------FIN-----')
