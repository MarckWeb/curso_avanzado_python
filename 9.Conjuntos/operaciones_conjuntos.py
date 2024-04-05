numeros1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros2 = {0, 2, 4, 6, 8, 10}

# interseccion de conjuntos: elementos comunes en ambos
print(numeros1.intersection(numeros2))
print(numeros1 & numeros2)

# diferencia de conjuntos: elementos de un conjunto que no estas en el otro
print(numeros1.difference(numeros2))
print(numeros1 - numeros2)


# el orden es importante(muestra los numeros de numeros2 que no estan en numeros1)
print(numeros2.difference(numeros1))
print(numeros2 - numeros1)


# diferencia simetrica de conjuntos (union del primer caso): union de conjuntos menos los comunes
# el orden no importa
print(numeros1.symmetric_difference(numeros2))
print(numeros2.symmetric_difference(numeros1))
print(numeros1 ^ numeros2)


# union de conjuntos
print(numeros1.union(numeros2))
print(numeros1 | numeros2)


# modificar diferencia: borrar los elementos d eun conjunto que estan en el otro
print('---difference_update---')
numeros1.difference_update(numeros2)
# numeros1 -= numeros2 con simbolo
numeros2 -= numeros1
print(numeros1)
print(numeros2)
