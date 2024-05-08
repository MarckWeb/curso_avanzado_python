import time
'''
1-. Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''


def dividir(num1=10, num2=2):
    if not num1 and num2:
        return f"Error, falta un numero"

    if num2 == 0:
        return f'introdugiste: {num2}, el divisor no debe ser 0'

    return num1 // num2


print(dividir())
print(dividir(0, 5))
print(dividir(10, 0))


'''
2-. Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''
numero = int(input('Escribi un numero:'))

if numero % 2 == 0:
    print('el numero es par')
else:
    print('el numero es impar')

'''3-.Escribir un programa, cada segundo debe mostrar la palabra mississippi'''
for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print('Lista o no, aquí vengo!')


'''
 4-.Escribe un programa que muestre por consola (con un print) los
  números de 1 a 100 (ambos incluidos y con un salto de línea entre
  cada impresión), sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 '''

# Ejercicio con condicion ternario


def fizzBuzz():
    for i in range(101):
        result = 'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)
        print(result if result else i)


fizzBuzz()

# Ejercicio con condicion if, elif


def fizzBuzz():
    for i in range(101):
        output = ''
        divisibleForTHree = i % 3 == 0
        divisibleForFive = i % 5 == 0
        if divisibleForTHree and divisibleForFive:
            output = 'FizzBuzz'
        elif divisibleForTHree:
            output = 'Fizz'
        elif divisibleForFive:
            output = 'Buzz'
        else:
            output = i
        print(output)


fizzBuzz()

'''
5-. Calcular la la velocidad
'''


def velocidad(distancia, tiempo):
    resultado = ""
    resultado = "la velocidad es " + \
        str(distancia / tiempo * 3600)+"km/h o " + \
        str(distancia * 1000 / tiempo)+"m/s"
    return resultado


print(velocidad(100, 1))

'''
 Programa una función para convertir grados Celsius a Fahrenheit y viceversa, pe. miFuncion(0,"C") devolverá 32°F.
'''
def convertirGrados(grados:int, unidad:str):
    validate_uni = len(unidad) == 1
    if unidad.upper() == 'C' and validate_uni:
        print(f'{grados}ºC = {(int(grados * 9/5) +32)}ºF')
    elif unidad.upper() == 'F' and validate_uni:
        print(f'{grados}ºF = {int(grados - 32)*(5/9)}ºC')
    else:
        print('El tipo de grados no existe')

#convertirGrados() TypeError
#convertirGrados('s') TypeError
#convertirGrados(2) TypeError
#convertirGrados(2, False) TypeError
convertirGrados(2, 'jola')
convertirGrados(2, 'E')
convertirGrados(0, 'F')
convertirGrados(100, 'C')
convertirGrados(32, 'F')


