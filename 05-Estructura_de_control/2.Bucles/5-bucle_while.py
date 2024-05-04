# los bucles while se ejecutan solo si la condicion es true.

temp = 32
print("fº    cº")
while temp < 73:
    print(temp, "   ", int((temp - 32)*5/9))
    temp = temp + 1

# en los bucles while siempres se debe asignar incrementar el valor, caso contrario el bucle sera infinito

n = 1
while n <= 10:
    print(n)
    n += 1


# EJEMPLO
i = 1
while i < 100:
    if i < 18:
        print(i, "menor de edad")
    else:
        print(i, "mayor de edad")
    i = i+1


x = 48
y = 8
n = 0
while x > 0:
    x = x - y
    n = n + 1
print(n)


a = 5
b = 8
r = 0
while a > 0:
    r = r + b
    a = a - 1
print(r)

# Determina una opción que entregue el mismo resultado que el código a continuación:
a = 4
b = 3
r = b
while a > 1:
    a = a - 1
    b2 = b
    r2 = 0
    while b2 > 0:
        r2 = r2 + r
        b2 = b2 - 1
    r = r2
print(r)
