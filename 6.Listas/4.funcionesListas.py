no_olvidar = ['huevos', 'palta', 'lechuga', 'naranjas']

no_olvidar.append('leche')

print('hay', len(no_olvidar), 'cosas por comprar')

# verificar si existe un elemnto indicado dentro de la lista

print('existe vino en la lista', ('vino' in no_olvidar))
print('existe pan en la lista', ('pan' in no_olvidar))
print('existe huevos en la lista', ('huevos' in no_olvidar))

# verificar en que posicion se encuentra un elemento

print('si palta esta en que posicion se encuentra?', no_olvidar.index('palta'))
print('si leche esta en que posicion se encuentra?', no_olvidar.index('leche'))
# print('si pulpo esta en que posicion se encuentra?', no_olvidar.index('pulpo')) # error no esta dentro de la lista


# CONVERTIR UN STRING EN UNA LISTA

texto = "Pérez, García, Martínez, Borja"
print('Primero: ', texto[0])
print('No lista: ', texto)

nueva_lista = []
inicio = 0
for i in range(0, len(texto)):
    if texto[i] == ",":
        nueva_lista.append(texto[inicio:i])
        inicio = i + 1
nueva_lista.append(texto[inicio:])

print(nueva_lista)

# cada vez que veamos una coma (',') dividimos esa parte el string desde que se inicio hasta el final, en la separacion podria ir cualquier caracter
lista_alumnos = "Pérez, García, Martínez, Borja"
alumnos = lista_alumnos.split(',')

print(alumnos)

# Ordenar las listas  de manera alfabetica

print('lista original: ', no_olvidar)
# para utilizar el metodo sort se debe teneer un listado de un solo typo ya sea string o number
no_olvidar.sort()
print('lista ordenado: ', no_olvidar)

# sort ordena de mayor a menor

precios = [10, 5, 4, 2, 1]
precios.sort()
print(precios)

# ordenado de listas, de acuerdo al precio menor de cada elemento

comprar = [[1800, 'huevos'], [2300, 'palta'],
           [450, 'naranjas'], [610, 'queso']]

print('original:', comprar)
comprar.sort()
print('Ordenado: ', comprar)

print(comprar[0])


lista_compras = ["pan", "huevo", "queso", "arroz", "jamon"]
lista_compras.append("maní")
lista_compras.remove("arroz")
lista_compras.insert(2, "leche")
print(lista_compras)
