# mostrar los numeros del 1 al 10
import random
num = 1
while num <= 10:
    print(num)
    num += 1  # num = num + 1
print('-----FIN-----')


"""recorrer la lista con un bucle while"""

nombres = ['Luis', 'Jorge', 'Maria', 'Laura', 'Pedro']
num = 0
while num < len(nombres):
    print(nombres[num])
    num += 1
print('-----FIN-----')

"""solicitar un password al usuario hasta que adivine que es 'curso'."""

password = ''

while password != 'curso':
    print('Contraseña Incorrecta')
    password = input('Introduce tu contraseña: ')

print('Contraseña Correcta')


"""
   Generar un numero aleatorio del 0 al 10
   Solicitar el numero al usuario hasta que lo adivine
   Le vamos dando pistas: te has pasado, te has quedado corto.
"""

print('--JUEGO ADIVINA EL NÙMERO__')
numero_randon = random.randint(0, 10)
numero = -1
print(numero_randon)
while numero_randon != numero:
    numero = int(input('Adivina el numero del 0 al 10: '))
    # dar pistas
    if numero_randon > numero:
        print('te has quedado corto')
    elif numero_randon < numero:
        print('te has pasado')
print('Felicidades!!! acertaste')


"""
   encontrar los numeros primos del 1 al 100
   un numero primo solo es divisible por si mismo y la unidad
   p.e. para probar si 7 es primo, recorremos sus posibles divisores del 2 al 6
"""

# bucles para recorrer lso nuemros hasta el 100
#   bucle para recorrer los posobles divisibles
#   si despues de recorrer todos siguen siendo primo lo mostramos

numero = 0

while numero < 101:
    print(numero)
    numero += 1
