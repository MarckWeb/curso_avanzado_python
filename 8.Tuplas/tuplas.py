"""
   Sobre todo se puede utilizar las tuplas par ahacer refrencia a un listado de cosas que no cambian, es decir los mese del ano, los signos horoscopo, puntos cardinales, etc
"""
# tuplas: son colecciones ordenadas ( con indice ) pero inmutables
# si se permiten elementos duplicados
# se crean utilizando los parentesis
# son como las variables constantes que no cambian de valor.


# Crear una tupla con los dias de la semana
dias = ('Lunes', 'Martes', 'Miercoles',
        'Jueves', 'Viernes', 'Sabado', 'Domingo')

# mostrar la tupla por pantalla
print(dias)

# mostrar el tipo
print(type(dias))


# Formas de crear una tupla vacia
tuple_vacia = ()
tupla_vacia = tuple()

# Formas de recorrer una tupla

for dia in dias:
    print(dia, end=' ')
print()

for i in range(len(dias)):
    print(dias[i], end=' - ')
print()

# Mostrar el miercoles
print('Miercoles', dias[2])  # al indice siempres se accede con corchetes

'''ERRORES!!!'''

# del dias[0]      TypeError: 'tuple' object doesn't support item deletion
# dias[0] = 'otro dia'     TypeError: 'tuple' object does not support item assignment
# dias.append('otro dia')  AttributeError: 'tuple' object has no attribute 'append'


# Cuantos elementos hay en la tupla
print('Longitud de dias es:', len(dias))


# Como puede haber elementos repetidos, contar cuantos lunes hay

print('Cuantos lunes hay en la tupla?', dias.count('Lunes'))

# en que posicion esta el viernes, si hay varios viernes me devuelve el primero en la tupla
print(dias.index('Viernes'))
print(dias.index('Viernes', 2))  # busca apartir del indice 2

# concatenar tuplas
# otra_tupla = dias + ('otro sabado')
# mas_tupla = dias + [8, 9, 10] TypeError: can only concatenate tuple (not "list") to tuple
# TypeError: can only concatenate tuple (not "str") to tuple

#
otra_tupla = dias + (1, 2, 3, 4, 5)  # ojo no se mofica la tupla dias
print(otra_tupla)

otro_sabado = dias + ('otro sabado', )
print(otro_sabado)

# el orden es importante
otro_sabado = ('otro sabado', ) + dias
print(otro_sabado)

final = (1, 2, 3, 4)+tuple([1, 2, 3, 4])
print(final)

# tuplas de 2 dimenciones

# tener cuidado con los strign ('Maria') en las tuplas, seran tuplas si tiene coma ('Maria',) al final
tupla_2d = (('Juan', 27, 'Soltero'), ('Maria',),
            ('Luis', 43, 'Casado', '2 hijos'))
for empleo in tupla_2d:
    for dato in empleo:
        print(dato, end=' ')
    print()

# Uso de slicing en tuplas

print(dias[1:4])
print(dias[::-1])

'''Operadores de pertenencia in y not in'''

print('Jueves' in dias)
print('Domingo' not in dias)


# Convertir una tupla en lista

lista_dias = list(dias)
print(lista_dias)

lista_de_numeros = tuple([1, 2, 2, 4, 5])
print(lista_de_numeros)
