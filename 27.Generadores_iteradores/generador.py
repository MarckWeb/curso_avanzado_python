def serie_numeros(num):  # retorna Generador [int]
    for n in range(num):
       # return n  # TypeError: 'int' object is not iterable
        yield n


for item in serie_numeros(10):
    print(item, end=' ')
print()

# Generador para crear las primeras potencia de 2 hasta el numero indicado
# ejemplo: num 4 -> 1,2,4,8(2 elevado a 0,1,2,3)


def generador_potencias(num):
    for n in range(num):
        yield 2 ** n


for item in generador_potencias(4):
    print(item, end=' ')
print()

# Ejercicio de fibinnaci


def fibonacci_generador(n):
    a, b = 0, 1
    for n in range(n):
        yield a
        a, b = b, a + b


# Uso del generador para obtener los primeros 10 números de Fibonacci
for numero in fibonacci_generador(10):
    print(numero, end=' ')
print()
# Otras formas de imprimir
print(list(fibonacci_generador(10)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(*fibonacci_generador(10), end=" ")  # 0 1 1 2 3 5 8 13 21 34
