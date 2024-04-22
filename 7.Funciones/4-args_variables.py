# funcion con numeros variable de argumentos, cuantoa numeros como parametro

def sumar(*numeros):
    print(numeros)
    suma = 0
    for num in numeros:
        suma += num
    return suma


print(sumar())
print(sumar(1, 2, 5, 6, 5))
print(sumar(1, 2, 5, 6, 5, 5, 5, 8, 8))
# print(sumar('hoal', 'quetal')) TypeError: unsupported operand type(s) for +=: 'int' and 'str'


# craer una funcion que recibe el nombre del alumno y las notas de las asignaturas en las que se ha matriculado
# retornar la nota media del alumno
# mostrar el nombre y la media recibida de la funcion
# en el caso de tener varios parametros si un de ellos es variable debe ir al final

def procesar_notas(nombre, *notas):
    # si no tiene * -> TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
    nota_media = sumar(*notas)/len(notas)
    return nombre + ' : ' + str(nota_media)


print(procesar_notas('Carlos', 5, 8, 7, 6, 4, 10))

tupla = (1, 2, 3, 4, 5)
# print(sumar(tupla))  # envio un solo parametro que es una tupla de numeros
print(sumar(*tupla))

for i in tupla:
    print(i)
