'''
   - Un conjunto es una colección de elementos pero que está desordenado es decir no hay un índice.
   - No se permite elementos duplicados, los ignora.
   - No se garantiza el orden de entra de los elementos (es decir la salida sera diferente).
   - Como todas las colecciones, permite elementos de diferentes tipos.
   - Se crean: {}
'''

conjunto = {'a', 'b', 'c', 'd', 'e', 'e'}
print(conjunto)  # {'b', 'e', 'd', 'c', 'a'}
print(type(conjunto))  # <class 'set'>

# Mas ejemplos
# 'naranja' no es igul a "Naranja"
frutas = {'Naranja', 'Naranja', 'Pera', 'Naranja', 'Platano'}
# mostrar el conjunto por pantalla
print(frutas)

# mostrar el tipo del conjunto
print(type(frutas))

# agregar fresas al conjunto
frutas.add('Fresas')
print(frutas)

# Eliminar platano
frutas.remove('Platano')
print(frutas)

# Longitud
print(len(frutas))

# quitar repeticiones en lista
lista = [1, 2, 3, 3, 3, 2]
lista1 = set(lista)
print(lista1)

# copiar
otra = frutas.copy()
print(otra)

# Borra todos os elementos
frutas.clear()
print(frutas)  # set()


print(frutas)
print(otra)

# tambien podemos utilizar in y not in

print('Fresas' in otra)
print('Fresas' not in otra)


# recorrer conjuntos

for fruta in otra:
    print(fruta, end=(' -> '))
print()


# set1.update(set2)
# cjto.discard(elto)
# set1.issuperset
# set1.issubset
