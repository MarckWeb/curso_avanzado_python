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
