def datos_trabajador(nombre, estadoCivil='Soltero', sueldo=21000):
    return nombre + ' esta ' + estadoCivil + ' gana ' + str(sueldo)


print(datos_trabajador('Jose'))
# print(datos_trabajador('David',  1800)) interpreta que 1800 es estado civil TypeError: can only concatenate str (not "int") to str
print(datos_trabajador('Jose', sueldo=21000))
print(datos_trabajador('Jose', estadoCivil='Casado'))
print(datos_trabajador('Jose', 'Casado', 35000))


# crear una funcion que recibe:
#   - datos como numero variable de argumento
#   - caracter separador opcional, por defecto " | "
#   separador.join(datos)
def unir_datos(*datos, separador=" | "):
    return separador.join(datos)


print(unir_datos('otro', 'a', 'e', 'i', 'o', 'u'))
print(unir_datos('otro', 'a', 'e', 'i', 'o', 'u', separador=", "))
print(unir_datos('otro', 'a', 'e', 'i', 'o', 'u', separador=" "))
print(unir_datos('otro', 'a', 'e', 'i', 'o', 'u', separador=" - "))

# No pongo el keyword separador, interpreta el separador como un dato mas
print(unir_datos('a', 'e', 'i', 'o', 'u', " - "))

# Probar a intercambiar el orden de los argumentos
# SyntaxError: positional argument follows keyword argument
# print(unir_datos(separador=" - ", 'a', 'e', 'i', 'o', 'u' ))

# Probar a intercambiar los parametros en la declaracion de la funcion
# SyntaxError: positional argument follows keyword argument
# print(unir_datos(separador=" - ", 'a', 'e', 'i', 'o', 'u' ))
