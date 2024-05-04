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

# Modifica el conjunto uniendo los elementos de otro conjunto
# numeros1.update(numeros2)
numeros1 |= numeros2
print('update', numeros1)  # 3n numero1 almacena numeros1 + numeros2
print('update', sorted(numeros1, reverse=True))

# set1.update(set2)
# cjto.discard(elto)
# set1.issuperset
# set1.issubset

# discard: Borra el elemento psado como argumento si lo encuentra, sino no hace nada
# TypeError: set.discard() takes exactly one argument (2 given)
# numeros1.discard(0, 2)
numeros1.discard(2)
print(numeros1)

# sino encuentra el elemento con remove devulve un error
# numeros1.remove(27)
# print(numeros1)  # KeyError: 27


# issuperset: comprueba si el primer conjunto contiene todos los datos del segundo
print(numeros1.issuperset(numeros2))
nums1 = {1, 2, 3, 4, 5}
nums2 = {1, 5}

print(nums1.issuperset(nums2))


# issubset: comprueba si el primer conjunto es subconjunto del sugundo,
# que todos los elementos del primer conjunto estan en el segundo

print(numeros1.issubset(numeros2))
print(nums2.issubset(nums1))
