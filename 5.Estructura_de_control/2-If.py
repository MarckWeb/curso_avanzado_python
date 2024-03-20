edad = 70
if edad > 17:
    print('puede ver la pelicula')
else:
    print('No puedes entrar')
print('listo')

# NOTA-. es importante que se respete el espacio el codigo dentro del if, no debe estar al mismo nivel


# las evaluaciones se hacen de arriba hacia abajo

# el orden en el que se escribe las condiciones son importantes
if edad > 65:
    print('Puedes ver la pelicula con super desceunto')
elif edad > 54:
    print('puedes ver la pelicula con descuento')

elif edad > 17:
    print('puedes ver la pelicula')
# else:
#     print('ve a otro lado')


# Las sentencias break y continue: más ejemplos
# Regresemos a nuestro programa que reconoce el más grande entre los números ingresados. Lo convertiremos dos veces, usando las instrucciones de break y continue.

# Analiza el código y determina como las usarías.

# La variante empleando break es la siguiente:

largest_number = -99999999
counter = 0

while True:
    number = int(
        input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

numbers = [10, 5, 7, 2, 1]
del numbers[1]
print(len(numbers))
print(numbers)
