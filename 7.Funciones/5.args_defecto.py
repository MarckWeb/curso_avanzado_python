def datos_trabajador(nombre, estadoCivil='Soltero', sueldo=21000):
    return nombre + ' esta ' + estadoCivil + ' gana ' + str(sueldo)


print(datos_trabajador('Jose'))
# print(datos_trabajador('David',  1800)) interpreta que 1800 es estado civil TypeError: can only concatenate str (not "int") to str
print(datos_trabajador('Jose', sueldo=21000))
print(datos_trabajador('Jose', estadoCivil='Casado'))
print(datos_trabajador('Jose', 'Casado', 35000))


# crear una funcion que recibe dos parametros:
#   - datos como numero variable de argumentos
#   - caracter separador optional


def numeros(separador='|', *datos):
    return separador.join([str(dato) for dato in datos])


print(numeros(' <> ', 1, 2, 3, 5, 9, 9, 8))
print(numeros(' - ', 'carlos', 'david', 'juan', 'bob'))
