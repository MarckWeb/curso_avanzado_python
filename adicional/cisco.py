import time
john = 3
mary = 5
adam = 6

print(str(john) + "," + str(mary) + "," + str(adam))

total_apples = john + mary + adam
print(total_apples)


# Un número menor o igual a cero produce una cadena vacía.

# Este sencillo programa "dibuja" un rectángulo, haciendo uso del antiguo operador (+) en un nuevo rol
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

print(1 // 2 * 3)

x = 1
y = 2
z = x
x = y
y = z
print(x, y)

x = 11
y = 4

x = x % y
x = x % y
y = y % x

print(y)

x = '3'
y = 6

print(x * y)

z = y = x = 1
print(x, y, z, sep='*')

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)


# Escribe un bucle for que cuente hasta cinco.
for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle, emplea : time.sleep(1)
print('Lista o no, aquí vengo!')
# Escribe una función print con el mensaje final.
