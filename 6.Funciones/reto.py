
# Definir una función: Crea una función llamada multiplicar que tome dos números como argumentos y devuelva su producto.

def multiplicar(a, b):
    return a * b

# Llamada a la función: Utiliza la función multiplicar para multiplicar los números 5 y 3, y guarda el resultado en una variable llamada resultado


resultado = multiplicar(5, 3)

# Argumentos y parámetros: Modifica la función multiplicar para que también pueda aceptar un tercer argumento opcional que determina si el resultado debe ser impreso en pantalla.


def multiplicar(a, b, imprimir=False):
    """Este es el docstring de la función"""
    resultado = a * b
    if imprimir:
        print("El resultado es:", resultado)
    return resultado


print(resultado)
# Valores predeterminados: Crea una función llamada saludar que tome un nombre como argumento y tenga un valor predeterminado de "Amigo". La función debe imprimir un saludo.


def saludar(nombre='Amigo'):
    """Este es el docstring de la función"""
    print('hola', nombre)


saludar()

# Retorno de valores: Crea una función llamada es_par que tome un número como argumento y devuelva True si el número es par y False si no lo es.


def es_par(num):
    """Este es el docstring de la función"""
    if num % 2 == 0:
        return True
    else:
        return False


print(es_par(4))

# *******************************


def funcion_misteriosa(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


print(funcion_misteriosa(102))
print(funcion_misteriosa(103))

# Qué hace la siguiente función?


def func_misteriosa(x):
    c = 0
    while x != 0:
        c += 1
        x = x//10
        print('sss', x)
    return c


print(func_misteriosa(10))


def suma(N):
    s = 0
    for i in range(N):
        print(i)
        s += i
    print(s)
    return s


print(suma(11))

# *********************


def funcion(x, y):
    return (x-8)*(y**2)


print(funcion(16, 1))


# encontrar el divisor mas grande

def max_divisor(n):
    maximo_actual = 0
    i = 1
    while i < n:
        if n % i == 0:
            maximo_actual = 1
        i += 1
    return maximo_actual


print(max_divisor(8))


# potencia
