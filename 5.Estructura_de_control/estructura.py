#  Crea una sentencia if que evalúe si un número es positivo, y en caso de que lo sea, imprime un mensaje que lo indique.
numero = 0
if numero > 0:
    print('el numero es positivo')
elif numero == 0:
    print(f'el numero es igual a {numero}')
else:
    print(f'el numero  {numero} no es positivo')


#  while: Utiliza un bucle while para imprimir los números del 1 al 10.
numero = 1
while numero < 11:
    print(numero)
    numero += 1

print('----------')
for numero in range(10):
    print(numero)

print('----------')
for numero in range(10):
    if numero == 5:
        break
    print(numero)

print('----------')
for numero in range(10):
    if numero == 5:
        continue
    print(numero)

print('----------')
for numero in range(10):
    if numero == 5:
        print(numero)
        pass
