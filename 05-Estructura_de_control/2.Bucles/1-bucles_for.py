# 📌 creando una lista [] de nombres

nombres = ['Luis', 'Jorge', 'Maria', 'Laura', 'Pedro']
print(type(nombres))  # <class 'list'>


# Por cada elemento que tengo en la lista nombres:
#  en este bloque lo mostramos por consola

for elemento in nombres:
    print(elemento, end=' ')
print('\n-----FIN-----')


"""Rangos"""

# mostrar los numeros del 0 al 9
for numero in range(10):  # rango va de 0 a numero -1
    print(numero, end=' ')
print('\n-----FIN-----')

# mostrar los numeros del 1 al 10
for numero in range(1, 11):  # rango va de 1 a numero -1
    print(numero, end=' , ')
print('\n-----FIN-----')

# mostra los numeros de 0 a 10 de 2 en 2
for numero in range(0, 11, 2):  # rango va de 1 a numero -1
    print(numero, end=' - ')
print('\n-----FIN-----')

# mostrar los numeros desde -10 hasta -100 de 10 en 10
for num in range(-100, -10, 10):  # rango va de -100 a -10
    print(num, end=' | ')
print('\n-----FIN-----')

for numero in range(-10, -101, -10):  # rango va de -10 a -100
    print(numero, end=' > ')
print('\n-----FIN-----')

# mostrar los numeros desde 10 hasta el 1
for num in range(10, 0, -1):  # rango va de 10 a 1
    print(num, end='>')
print('\n-----FIN-----')
for i in range(10, 0, -1):
    print(i, end=" / ")
