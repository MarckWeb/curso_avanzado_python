import traceback
# sumar los numeros de una lista
datos = ['1', '2', 'tres', '4', '5']
suma = 0

for i in range(len(datos) + 1):
    try:
        # acceder al dato
        dato = datos[i]

        # lo convierto a numero
        numero = int(dato)

        # mostrar el numero obtenido
        print('Numero:' + numero)

    except (IndexError, ValueError, TypeError, BaseException) as ex:
        print('Error de tipo: ', type(ex))
        print('Mensaje del error: ', ex)
        traceback.print_exc()
    else:
        # sumar el numero
        suma += numero
print('Suma:', suma)
