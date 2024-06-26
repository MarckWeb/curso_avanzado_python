
no_olvidar = ['huevos', 'palta', 'lechuga', 'naranjas', 7000]

print(type(no_olvidar))
print(no_olvidar)

# pedido cafeteria = variables dentro de listas

mesa = 5
producto = 'express'
cantidad = 2
costo = 500
pedido = [producto, mesa, cantidad, costo, cantidad * costo]
print(pedido)


# listas dentro de listas
primer_pedido = ['express', 5, 2, 500, 1000]
segundo_pedido = ['corto', 8, 3, 500, 2000]
especial = ['cafe del dia', 10]
pedidos = [primer_pedido, segundo_pedido, especial, True]

print(pedidos)


# listas vacias -.  sirve para poder almacenar d emanera dinamica datos de considerems que debemos manejra en un listado

lista_vacia1 = []
lista_vacia2 = list()
print(lista_vacia1)
print(lista_vacia2)

# Modificar y manipular elementos dentro de las listas

print(no_olvidar[0])
print(no_olvidar[2])

# acceder a trozos o seccion de la lista
# mostra los elemntos de las pocisiones de 1 hasta 4-1
print(no_olvidar[1: 4])

"""slising"""

# lista[inicio : fin : step]
# desde lista [inicio] hasta lista [fin-1], en pasos de step

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# muestra las letras desde el indice 2 hasta el 6
print(letras[2:7])  # [c, d, e, f, g]

# muestra las letras desde el indice 2 hasta el 7, pero de dos en dos
print(letras[2:7:2])  # ['c', 'e', 'g']

# muestra las letras desde el indice 7 hasta el final de la lista
print(letras[7:])  # ['h', 'i', 'j']

# mmuestra las letras desde indice 0 hasta el el 5, pero de 3 en 3
print(letras[:5:3])  # ['a', 'd']

# muestra una lista vacia por que no hay rango desde la posicion 2 hasta la una
print(letras[2:2])  # []

# si colocamos un steo de -1 vemos la lista en sentido inversp
print(letras[::-1])  # ['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']


def agregar_amigo(lista_amigos, nuevo_amigo):
    lista_amigos = lista_amigos + nuevo_amigo
    return lista_amigos


print(agregar_amigo(['bob', 'marck'], ['rob']))


# ejercicios
''' 
Dada una lista mi_lista que contiene los siguientes elementos [3, 6, 2, 7, "pera", False, 4.5]
'''

mi_lista = [3, 6, 2, 7, "pera", False, 4.5]

'''Accede al tercer elemento (índice 2) y guárdalo en una variable llamada tercer_elemento.'''

tercer_elemento = mi_lista[2]

'''Accede al último elemento usando un índice negativo y guárdalo en una variable llamada ultimo_elemento.'''

ultimo_elemento = mi_lista[-1]

'''Cambia el valor del segundo elemento (índice 1) a "seis".'''

mi_lista[1] = 6

'''Añade el elemento "nuevo" al final de la lista.'''

mi_lista.append('nuevo')

'''Inserta el elemento "inserción" en la segunda posición (índice 1).'''

mi_lista.insert(1, 'insercion')
print(mi_lista)

'''Elimina el primer elemento de valor False que encuentres en la lista.'''

mi_lista.remove(False)
print(mi_lista)

'''Recorre la lista usando un bucle for e imprime cada elemento.'''

for elemento in mi_lista:
    print(elemento, end=' ')
print('')
