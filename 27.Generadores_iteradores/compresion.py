

lista = [1 if x % 2 == 0 else 0 for x in range(10)]
generador = (1 if x % 2 == 0 else 0 for x in range(10))

print(lista)
print(generador)

# las listas son iterables
for num in lista:
    print(num, end=' ')
print()


for num in generador:
    print(num, end=' ')
print()
