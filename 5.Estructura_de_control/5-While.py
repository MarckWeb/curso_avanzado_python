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
