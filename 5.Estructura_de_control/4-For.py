# 2:15
# en el siguiente codigo se crea una variable que iterara desde cero hasta 21 no incluido, es decir solo hasta 20
for temp in range(3):
    print(temp, "   ", int((temp - 32) * 5/9))


# range(n) -. crea uan secuencia de numeros, que parte desde 0 y llega hasta fin -1

# mostrara un numero del 0 al 10, el 11 no se cuenta
for i in range(11):
    print(i)


# range(inicio, fin)-. crea una secuencia de numeros, que parte desde inicio y llega hasta fin -1

for i in range(8, 14):
    print(i)  # mostrara un numero del 8 al 13, es decir 14 -1


# range(inicio, fin, paso)-. crea una secuencia de numeros, que parte desde inicio y llega hasta fin -1, avanzando de a paso numeros(de tres en tres)

for i in range(4, 101, 3):
    print(i)  # resultado de 4 avanzando de 3 en 3 hasta llegar a 100

for i in range(100, 110, 2):
    print(i)  # range(100,110,2) genera la secuencia desde 100 hasta 109, saltando de 2 en 2, por lo que generará 100, 102, 104, 106 y 108 (pero no 110, dado que es mayor que 109


# EJEMPLO

for i in range(1, 25):
    if i < 18:
        print(i, "menor de edad")
    else:
        print(i, "mayor de edad")


a = 3
for i in range(2, 3):
    a = a * i
    print(a)


a = 2
for i in range(1, 4):
    a = i ** a
print(a)
