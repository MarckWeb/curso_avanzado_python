# escriba una función de nombre mcd que reciba dos números n1 y n2 como argumentos, y retorne el máximo común divisor. Por ejemplo para los argumentos 10 y 15 debe retornar 5.

def mcd(n1, n2):
    while n2 != 0:
        temp = n1
        n1 = n2
        n2 = temp % n2
    return n1


resultado = mcd(10, 15)
print("El máximo común divisor es:", resultado)


def mcd(a, b):
    # Iterar mientras b no sea cero
    while b != 0:
        print("a =", a, ", b =", b)
        # Guardar el valor actual de b en a
        temp = a  # // 15 // 15
        a = b  # // 10 // 5
        # Calcular el residuo de a dividido por b y almacenarlo en b
        b = temp % b  # // 5 // 0
    # Cuando b sea cero, devolver el valor de a, que será el MCD
    print("a =", a, ", b =", b)
    return a


# Ejemplo de uso
resultado = mcd(10, 15)
print("El máximo común divisor es:", resultado)


# Escribe una función exponente, que dado un número n, retorne el exponente de dicha potencia de 2 más grande. Por ejemplo, si el número es 65, tu programa debe retornar 6, ya que 2⁶  = 64.

def exponente(n):
    base = 2
    exp = 0
    while base <= n:
        base *= 2
        exp += 1
    return exp


print(exponente(80))
print(exponente(65))
print(exponente(128))
print(exponente(208))
print(exponente(256))

# Considere que existen los números primos y los números pandigitales. Los números pandigitales son aquellos que contienen todos los dígitos del 0 al 9 al menos una vez, como el 1023478695. Escribe una función panprimo que determine si un número n es pandigital y si al mismo tiempo, sus últimos 3 dígitos conforman un número primo, retornando True o False según corresponda. Por ejemplo:

# 1) El número 2424643 cumple que sus últimos 3 dígitos conforman un número primo (643), pero no es pandigital por lo tu función que debería retornar False.

# 2) El número 1234567890 cumple que es pandigital, pero sus últimos 3 dígitos no conforman un primo (890), por lo que tu función debería retornar False.

# 3) El número 10123485769 cumple que es pandigital y además el número conformado por sus 3 últimos dígitos (769) es primo, por lo que debería retornar True.

# Tip1: Puedes convertir un entero a una cadena de texto con el método str(numero), y puedes verificar si alguna letra está en el esta cadena de texto haciendo if letra in string: ...

# Tip2: Un número es primo si solo es divisible por 1 y por sí mismo. Para obtener los últimos tres dígitos, puedes obtener el resto del número en su división con 100.


def es_pandigital(numero):
    cadena_numero = str(numero)
    # Verifica si todos los dígitos del 0 al 9 están presentes
    return len(set(cadena_numero)) == 10


def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True


def panprimo(n):
    if len(str(n)) < 10:
        return False
    ultimos_tres_digitos = n % 1000
    if es_pandigital(n) and es_primo(ultimos_tres_digitos):
        return True
    return False


# Ejemplos de uso
print(panprimo(2424643))      # Salida: False
print(panprimo(1234567890))   # Salida: False
print(panprimo(10123485769))  # Salida: True
